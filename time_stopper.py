import datetime
import tkinter as tk


class TimeStopper:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('500x400')
        self.root.title('Time Stopper')

        self.clock = tk.Label(self.root)
        self.clock.pack(pady=100)

        self.button_pause_or_start = tk.Button(self.root,
                                               text='Pause/Start',
                                               font=('Arial', 15),
                                               command=self.toggle_pause)
        self.button_pause_or_start.pack()

        self.button_reset = tk.Button(self.root,
                                      text='Reset Time',
                                      font=('Arial', 15),
                                      command=self.reset_time)
        self.button_reset.pack(pady=(10, 0), ipadx=2.5)

        self.paused = False
        self.paused_time = None
        self.time_difference = datetime.timedelta(hours=0, minutes=0, seconds=0, milliseconds=0)
        self.update_time()

        self.root.mainloop()

    def update_time(self):
        if not self.paused:
            time = datetime.datetime.now()

            time -= self.time_difference

            self.clock.config(text=time.strftime('%H:%M:%S:%f')[:-3], font=('Arial', 20))

        self.root.after(2, self.update_time)

    def toggle_pause(self):
        if not self.paused:
            self.paused = True
            self.paused_time = datetime.datetime.now()

            return

        self.time_difference += datetime.datetime.now() - self.paused_time
        self.paused = False

    def reset_time(self):
        self.time_difference = datetime.timedelta(hours=0, minutes=0, seconds=0, milliseconds=0)
        self.paused = False


if __name__ == "__main__":
    TimeStopper()
