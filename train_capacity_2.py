import mysql.connector

#conection for SQL & PYTHON
class capacity:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user= "root",
            password= "Ashok@1995",
            database="railway"
            )
    def capacitydetails(self,train_no,ac_1,ac_2,ac_3,sleeper,gen):
        self.cur=self.conn.cursor()    #for reuse
        self.cur.execute(f"INSERT INTO train_capacity VALUES({train_no},{ac_1},{ac_2},{ac_3},{sleeper},{gen})")
        self.conn.commit()
        print("Data has been inserted sucessfully")