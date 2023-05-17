import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.root.resizable(False, False)

        self.minutes = 0
        self.seconds = 0
        self.paused = False
        self.timer_running = False
        self.time_limit = 0

        self.time_label = tk.Label(
            self.root,
            text=self.get_time_formatted(),
            font=("Helvetica", 48),
            padx=10,
            pady=5
        )
        self.time_label.pack()

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.minutes_label = tk.Label(
            self.entry_frame,
            text="Minutes:",
            font=("Helvetica", 14)
        )
        self.minutes_label.grid(row=0, column=0)

        self.minutes_entry = tk.Entry(
            self.entry_frame,
            font=("Helvetica", 14),
            width=5
        )
        self.minutes_entry.grid(row=0, column=1, padx=5)

        self.seconds_label = tk.Label(
            self.entry_frame,
            text="Seconds:",
            font=("Helvetica", 14)
        )
        self.seconds_label.grid(row=0, column=2)

        self.seconds_entry = tk.Entry(
            self.entry_frame,
            font=("Helvetica", 14),
            width=5
        )
        self.seconds_entry.grid(row=0, column=3, padx=5)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(
            self.button_frame,
            text="Start",
            command=self.start_timer,
            font=("Helvetica", 14)
        )
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(
            self.button_frame,
            text="Pause",
            command=self.pause_timer,
            state=tk.DISABLED,
            font=("Helvetica", 14)
        )
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(
            self.button_frame,
            text="Reset",
            command=self.reset_timer,
            font=("Helvetica", 14)
        )
        self.reset_button.grid(row=0, column=2, padx=5)

        self.stop_button = tk.Button(
            self.button_frame,
            text="Stop",
            command=self.stop_timer,
            state=tk.DISABLED,
            font=("Helvetica", 14)
        )
        self.stop_button.grid(row=0, column=3, padx=5)

        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)

    def get_time_formatted(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

    def start_timer(self):
        if not self.timer_running:
            self.minutes = int(self.minutes_entry.get())
            self.seconds = int(self.seconds_entry.get())

            if self.minutes < 0 or self.seconds < 0:
                messagebox.showwarning("Invalid Time", "Please enter a valid time.")
                return

            self.time_limit = self.minutes * 60 + self.seconds

            if self.time_limit == 0:
                messagebox.showwarning("Invalid Time", "Please enter a non-zero time.")
                return

            self.start_button.configure(state=tk.DISABLED)
            self.pause_button.configure(state=tk.NORMAL)
            self.stop_button.configure(state=tk.NORMAL)

            self.timer_running = True
            self.update_timer()

    def pause_timer(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.configure(text="Resume")
        else:
            self.pause_button.configure(text="Pause")
            self.update_timer()

    def reset_timer(self):
        self.minutes_entry.delete(0, tk.END)
        self.seconds_entry.delete(0, tk.END)
        self.start_button.configure(state=tk.NORMAL)
        self.pause_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.DISABLED)
        self.timer_running = False
        self.paused = False
        self.minutes = 0
        self.seconds = 0
        self.time_limit = 0
        self.time_label.configure(text=self.get_time_formatted())

    def stop_timer(self):
        self.timer_running = False
        self.root.destroy()

    def update_timer(self):
        if self.timer_running and not self.paused:
            if self.time_limit == 0:
                self.timer_running = False
                messagebox.showinfo("Countdown Timer", "Time's up!")
                self.reset_timer()
            else:
                self.time_limit -= 1
                self.minutes = self.time_limit // 60
                self.seconds = self.time_limit % 60

        self.time_label.configure(text=self.get_time_formatted())

        if self.timer_running:
            self.root.after(1000, self.update_timer)

    def confirm_exit(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()


# Create the CountdownTimer class and run the timer
timer = CountdownTimer()
timer.run()
