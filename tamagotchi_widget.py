
import json
import os
import time
import tkinter as tk

# ----------------------------------------------------------------------
# ARTE ASCII / BRAILLE
# ----------------------------------------------------------------------

DEFAULT_ART = """\
⠀⢖⣔⣆⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀
⠐⠓⣆⠒⠁⠀⠀⢀⡀⠀⠀⠀⠀⠀⡠⢤⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡯⠙⠒⠒⠒⠖⠞⠁⠀⡇⠀⠉⡾⡆⣇⠀⠀⠀⠀
⠐⠏⠀⠀⠀⢄⡸⠅⣠⣄⠀⠠⠶⠤⠀⠀⣳⠤⠀⠈⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣒⣆⠈⠁⠘⠃⠀⠀⠀⠀⠠⣟⡁⠀⠀⠀⠀⠀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⠘⠦⣤⠀⠀⠀⠀⠀⠰⡞⠀⣀⢄⠀⠀⠀⠀⢀⠺⠀
⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠘⣶⠋⢠⠃⠀⠀⠲⡃⡒⠄
⠀⠀⢎⣯⡆⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⣇⠀⠐⠀⠉⠈⠉⠀
⠀⠈⠒⠓⠁⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠚⠂⠀⠀⠀⠀⠀⠀"""




EXTRA_LOVE_ART = """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠁⠀⠀⠸⠄⠒⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠐⠒⠒⠒⠀⠤⢀⡀⠀⠠⠊⠀⠀⠀⠀⡀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀
⠀⠰⠀⠀⠀⠀⠀⠀⠀⢈⡐⢄⠀⠀⠀⡀⠤⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀
⡈⠉⠑⠀⢀⠀⢀⠀⡇⠐⠀⠖⠒⠒⠒⠃⠠⢀⣔⠅⡆⡘⠀⠀⠀⠀⠀⠀⠀
⠡⠀⠀⠀⠀⠀⠀⣁⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠗⠐⠂⠐⠒⠠⠄⡀⠀
⠀⠑⢄⠀⠀⠀⠑⠈⠀⠀⠀⣀⠀⠀⠀⠀⡀⠀⠀⢀⠸⢴⠈⠈⠀⠀⠀⠈⢱
⠀⠀⡠⠋⠁⢔⠇⠀⠀⠠⣘⡋⠀⠐⠓⠀⠻⢂⠀⠀⠂⢞⡀⢀⠀⠀⣀⠠⠂
⠀⡔⠀⠀⠀⡨⠚⢌⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡨⠜⠂⠀⠈⠂⠈⠑⢀
⡘⠀⠀⠀⠀⠀⠐⠃⠀⠀⠀⠄⠤⠤⠤⠤⠄⠀⠔⠈⠁⠀⠀⠀⠀⡀⡄⠖⠁
⢃⣀⣀⠀⠀⠈⠀⠀⠀⠀⠀⡀⠀⠀⠀⠘⢁⠀⠀⠀⠑⠔⠐⠈⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠄⠺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠁⠀⠐⠂⠉⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠰⠤⣀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠁⠀⠀⠀⠀"""



RANDOM_ART = """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⣥⣼⢩⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⠀⢰⠁⠀⠀⣀⡔⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠃⠀⠸⠀⠀⡠⠋⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⣇⠔⠉⠀⠀⠀⠀⠉⠢⢄⠠⠤⢤⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠤⣇⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀
⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠉⣷⠃⠀⠈⠉⠀⢀⣤⠀⠀⠀⠨⠀⠀⠀
⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⡇⠓⠀⠀⠚⠅⠀⠉⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠒⠤⣀⣀⣀⣀⢷⡪⡀⠀⠀⠀
⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠠⣀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀
⠀⢀⡰⠉⢆⠀⠀⢀⣆⡀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢆⠀⢸⡀⠀⡠⠤⡀
⠀⢧⣤⡴⠃⠷⡄⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⢸⠘⠛⡴⡞⢧
⠀⠀⠀⣀⠔⢊⡡⠔⠒⠒⠂⠤⠤⠤⠤⠤⠤⠤⠤⠤⢇⠘⢖⠲⢌⣑⡎
⠀⠀⢰⠁⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠊⠀⠀⠀⠀
⠀⠀⠘⢦⣈⠒⠠⠤⠤⠤⠔⠒⠒⠒⠒⠒⠢⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣆⠀⠀⠀⠀⠉⠉⠑⠒⠒⠒⠒⠒⠒⠒⠒⠈⠀⠀⠀"""



