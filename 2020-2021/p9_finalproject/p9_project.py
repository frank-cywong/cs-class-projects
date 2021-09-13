import matplotlib.pyplot as plt
import matplotlib.dates as mdates # for date stuff
import datetime # also date stuff

def csv_to_data(fn):
	# basically implementing my own csv library could have probably used python's inbuilt one
    f = open(fn)
    line = f.readline() # drops headers automatically
    data = []
    while True:
        line = f.readline()
        if line == "":
            return data
        temps = ""
        quotemode = False
        data.append([])
        for char in line:
            if char == '"':
                if(quotemode):
                    quotemode = False
                else:
                    quotemode = True
            elif ((char == ',') and (not quotemode)):
                data[(len(data)-1)].append(temps)
                temps = ""
            else:
                temps += char
        if(temps[-1] == '\n'):
            temps = temps[:-1]
        data[(len(data)-1)].append(temps)

plt.style.use('p9_project.mplstyle')
# adds custom stylesheet, makes it blend well with website

# file 1, process for js searching - you know what i used datetime anyways why didn't i just use the json library here oh well

f = 'data-by-modzcta.csv'
data = csv_to_data(f)
data_json = '{'
modzcta_json = '{'
def sortbycaserate(s): # for use with sorted()
    return s[1]
def sortbydeathrate(s):
    return s[2]
def sortbypositivityrate(s):
    return s[3]
def sortbytestrate(s):
    return s[4]
data2 = []
for row in data:
    zipcodes = row[3].split(',')
    for i in zipcodes:
        if(i[0] == " "):
            i = i[1:]
        modzcta_json += ('"'+str(i)+'":['+str(row[0])+',"'+str(row[1])+'"],')
    data2.append([str(row[0]),float(row[7]),float(row[10]),float(row[11]),round(float(row[12])/float(row[8]),3)]) # modzcta, case rate, death rate, test positive rate, tests taken over population
modzcta_json = modzcta_json[:-1]
modzcta_json += "}"
data3 = sorted(data2,key=sortbycaserate)
data4 = sorted(data2,key=sortbydeathrate)
data5 = sorted(data2,key=sortbypositivityrate)
data6 = sorted(data2,key=sortbytestrate,reverse=True) # higher testing rates are better
datadict = {}
i = 1
for modzcta in data3:
    datadict[modzcta[0]] = [modzcta[1],i,modzcta[2],0,modzcta[3],0,modzcta[4],0]
    i += 1
i = 1
for modzcta in data4:
    (datadict[modzcta[0]])[3] = i
    i += 1
i = 1
for modzcta in data5:
    (datadict[modzcta[0]])[5] = i
    i += 1
i = 1
for modzcta in data6:
    (datadict[modzcta[0]])[7] = i
    i += 1
for modzcta,info in datadict.items():
    data_json += ('"'+modzcta+'":[')
    for i in info:
        data_json += (str(i)+",")
    data_json = data_json[:-1]
    data_json += ("],")
data_json = data_json[:-1]
data_json += "}"
#f = open('p9_project_data.json','w')
#f.write(data_json)
#f.close()
#f = open('p9_project_modzcta.json','w')
#f.write(modzcta_json)
#f.close()

# file 2, process into combined graph
fn = 'data-by-day.csv'
n_data = csv_to_data(fn)
x = []
y1 = [[],[],[]]
y2 = [[],[],[]]
y3 = [[],[]]
y1max = 0
y2max = 0
for row in n_data:
    datetime_matplotlib = mdates.date2num(datetime.datetime.strptime(row[0],"%m/%d/%Y"))
    x.append(datetime_matplotlib)
    y1[0].append(int(row[6]))
    y1[1].append(int(row[8]))
    y1[2].append(int(row[9]))
    if(int(row[6]) > y1max):
        y1max = int(row[6])
    # date, case count (7 day average), hospitalisation (7 day avg), deaths (7 day avg), case count incl prob (7 day avg), deaths incl prob (7 day avg)
    y2[0].append(int(row[7]))
    y2[1].append(int(row[8]))
    y2[2].append(int(row[10]))
    if(int(row[7]) > y2max):
        y2max = int(row[7])
    y3[0].append(round(int(row[8])/max(int(row[7]),1)*100,2))
    y3[1].append(round(int(row[10])/max(int(row[7]),1)*100,2))
