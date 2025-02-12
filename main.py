# check hetansh check again and again here
# import mainpage.py
import os
import mysql.connector


mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="chatsystem"
)
mycursor = mydb.cursor()

class login :
    def login_page(this):
        valid_inputs = True
        new_choice=0
        while(valid_inputs == True) :
            print("-------------------------------------Login Page-------------------------------------")
            print("\t\t\t\t\t\t1. Login")
            print("\t\t\t\t\t\t2. Sign Up")
            print("\t\t\t\t\t\t3. Exit")
            print()
            choice = int(input("Enter choice : "))
            status=False


            if choice == 2:
                login_username = input("Enter name : ")
                if (login_username.isalpha()):
                    pass
                else:
                    print("name should be alphabets only")
                    valid_inputs = False
                    break

                login_mobileno = input("Enter number : ")
                if(login_mobileno.isdigit() and len(login_mobileno) == 10):
                    pass
                else:
                    print("number should be 10 digits only")
                    valid_inputs = False
                    break

                    
                login_email = input("Enter email : ")
            
                if "@gmail.com" in login_email:
                    pass
                else:
                    print("email should be @gmail.com")
                    valid_inputs = False
                    break


                login_password = input("Enter password : ")
                if (login_password.isdigit()):
                    status=True
                    pass
                else:
                    print("Invalid Password")
                    valid_inputs = False    
                    break
        
                login_select="select * from user"
                mycursor.execute(login_select)
                myresult = mycursor.fetchall()
                flag=1
                for row in myresult:
                        if row[2]!=login_mobileno :
                            if row[3]!=login_email :
                                if status==True :
                                    sign_insert="insert into user(user_name,user_mno,user_email,user_password) values(%s,%s,%s,%s)"
                                    mycursor.execute(sign_insert,(login_username,login_mobileno,login_email,login_password))
                                    print("sign up successfully")
                                    new_choice=1
                                    mydb.commit()
                                    break
                            else :
                                flag=0
                                break
                if flag==0 :
                    print("failed")
            
                if new_choice==1 :
                    print("you need to login...")
                    login_username1 = input("Enter name : ")
                    if (login_username1==login_username):     
                        login_mobileno1 = input("Enter number : ")
                        if(login_mobileno1==login_mobileno):
                            login_email1 = input("Enter email : ")
                            if login_email1==login_email :
                                login_password1 = input("Enter password : ")
                                if login_password1==login_password :
                                    print("login successfully")
                                    obj=(login_username,login_mobileno,login_email,login_password)
                                    this.contactlist(obj)

            elif choice == 1:
                login_username = input("Enter name : ")
                if (login_username.isalpha()):
                    pass
                else:
                    print("name should be alphabets only")
                    valid_inputs = False
                    break

                login_mobileno = input("Enter number : ")
                if(login_mobileno.isdigit() and len(login_mobileno) == 10):
                    pass
                else:
                    print("number should be 10 digits only")
                    valid_inputs = False
                    break

                    
                login_email = input("Enter email : ")
            
                if "@gmail.com" in login_email:
                    pass
                else:
                    print("email should be @gmail.com")
                    valid_inputs = False
                    break


                login_password = input("Enter password : ")
                if (login_password.isdigit()):
                    status=True
                    pass
                else:
                    print("Invalid Password")
                    valid_inputs = False    
                    break
        
                login_select="select * from user"
                mycursor.execute(login_select)
                myresult = mycursor.fetchall()
                flag=1
                for row in myresult:
                    if row[1]==login_username:
                        if row[2]==login_mobileno :
                            if row[3]==login_email :
                                if row[4]==login_password :

                                    if status==True :
                                        print("login successfully")
                                        obj=(login_username,login_mobileno,login_email,login_password)
                                        flag=1
                                        this.contactlist(obj)
                                    else :
                                        flag=0
                if flag==0 :
                    print("login failed")

            if choice==3 :
                print("exit")
                break
    
    def contactlist(this,obj) :
        print("no. of contact in your list : ")
        con_no=int(input())
        f1=open(obj[0]+".txt","w")
        flag=1
        for i in range(con_no) :
            print("enter contact name : ")
            name=input()
            print("enter contact number : ")
            num=input()
            if(num.isdigit() and len(num) == 10):
                    pass
            else:
                print("number should be 10 digits only")
                flag=0
                break
            f1.write(name+" "+str(num)+"\n")
            contact_insert="insert into contact (user_name,contact_name,contact_no,block_users) values(%s,%s,%s,%s)"
            mycursor.execute(contact_insert,(obj[0],name,num,True))
            mydb.commit()
        f1.close()
        if flag==1 : 
            this.mainmenu(obj)

    def mainmenu(this,obj) :
        print("-"*60)
        print("1.send message")
        print("2.receive message")
        print("3.create group")
        print("4.block number")
        print("5.exit")
        print("enter your choice : ")
        msg_choice = int(input())

        f2=open(obj[0]+".txt","r")
        con_list=f2.readlines()
        f2.close()
        if msg_choice==1 :
            flag=1
            receiver_name = input("Enter the name to send message : ")
            for i in con_list :
                con_list_space=i.split(" ")
                if con_list_space[0]==receiver_name :
                    flag=1
                    break
                else :
                    flag=0
            if flag==0 :
                print("number not found")
            else :
                print("Enter your message: ")
                send_msg = input()

                table_name1 = obj[0] + "_" + receiver_name
                table_name2 = receiver_name + "_" + obj[0]

                check_query = f"""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = 'chatsystem' 
                AND table_name IN ('{table_name1}', '{table_name2}');
                """
                mycursor.execute(check_query)
                existing_tables = mycursor.fetchall()
                print(existing_tables)
                flag=1
                if not existing_tables:  # If result is empty, no table exists
                    new_table_name = table_name1  # Define the new table name
                    create_table_query = f"""
                    CREATE TABLE {new_table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_name VARCHAR(255),
                    message TEXT,
                    receiver_name VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                    """
    
                    mycursor.execute(create_table_query)
                    mydb.commit()
                    print(f"✅ New table '{new_table_name}' created.")
                    flag=1
                else:
                    print("✅ A valid table already exists. No need to create a new one.")
                    flag=0
                
                if flag==1 :
                    print(new_table_name)
                    msg_insert = "INSERT INTO {new_table_name} (user_name, message, receiver_name) VALUES (%s, %s, %s)"
                    mycursor.execute(msg_insert, (obj[0], send_msg, receiver_name))
                    mydb.commit()
                else :
                    table_final=existing_tables[0][0]
                    msg_insert = "INSERT INTO "+table_final + "(user_name, message, receiver_name) VALUES (%s, %s, %s)"
                    mycursor.execute(msg_insert, (obj[0], send_msg, receiver_name))
                    mydb.commit()

                    
            if flag==1 :
                f3=open(new_table_name+".txt","w")
                f3.write(obj[0]+" : "+send_msg+"\n")
                f3.close()
            else :
                f3=open(table_final+".txt","a")
                f3.write(obj[0]+" : "+send_msg+"\n")
                f3.close()


            
l1=login()
l1.login_page()