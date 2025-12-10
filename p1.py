import mysql.connector
import os
def create_mydb():
 mydb = None
 try:
  mydb = mysql.connector.connect(
   host="localhost",
 user="fatemeh",
   password="Aa123456",
    database="fatemeh"
 )
 except mysql.connector.Error as err:
  print("Connection error:", err)
 return mydb


def user_data():
    name=input("name:")
    lastname=input("lastname:")
    birth_year=int(input("birth_year:"))
    return name,lastname,birth_year

def save_user(mydb,name,lastname,birth_year):
    cursor=mydb.cursor()
    if 1990<=birth_year<=2000:
        cursor.execute("insert into users(name,lastname,birth_year)values(%s,%s,%s)" ,(name,lastname,birth_year))
        mydb.commit()
    else:
    
        with open("file_users.txt","a+") as f:
            f.write(f"{name}{lastname}{birth_year}\n")
            f.close()
        
def count(mydb):
    db_count=0
    file_count=0
    cursor=mydb.cursor()
    cursor.execute("select count(*)from users")
    db_count=cursor.fetchone()[0]
    cursor.close()

    with open("file_users.txt","r") as f:
        file_count= sum(1 for line in f )

    return db_count, file_count
    
def main():
    mydb=create_mydb()
    if mydb is not None:
        while True:
             name, last_name ,birth_year= user_data()
             save_user(mydb,name,last_name,birth_year)
 
             another=input("ezafe mikoni?(yes/no):")
             if another != "yes":
                     break
             
    db_count , file_count = count(mydb)
    print(f"zakhire database{ db_count}:")
    print(f"zakhire file{file_count}:")
    mydb.close()
    
if __name__ == "__main__":
   main()
