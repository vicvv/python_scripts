import tkinter as tk


class Histogram:
    # constructor
    def __init__(self, mstr_rt=None):

        # -------------- store root reference locally --------------
        stand_in = tk.Tk()
        self.set_root(stand_in)

        # -------------- one message widget ------------------------
        header = "Graphic Title"
        self.msg_head = tk.Message(self.root, text=header)
        self.msg_head.config(font=("times", 12, "bold"), width=300)

        # ----------------- some button widgets ------------------
        self.but_4201 = tk.Button(self.root, text="Filter 4201 ON",command=lambda: self.toggle_filter_list(1), bg="Green")
        self.but_4204 = tk.Button(self.root, text="Filter 4204 ON", command=lambda: self.toggle_filter_list(2), bg="Green")
        self.but_4205 = tk.Button(self.root, text="Filter 4205 ON",command=lambda: self.toggle_filter_list(4), bg="Green")
        self.but_4213 = tk.Button(self.root, text="Filter 4213 ON",command=lambda: self.toggle_filter_list(0), bg="Green")
        self.but_4218 = tk.Button(self.root, text="Filter 4218 ON",command=lambda: self.toggle_filter_list(3), bg="Green")
        self.but_Out = tk.Button(self.root, text="Filter Out ON",command=lambda: self.toggle_filter_list(5), bg="Green")
        # self.but_add = tk.Button(self.root, text = "Add")
        # self.but_add.config(command = self.update_answer)

        # ------------ place all widgets using grid layout -------------
        self.msg_head.grid(row=0, column=2, columnspan=3, sticky=tk.EW)

        self.but_4201.grid(row=1, column=0, padx=5, sticky=tk.EW)
        self.but_4204.grid(row=2, column=0, padx=5, sticky=tk.EW)
        self.but_4205.grid(row=3, column=0, padx=5, sticky=tk.EW)
        self.but_4213.grid(row=4, column=0, padx=5, sticky=tk.EW)
        self.but_4218.grid(row=5, column=0, padx=5, sticky=tk.EW)
        self.but_Out.grid(row=6, column=0, padx=5, sticky=tk.EW)



    # mutators
    def set_root(self, rt):
        if Histogram.valid_tk_root(rt):
            self.root = rt
            return True
        # else
        return False

    def set_title(self, title):
        if type(title) == str:
            self.root.title = title
            return True
        # else
        return False

    # accessor
    def get_root(self):
        return self.root

    # static helper
    @staticmethod
    def valid_tk_root(am_i_a_root):
        if type(am_i_a_root) == tk.Tk:
            return True
        else:
            return False

    def toggle_filter_list(self, sensor_num):
        # print(filter_list)
        global filter_list
        if sensor_num in filter_list:
            del filter_list[filter_list.index(sensor_num)]
            if sensor_num == 0:
                self.but_4213.config(text="Filter 4213 OFF", bg="Red")
            elif sensor_num == 1:
                self.but_4201.config(text="Filter 4201 OFF", bg="Red")
            elif sensor_num == 2:
                self.but_4204.config(text="Filter 4204 OFF", bg="Red")
            elif sensor_num == 3:
                self.but_4218.config(text="Filter 4218 OFF", bg="Red")
            elif sensor_num == 4:
                self.but_4205.config(text="Filter 4205 OFF", bg="Red")
            elif sensor_num == 5:
                self.but_Out.config(text="Filter Out  OFF", bg="Red")
        else:
            filter_list.append(sensor_num)
            if sensor_num == 0:
                self.but_4213.config(text="Filter 4213 ON", bg="Green")
            elif sensor_num == 1:
                self.but_4201.config(text="Filter 4201 ON", bg="Green")
            elif sensor_num == 2:
                self.but_4204.config(text="Filter 4204 ON", bg="Green")
            elif sensor_num == 3:
                self.but_4218.config(text="Filter 4218 ON", bg="Green")
            elif sensor_num == 4:
                self.but_4205.config(text="Filter 4205 ON", bg="Green")
            elif sensor_num == 5:
                self.but_Out.config(text="Filter Out  ON", bg="Green")


# client program  -----------------------------------------

root_win = tk.Tk()
filter_list = [0, 1, 2, 3, 4, 5]
demo_cls_ref = Histogram(root_win)

demo_cls_ref.get_root().title("Histogram")
demo_cls_ref.get_root().mainloop()