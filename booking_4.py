import mysql.connector

#conection for SQL & PYTHON
class book:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user= "root",
            password= "Ashok@1995",
            database="railway"
            )
    def trainfetch(self,src,dest):
        cur=self.conn.cursor()
        cur.execute(f'''select routes.train_no,source,stop1,stop2,stop3,stop4,destination from routes inner join train_det 
                                on routes.train_no = train_det.train_no where source='{src}' or stop1='{src}' or stop2='{src}' 
                                or stop3='{src}' or stop4='{src}';''')
        dt=cur.fetchall()
        try:
            bk=[]
            for i in dt:
                for j in i[i.index(src)+1:]:
                    if j==dest:                            # try and except we using for pass the out into another stop
                        #print(i)
                        bk.append(i)
        except:
            pass
        print(bk)


    def passengerdetails(self,pid,pname,age,mbl,gender):
        self.cur=self.conn.cursor()    #for reuse
        self.cur.execute(f"INSERT INTO psgr_det VALUES({pid},'{pname}',{age},{mbl},'{gender}')")
        self.conn.commit()
        print("Data has been inserted sucessfully")

    def transactionsdetails(self,tid,fare,pid,payment_mode):
        self.cur=self.conn.cursor()    #for reuse
        self.cur.execute(f"INSERT INTO transactions VALUES({tid},{fare},{pid},'{payment_mode}')")
        self.conn.commit()
        print("Data has been inserted sucessfully")
        
    def bookingdetails(self,book_id,tid,train_no,pid,cls,seatno,source,dest):
        self.cur=self.conn.cursor()    #for reuse
        self.cur.execute(f"INSERT INTO book_tic VALUES({book_id},{tid},{train_no},{pid},'{cls}',{seatno},'{source}','{dest}')")
        self.conn.commit()
        print("Ticket has been booked")
        print(pid,seatno,book_id,cls,source,dest,tid)    
  
  