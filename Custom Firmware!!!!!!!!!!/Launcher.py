"""
TGH - The Great Handheld
Custom Game Launcher v3.0
Raspberry Pi Zero 2W | 800x480 Display
By DK
"""

import pygame
import subprocess
import os
import sys
import time
import math
import random
import threading

# =============================================
# HARDWARE DETECTION
# =============================================

GPIO_AVAILABLE = False
ADS_AVAILABLE  = False

try:
    import RPi.GPIO as GPIO
    GPIO_AVAILABLE = True
except ImportError:
    pass

try:
    import board
    import busio
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    ADS_AVAILABLE = True
except ImportError:
    pass

# =============================================
# CONFIGURATION
# =============================================

# ROM paths
ROMS_PATH   = "/home/pi/roms" if GPIO_AVAILABLE else "roms"
SAVES_PATH  = "/home/pi/saves" if GPIO_AVAILABLE else "saves"
STATES_PATH = "/home/pi/states" if GPIO_AVAILABLE else "states"

# RetroArch
RETROARCH_PATH = "/usr/bin/retroarch"
CORES = {
    "NES":  "/opt/cores/fceumm_libretro.so",
    "SNES": "/opt/cores/snes9x_libretro.so",
    "GB":   "/opt/cores/gambatte_libretro.so",
    "GBC":  "/opt/cores/gambatte_libretro.so",
    "GBA":  "/opt/cores/mgba_libretro.so",
    "GEN":  "/opt/cores/genesis_plus_gx_libretro.so",
    "SMS":  "/opt/cores/genesis_plus_gx_libretro.so",
}

# Display
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 480
FPS           = 60

# =============================================
# GPIO PIN MAPPING
# =============================================

BTN_UP    = 5
BTN_DOWN  = 6
BTN_LEFT  = 13
BTN_RIGHT = 26
BTN_A     = 17
BTN_B     = 27
BTN_X     = 22
BTN_Y     = 23
BTN_START = 4
BTN_SEL   = 25
BTN_L1    = 12   # Left joystick click
BTN_R1    = 16   # Right joystick click

ALL_BTNS = [BTN_UP, BTN_DOWN, BTN_LEFT, BTN_RIGHT,
            BTN_A, BTN_B, BTN_X, BTN_Y,
            BTN_START, BTN_SEL, BTN_L1, BTN_R1]

# =============================================
# JOYSTICK CONFIG (ADS1115)
# =============================================

# ADS1115 channel mapping
JOY_L_X_CH = 0   # AIN0
JOY_L_Y_CH = 1   # AIN1
JOY_R_X_CH = 2   # AIN2
JOY_R_Y_CH = 3   # AIN3

# Joystick deadzone (0.0 - 1.0)
JOY_DEADZONE = 0.25

# Joystick center value (ADS1115 at 3.3V input = ~13107 at center with 5V joystick via divider)
JOY_CENTER   = 13107
JOY_MAX      = 26214

# =============================================
# AUDIO CONFIG
# =============================================

AUDIO_ENABLED  = True
AUDIO_FREQ     = 44100
AUDIO_SIZE     = -16
AUDIO_CHANNELS = 2
AUDIO_BUFFER   = 512
VOLUME         = 0.8

# =============================================
# COLORS
# =============================================

C_BG      = (12,  12,  20)
C_WHITE   = (255, 255, 255)
C_GRAY    = (130, 130, 150)
C_DGRAY   = (35,  35,  50)
C_TEXT    = (220, 220, 235)
C_SEL_BG  = (28,  28,  45)
C_GREEN   = (80,  200, 100)
C_RED     = (220, 70,  70)
C_YELLOW  = (255, 200, 50)
C_BLUE    = (80,  120, 200)

# =============================================
# SYSTEM DEFINITIONS
# =============================================

SYSTEMS = [
    {"id": "NES",  "short": "NES",
     "name": "Nintendo\nEntertainment\nSystem",
     "color": (220, 50,  50),
     "ext": [".nes"],
     "year": "1983"},
    {"id": "SNES", "short": "SNES",
     "name": "Super Nintendo\nEntertainment\nSystem",
     "color": (130, 80,  200),
     "ext": [".sfc", ".smc"],
     "year": "1990"},
    {"id": "GB",   "short": "GB",
     "name": "Game Boy",
     "color": (100, 160, 60),
     "ext": [".gb"],
     "year": "1989"},
    {"id": "GBC",  "short": "GBC",
     "name": "Game Boy\nColor",
     "color": (60,  180, 140),
     "ext": [".gbc"],
     "year": "1998"},
    {"id": "GBA",  "short": "GBA",
     "name": "Game Boy\nAdvance",
     "color": (80,  120, 200),
     "ext": [".gba"],
     "year": "2001"},
    {"id": "GEN",  "short": "SEGA",
     "name": "Sega\nGenesis",
     "color": (30,  144, 255),
     "ext": [".md", ".gen", ".bin"],
     "year": "1988"},
    {"id": "SMS",  "short": "SMS",
     "name": "Sega Master\nSystem",
     "color": (255, 140, 0),
     "ext": [".sms"],
     "year": "1985"},
]

