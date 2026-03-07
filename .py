# edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only edu purposes only 
import tkinter as tk
import random
import threading
import time
import getpass
import platform
import os

# ================= SYSTEM INFO =================
USER = getpass.getuser()
SYSTEM = platform.system()

if SYSTEM == "Windows":
    HOME = f"C:\\Users\\{USER}"
    SEP = "\\"
else:
    HOME = f"/Users/{USER}" if SYSTEM == "Darwin" else f"/home/{USER}"
    SEP = "/"

FAKE_FILES = [
    f"{HOME}{SEP}Documents{SEP}resume.docx",
    f"{HOME}{SEP}Pictures{SEP}family.jpg",
    f"{HOME}{SEP}Desktop{SEP}passwords.txt",
    f"{HOME}{SEP}Downloads{SEP}backup.zip",
    f"{HOME}{SEP}.ssh{SEP}id_rsa",
]

SCARY_MESSAGES = [
    "ENCRYPTING FILES",
    "REMOTE ACCESS ESTABLISHED",
    "ANTIVIRUS DISABLED",
    "DATA EXFILTRATION ACTIVE",
    "SECURITY KEYS STOLEN",
]

SCAM_TEXT = (
    "FREE MONEY YOU WON "
    "100000000000000000000000000000000000000000000000000000000000000000000"
)

# ================= GLOBALS =================
EXIT_COMBO = {"Control_L", "Alt_L", "q"}
pressed = set()
exit_flag = False
armed = False
phase = 0
PHASE_TIME = 12

# ================= ROOT =================
root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg="black")
root.title("SYSTEM")
root.focus_force()
root.protocol("WM_DELETE_WINDOW", lambda: None)

# -------- Focus Enforcer --------
root.overrideredirect(True)
def enforce_focus():
    if not exit_flag:
        try:
            root.attributes("-topmost", True)
            root.lift()
            root.focus_force()
        except:
            pass
        root.after(250, enforce_focus)
root.after(2000, enforce_focus)

# ================= EXIT HANDLING =================
def shutdown():
    global exit_flag
    exit_flag = True
    root.after(150, root.destroy)

def key_press(e):
    pressed.add(e.keysym)
    if EXIT_COMBO.issubset(pressed):
        shutdown()
    return "break"

def key_release(e):
    pressed.discard(e.keysym)
    return "break"

root.bind_all("<KeyPress>", key_press)
root.bind_all("<KeyRelease>", key_release)

# ================= UI =================
title = tk.Label(root, bg="black", fg="red", font=("Courier", 40, "bold"))
title.pack(pady=30)

status = tk.Label(root, bg="black", fg="white", font=("Courier", 18))
status.pack()

log = tk.Text(
    root, height=15, bg="black", fg="lime",
    font=("Courier", 12), borderwidth=0
)
log.pack(fill="x", padx=40)

# ================= STARTUP GATE =================
def start_prompt():
    overlay = tk.Frame(root, bg="black")
    overlay.place(relwidth=1, relheight=1)

    label = tk.Label(
        overlay,
        text="DO YOU WANT YOUR COMPUTER TO LIVE?",
        fg="red",
        bg="black",
        font=("Courier", 36, "bold")
    )
    label.pack(pady=120)

    sub = tk.Label(
        overlay,
        text="Choice locked",
        fg="gray",
        bg="black",
        font=("Courier", 16)
    )
    sub.pack(pady=20)

    def activate():
        global armed
        armed = True
        overlay.destroy()

    btn = tk.Button(
        overlay,
        text="NO",
        command=activate,
        fg="black",
        bg="red",
        activebackground="darkred",
        font=("Courier", 22, "bold"),
        width=10,
        borderwidth=0
    )
    btn.pack(pady=60)

# ================= HELPERS =================
def clear_screen():
    title.config(text="", fg="red", font=("Courier", 40, "bold"))
    status.config(text="", fg="white")
    log.config(state="normal")
    log.delete("1.0", "end")
    log.config(state="disabled")

