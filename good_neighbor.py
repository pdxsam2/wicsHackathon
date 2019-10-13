#Setup
import datetime

#Constants
CONST_DIST= 0.01

#classes and data types
class issues:
    def __init__(self, category, longitude, latitude):
        self.cat = category
        self.longi = longitude
        self.lati = latitude
        #self.time = time
        self.count = 1


#functions
#
#
#calculates the distance between two locations 
def distance(new, recorded):
    distance = ((new.lati - recorded.lati)**2 + (new.longi - recorded.longi)**2)**.5
    #print(distance)
    return distance

#this inserts either an addition to the count of the list "node", or a new "node" at the end
    #Whether or not a new node is added is dependent on the distance between 2 points to avoid overpopulating the list

def insert(issue, runningIssues):
    closest= 0
    minimum= CONST_DIST
    flag= 0
    #either appends or checks where to add in the list
    if(len(runningIssues) == 0):
        runningIssues.append(issue)
    else:
        for i in range(0,len(runningIssues)):
            #checking category
            if(issue.cat == runningIssues[i].cat):
                dist= distance(issue, runningIssues[i])
                #checking minimum 
                if(dist < minimum):
                    minimum= dist
                    closest= i
                    flag += 1
        #checks to see if the minimum has changed, if true then the new issue is appended to the list, if false then the count of the minimum is increased
        if(flag == 0):
            runningIssues.append(issue)
        else:
            runningIssues[closest].count += 1


#data testing #
#
runningIssues= list()
#external data

with open("entries.txt", "r") as f:
    lines= f.readlines()
    for line in lines:
        print(line)
        cat, longi, lat= line.split(",")
        longi= float(longi)
        lat= float(lat)
        new_issue= issues(cat, longi, lat)
        insert(new_issue, runningIssues)
#display 
for issues in range(0, len(runningIssues)):
     print(runningIssues[issues].cat)
     print(runningIssues[issues].longi)
     print(runningIssues[issues].lati)

#writing out to the external data file
with open("entries.txt", "w") as f:
    data= []
    for i in range(0, len(runningIssues)):
        data.append(','.join([runningIssues[i].cat, runningIssues[i].longi, runningIssues[i].lati]))
    print(data)
    out= '\n'.join(data)
    f.write(out)


