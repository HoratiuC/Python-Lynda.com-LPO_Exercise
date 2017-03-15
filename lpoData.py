from statistics import mean, median

#open csv file containing data
with open ('C:\\Users\\HoratiuC\\Documents\\diverse\\prog\\lpo\\lpo_data.csv','r+') as f:
    l = f.read().split('\n')
all_years = []
for i in l:
    all_years.append(i.split(','))

#create separate lists for each year
y2012 = [all_years[i] for i in range(len(all_years)-1) if all_years[i][0] == '2012']
y2013 = [all_years[i] for i in range(len(all_years)-1) if all_years[i][0] == '2013']
y2014 = [all_years[i] for i in range(len(all_years)-1) if all_years[i][0] == '2014']
y2015 = [all_years[i] for i in range(len(all_years)-1) if all_years[i][0] == '2015']

#create list with air temperatures for each year
air_temp = [float(all_years[i][1]) for i in range(1,len(all_years)-1)]
air_temp2012 = [float(y2012[i][1]) for i in range(len(y2012))]
air_temp2013 = [float(y2013[i][1]) for i in range(len(y2013))]
air_temp2014 = [float(y2014[i][1]) for i in range(len(y2014))]
air_temp2015 = [float(y2015[i][1]) for i in range(len(y2015))]

#create list with barometrci pressures for each year
barom_press = [float(all_years[i][2]) for i in range(1,len(all_years)-1)]
barom_press2012 = [float(y2012[i][2]) for i in range(len(y2012))]
barom_press2013 = [float(y2013[i][2]) for i in range(len(y2013))]
barom_press2014 = [float(y2014[i][2]) for i in range(len(y2014))]
barom_press2015 = [float(y2015[i][2]) for i in range(len(y2015))]

#define functions for mean and median for each year and all years

def all_years_air_temp_mean():
    return mean(air_temp)
def all_years_air_temp_median():
    return median(air_temp)
def all_years_barom_press_mean():
    return mean(barom_press)
def all_years_barom_press_median():
    return median(barom_press)

def y2012_air_temp_mean():
    return mean(air_temp2012)
def y2012_air_temp_median():
    return median(air_temp2012)
def y2012_barom_press_mean():
    return mean(barom_press2012)
def y2012_barom_press_median():
    return median(barom_press2012)

def y2013_air_temp_mean():
    return mean(air_temp2013)
def y2013_air_temp_median():
    return median(air_temp2013)
def y2013_barom_press_mean():
    return mean(barom_press2013)
def y2013_barom_press_median():
    return median(barom_press2013)

def y2014_air_temp_mean():
    return mean(air_temp2014)
def y2014_air_temp_median():
    return median(air_temp2014)
def y2014_barom_press_mean():
    return mean(barom_press2014)
def y2014_barom_press_median():
    return median(barom_press2014)

def y2015_air_temp_mean():
    return mean(air_temp2015)
def y2015_air_temp_median():
    return median(air_temp2015)
def y2015_barom_press_mean():
    return mean(barom_press2015)
def y2015_barom_press_median():
    return median(barom_press2015)
