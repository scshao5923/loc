import datetime
import sqlite3
import time
import location
tdy=datetime.date.today()
wkDat="{0:04}{1:02}{2:02}".format(tdy.year,tdy.month,tdy.day)
conn = sqlite3.connect("loc.db")
cursor = conn.cursor()
cursor.execute('select max(batid) dummy from loc where batid like ?',(wkDat+'%',))
batid=cursor.fetchone()[0]
batid=(str(int(batid)+1)) if batid else str(int(wkDat)*100)
sec=0
while not sec:
    try:
        sec=int(input('請輸入秒數：'))
    except:
        sec=0
cnt=0
try:
    while True:
        txdat=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cnt=cnt+1
        print(cnt)
        #location.start_updates()
        loc=location.get_location()
        while not loc:
        	loc=location.get_location()
        #location.stop_updates()
        cursor.execute(
            "insert into loc(batid, latitude, longitude, altitude, timestamp, horizontal_accuracy, vertical_accuracy, speed, cuorse, txdat) values(?,?,?,?,?,?,?,?,?,?)",
            (batid,loc['latitude'],loc['longitude'],loc['altitude'],loc['timestamp'],loc['horizontal_accuracy'],loc['vertical_accuracy'],loc['speed'],loc['course'],txdat)
        )
        conn.commit()
        time.sleep(sec)
finally:
        cursor.close()
        conn.close()




