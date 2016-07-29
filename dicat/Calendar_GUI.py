__author__ = 'cmadjar'

from Tkinter import *
import ttk


class CalendarFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.parent = parent

        self.draw_weekly_calendar()

    def draw_weekly_calendar(self):

        self.day_frame = ttk.Frame(self.parent)
        self.time_frame = ttk.Frame(self.parent)

        self.day_frame.pack(expand=1, fill='both')
        self.time_frame.pack(expand=1, fill='both')

        self.draw_week_day_frame()
        self.draw_time_frame()

    def draw_week_day_frame(self):

        # Initialize day variables
        self.mon_var = StringVar()
        self.tue_var = StringVar()
        self.wed_var = StringVar()
        self.thu_var = StringVar()
        self.fri_var = StringVar()
        self.sat_var = StringVar()
        self.sun_var = StringVar()

        # Set the day variables to Day of the week for now
        # TODO: grep the full day information (DD-MM-YYYY)
        self.mon_var.set('Monday')
        self.tue_var.set('Tuesday')
        self.wed_var.set('Wednesday')
        self.thu_var.set('Thursday')
        self.fri_var.set('Friday')
        self.sat_var.set('Saturday')
        self.sun_var.set('Sunday')

        # Create day widgets the top row content
        self.mon = ttk.Label(self.day_frame, textvariable=self.mon_var, width=9)
        self.tue = ttk.Label(self.day_frame, textvariable=self.tue_var, width=9)
        self.wed = ttk.Label(self.day_frame, textvariable=self.wed_var, width=9)
        self.thu = ttk.Label(self.day_frame, textvariable=self.thu_var, width=9)
        self.fri = ttk.Label(self.day_frame, textvariable=self.fri_var, width=9)
        self.sat = ttk.Label(self.day_frame, textvariable=self.sat_var, width=9)
        self.sun = ttk.Label(self.day_frame, textvariable=self.sun_var, width=9)

        # Draw the day
        # padx=(99,5) for monday to push it to the right so that monday column
        # does not end up with the displayed hours
        self.mon.grid(row=0, column=1, padx=(99,5), pady=5, sticky=N+S+E+W)
        self.tue.grid(row=0, column=2, padx=5, pady=5, sticky=N+S+E+W)
        self.wed.grid(row=0, column=3, padx=5, pady=5, sticky=N+S+E+W)
        self.thu.grid(row=0, column=4, padx=5, pady=5, sticky=N+S+E+W)
        self.fri.grid(row=0, column=5, padx=5, pady=5, sticky=N+S+E+W)
        self.sat.grid(row=0, column=6, padx=5, pady=5, sticky=N+S+E+W)
        self.sun.grid(row=0, column=7, padx=5, pady=5, sticky=N+S+E+W)

    def draw_time_frame(self):

        # Create hours widget that will be written on the first column of
        # the self.time_frame frame
        self.h00am00 = ttk.Label(self.time_frame, text='00:00 AM')
        self.h01am00 = ttk.Label(self.time_frame, text='01:00 AM')
        self.h02am00 = ttk.Label(self.time_frame, text='02:00 AM')
        self.h03am00 = ttk.Label(self.time_frame, text='03:00 AM')
        self.h04am00 = ttk.Label(self.time_frame, text='04:00 AM')
        self.h05am00 = ttk.Label(self.time_frame, text='05:00 AM')
        self.h06am00 = ttk.Label(self.time_frame, text='06:00 AM')
        self.h07am00 = ttk.Label(self.time_frame, text='07:00 AM')
        self.h08am00 = ttk.Label(self.time_frame, text='08:00 AM')
        self.h09am00 = ttk.Label(self.time_frame, text='09:00 AM')
        self.h10am00 = ttk.Label(self.time_frame, text='10:00 AM')
        self.h11am00 = ttk.Label(self.time_frame, text='11:00 AM')
        self.h12pm00 = ttk.Label(self.time_frame, text='Noon    ')
        self.h01pm00 = ttk.Label(self.time_frame, text='01:00 PM')
        self.h02pm00 = ttk.Label(self.time_frame, text='02:00 PM')
        self.h03pm00 = ttk.Label(self.time_frame, text='03:00 PM')
        self.h04pm00 = ttk.Label(self.time_frame, text='04:00 PM')
        self.h05pm00 = ttk.Label(self.time_frame, text='05:00 PM')
        self.h06pm00 = ttk.Label(self.time_frame, text='06:00 PM')
        self.h07pm00 = ttk.Label(self.time_frame, text='07:00 PM')
        self.h08pm00 = ttk.Label(self.time_frame, text='08:00 PM')
        self.h09pm00 = ttk.Label(self.time_frame, text='09:00 PM')
        self.h10pm00 = ttk.Label(self.time_frame, text='10:00 PM')
        self.h11pm00 = ttk.Label(self.time_frame, text='11:00 PM')

        # Draw the times
        self.h00am00.grid(row=1,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h01am00.grid(row=2,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h03am00.grid(row=3,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h04am00.grid(row=4,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h05am00.grid(row=5,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h06am00.grid(row=6,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h07am00.grid(row=7,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h08am00.grid(row=8,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h09am00.grid(row=9,  column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h10am00.grid(row=10, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h11am00.grid(row=11, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h12pm00.grid(row=12, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h01pm00.grid(row=13, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h02pm00.grid(row=14, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h03pm00.grid(row=15, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h04pm00.grid(row=16, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h05pm00.grid(row=17, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h06pm00.grid(row=18, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h07pm00.grid(row=19, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h08pm00.grid(row=20, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h09pm00.grid(row=21, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h10pm00.grid(row=22, column=0, padx=5, pady=5, sticky=N+S+E+W)
        self.h11pm00.grid(row=23, column=0, padx=5, pady=5, sticky=N+S+E+W)

def main():
    root = Tk()
    root.wm_title("Calendar Test")
    CalendarFrame(root).pack()
    root.mainloop()

if __name__ == "__main__":
    main()