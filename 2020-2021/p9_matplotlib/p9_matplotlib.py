import matplotlib.pyplot as plt

f = open("nyc-population.csv")
temp = f.readline()
bouroughs = temp.split(',')[1:]
data = []
while True:
    temp = f.readline() # drops first line automatically
    if (not temp):
        break
    temp2 = temp.split(',')
    data.append(temp2)
# manhattan
max_data = 0
million = 1000000 
toplotx = []
toploty = []
for value in data:
    toplotx.append(int(value[0]))
    toploty.append((int(value[1])/million))
    if((int(value[1])/million) > max_data):
        max_data = (int(value[1])/million)
plt.plot(toplotx,toploty)
plt.title("Population of Manhattan by Year")
plt.axis([1790,2010,0,max_data*1.1])
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.savefig("p9_manhattanpopulation.png")
plt.show()
plt.close()
# all bouroughs (how do you spell this)
plotdatay = []
toplotx = []
max_data = 0
i = 0
for value in data:
    toplotx.append(int(value.pop(0)))
    i = 0
    for y in value:
        if(len(plotdatay) <= i):
            plotdatay.append([])
        plotdatay[i].append(int(y)/million)
        if(int(y)/million > max_data):
            max_data = int(y)/million
        i += 1
i = 0
for data in plotdatay:
    plt.plot(toplotx, data, label = bouroughs[i])
    i += 1
plt.legend()
plt.axis([1790,2010,0,max_data*1.1])
plt.title("Population of NYC by Borough by Year") # thanks google for teaching me how to spell borough
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.savefig("p9_nycpopulation.png")
plt.show()