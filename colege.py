import mysql.connector as mysql
db = mysql.connect(host = "localhost",user ="root",password="",database ="colege")
command_handler = db.cursor(buffered = True)



def auth_student():
    print("")
    print("students login")
    print("")
    username =input(str("Username :"))
    password = input(str("Password: "))
    query_vals = (username,password,"student")
    command_handler.execute("SELECT username FROM users WHERE username =%s AND password =%s AND privilege =%s",query_vals) 
    if command_handler.rowcount <=0:
        print("Invalid log details")
    else:
        student_session(username)

def student_session(username):
    while 1:
        print("Student's Menu")
        print("")
        print("1. View register")
        print("2. Download register")
        print("3. Logout") 

        user_option = input(str("Option :"))
        if user_option == "1":
            username = (str(username),)
            command_handler.execute("SELECT date,username,status FROM attendance WHERE username =%s",username)
            records = command_handler.fetchall()
            for record in records:
                print(record)
        elif user_option == "2":  
            print("Download register")
            username = (str(username),)
            command_handler.execute("SELECT date,username,status FROM attendance WHERE username =%s",username)
            records = command_handler.fetchall()
            for record in records:
                with open("register.txt","w") as f:
                    f.write(str(records)+ "\n")
                    f.close()
            print("All records saved")
        elif user_option == "3":
            break

        else:
            print("No valid option was selected")    

 


def teacher_session():
    while 1:
          print("")
          print("Teacher menu")
          print("1. Mark student register ")
          print("2. View register")
          print("3. logout")
           
          user_option = input(str("Option: "))
          if user_option == "1":
               print("")
               print("Mark student register")
               command_handler.execute("SELECT username FROM users WHERE privilege = 'student' ") 
               records = command_handler.fetchall()
               date = input(str("Date :DD/MM/YYYY : "))
               for record in records:
                   record = str(record).replace("'","")
                   record = str(record).replace(",","")
                   record = str(record).replace("(","")
                   record = str(record).replace(")","")
                   #present | Absent |late
                   status = input(str("Status for " + str(record) + " P/A/L: "))
                   query_vals = (str(record),date,status)
                   command_handler.execute("INSERT INTO attendance (username,date,status) VALUES(%s,%s,%s)",query_vals)
                   db.commit()
                   print(record + "Marked as " + status)
          elif user_option == "2":
              print("")
              print("Viewing all student registers ")
              command_handler.execute("SELECT username,date,status FROM attendance")
              records = command_handler.fetchall()
              print("display all registers")
              for record in records:
                  print(record)

          elif user_option == "3":
              break
          else:
              print("No valid option was selected")





def admin_session():
      while 1:
          print("")
          print("admin menu")
          print("1. Register new student")
          print("2. Register new teacher")
          print("3. Delete  existing student")
          print("4. Delete existing  teacher")
          print("5. logout")

          user_option = input(str("Option :"))
          if user_option == "1":
              print("")
              print("Register New student")
              username = input(str("Student username :"))
              password = input(str("Student Password :"))
              query_vals = (username,password)
              command_handler.execute("INSERT INTO users (username,password,privilege)VALUES(%s,%s,'student')",query_vals)
              db.commit()
              print(username + " Has been registered as a student")   
          elif user_option == "2":
              print("")
              print("Register New Teacher")
              username = input(str("Teacher username :"))
              password = input(str("Teacher Password :"))
              query_vals = (username,password)
              command_handler.execute("INSERT INTO users (username,password,privilege)VALUES(%s,%s,'teacher')",query_vals)
              db.commit()
              print(username + " Has been registered as a Teacher")  
          elif user_option == "3":
              print("")
              print("Delete existing student account")
              username =input(str("Student username :"))
              query_vals = (username,"student")
              command_handler.execute("DELETE FROM users WHERE username =%s AND privilege = %s",query_vals)
              db.commit()
              if command_handler.rowcount < 1:
                  print("User not found")
              else:
                  print(username + "  has been Deleted ")   
          elif user_option == "4":  
               print("")
               print("Delete existing teacher account")
               username =input(str("teacher username :"))
               query_vals = (username,"teacher")
               command_handler.execute("DELETE FROM users WHERE username =%s AND privilege = %s",query_vals)
               db.commit()
               if command_handler.rowcount < 1:
                  print("User not found")
               else:
                  print(username + "  has been Deleted ")        
          elif user_option == "5":
              break 
          else:
            print("No valid option selected")

              

def auth_admin():
      print("")
      print("Admin Login")
      print("")
      Username = input (str("Username :"))
      password = input (str("password :"))
      if Username == "admin":
          if password == "password":
              admin_session()
          else:
              print("Incorrect password ")
          
      else:
          print ("Login details not recognised ")

def auth_teacher():
    print("")
    print("Teacher Login")
    print("")
    username = input(str("Username"))
    password = input(str("Password :"))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM users WHERE username =%s AND password =%s AND privilege = 'teacher'",query_vals)
    if command_handler.rowcount <=0:
        print("Login not recognised")
    else:
            teacher_session()
def main():
    while 1:
        print("Welcome to the system")
        print("")
        print("1. login as student")
        print("2. login as teacher ")
        print("3. login as admin")

        user_option = input(str("Option :"))
        if user_option == "1" :
            auth_student()
        elif user_option == "2" :   
             auth_teacher()
        elif user_option == "3":
         auth_admin()
        else:
            print("invalid input selected please try again")    
main()  