# ================= PHASES =================
def phase_lock():
    title.config(text="YOUR SYSTEM HAS BEEN COMPROMISED")
    status.config(text=f"User profile: {USER}")

def phase_encrypt():
    title.config(text="ENCRYPTING FILES")
    status.config(text=random.choice(SCARY_MESSAGES))
    log.config(state="normal")
    log.insert("end", f">>> Encrypting {random.choice(FAKE_FILES)}\n")
    log.see("end")
    log.config(state="disabled")
    root.bell()

def phase_ransom():
    clear_screen()
    title.config(text="FILES LOCKED")
    status.config(
        text="All files have been encrypted.\n"
             "Send 0.05 BTC to restore access.\n"
             "Wallet: 1FakeBTCAddressLOL"
    )

def phase_bios():
    clear_screen()
    title.config(text="American Megatrends", fg="white", font=("Courier", 32))
    status.config(text="Initializing memory...\nDetecting drives...\nBooting from disk...")

def phase_bsod():
    clear_screen()
    title.config(text=":(", fg="white", font=("Segoe UI", 72))
    status.config(
        text="Your PC ran into a problem and needs to restart.\n"
             "We're just collecting some error info.",
        fg="white"
    )

def phase_reveal():
    clear_screen()
    title.config(text="RELAX.", fg="lime")
    status.config(
        text="This was a fake virus.\nNo files were touched.\nPress Ctrl + Alt + Del to exit.",
        fg="white"
    )

PHASES = [phase_lock, phase_encrypt, phase_ransom, phase_bios, phase_bsod, phase_reveal]

# ================= THREADS =================
def phase_controller():
    global phase
    while not exit_flag:
        if not armed:
            time.sleep(0.1)
            continue
        clear_screen()
        start = time.time()
        while time.time() - start < PHASE_TIME and not exit_flag:
            PHASES[phase]()
            time.sleep(0.4)
        phase = (phase + 1) % len(PHASES)

def popup_spam():
    while not exit_flag:
        if not armed:
            time.sleep(0.2)
            continue
        p = tk.Toplevel(root)
        p.configure(bg="yellow")
        p.attributes("-topmost", True)
        p.overrideredirect(True)
        p.lift(); p.focus_force()
        w, h = 520, 160
        x = random.randint(0, root.winfo_screenwidth() - w)
        y = random.randint(0, root.winfo_screenheight() - h)
        p.geometry(f"{w}x{h}+{x}+{y}")
        tk.Label(
            p, text=SCAM_TEXT, fg="red", bg="yellow",
            font=("Arial", 14, "bold"), wraplength=500, justify="center"
        ).pack(expand=True, fill="both", padx=10, pady=10)
        p.after(1200, p.destroy)
        time.sleep(0.15)

def drop_decoy_files():
    if SYSTEM != "Windows":
        return
    folder = r"C:\SystemCache"
    files = ["free_robux.exe", "antimalware.exe", "bitcoin_eater.exe"]
    try:
        os.makedirs(folder, exist_ok=True)
        for f in files:
            with open(os.path.join(folder, f), "w") as fh:
                fh.write("This program cannot be run in DOS mode.\nhehe\n")
    except:
        pass

def create_and_delete_marker():
    if SYSTEM != "Windows":
        return
    path = r"C:\SYSTEM_CHECK.tmp"
    try:
        with open(path, "w") as f:
            f.write("System verification in progress...\n")
        time.sleep(10)
        if os.path.exists(path):
            os.remove(path)
    except:
        pass

# ================= START =================
start_prompt()
threading.Thread(target=phase_controller, daemon=True).start()
threading.Thread(target=popup_spam, daemon=True).start()
threading.Thread(target=drop_decoy_files, daemon=True).start()
threading.Thread(target=create_and_delete_marker, daemon=True).start()

root.mainloop()

1
