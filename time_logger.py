import datetime
import tkinter as tk


class TimeLogger:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('500x400')
        self.root.title('Time Logger')

        self.clock = tk.Label(self.root)
        self.clock.pack(pady=(10, 0))

        self.text_box_with_times = tk.Text(self.root,
                                           width=40, height=10,
                                           state='disabled')
        self.text_box_with_times.pack()

        self.text_box_with_times.tag_configure('bigger_font', font=('Arial', 12))
        self.text_box_with_times.tag_configure('spaced', spacing3=4)

        self.log_button = tk.Button(self.root,
                                    text='Log',
                                    font=('Arial', 15),
                                    command=self.log_time)
        self.log_button.pack(pady=10, ipadx=9)

        self.reset_button = tk.Button(self.root,
                                      text='Reset',
                                      font=('Arial', 15),
                                      command=self.reset)
        self.reset_button.pack()

        self.update_time()

        self.root.mainloop()

    @staticmethod
    def enable_text_box_action(f):
        def wrapper(self):
            self.text_box_with_times.config(state='normal')
            result = f(self)
            self.text_box_with_times.config(state='disabled')

            return result

        return wrapper

    def update_time(self):
        time = datetime.datetime.now()

        self.clock.config(text=time.strftime('%H:%M:%S:%f')[:-3], font=('Arial', 20))

        self.root.after(2, self.update_time)

    @enable_text_box_action
    def log_time(self):
        self.text_box_with_times.insert('end', self.clock.cget('text') + '\n')
        self.text_box_with_times.tag_add('bigger_font', "end-2c linestart", "end")
        self.text_box_with_times.tag_add('spaced', "end-2c linestart", "end")
        self.text_box_with_times.see('end')

    @enable_text_box_action
    def reset(self):
        self.text_box_with_times.delete('1.0', tk.END)


if __name__ == "__main__":
    TimeLogger()
