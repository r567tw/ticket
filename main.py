from helpers import notify
from TRA import ticket as TRA
from dotenv import load_dotenv
import os



load_dotenv()

pid = os.getenv('pid')
startStation = os.getenv('startStation')
endStation = os.getenv('endStation')
rideDate = os.getenv('rideDate')
trainNoList1 = os.getenv('trainNoList1')
trainNoList2 = os.getenv('trainNoList2')

message = TRA.get(pid,startStation,endStation,rideDate,trainNoList1,trainNoList2)
notify.send(message=message)