# =============================================
# HELPERS
# =============================================

def lerp(a, b, t):
    return a + (b - a) * t

def rr(surface, color, rect, radius, width=0):
    pygame.draw.rect(surface, color, rect, width, border_radius=radius)

def clamp(val, mn, mx):
    return max(mn, min(mx, val))

def get_games(system_id, extensions):
    games = []
    path  = os.path.join(ROMS_PATH, system_id)
    os.makedirs(path, exist_ok=True)
    if os.path.exists(path):
        for f in sorted(os.listdir(path)):
            if os.path.splitext(f)[1].lower() in extensions:
                games.append({
                    "name": os.path.splitext(f)[0],
                    "path": os.path.join(path, f),
                })
    return games

def get_battery():
    try:
        with open("/sys/class/power_supply/BAT0/capacity") as f:
            return int(f.read().strip())
    except:
        return None

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return int(f.read().strip()) // 1000
    except:
        return None

# =============================================
# AUDIO MANAGER
# =============================================

class AudioManager:
    def __init__(self):
        self.enabled = False
        self.volume  = VOLUME
        if AUDIO_ENABLED:
            try:
                pygame.mixer.pre_init(AUDIO_FREQ, AUDIO_SIZE,
                                      AUDIO_CHANNELS, AUDIO_BUFFER)
                pygame.mixer.init()
                self.enabled = True
                self.sounds  = {}
                self._gen_sounds()
            except Exception as e:
                print(f"Audio init failed: {e}")

    def _gen_sounds(self):
        """Generate simple beep sounds using pygame."""
        if not self.enabled:
            return
        try:
            # Navigate sound - short beep
            self.sounds["nav"]    = self._make_beep(440, 0.05)
            # Select sound - higher beep
            self.sounds["select"] = self._make_beep(880, 0.08)
            # Back sound - lower beep
            self.sounds["back"]   = self._make_beep(220, 0.07)
            # Launch sound - ascending beeps
            self.sounds["launch"] = self._make_beep(660, 0.15)
            # Error sound
            self.sounds["error"]  = self._make_beep(150, 0.1)
        except Exception as e:
            print(f"Sound gen failed: {e}")

    def _make_beep(self, freq, duration):
        """Generate a simple sine wave beep."""
        import numpy as np
        sample_rate = AUDIO_FREQ
        samples     = int(sample_rate * duration)
        t           = [i / sample_rate for i in range(samples)]
        wave        = [int(32767 * 0.3 * math.sin(2 * math.pi * freq * s))
                       for s in t]
        # Fade out
        for i in range(min(100, samples)):
            wave[samples-1-i] = int(wave[samples-1-i] * (i/100))
        buf = bytes(sum(([v & 0xFF, (v >> 8) & 0xFF] for v in wave), []))
        sound = pygame.mixer.Sound(buffer=buf)
        sound.set_volume(self.volume)
        return sound

    def play(self, name):
        if self.enabled and name in self.sounds:
            try:
                self.sounds[name].play()
            except:
                pass

    def set_volume(self, vol):
        self.volume = clamp(vol, 0.0, 1.0)
        for s in self.sounds.values():
            s.set_volume(self.volume)

# =============================================
# JOYSTICK MANAGER (ADS1115)
# =============================================

class JoystickManager:
    def __init__(self):
        self.available = False
        self.lx = 0.0
        self.ly = 0.0
        self.rx = 0.0
        self.ry = 0.0
        self._last_dir = None
        self._dir_timer = 0

        if ADS_AVAILABLE:
            try:
                i2c        = busio.I2C(board.SCL, board.SDA)
                ads        = ADS.ADS1115(i2c)
                self.ch_lx = AnalogIn(ads, JOY_L_X_CH)
                self.ch_ly = AnalogIn(ads, JOY_L_Y_CH)
                self.ch_rx = AnalogIn(ads, JOY_R_X_CH)
                self.ch_ry = AnalogIn(ads, JOY_R_Y_CH)
                self.available = True
                print("ADS1115 joysticks initialized!")
            except Exception as e:
                print(f"ADS1115 init failed: {e}")

    def _read_axis(self, channel):
        """Read and normalize axis value to -1.0 to 1.0."""
        try:
            raw = channel.value
            norm = (raw - JOY_CENTER) / JOY_MAX
            norm = clamp(norm, -1.0, 1.0)
            if abs(norm) < JOY_DEADZONE:
                return 0.0
            return norm
        except:
            return 0.0

    def update(self):
        if not self.available:
            return
        self.lx = self._read_axis(self.ch_lx)
        self.ly = self._read_axis(self.ch_ly)
        self.rx = self._read_axis(self.ch_rx)
        self.ry = self._read_axis(self.ch_ry)

    def get_direction(self):
        """Return directional input from left joystick."""
        if not self.available:
            return None
        if self._dir_timer > 0:
            self._dir_timer -= 1
            return None
        if self.ly < -0.5:
            self._dir_timer = 15
            return "UP"
        if self.ly > 0.5:
            self._dir_timer = 15
            return "DOWN"
        if self.lx < -0.5:
            self._dir_timer = 15
            return "LEFT"
        if self.lx > 0.5:
            self._dir_timer = 15
            return "RIGHT"
        return None