EATING_ART = """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣀⣀⣠⠤⠒⠒⠓⠒⠧⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠀⢀⡀⢀⣠⢊⠁⠉⢦⢠⠔⠒⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡜⠀⠀⠀⠈⢁⡀⠒⠉⠀⠀⠖⠉⠙⠦⠤⠚⠑⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀
⢇⠀⠀⠀⠀⠛⠚⠀⠀⣀⠀⠶⠄⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀
⠈⢢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠤⡀⠀⠀⠀⠀
⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀
⠀⠈⡆⠀⠀⠒⢆⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠠⣤⠛⠤⣤⡊⠀⠀⠀
⠀⠀⠙⠢⠤⠴⠓⠦⢄⡔⠿⣁⡤⣤⣄⣤⣀⠭⠱⡀⠀⡱⠤⣀⣈⠉⢉⣲
⠀⠀⠀⠀⠀⠀⠀⠀⠸⢔⡘⠀⠉⠉⠉⠁⠀⢀⣰⠿⠉⠀⠀⠀⠀⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠒⠒⠒⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

SLEEP_ART = """\
⠀⠀⠀⠈⣩⠟⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⠈⠉⠁⠀⣠⠔⠋⠉⠉⠉⠉⠛⠶⣄⠀⠀⠀⠀⠀
⠀⢠⣞⡁⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⠀
⠀⢠⡀⠀⣀⠯⠔⠒⠢⢄⠀⠀⠀⠀⠀⠀⠀⠈⣷⢤⡀⠀
⠀⠺⢂⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠙⣆
⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢀⣠⠞⠁⠀⢀⡏
⠙⠘⠙⠣⠤⠤⣤⡶⣄⣰⠧⠴⠖⠚⠋⠹⣇⢀⣠⡴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀ """

# ----------------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------------

STATE_DIR = os.path.expanduser("~/.local/share/tamagotchi-widget")
STATE_FILE = os.path.join(STATE_DIR, "state.json")

TICK_MS = 60_000          
HUNGER_DECAY = 2         
HAPPY_DECAY = 1           
ENERGY_DECAY = 1          
ENERGY_REGEN_SLEEP = 6    

FEED_HUNGER_GAIN = 18
FEED_HAPPY_GAIN = 3
LOVE_HAPPY_GAIN = 12
WAKE_ENERGY_GAIN = 35

EAT_ANIM_MS = 2500        

BG_SHELL = "#5b7fd1"      
BG_SHELL_DARK = "#3f5aa8"
SCREEN_BG = "#c9d9c0"     
SCREEN_FG = "#3f5a3f"     
BTN_BLUE = "#7a97e6"
BTN_BLUE_DARK = "#2f4a8f"


def clamp(v, lo=0, hi=100):
    return max(lo, min(hi, v))


# ----------------------------------------------------------------------
# ESTADO PERSISTENTE
# ----------------------------------------------------------------------

def load_state():
    default = {
        "hunger": 80,
        "happiness": 80,
        "energy": 100,
        "sleeping": False,
        "last_tick": time.time(),
    }
    if not os.path.exists(STATE_FILE):
        return default
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        for k, v in default.items():
            data.setdefault(k, v)
        return data
    except (json.JSONDecodeError, OSError):
        return default


def save_state(state):
    os.makedirs(STATE_DIR, exist_ok=True)
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f)
    except OSError:
        pass


# ----------------------------------------------------------------------
# WIDGET
# ----------------------------------------------------------------------

class TamagotchiWidget:
    def __init__(self):
        self.state = load_state()
        self._catch_up_time()

        self.root = tk.Tk()
        self.root.title("caTamagotchi")
        self.root.overrideredirect(True)   
        self.root.attributes("-topmost", True)
        self.root.configure(bg=BG_SHELL)

        self._revert_job = None
        self._flash_job = None

        self._build_ui()
        self._position_window()
        self._refresh_screen("¡Hola! :)")

        self.root.bind("1", lambda e: self.love())
        self.root.bind("2", lambda e: self.feed())
        self.root.bind("3", lambda e: self.toggle_sleep())

        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.after(TICK_MS, self._tick)

    # -- construcción de la interfaz -----------------------------------

    def _build_ui(self):
        WIDTH = 300

        # Barra superior (para arrastrar la ventana + botón cerrar)
        top = tk.Frame(self.root, bg=BG_SHELL_DARK, height=22)
        top.pack(fill="x")
        top.bind("<ButtonPress-1>", self._start_move)
        top.bind("<B1-Motion>", self._do_move)

        close_btn = tk.Label(top, text="×", bg=BG_SHELL_DARK, fg="white",
                              font=("DejaVu Sans", 12, "bold"), cursor="hand2")
        close_btn.pack(side="right", padx=6)
        close_btn.bind("<Button-1>", lambda e: self.quit())

        title = tk.Label(top, text="caTamagotchi", bg=BG_SHELL_DARK, fg="white",
                          font=("DejaVu Sans", 9, "bold"))
        title.pack(side="left", padx=6)
        title.bind("<ButtonPress-1>", self._start_move)
        title.bind("<B1-Motion>", self._do_move)

       
        screen_border = tk.Frame(self.root, bg="black", padx=3, pady=3)
        screen_border.pack(padx=14, pady=(10, 6))

        self.screen = tk.Label(
            screen_border, text=DEFAULT_ART, justify="center",
            bg=SCREEN_BG, fg=SCREEN_FG, font=("DejaVu Sans Mono", 10),
            width=28, height=10, padx=6, pady=6,
        )
        self.screen.pack()

    
        self.msg_var = tk.StringVar(value="")
        self.msg_label = tk.Label(self.root, textvariable=self.msg_var,
                                   bg=BG_SHELL, fg="white",
                                   font=("DejaVu Sans", 9, "italic"))
        self.msg_label.pack(pady=(0, 2))

        # Barra de stats
        self.stats_var = tk.StringVar(value="")
        stats_label = tk.Label(self.root, textvariable=self.stats_var,
                                bg=BG_SHELL, fg="white",
                                font=("DejaVu Sans Mono", 9))
        stats_label.pack(pady=(0, 8))


        btn_row = tk.Frame(self.root, bg=BG_SHELL)
        btn_row.pack(pady=(0, 14))

        self._make_circle_button(btn_row, "♥", "Amor (1)", self.love).grid(row=0, column=0, padx=14)
        self._make_circle_button(btn_row, "🍽", "Comer (2)", self.feed).grid(row=0, column=1, padx=14)
        self.sleep_canvas = self._make_circle_button(btn_row, "☾", "Dormir (3)", self.toggle_sleep)
        self.sleep_canvas.grid(row=0, column=2, padx=14)

        self._update_stats_label()

    def _make_circle_button(self, parent, symbol, tooltip, command):
        size = 46
        c = tk.Canvas(parent, width=size, height=size, bg=BG_SHELL,
                       highlightthickness=0, cursor="hand2")
        c.create_oval(2, 2, size - 2, size - 2, fill=BTN_BLUE, outline=BTN_BLUE_DARK, width=2)
        c.create_text(size / 2, size / 2, text=symbol, font=("DejaVu Sans", 16))
        c.bind("<Button-1>", lambda e: command())
        return c

    def _position_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width() or 300
        h = self.root.winfo_height() or 380
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = sw - w - 40
        y = sh - h - 60
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    # -- mover ventana arrastrando --------------------------------------

    def _start_move(self, event):
        self._drag_x = event.x
        self._drag_y = event.y

    def _do_move(self, event):
        x = self.root.winfo_x() + (event.x - self._drag_x)
        y = self.root.winfo_y() + (event.y - self._drag_y)
        self.root.geometry(f"+{x}+{y}")



    def _catch_up_time(self):

        now = time.time()
        elapsed_min = (now - self.state.get("last_tick", now)) / 60.0
        elapsed_min = max(0, min(elapsed_min, 24 * 60))  
        ticks = int(elapsed_min)  
        if ticks <= 0:
            self.state["last_tick"] = now
            return
        if self.state.get("sleeping"):
            self.state["energy"] = clamp(self.state["energy"] + ENERGY_REGEN_SLEEP * ticks)
        else:
            self.state["hunger"] = clamp(self.state["hunger"] - HUNGER_DECAY * ticks)
            self.state["happiness"] = clamp(self.state["happiness"] - HAPPY_DECAY * ticks)
            self.state["energy"] = clamp(self.state["energy"] - ENERGY_DECAY * ticks)
        self.state["last_tick"] = now

    def _tick(self):
        if self.state.get("sleeping"):
            self.state["energy"] = clamp(self.state["energy"] + ENERGY_REGEN_SLEEP)
        else:
            self.state["hunger"] = clamp(self.state["hunger"] - HUNGER_DECAY)
            self.state["happiness"] = clamp(self.state["happiness"] - HAPPY_DECAY)
            self.state["energy"] = clamp(self.state["energy"] - ENERGY_DECAY)
            if self.state["hunger"] < 20:
                self.msg_var.set("¡Tengo hambre! 🍽")
            elif self.state["happiness"] < 20:
                self.msg_var.set("Caramelo se siente solo... dale amor ♥")
        self.state["last_tick"] = time.time()
        self._update_stats_label()
        save_state(self.state)
        self.root.after(TICK_MS, self._tick)

    def _update_stats_label(self):
        s = self.state
        self.stats_var.set(
            f"♥{s['happiness']:>3}  🍽{s['hunger']:>3}  🗲{s['energy']:>3}"
        )

    def _set_art(self, art):
        self.screen.config(text=art)

    def _cancel_pending_revert(self):
        if self._revert_job is not None:
            self.root.after_cancel(self._revert_job)
            self._revert_job = None

    def _refresh_screen(self, message=""):
        if self.state.get("sleeping"):
            self._set_art(SLEEP_ART)
        else:
            self._set_art(DEFAULT_ART)
        if message:
            self.msg_var.set(message)
        self._update_stats_label()

    
    def feed(self):
        if self.state.get("sleeping"):
            self.msg_var.set("Shh... está durmiendo zzz")
            return
        self.state["hunger"] = clamp(self.state["hunger"] + FEED_HUNGER_GAIN)
        self.state["happiness"] = clamp(self.state["happiness"] + FEED_HAPPY_GAIN)
        save_state(self.state)
        self._update_stats_label()
        self._set_art(EATING_ART)
        self.msg_var.set("¡Ñam ñam! ")
        self._cancel_pending_revert()
        self._revert_job = self.root.after(EAT_ANIM_MS, lambda: self._refresh_screen(""))

    def love(self):
        if self.state.get("sleeping"):
            self.msg_var.set("Shh... está durmiendo zzz")
            return
        self.state["happiness"] = clamp(self.state["happiness"] + LOVE_HAPPY_GAIN)
        save_state(self.state)
        self._update_stats_label()
        self.msg_var.set("¡Le encantó el cariño! ♥")
        self._flash_screen()

    def _flash_screen(self):
     
        self.screen.config(bg="#f2c6d9")
        if self._flash_job is not None:
            self.root.after_cancel(self._flash_job)
        self._flash_job = self.root.after(300, lambda: self.screen.config(bg=SCREEN_BG))

    def toggle_sleep(self):
        self._cancel_pending_revert()
        if self.state.get("sleeping"):
            self.state["sleeping"] = False
            self.state["energy"] = clamp(self.state["energy"] + WAKE_ENERGY_GAIN)
            save_state(self.state)
            self._refresh_screen("¡Buenos días! ˗ˏˋ ★ ˎˊ˗ ")
        else:
            self.state["sleeping"] = True
            save_state(self.state)
            self._refresh_screen("Zzz... durmiendo zzz")

    def quit(self):
        self.state["last_tick"] = time.time()
        save_state(self.state)
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    TamagotchiWidget().run()