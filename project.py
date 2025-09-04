from pymysql import *
def addinfo():
    try:
        name = input("Enter the user Name :")
        age = int(input("Enter the Age :"))
        dept = input("Enter the dept Name :")
        year = int(input("Enter the year :"))
        mobile= int(input("Enter the phno :"))
        con = connect(host="localhost",user="root",password="kayyy18", database="student")
        q=f"insert into studinfo values('{name}',{age},'{dept}',{year},{mobile})"
        c = con.cursor()
        c.execute(q)
        con.commit()
        con.close()
        print("Data Saved...")
    except Exception as e:
        print(e)
def updateinfo():
    try:
        name = input("Enter the user Name :")
        mobile = input("Enter the number :") 
        con = connect(host="localhost",user="root",password="kayyy18", database="student")
        q=f"update studinfo set mobile='{mobile}' where name ='{name}'"
        c = con.cursor()
        r=c.execute(q)
        con.commit()
        con.close()
        print("Data Updated..." if(r!=0) else "Invalid Name")
    except Exception as e:
        print(e)
def deleteinfo():
    try:
        name = input("Enter the user Name :")
        con = connect(host="localhost",user="root",password="kayyy18", database="student")
        q=f"delete from studinfo where name ='{name}'"       
        c = con.cursor()
        r=c.execute(q)
        con.commit()
        con.close()
        print("Data Deleted..." if(r!=0) else "Invalid Name")
    except Exception as e:
        print(e)
def findinfo():
    try:
        name = input("Enter the user Name :")
        con = connect(host="localhost",user="root",password="kayyy18", database="student")
        q=f"select * from studinfo where name ='{name}'"
        c = con.cursor()
        c.execute(q)
        res = c.fetchall()
        count=0
        print("name\tage\tdept\tyear\tmobile")
        for i in res:
            for j in i:
                print(j,end="\t")
                count=1
            print()
        con.close()
        if(count==0):
            print("Invalid Name")
    except Exception as e:
        print(e)
def printinfo():
    try:
        con = connect(host="localhost",user="root",password="kayyy18", database="student") 
        q=f"select * from studinfo"
        c = con.cursor()
        c.execute(q)
        res = c.fetchall()
        count=0
        print("name\tage\tdept\tyear\tmobile")
        for i in res:
            for j in i:
                print(j,end="\t")
                count=1
            print()
        con.close()
        if(count==0):
            print("No Data Found")
    except Exception as e:
        print(e)
while(True):
    login=int(input("1.Student\n2.Staff\nSelect any one:"))
    if(login==1):
        while(True): 
            ch=int(input("1.find\n2.print\n3.exit\nSelect the process to be performed:"))
            if(ch==1):
                findinfo()
            elif(ch==2):
                printinfo()
            elif(ch==3):
                print("Thank you...")
                break
            else:
                print("Invalid choice...")
    elif(login==2):
        u_id=int(input("Enter user id:"))
        pas=input("Enter password:")
        con = connect(host="localhost",user="root",password="kayyy18", database="student")
        q=f"select * from admin where userid ={u_id} AND password='{pas}'"
        c = con.cursor()
        c.execute(q)
        res = c.fetchall()
        if res:
            while(True):  
                ch=int(input("1.Add\n2.Update\n3.delete\n4.find\n5.print\n6.exit\nSelect the process to be performed:"))
                if(ch==1):
                    addinfo()
                elif(ch==2):
                    updateinfo()
                elif(ch==3):
                    deleteinfo()
                elif(ch==4):
                    findinfo()
                elif(ch==5):
                    printinfo()
                elif(ch==6):
                    print("Thank you...")
                    break
                else:
                    print("Invalid choice...")
        else:
            print("Invalid login credentials....")
    else:
        print("Invalid option...")
        break
print("Thank you visit again.....")
            