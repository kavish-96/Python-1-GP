# import mainpage.py
import os
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="chatsystem"
)
mycursor = mydb.cursor()


class login:

    def login_page(this):
        valid_inputs = True
        new_choice = 0
        while valid_inputs == True:
            print()
            print("-" * 70, "login page", "-" * 70)
            print()
            print("\t\t\t\t\t\t\t\t1. Login")
            print("\t\t\t\t\t\t\t\t2. Sign Up")
            print("\t\t\t\t\t\t\t\t3. Exit")
            print()
            print("-" * 150)
            print()
            choice = int(input("Enter choice : "))
            print()
            status = False

            if choice == 1:
                print()
                login_username = input("\tEnter name : ")
                if login_username.isalpha():
                    pass
                else:
                    print("\tname should be alphabets only")
                    valid_inputs = False
                    break

                login_mobileno = input("\tEnter number : ")
                if login_mobileno.isdigit() and len(login_mobileno) == 10:
                    pass
                else:
                    print("\tnumber should be 10 digits only")
                    valid_inputs = False
                    break

                login_email = input("\tEnter email : ")

                if "@gmail.com" in login_email:
                    pass
                else:
                    print("\temail should be @gmail.com")
                    valid_inputs = False
                    break

                login_password = input("\tEnter password : ")
                if login_password.isdigit():
                    status = True
                    pass
                else:
                    print("\tInvalid Password")
                    valid_inputs = False
                    break

                login_select = "select * from user"
                mycursor.execute(login_select)
                myresult = mycursor.fetchall()
                flag = 1
                for row in myresult:
                    if row[1] == login_username:
                        if row[2] == login_mobileno:
                            if row[3] == login_email:
                                if row[4] == login_password:

                                    if status == True:
                                        print("\tlogin successfully")
                                        obj = (
                                            login_username,
                                            login_mobileno,
                                            login_email,
                                            login_password,
                                        )
                                        flag = 1
                                        this.mainmenu(obj)
                                    else:
                                        flag = 0
                if flag == 0:
                    print("\tlogin failed")

            elif choice == 2:
                print()
                login_username = input("\tEnter name : ")
                if login_username.isalpha():
                    pass
                else:
                    print("\tname should be alphabets only")
                    valid_inputs = False
                    break

                login_mobileno = input("\tEnter number : ")
                if login_mobileno.isdigit() and len(login_mobileno) == 10:
                    pass
                else:
                    print("\tnumber should be 10 digits only")
                    valid_inputs = False
                    break

                login_email = input("\tEnter email : ")

                if "@gmail.com" in login_email:
                    pass
                else:
                    print("\temail should be @gmail.com")
                    valid_inputs = False
                    break

                login_password = input("\tEnter password : ")
                if login_password.isdigit():
                    status = True
                    pass
                else:
                    print("\tInvalid Password")
                    valid_inputs = False
                    break

                login_select = "select * from user"
                mycursor.execute(login_select)
                myresult = mycursor.fetchall()
                flag = 1
                if myresult == []:
                    if status == True:
                        sign_insert = "insert into user(user_name,user_mno,user_email,user_password) values(%s,%s,%s,%s)"
                        mycursor.execute(
                            sign_insert,
                            (
                                login_username,
                                login_mobileno,
                                login_email,
                                login_password,
                            ),
                        )
                        print()
                        print("\tsign up successfully")
                        print()
                        print()
                        new_choice = 1
                        mydb.commit()
                        # break
                else:
                    for row in myresult:
                        if row[2] != login_mobileno:
                            if row[3] != login_email:
                                if status == True:
                                    sign_insert = "insert into user(user_name,user_mno,user_email,user_password) values(%s,%s,%s,%s)"
                                    mycursor.execute(
                                        sign_insert,
                                        (
                                            login_username,
                                            login_mobileno,
                                            login_email,
                                            login_password,
                                        ),
                                    )
                                    print("\tsign up successfully")
                                    new_choice = 1
                                    mydb.commit()
                                    break
                            else:
                                flag = 0
                                break
                if flag == 0:
                    print("\tfailed")

                if new_choice == 1:
                    print("\tyou need to login...")
                    print()
                    print()
                    login_username1 = input("\tEnter name : ")
                    if login_username1 == login_username:
                        login_mobileno1 = input("\tEnter number : ")
                        if login_mobileno1 == login_mobileno:
                            login_email1 = input("\tEnter email : ")
                            if login_email1 == login_email:
                                login_password1 = input("\tEnter password : ")
                                if login_password1 == login_password:
                                    print()
                                    print("\tlogin successfully")
                                    print()
                                    # obj = (
                                    #     login_username,
                                    #     login_mobileno,
                                    #     login_email,
                                    #     login_password,
                                    # )
                                    # this.contactlist(obj)

            elif choice == 3:
                print("\texit")
                break

    def contactlist(this, obj):
        user_id_select = "select user_id from user where user_name='" + obj[0] + "'"
        mycursor.execute(user_id_select)
        myresult = mycursor.fetchall()
        print()

        con_no = int(input("\tno. of contacts you want add in list : "))
        f1 = open(obj[0] + ".txt", "a")
        flag = 1
        for i in range(con_no):
            name = input("\tenter contact name : ")
            num = input("\tenter contact number : ")
            print()
            if num.isdigit() and len(num) == 10:
                pass
            else:
                print("\tnumber should be 10 digits only")
                flag = 0
                break
            f1.write(name + " " + str(num) + "\n")
            contact_insert = "insert into contact (user_id,user_name,contact_name,contact_no,block_users) values(%s,%s,%s,%s,%s)"
            mycursor.execute(contact_insert, (myresult[0][0], obj[0], name, num, True))
            mydb.commit()
        print()
        f1.close()
        if flag == 1:
            this.mainmenu(obj)

    def mainmenu(this, obj):
        # mainmenu_flag=True
        while True:
            print()
            print("\t1.send message")
            print("\t2.receive message")
            print("\t3.create group")
            print("\t4.add contact")
            print("\t5.block contact")
            print("\t6.log out")
            print()

            msg_choice = int(input("\tenter your choice : "))

            f2 = open(obj[0] + ".txt", "r")
            con_list = f2.readlines()
            f2.close()

            if msg_choice == 1:
                flag = 1
                print()
                # print("\t\t|=================contact================ | =================number================|")
                print()
                count = 1
                for i in con_list:
                    j = i.split(" ")
                    print(f"\t{count}.{j[0] :<10} : {j[1] :<10}")
                    count = count + 1
                print()

                receiver_name = input("\tEnter the name to send message : ")
                select_receiver = "select * from contact"
                mycursor.execute(select_receiver)
                con_obj = mycursor.fetchall()
                block_flag=0
                for i in con_obj:
                    if i[3] == receiver_name:
                        if i[2] == obj[0] :
                            flag=0
                            if i[5]==True:
                                block_flag = 1
                                break

                if block_flag == 0:
                    print("\tnumber blocked")

                if flag == 1:
                    print("number not found")

                else :

                    for i in con_list:
                        con_list_space = i.split(" ")
                        if con_list_space[0] == receiver_name  :
                            flag = 1
                            break
                        else:
                            flag = 0
                    if flag == 0:
                        print("\tnumber not found")
                    else:
                        print()
                        send_msg = input("\tEnter your message: ")

                        table_name1 = obj[0] + "_" + receiver_name
                        table_name2 = receiver_name + "_" + obj[0]

                        check_query = f"""
                        SELECT table_name FROM information_schema.tables 
                        WHERE table_schema = 'chatsystem' 
                        AND table_name IN ('{table_name1}', '{table_name2}');
                        """
                        mycursor.execute(check_query)
                        existing_tables = mycursor.fetchall()
                        # print(existing_tables)
                        flag = 1
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
                            # print(f"\t✅ New table '{new_table_name}' created.")
                            flag = 1
                        else:
                            # print("✅ A valid table already exists. No need to create a new one.")
                            flag = 0

                        if flag == 1:
                            print(new_table_name)
                            msg_insert = (
                                "INSERT INTO "
                                + new_table_name
                                + " (user_name, message, receiver_name) VALUES (%s, %s, %s)"
                            )
                            mycursor.execute(msg_insert, (obj[0], send_msg, receiver_name))
                            mydb.commit()
                        else:
                            table_final = existing_tables[0][0]
                            msg_insert = (
                                "INSERT INTO "
                                + table_final
                                + "(user_name, message, receiver_name) VALUES (%s, %s, %s)"
                            )
                            mycursor.execute(msg_insert, (obj[0], send_msg, receiver_name))
                            mydb.commit()

                    if flag == 1:
                        f3 = open(new_table_name + ".txt", "a")
                        f3.write(obj[0] + " : " + send_msg + "\n")
                        f3.close()
                    else:
                        f3 = open(table_final + ".txt", "a")
                        f3.write(obj[0] + " : " + send_msg + "\n")
                        f3.close()

            elif msg_choice == 2:
                print()
                count = 1
                for i in con_list:
                    j = i.split(" ")
                    print(f"\t{count}.{j[0] :<10} : {j[1] :<10}")
                    # print()
                    count = count + 1
                    # print("\t\t\t","="*40,"|","="*40)
                print()
                sender_name = input("\tenter sender name : ")

                select_receiver = "select * from contact"
                mycursor.execute(select_receiver)
                con_obj = mycursor.fetchall()
                flag = 0
                block_flag=0
                for i in con_obj:
                    if i[3] == sender_name:
                        if i[2] == obj[0] :
                            flag = 1
                            if i[5]==True:
                                print("\t✅ You are already in contact with this user.")
                                block_flag=1
                                break
                        

                if block_flag==0 :
                    print("contact blocked")
                elif flag == 0:
                    print("\tnumber not found")

                else:
                    received_msg = []
                    folder_path = "D:\pythongroup"
                    files = os.listdir(folder_path)
                    # print(files)
                    file1 = sender_name + "_" + obj[0] + ".txt"
                    file2 = obj[0] + "_" + sender_name + ".txt"
                    flag = 1
                    if file1 in files:
                        f4 = open(file1, "r")
                        read_sender = f4.readlines()
                        for i in read_sender:
                            received_msg.append(i)
                        f4.close()

                    elif file2 in files:
                        f5 = open(file2, "r")
                        read_sender = f5.readlines()
                        for i in read_sender:
                            received_msg.append(i)
                        f5.close()

                    else:
                        flag = 0

                    if flag == 1:
                        print("\tmessages from", sender_name)
                        for i in received_msg:
                            print("\t", i)
                    else:
                        print("\tno chat found")

            elif msg_choice == 4 :
                this.contactlist(obj)

            elif msg_choice == 5:
                print()
                count = 1
                for i in con_list:
                    j = i.split(" ")
                    print(f"\t{count}.{j[0] :<10} : {j[1] :<10}")
                    # print()
                    count = count + 1
                    # print("\t\t\t","="*40,"|","="*40)
                print()
                block_name = input("\tenter the name of the person you want to block : ")

                select_for_block = "select * from contact"
                mycursor.execute(select_for_block)
                con_obj = mycursor.fetchall()
                flag = 0
                for i in con_obj:
                    if i[3] == block_name:
                        if i[2] == obj[0] and i[5]==1:
                            block_query="update contact set block_users = False where contact_name = '" + block_name + "' and user_name = '" + obj[0]+"'"
                            mycursor.execute(block_query)
                            mydb.commit()
                            flag = 1
                            break

                if flag == 0:
                    print("\tnumber not found")

                else:
                    print(block_name,"block successfully")


            elif msg_choice == 6:
                # mainmenu_flag=False
                break


l1 = login()
l1.login_page()