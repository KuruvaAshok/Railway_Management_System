# importing required modules
from traindetails_1 import details
from train_capacity_2 import capacity
from routes_3 import routes
from booking_4 import book
import numpy as np

print("------------welcome to railway modules------------")
print("------------for Inserting the Data Enter - 1--")
print("------------for Reading the Data Enter - 2--")
print("------------for Updating the Data Enter - 3--")
print("------------for Deleting the Data Enter - 4--")


opr=int(input("Please Enter your Opertaion: "))
if opr==1:
    print("--- For Inserting the data traindetials press 1---")
    print("--- For Inserting the data traincapacity press 2---")
    print("--- For Inserting the data routes press 3---")
    print("--- For Booking for ticket press 4---")
    inopr=int(input("please select an operation: "))
    if inopr==1:
        obj=details()
        train_no=int(input("please enter the train no:"))
        train_name=input("please enter the train name:")
        source=input("please enter the source station:")
        destination=input("please enter the destination name:")
        obj.traindetails(train_no,train_name,source,destination) 
    if inopr==2:
        obj=capacity()
        obj1=details()
        obj1.trainnofetch()
        train_no=int(input("please enter the train no: "))
        ac_1=int(input("Please enter the capacity of ac_1: "))
        ac_2=int(input("Please enter the capacity of ac_2: "))
        ac_3=int(input("Please enter the capacity of ac_3: "))
        sleeper=int(input("Please enter the capacity of sleepe class: "))
        gen=int(input("Please enter the capacity of general class: "))
        obj.capacitydetails(train_no,ac_1,ac_2,ac_3,sleeper,gen)
    if inopr==3:
        obj=routes()
        obj1=details()
        obj1.trainnofetch()
        train_no=int(input("please enter the train no: "))
        stop1=input("Please enter the capacity of stop_1: ")
        stop2=input("Please enter the capacity of stop_2: ")
        stop3=input("Please enter the capacity of stop_3: ")
        stop4=input("Please enter the capacity of stop_4: ")
        obj.routesdetails(train_no,stop1,stop2,stop3,stop4)
    if inopr==4:
        source = input('From: ')
        dest = input('To: ')
        obj=book()
        obj.trainfetch(source,dest)
        train_no=int(input("Please enter the trainno: "))
        cls=input("enter the class: ")

        #passenger info
        pid=int(input("enter the passenger id: "))
        pname=input("Please enter the passenger name: ")
        age=int(input("Please enter the age: "))
        mbl=int(input("Please enter mbl number: "))
        gender=input("Please enter the gender: ")        
        obj.passengerdetails(pid,pname,age,mbl,gender)

        #transaction details
        tid=int(input("Please enter transaction id: "))
        fare=int(input("Please enter the amount: "))
        payment_mode=input("Please enter payment_mode: ")
        obj.transactionsdetails(tid,fare,pid,payment_mode)

        #booking details
        book_id=np.random.randint(1,50000,1)[0] 
        seatno=np.random.randint(1,50,1)[0]
        obj.bookingdetails(book_id,tid,train_no,pid,cls,seatno,source,dest)


if opr==2:
    pass
if opr==3:
    pass
if opr==4:
    pass




























   

