import sys
from datetime import datetime

x = ['ST', 0, -1]
y = ['ST', 0, -1]
z = ['ST', 0, -1]
vehicles = {'x':x, 'y':y, 'z':z}
current_model = "init"

logResult = {'x':{'mode0':[0,0], 'mode2':[0,2]}, 'y':{'mode0':[0,0], 'mode2':[0,2]}, 'z':{'mode0':[0,0], 'mode2':[0,2]}}

def durationDump(duration, model, mode):
    mode_val = "mode"+str(mode)
    logResult[model][mode_val][0] += duration
    print logResult[model]
   
   
def calculateDuration(ST, ET):
    print ST, ET
    fmt = '%Y-%m-%d %H:%M:%S'
    tstamp1 = datetime.strptime(ST, fmt)
    tstamp2 = datetime.strptime(ET, fmt)

    td = tstamp2 - tstamp1
    td_mins = int(round(td.total_seconds()))
    print td_mins
    return td_mins


def recordData(timestamp, mode, model):
    global current_model
    if current_model == 'init':
        current_model = model
        vehicles[current_model][0] = timestamp
        vehicles[current_model][2] = mode
        print vehicles[current_model]
        return
    
    if mode != vehicles[current_model][2] or model != current_model:
        durationDump(calculateDuration(vehicles[current_model][0], timestamp), current_model, vehicles[current_model][2])
        print current_model
        current_model = model
        vehicles[current_model][0] = timestamp
        vehicles[current_model][2] = mode
        print vehicles[current_model]
        print vehicles[current_model][1], current_model

        
            
if __name__ == '__main__':            
    logs = ["1,2016-05-02 09:14:32, lat, long, 2, x", "4,2016-05-02 09:14:42, lat, long, 0, x", "5,2016-05-02 09:14:48, lat, long, 0, y", "10,2016-05-02 09:15:03, lat, long, 2, x"]
    
    for logEntry in logs:
        data = logEntry.split(",")
        print data
        print data[1], data[4].strip(),  data[5].strip()
        recordData(data[1], data[4].strip(), data[5].strip())
        #print vehicles['x'], vehicles['y'], vehicles['z']
        
    
            