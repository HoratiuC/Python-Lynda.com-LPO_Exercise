from tkinter import *
from tkinter import ttk
from lpoData import all_years_air_temp_mean, all_years_air_temp_median, all_years_barom_press_mean, all_years_barom_press_median, y2012_air_temp_mean, y2012_air_temp_median, y2012_barom_press_mean, y2012_barom_press_median, y2013_air_temp_mean, y2013_air_temp_median, y2013_barom_press_mean, y2013_barom_press_median, y2014_air_temp_mean, y2014_air_temp_median, y2014_barom_press_mean, y2014_barom_press_median, y2015_air_temp_mean, y2015_air_temp_median, y2015_barom_press_mean, y2015_barom_press_median

class LPO:

    def __init__(self, master):
        master.title('Lake Pend Oreille')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')

        #configure GUI style
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Times New Roman',12))
        self.style.configure('Header.TLabel', font = ('Times New Roman',14, 'bold'))

        #create header frame
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'C:\\Users\\HoratiuC\\Documents\\diverse\\prog\\lpo\\lpo_logo.gif')        
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0)
        ttk.Label(self.frame_header, text = 'LPO 2012 - 2015 Data', style = 'Header.TLabel').grid(row = 0, column = 1)

        #create content frame
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Choose year:', style = 'Header.TLabel').grid(row = 0, column = 0)
        self.years = StringVar()
        self.combo = ttk.Combobox(self.frame_content, textvariable = self.years, values = ("2012", "2013", "2014", "2015","All years"))
        self.combo.grid(row = 0, column =1)
        ttk.Button(self.frame_content, text = 'Submit', command = self.callback, style = 'TButton').grid(row = 1, column = 0, columnspan = 2)
       
        #create results frame
        self.frame_results = ttk.Frame(master)        

        ttk.Label(self.frame_results, text = 'Air Temperature Mean:', style = 'Header.TLabel').grid(row = 0, column = 0, padx = 5)        
        ttk.Label(self.frame_results, text = 'Air Temperature Median:', style = 'Header.TLabel').grid(row = 1, column = 0, padx = 5)
        ttk.Label(self.frame_results, text = 'Barometric Pressure Mean:', style = 'Header.TLabel').grid(row = 2, column = 0, padx = 5)        
        ttk.Label(self.frame_results, text = 'Barometric Pressure Median:', style = 'Header.TLabel').grid(row = 3, column = 0, padx = 5)

        self.air_mean = StringVar()
        self.air_median = StringVar()
        self.barom_mean = StringVar()
        self.barom_median = StringVar()

        ttk.Label(self.frame_results, textvariable = self.air_mean).grid(row = 0, column = 1)
        ttk.Label(self.frame_results, textvariable = self.air_median).grid(row = 1, column = 1)  
        ttk.Label(self.frame_results, textvariable = self.barom_mean).grid(row = 2, column = 1)
        ttk.Label(self.frame_results, textvariable = self.barom_median).grid(row = 3, column = 1)       
        
    
    def callback(self):
        if self.combo.get() == '2012':
            y1 = y2012_air_temp_mean()
            y2 = y2012_air_temp_median()
            y3 = y2012_barom_press_mean()
            y4 = y2012_barom_press_median()
            self.air_mean.set('{0:.2f}'.format(y1))
            self.air_median.set('{0:.2f}'.format(y2))
            self.barom_mean.set('{0:.2f}'.format(y3))
            self.barom_median.set('{0:.2f}'.format(y4))
        if self.combo.get() == '2013':
            y1 = y2013_air_temp_mean()
            y2 = y2013_air_temp_median()
            y3 = y2013_barom_press_mean()
            y4 = y2013_barom_press_median()
            self.air_mean.set('{0:.2f}'.format(y1))
            self.air_median.set('{0:.2f}'.format(y2))
            self.barom_mean.set('{0:.2f}'.format(y3))
            self.barom_median.set('{0:.2f}'.format(y4))
        if self.combo.get() == '2014':
            y1 = y2014_air_temp_mean()
            y2 = y2014_air_temp_median()
            y3 = y2014_barom_press_mean()
            y4 = y2014_barom_press_median()
            self.air_mean.set('{0:.2f}'.format(y1))
            self.air_median.set('{0:.2f}'.format(y2))
            self.barom_mean.set('{0:.2f}'.format(y3))
            self.barom_median.set('{0:.2f}'.format(y4))
        if self.combo.get() == '2015':
            y1 = y2015_air_temp_mean()
            y2 = y2015_air_temp_median()
            y3 = y2015_barom_press_mean()
            y4 = y2015_barom_press_median()
            self.air_mean.set('{0:.2f}'.format(y1))
            self.air_median.set('{0:.2f}'.format(y2))
            self.barom_mean.set('{0:.2f}'.format(y3))
            self.barom_median.set('{0:.2f}'.format(y4))
        if self.combo.get() == 'All years':
            y1 = all_years_air_temp_mean()
            y2 = all_years_air_temp_median()
            y3 = all_years_barom_press_mean()
            y4 = all_years_barom_press_median()
            self.air_mean.set('{0:.2f}'.format(y1))
            self.air_median.set('{0:.2f}'.format(y2))
            self.barom_mean.set('{0:.2f}'.format(y3))
            self.barom_median.set('{0:.2f}'.format(y4))
        self.frame_results.pack(side = TOP)
        
def main():
    root = Tk()
    lpo = LPO(root)
    root.mainloop()

if __name__ == "__main__": main()