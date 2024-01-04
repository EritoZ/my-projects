import datetime
import tkinter as tk


class TimeStopper:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('500x400')
        self.root.title('Clock Stopper')

        self.clock = tk.Label(self.root)
        self.clock.pack(pady=100)

        self.button_pause_or_start = tk.Button(self.root,
                                               text='Pause/Start',
                                               font=('Arial', 15),
                                               command=self.toggle_pause,)
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

    def create_timedelta_from_now(self):
        now = datetime.datetime.now()

        return datetime.timedelta(hours=now.hour, minutes=now.minute,
                                  seconds=now.second, milliseconds=now.microsecond // 1000)

    def update_time(self):

        if not self.paused:
            time = self.create_timedelta_from_now()

            time -= self.time_difference

            self.clock.config(text=str(time)[:-3], font=('Arial', 20))

        self.root.after(10, self.update_time)

    def toggle_pause(self):
        if not self.paused:
            self.paused = True
            self.paused_time = self.create_timedelta_from_now()

            return

        self.time_difference += self.create_timedelta_from_now() - self.paused_time
        self.paused = False

    def reset_time(self):
        self.time_difference = datetime.timedelta(hours=0, minutes=0, seconds=0, milliseconds=0)
        self.paused_time = self.create_timedelta_from_now()
        self.clock.config(text=str(self.paused_time)[:-3], font=('Arial', 20))


TimeStopper()