# =============================================
# GPIO MANAGER
# =============================================

class GPIOManager:
    def __init__(self):
        self.available = GPIO_AVAILABLE
        self._state    = {p: True for p in ALL_BTNS}
        self._prev     = {p: True for p in ALL_BTNS}

        if self.available:
            GPIO.setmode(GPIO.BCM)
            for pin in ALL_BTNS:
                if pin:
                    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            print("GPIO initialized!")

    def update(self):
        if not self.available:
            return
        self._prev = self._state.copy()
        for pin in ALL_BTNS:
            if pin:
                self._state[pin] = GPIO.input(pin)

    def pressed(self, pin):
        """Returns True if button was just pressed this frame."""
        if not self.available or not pin:
            return False
        return not self._state[pin] and self._prev[pin]

    def held(self, pin):
        """Returns True if button is currently held."""
        if not self.available or not pin:
            return False
        return not self._state[pin]

    def cleanup(self):
        if self.available:
            GPIO.cleanup()

# =============================================
# MAIN LAUNCHER
# =============================================

class Launcher:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("TGH - The Great Handheld")

        flags = pygame.FULLSCREEN if GPIO_AVAILABLE else 0
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), flags)
        self.clock  = pygame.time.Clock()

        # Fonts
        self.fXL = pygame.font.SysFont("Arial", 52, bold=True)
        self.fLG = pygame.font.SysFont("Arial", 34, bold=True)
        self.fMD = pygame.font.SysFont("Arial", 22, bold=True)
        self.fSM = pygame.font.SysFont("Arial", 17)
        self.fXS = pygame.font.SysFont("Arial", 13)

        # Hardware managers
        self.gpio  = GPIOManager()
        self.joy   = JoystickManager()
        self.audio = AudioManager()

        # State machine
        # States: system_select | game_select | library | settings | confirm_launch
        self.state      = "system_select"

        # System carousel
        self.sys_idx    = 0
        self.sys_anim   = 0.0

        # Game list
        self.game_idx   = 0
        self.scroll     = 0
        self.max_vis    = 7
        self.games      = []

        # Animation
        self.tick       = 0
        self.cooldown   = 0

        # Notification
        self.notif_text  = ""
        self.notif_timer = 0

        # Volume
        self.volume     = VOLUME

        # Confirm launch
        self.confirm_sel = 0  # 0=Yes 1=No

        # Stars background
        self.stars = [
            (random.randint(0, SCREEN_WIDTH),
             random.randint(0, SCREEN_HEIGHT),
             random.random())
            for _ in range(70)
        ]

        # Init
        self.ensure_folders()
        self.reload_games()
        print("TGH Launcher initialized!")

    # ---- SETUP ----

    def ensure_folders(self):
        for s in SYSTEMS:
            os.makedirs(os.path.join(ROMS_PATH,  s["id"]), exist_ok=True)
        os.makedirs(SAVES_PATH,  exist_ok=True)
        os.makedirs(STATES_PATH, exist_ok=True)

    def reload_games(self):
        s = SYSTEMS[self.sys_idx]
        self.games    = get_games(s["id"], s["ext"])
        self.game_idx = 0
        self.scroll   = 0

    def notify(self, text, duration=120):
        self.notif_text  = text
        self.notif_timer = duration

    # ---- INPUT ----

    def handle_input(self):
        if self.cooldown > 0:
            self.cooldown -= 1

        # Update hardware
        self.gpio.update()
        self.joy.update()

        # Pygame events (keyboard for PC testing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if not self.handle_key(event.key):
                    return False

        # GPIO input
        if GPIO_AVAILABLE:
            self._handle_gpio()

        # Joystick input
        joy_dir = self.joy.get_direction()
        if joy_dir and self.cooldown == 0:
            self._handle_direction(joy_dir)

        return True

    def handle_key(self, k):
        """Keyboard handler for PC testing."""
        if self.cooldown > 0:
            return True

        # Quit
        if k == pygame.K_q and not GPIO_AVAILABLE:
            return False

        # Direction keys
        dirs = {
            pygame.K_UP:    "UP",
            pygame.K_DOWN:  "DOWN",
            pygame.K_LEFT:  "LEFT",
            pygame.K_RIGHT: "RIGHT",
        }
        if k in dirs:
            self._handle_direction(dirs[k])
            return True

        # Action keys
        if self.state == "system_select":
            if k in (pygame.K_RETURN, pygame.K_SPACE):
                self._action_select()
            elif k == pygame.K_TAB:
                self.state = "library"
                self.audio.play("nav")
            elif k == pygame.K_s:
                self.state = "settings"
                self.audio.play("nav")

        elif self.state == "game_select":
            if k in (pygame.K_RETURN, pygame.K_SPACE):
                self._action_select()
            elif k == pygame.K_ESCAPE:
                self.state = "system_select"
                self.audio.play("back")
            elif k == pygame.K_r:
                self.reload_games()
                self.notify("Library refreshed!")

        elif self.state == "confirm_launch":
            if k == pygame.K_LEFT:
                self.confirm_sel = 0
            elif k == pygame.K_RIGHT:
                self.confirm_sel = 1
            elif k in (pygame.K_RETURN, pygame.K_SPACE):
                if self.confirm_sel == 0:
                    self._launch()
                else:
                    self.state = "game_select"
                    self.audio.play("back")
            elif k == pygame.K_ESCAPE:
                self.state = "game_select"
                self.audio.play("back")

        elif self.state in ("library", "settings"):
            if k in (pygame.K_ESCAPE, pygame.K_b):
                self.state = "system_select"
                self.audio.play("back")
            elif k == pygame.K_r and self.state == "library":
                self.reload_games()
                self.notify("Library refreshed!")

        # Volume control
        if k == pygame.K_PLUS or k == pygame.K_EQUALS:
            self._vol_up()
        elif k == pygame.K_MINUS:
            self._vol_down()

        return True

    def _handle_gpio(self):
        """Handle physical button presses."""
        if self.cooldown > 0:
            return

        # Direction buttons
        if self.gpio.pressed(BTN_UP):
            self._handle_direction("UP")
        elif self.gpio.pressed(BTN_DOWN):
            self._handle_direction("DOWN")
        elif self.gpio.pressed(BTN_LEFT):
            self._handle_direction("LEFT")
        elif self.gpio.pressed(BTN_RIGHT):
            self._handle_direction("RIGHT")

        # A button - Select/Confirm
        if self.gpio.pressed(BTN_A):
            self._action_select()
            self.cooldown = 15

        # B button - Back
        if self.gpio.pressed(BTN_B):
            self._action_back()
            self.cooldown = 15

        # Start - Go to game select
        if self.gpio.pressed(BTN_START):
            if self.state == "system_select":
                self._action_select()
            self.cooldown = 15

        # Select - Go to library
        if self.gpio.pressed(BTN_SEL):
            if self.state != "library":
                self.state = "library"
                self.audio.play("nav")
            else:
                self.state = "system_select"
                self.audio.play("back")
            self.cooldown = 15

        # X button - Settings
        if self.gpio.pressed(BTN_X):
            if self.state != "settings":
                self.state = "settings"
                self.audio.play("nav")
            self.cooldown = 15

        # Y button - Refresh
        if self.gpio.pressed(BTN_Y):
            self.reload_games()
            self.notify("Library refreshed!")
            self.cooldown = 15

        # L1 - Volume down
        if self.gpio.pressed(BTN_L1):
            self._vol_down()
            self.cooldown = 8

        # R1 - Volume up
        if self.gpio.pressed(BTN_R1):
            self._vol_up()
            self.cooldown = 8

    def _handle_direction(self, direction):
        """Handle directional input from buttons or joystick."""
        if self.cooldown > 0:
            return

        if self.state == "system_select":
            if direction == "LEFT":
                self.sys_idx = (self.sys_idx - 1) % len(SYSTEMS)
                self.reload_games()
                self.audio.play("nav")
                self.cooldown = 10
            elif direction == "RIGHT":
                self.sys_idx = (self.sys_idx + 1) % len(SYSTEMS)
                self.reload_games()
                self.audio.play("nav")
                self.cooldown = 10

        elif self.state == "game_select":
            if direction == "UP":
                self._prev_game()
                self.audio.play("nav")
                self.cooldown = 8
            elif direction == "DOWN":
                self._next_game()
                self.audio.play("nav")
                self.cooldown = 8
            elif direction == "LEFT":
                self.state = "system_select"
                self.audio.play("back")
                self.cooldown = 10

        elif self.state == "confirm_launch":
            if direction in ("LEFT", "RIGHT"):
                self.confirm_sel = 1 - self.confirm_sel
                self.audio.play("nav")
                self.cooldown = 8

        elif self.state == "settings":
            if direction == "UP":
                self._vol_up()
                self.cooldown = 8
            elif direction == "DOWN":
                self._vol_down()
                self.cooldown = 8

    def _action_select(self):
        """Handle A/Enter press."""
        if self.state == "system_select":
            if self.games:
                self.state = "game_select"
                self.audio.play("select")
            else:
                self.notify(f"No ROMs! Add to roms/{SYSTEMS[self.sys_idx]['id']}/")
                self.audio.play("error")

        elif self.state == "game_select":
            if self.games:
                self.state    = "confirm_launch"
                self.confirm_sel = 0
                self.audio.play("select")

        elif self.state == "confirm_launch":
            if self.confirm_sel == 0:
                self._launch()
            else:
                self.state = "game_select"
                self.audio.play("back")

    def _action_back(self):
        """Handle B/Escape press."""
        if self.state == "game_select":
            self.state = "system_select"
            self.audio.play("back")
        elif self.state == "confirm_launch":
            self.state = "game_select"
            self.audio.play("back")
        elif self.state in ("library", "settings"):
            self.state = "system_select"
            self.audio.play("back")

    def _prev_game(self):
        if not self.games:
            return
        self.game_idx = (self.game_idx - 1) % len(self.games)
        if self.game_idx < self.scroll:
            self.scroll = self.game_idx

    def _next_game(self):
        if not self.games:
            return
        self.game_idx = (self.game_idx + 1) % len(self.games)
        if self.game_idx >= self.scroll + self.max_vis:
            self.scroll = self.game_idx - self.max_vis + 1

    def _vol_up(self):
        self.volume = clamp(self.volume + 0.1, 0.0, 1.0)
        self.audio.set_volume(self.volume)
        self.notify(f"Volume: {int(self.volume*100)}%", 60)

    def _vol_down(self):
        self.volume = clamp(self.volume - 0.1, 0.0, 1.0)
        self.audio.set_volume(self.volume)
        self.notify(f"Volume: {int(self.volume*100)}%", 60)

    def _launch(self):
        if not self.games:
            return
        game   = self.games[self.game_idx]
        sys_id = SYSTEMS[self.sys_idx]["id"]
        core   = CORES.get(sys_id, "")

        self.audio.play("launch")

        if not os.path.exists(RETROARCH_PATH):
            self.notify(f"[PC TEST] Would launch: {game['name']}")
            self.state = "game_select"
            return

        # Launch RetroArch
        pygame.quit()
        subprocess.run([
            RETROARCH_PATH,
            "-L", core,
            "--fullscreen",
            "--savestate-auto-load",
            game["path"]
        ])

        # Re-init after RetroArch exits
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            pygame.FULLSCREEN if GPIO_AVAILABLE else 0
        )
        self.state = "game_select"
        self.notify(f"Welcome back!")

    # ---- DRAWING ----

    def _draw_bg(self):
        self.screen.fill(C_BG)
        for x, y, b in self.stars:
            flicker = 0.5 + 0.5 * math.sin(self.tick * 0.04 + b * 10)
            c = int(70 * b * flicker)
            if c > 0:
                pygame.draw.circle(self.screen, (c, c, c+15), (int(x), int(y)), 1)
        col = SYSTEMS[self.sys_idx]["color"]
        for i in range(80):
            a = int(35 * (1 - i/80))
            pygame.draw.line(self.screen,
                (col[0]*a//255, col[1]*a//255, col[2]*a//255),
                (0, i), (SCREEN_WIDTH, i))

    def _draw_header(self):
        col = SYSTEMS[self.sys_idx]["color"]
        pygame.draw.rect(self.screen, col, (0, 0, SCREEN_WIDTH, 3))

        logo = self.fLG.render("TGH", True, col)
        self.screen.blit(logo, (16, 7))
        dot  = self.fSM.render(" • The Great Handheld  by DK", True, C_GRAY)
        self.screen.blit(dot, (16 + logo.get_width(), 14))

        # Right side info
        rx = SCREEN_WIDTH - 16
        clk = self.fSM.render(time.strftime("%H:%M"), True, C_GRAY)
        rx -= clk.get_width()
        self.screen.blit(clk, (rx, 8))

        # CPU temp
        temp = get_cpu_temp()
        if temp is not None:
            tc   = C_RED if temp > 70 else C_GREEN
            ttxt = self.fXS.render(f"CPU {temp}°C", True, tc)
            rx  -= ttxt.get_width() + 12
            self.screen.blit(ttxt, (rx, 10))

        # Battery
        bat = get_battery()
        if bat is not None:
            bc   = C_RED if bat < 20 else C_GREEN
            btxt = self.fXS.render(f"BAT {bat}%", True, bc)
            rx  -= btxt.get_width() + 12
            self.screen.blit(btxt, (rx, 10))

        # Volume indicator
        vol_txt = self.fXS.render(f"VOL {int(self.volume*100)}%", True, C_GRAY)
        rx -= vol_txt.get_width() + 12
        self.screen.blit(vol_txt, (rx, 10))

        pygame.draw.line(self.screen, (40,40,60), (0,48), (SCREEN_WIDTH,48))

    def _draw_system_select(self):
        self.sys_anim = lerp(self.sys_anim, float(self.sys_idx), 0.14)

        CARD_W  = 185
        CARD_H  = 260
        SPACING = 24
        CX      = SCREEN_WIDTH  // 2
        CY      = SCREEN_HEIGHT // 2 + 18

        for i, s in enumerate(SYSTEMS):
            offset = i - self.sys_anim
            x      = CX + offset * (CARD_W + SPACING) - CARD_W // 2
            if x < -CARD_W - 60 or x > SCREEN_WIDTH + 60:
                continue

            selected = (i == self.sys_idx)
            scale    = lerp(0.70, 1.0, max(0.0, 1.0 - abs(offset) * 0.75))
            sw       = int(CARD_W * scale)
            sh       = int(CARD_H * scale)
            cx       = int(x + (CARD_W - sw) / 2)
            cy       = CY - sh // 2
            col      = s["color"]

            # Shadow
            shad = pygame.Surface((sw+12, sh+12), pygame.SRCALPHA)
            pygame.draw.rect(shad, (0,0,0,90),
                             (6, 6, sw, sh), border_radius=16)
            self.screen.blit(shad, (cx-6, cy-6))

            # Card
            bg_col = tuple(int(c*0.13) for c in col)
            rr(self.screen, bg_col, (cx, cy, sw, sh), 14)

            if selected:
                pulse = int(160 + 80 * math.sin(self.tick * 0.09))
                bc    = tuple(min(255, int(c * pulse // 255)) for c in col)
                rr(self.screen, bc, (cx, cy, sw, sh), 14, 3)
            else:
                rr(self.screen, tuple(int(c*0.35) for c in col),
                   (cx, cy, sw, sh), 14, 2)

            # System short name
            alpha = max(0.25, 1.0 - abs(offset) * 0.55)
            tc    = tuple(int(c * alpha) for c in col) if not selected else col
            label = self.fXL.render(s["short"], True, tc)
            lx    = cx + sw//2 - label.get_width()//2
            ly    = cy + sh//2 - label.get_height()//2 - 18
            self.screen.blit(label, (lx, ly))

            if selected:
                yr = self.fXS.render(f"Since {s['year']}", True, C_GRAY)
                self.screen.blit(yr, (cx + sw//2 - yr.get_width()//2,
                                      ly + label.get_height() + 2))
                gc = len(self.games)
                ct = self.fXS.render(
                    f"{gc} game{'s' if gc != 1 else ''}",
                    True, C_WHITE)
                self.screen.blit(ct, (cx + sw//2 - ct.get_width()//2,
                                      cy + sh - 28))
            else:
                gc = "?" 
                ct = self.fXS.render(f"{gc} games", True, C_GRAY)
                self.screen.blit(ct, (cx + sw//2 - ct.get_width()//2,
                                      cy + sh - 28))

        # Dot indicators
        DOT_Y = CY + CARD_H//2 + 20
        total = len(SYSTEMS) * 16
        dx    = SCREEN_WIDTH//2 - total//2
        for i in range(len(SYSTEMS)):
            if i == self.sys_idx:
                pygame.draw.circle(self.screen,
                                   SYSTEMS[self.sys_idx]["color"],
                                   (dx + i*16, DOT_Y), 5)
            else:
                pygame.draw.circle(self.screen, C_DGRAY,
                                   (dx + i*16, DOT_Y), 4)

        # Controls hint
        hints = [
            ("◄►", "Navigate"),
            ("A/ENTER", "Select"),
            ("SEL", "Library"),
            ("X", "Settings"),
            ("L1/R1", "Volume"),
        ]
        hx = SCREEN_WIDTH//2 - 280
        hy = SCREEN_HEIGHT - 22
        for key, action in hints:
            kt = self.fXS.render(key, True, SYSTEMS[self.sys_idx]["color"])
            at = self.fXS.render(f" {action}  ", True, C_GRAY)
            self.screen.blit(kt, (hx, hy))
            hx += kt.get_width()
            self.screen.blit(at, (hx, hy))
            hx += at.get_width()

    def _draw_game_select(self):
        s   = SYSTEMS[self.sys_idx]
        col = s["color"]

        # Left panel
        PW = 210
        ps = pygame.Surface((PW, SCREEN_HEIGHT-52), pygame.SRCALPHA)
        ps.fill((18, 18, 32, 210))
        self.screen.blit(ps, (0, 52))

        y = 68
        for line in s["name"].split("\n"):
            t = self.fMD.render(line, True, col)
            self.screen.blit(t, (12, y))
            y += 26
        yr = self.fXS.render(f"Since {s['year']}", True, C_GRAY)
        self.screen.blit(yr, (12, y+4))
        pygame.draw.line(self.screen, (50,50,70), (0, y+28), (PW, y+28))

        gc = self.fSM.render(
            f"{len(self.games)} ROM{'s' if len(self.games)!=1 else ''}",
            True, C_WHITE)
        self.screen.blit(gc, (12, y+36))

        # Joystick status
        if self.joy.available:
            jt = self.fXS.render(
                f"JOY L:{self.joy.lx:.1f},{self.joy.ly:.1f}",
                True, C_GRAY)
            self.screen.blit(jt, (12, SCREEN_HEIGHT-50))

        rh = self.fXS.render("[Y] Refresh  [B] Back", True, C_GRAY)
        self.screen.blit(rh, (12, SCREEN_HEIGHT-30))

        pygame.draw.line(self.screen, (40,40,60),
                         (PW, 52), (PW, SCREEN_HEIGHT))

        LX  = PW + 14
        LW  = SCREEN_WIDTH - LX - 22
        IH  = 44
        LY  = 62

        title = self.fMD.render("SELECT GAME", True, C_GRAY)
        self.screen.blit(title, (LX, LY-8))
        pygame.draw.line(self.screen, col,
                         (LX, LY+18), (SCREEN_WIDTH-18, LY+18))

        if not self.games:
            msg = self.fMD.render("No ROMs found!", True, C_GRAY)
            self.screen.blit(msg, (LX + LW//2 - msg.get_width()//2,
                                   SCREEN_HEIGHT//2))
            sub = self.fXS.render(
                f"Add {s['ext'][0]} files to roms/{s['id']}/",
                True, C_GRAY)
            self.screen.blit(sub, (LX + LW//2 - sub.get_width()//2,
                                   SCREEN_HEIGHT//2 + 28))
        else:
            for i in range(self.max_vis):
                idx = self.scroll + i
                if idx >= len(self.games):
                    break
                game = self.games[idx]
                sel  = (idx == self.game_idx)
                gy   = LY + 26 + i * IH

                if sel:
                    rr(self.screen, C_SEL_BG, (LX-4, gy-2, LW+4, IH-4), 8)
                    rr(self.screen, col,       (LX-4, gy-2, LW+4, IH-4), 8, 2)
                    arr = self.fSM.render("►", True, col)
                    ax  = LX + int(3*math.sin(self.tick*0.15))
                    self.screen.blit(arr, (ax, gy+10))
                    nm  = self.fMD.render(game["name"], True, C_WHITE)
                    self.screen.blit(nm, (LX+24, gy+8))
                else:
                    if i % 2 == 0:
                        pygame.draw.rect(self.screen, (18,18,30),
                                         (LX-4, gy-2, LW+4, IH-4),
                                         border_radius=6)
                    nm = self.fSM.render(game["name"], True, C_TEXT)
                    self.screen.blit(nm, (LX+14, gy+11))

            # Scrollbar
            if len(self.games) > self.max_vis:
                BH = SCREEN_HEIGHT - LY - 50
                BX = SCREEN_WIDTH - 13
                pygame.draw.rect(self.screen, C_DGRAY,
                                 (BX, LY+26, 6, BH), border_radius=3)
                TH = max(24, BH * self.max_vis // len(self.games))
                TY = (LY+26 +
                      (BH-TH) * self.scroll //
                      max(1, len(self.games)-self.max_vis))
                pygame.draw.rect(self.screen, col,
                                 (BX, TY, 6, TH), border_radius=3)

        h = self.fXS.render(
            "▲▼/Joystick Navigate   A/ENTER Launch   B/ESC Back",
            True, C_GRAY)
        self.screen.blit(h, (SCREEN_WIDTH//2 - h.get_width()//2,
                              SCREEN_HEIGHT-22))

    def _draw_confirm_launch(self):
        """Confirmation dialog before launching game."""
        if not self.games:
            return
        game = self.games[self.game_idx]
        col  = SYSTEMS[self.sys_idx]["color"]

        # Dimmed background
        dim = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        dim.fill((0, 0, 0, 160))
        self.screen.blit(dim, (0, 0))

        # Dialog box
        DW, DH = 420, 200
        DX = SCREEN_WIDTH//2  - DW//2
        DY = SCREEN_HEIGHT//2 - DH//2
        rr(self.screen, (20, 20, 35), (DX, DY, DW, DH), 16)
        rr(self.screen, col,          (DX, DY, DW, DH), 16, 3)

        # Title
        t = self.fMD.render("Launch Game?", True, col)
        self.screen.blit(t, (SCREEN_WIDTH//2 - t.get_width()//2, DY+20))

        # Game name
        name = game["name"]
        if len(name) > 35:
            name = name[:32] + "..."
        n = self.fSM.render(name, True, C_WHITE)
        self.screen.blit(n, (SCREEN_WIDTH//2 - n.get_width()//2, DY+60))

        # System
        s = self.fXS.render(SYSTEMS[self.sys_idx]["short"], True, C_GRAY)
        self.screen.blit(s, (SCREEN_WIDTH//2 - s.get_width()//2, DY+88))

        # Yes / No buttons
        for i, (label, clr) in enumerate([("YES", C_GREEN), ("NO", C_RED)]):
            bw   = 120
            bx   = SCREEN_WIDTH//2 - bw - 10 + i * (bw + 20)
            by   = DY + DH - 58
            sel  = (self.confirm_sel == i)
            bgc  = (40, 80, 40) if (sel and i==0) else \
                   (80, 40, 40) if (sel and i==1) else (30, 30, 50)
            rr(self.screen, bgc, (bx, by, bw, 40), 10)
            rr(self.screen, clr if sel else C_GRAY,
               (bx, by, bw, 40), 10, 2)
            lt = self.fMD.render(label, True, clr if sel else C_GRAY)
            self.screen.blit(lt, (bx + bw//2 - lt.get_width()//2, by+8))

    def _draw_library(self):
        col   = SYSTEMS[self.sys_idx]["color"]
        title = self.fLG.render("ROM LIBRARY", True, col)
        self.screen.blit(title, (30, 62))
        pygame.draw.line(self.screen, col, (30, 100), (SCREEN_WIDTH-30, 100))

        sub = self.fXS.render(
            "ROM files go in these folders on the MicroSD card:",
            True, C_GRAY)
        self.screen.blit(sub, (30, 110))

        y = 130
        for s in SYSTEMS:
            games = get_games(s["id"], s["ext"])
            count = len(games)
            sc    = s["color"]
            bg    = tuple(int(c*0.12) for c in sc)
            rr(self.screen, bg, (25, y, SCREEN_WIDTH-50, 50), 10)
            rr(self.screen, tuple(int(c*0.4) for c in sc),
               (25, y, SCREEN_WIDTH-50, 50), 10, 2)

            nm = self.fMD.render(s["short"], True, sc)
            self.screen.blit(nm, (40, y+6))

            path = self.fXS.render(
                f"roms/{s['id']}/   •   " + "/".join(s["ext"]),
                True, C_GRAY)
            self.screen.blit(path, (40, y+28))

            st = (self.fMD.render(f"✓ {count} ROMs", True, C_GREEN)
                  if count > 0 else
                  self.fMD.render("✗ Empty", True, C_RED))
            self.screen.blit(st, (SCREEN_WIDTH - st.get_width() - 45, y+14))
            y += 58

        h = self.fXS.render("[Y] Refresh   [B/ESC] Back", True, C_GRAY)
        self.screen.blit(h, (SCREEN_WIDTH//2 - h.get_width()//2,
                              SCREEN_HEIGHT-24))

    def _draw_settings(self):
        col   = SYSTEMS[self.sys_idx]["color"]
        title = self.fLG.render("SETTINGS", True, col)
        self.screen.blit(title, (30, 62))
        pygame.draw.line(self.screen, col, (30, 100), (SCREEN_WIDTH-30, 100))

        temp = get_cpu_temp()
        bat  = get_battery()

        rows = [
            ("Display",   f"800x480  |  Fullscreen: {'ON' if GPIO_AVAILABLE else 'OFF'}"),
            ("Audio",     f"Volume: {int(self.volume*100)}%  |  I2S: MAX98357A  |  [L1]-  [R1]+"),
            ("Controls",  f"GPIO Buttons  |  ADS1115 Joysticks: {'OK' if self.joy.available else 'NOT FOUND'}"),
            ("Hardware",  f"Temp: {temp}°C" if temp else "Temp: N/A" +
                          f"  |  Battery: {bat}%" if bat else "  |  Battery: N/A"),
            ("System",    "TGH Firmware v3.0  |  Python + Pygame"),
            ("ROMs",      ROMS_PATH),
        ]

        y = 115
        for label, value in rows:
            rr(self.screen, C_DGRAY, (25, y, SCREEN_WIDTH-50, 48), 10)
            lbl = self.fMD.render(label, True, col)
            val = self.fSM.render(value, True, C_TEXT)
            self.screen.blit(lbl, (40, y+4))
            self.screen.blit(val, (40, y+26))
            y += 56

        h = self.fXS.render("[B/ESC] Back   [▲▼/Joystick] Volume", True, C_GRAY)
        self.screen.blit(h, (SCREEN_WIDTH//2 - h.get_width()//2,
                              SCREEN_HEIGHT-24))

    def _draw_notification(self):
        if self.notif_timer <= 0:
            return
        self.notif_timer -= 1
        alpha = min(255, self.notif_timer * 8)
        col   = SYSTEMS[self.sys_idx]["color"]
        surf  = pygame.Surface((SCREEN_WIDTH-60, 36), pygame.SRCALPHA)
        surf.fill((30, 30, 50, min(200, alpha)))
        self.screen.blit(surf, (30, SCREEN_HEIGHT-64))
        t = self.fSM.render(self.notif_text, True, col)
        self.screen.blit(t, (SCREEN_WIDTH//2 - t.get_width()//2,
                              SCREEN_HEIGHT-58))

    def draw(self):
        self._draw_bg()
        self._draw_header()

        if   self.state == "system_select":   self._draw_system_select()
        elif self.state == "game_select":      self._draw_game_select()
        elif self.state == "confirm_launch":
            self._draw_game_select()
            self._draw_confirm_launch()
        elif self.state == "library":          self._draw_library()
        elif self.state == "settings":         self._draw_settings()

        self._draw_notification()
        pygame.display.flip()

    # ---- MAIN LOOP ----

    def run(self):
        running = True
        while running:
            self.tick  += 1
            running     = self.handle_input()
            self.draw()
            self.clock.tick(FPS)

        self.gpio.cleanup()
        pygame.quit()
        sys.exit()

# =============================================
# ENTRY POINT
# =============================================

if __name__ == "__main__":
    launcher = Launcher()
    launcher.run()