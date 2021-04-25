time=str(input())
if time[-2] =="AM" and time[:2] == "12":
    print("00" + time[2:-2])
elif time[-2] == "AM":
    print(time[:-2])
elif time[-2]=="PM" and time[:2] == "12":
    print(time[:-2])
if time[-2]=="PM":
    t1=str(int(time[:2]) + 12) + time[2:8]
    if t1[:2] == "24":
        print("00" + t1[2:8])
    else:
        print(t1)
