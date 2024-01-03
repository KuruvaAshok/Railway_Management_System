import mysql.connector

#conection for SQL & PYTHON
class routes:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user= "root",
            password= "Ashok@1995",
            database="railway"
            )

    def routesdetails(self,train_no,stop1,stop2,stop3,stop4):
            self.cur=self.conn.cursor()    #for reuse
            self.cur.execute(f"INSERT INTO routes VALUES({train_no},'{stop1}','{stop2}','{stop3}','{stop4}')")
            self.conn.commit()
            print("Data has been inserted sucessfully")