labels1 = ["Citywide Case Count (7 day average)","Citywide Hospitalisation Count (7 day average)","Citywide Death Count (7 day average)"]
labels2 = ["Citywide Case Count (7 day average) (Including Probable Cases)","Citywide Hospitalisation Count (7 day average)","Citywide Death Count (7 day average) (Including Probable Cases)"]
labels3 = ["Cases Hospitalised over Cases Reported (Percent)","Deaths over Cases Reported (Percent)"]
# plot 1 - without probable cases
for i in range(len(y1)):
    plt.plot(x,y1[i],label=labels1[i])
plt.title("NYC Covid-19 Data by Date")
plt.xlabel("Date")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator()) # stuff to deal with dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y')) # stuff to deal with dates
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y') # stuff to deal with dates
plt.legend(loc="upper right") # just for better looks
plt.ylim(0,y1max*1.3)
plt.show()
plt.close()
# plot 2 - includes probable cases
for i in range(len(y2)):
    plt.plot(x,y2[i],label=labels2[i])
plt.title("NYC Covid-19 Data by Date (Including Probable Cases)")
plt.xlabel("Date")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
plt.legend(loc="upper right")
plt.ylim(0,y2max*1.3)
plt.show()
plt.close()
# plot 3 - rate of death & rate of hospitalisations (counts probable cases)
for i in range(len(y3)):
    plt.plot(x,y3[i],label=labels3[i])
plt.title("NYC Covid-19 Hospitalisation and Death Counts over Cases by Date")
plt.xlabel("Date")
plt.ylabel("Percent")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
plt.legend(loc="upper right")
plt.ylim(0,50)
plt.show()
plt.close()
#file 3 - testing data
fn = 'testing-turnaround.csv'
t_data = csv_to_data(fn)
t_x = []
t_ys = [[], [], [], [], [], []]
for row in t_data:
    datetime_matplotlib = mdates.date2num(datetime.datetime.strptime(row[0],"%m/%d/%Y"))
    t_x.append(datetime_matplotlib)
    for i in range(1,len(row)):
        (t_ys[(i-1)]).append(float(row[i]))
# plot 1 - tests by date
plt.plot(t_x,(t_ys[0]))
plt.title("NYC Covid-19 Tests Administered by Week")
plt.xlabel("Date of Week Ending")
plt.ylabel("Tests Administered")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
plt.show()
plt.close()
# plot 2 - tests by 25th, 50th, and 75th percentile in speed
plt.plot(t_x,t_ys[5],label="75th Percentile")
plt.plot(t_x,t_ys[3],label="50th Percentile (Median)")
plt.plot(t_x,t_ys[4],label="25th Percentile")
plt.title("NYC Covid-19 Test Result Turnaround Speed by Week")
plt.xlabel("Date of Week Ending")
plt.ylabel("Test Result Turnaround Speed (Days)")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
plt.legend()
plt.show()
plt.close()
# plot 3 - tests by turnaround time less than
plt.plot(t_x,t_ys[1],label="Tests Returned by 24 Hours")
plt.plot(t_x,t_ys[2],label="Tests Returned by 48 Hours")
plt.title("NYC Covid-19 Test Result Turnaround Speed by Week")
plt.xlabel("Date of Week Ending")
plt.ylabel("Percent")
plt.ylim(0,100)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
plt.legend()
plt.show()
plt.close()

#file 4 - testing positivity rates
fn = "tests.csv"
p_data = csv_to_data(fn)
p_x = []
y1 = []
y2 = []
for row in p_data:
    datetime_matplotlib = mdates.date2num(datetime.datetime.strptime(row[0],"%m/%d/%Y"))
    p_x.append(datetime_matplotlib)
    y1.append(int(row[1]))
    y2.append(float(row[3])*100)
#plot 1 - tests by date (day)
plt.plot(p_x,y1)
plt.title("NYC Covid-19 Tests Administered by Day")
plt.xlabel("Date")
plt.ylabel("Tests Administered")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
plt.show()
plt.close()
#plot 2 - positivity rate by day
plt.plot(p_x,y2)
plt.title("NYC Covid-19 Test Positivity Rate by Day")
plt.xlabel("Date")
plt.ylabel("Test Positivity Rate (percent)")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
ax.format_xdata = mdates.DateFormatter('%m/%d/%Y')
plt.show()
plt.close()