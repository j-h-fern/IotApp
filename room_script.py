
import serial as S
import time
import threading as T
import pymongo as pm

cont = True
result = []
time_stamp = []


ser = S.Serial('COM5',9600,timeout =1)

def read():

    while(cont):
        line = ser.readline()
        if line:
            time_stamp.append(time.time)
            string = line.decode()
            
            if(string != "\n"):
                result.append(string)
                print(string)
            

def user_in():
    
    print("press any key to stop")
    i = input()
    cont = False

    
        


if __name__ == "__main__":
    read_thread = T.Thread(target=read
    , name= 'r1',daemon=True)

    read_thread.start()

    client = pm.MongoClient("mongodb+srv://user:<1234>@cluster0.3kikq.mongodb.net/?retryWrites=true&w=majority")

    db = client["IotDB"]
    col = db["PID_time"]

    print("press any key to stop")
    i = input()
    cont = False
    read_thread.join()
    print(result)
    i=0
    for v in result:
        i+=1
        dict = {
            "count": i+1,
            "time": time_stamp[i]
        }

        col.insert_one(dict)
           







        
