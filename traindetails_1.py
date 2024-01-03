import mysql.connector

#conection for SQL & PYTHON
class details:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user= "root",
            password= "Ashok@1995",
            database="railway"
            )
    def traindetails(self,train_no,train_name,source,destination):
        self.cur=self.conn.cursor()    #for reuse
        self.cur.execute(f"INSERT INTO train_det VALUES({train_no},'{train_name}','{source}','{destination}')")
        self.conn.commit()
        print("Data has been inserted sucessfully")

    def trainnofetch(self):
        self.cur=self.conn.cursor()
        self.cur.execute('''Select train_det.train_no from train_det left join 
                         train_capacity on train_det.train_no=train_capacity.train_no where ac_1 is null''')
        print(self.cur.fetchall())
        
    def trainnofetch(self):
        self.cur=self.conn.cursor()
        self.cur.execute('''Select train_det.train_no,train_det.source,train_det.destination from train_det left join 
                         routes on train_det.train_no=routes.train_no where stop1 is null''')
        print(self.cur.fetchall())
    

                                                                                            

   
