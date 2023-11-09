import subprocess as sp
import pymysql
import pymysql.cursors


def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")

def AddStadium():

    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new stadium's details: ")
        row["Name"] = input("Name :")
        row["Capacity"] = int(input("Capacity :"))
        Address = (input("Address (country-state-city-street): ")).split('-')
        row["Address_country"] = Address[0]
        row["Address_state"] = Address[1]
        row["Address_city"] = Address[2]
        row["Address_street"] = Address[3]

        query = "INSERT INTO STADIUM(Name,Capacity,Address_country,Address_state,Address_city,Address_street) VALUES('%s', '%d', '%s', '%s', '%s', '%s')" % (
            row["Name"], row["Capacity"], row["Address_country"], row["Address_state"], row["Address_city"], row["Address_street"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def AddPlayer():
   
    try:
        
        row = {}
        print("Enter new player's details: ")
        row["Name"] = input("Enter Name: ")
        dob = input("Birth Date (YYYY-MM-DD): ").split('-')
        row["Date_date"] = int(dob[2]) 
        row["Date_month"] = int(dob[1]) 
        row["Date_year"] = int(dob[0])

        row["JerseyNum"] = int(input("JerseyNum: "))
        row["Age"] = int(input("Age: "))
        row["AllRounder"] = input("Allrounder(Y/N): ")
        row["Player_teamid"] =int(input("Team ID: "))

        query = "INSERT INTO PLAYERS VALUES('%s','%d','%d','%d','%d','%d','%c','%d')" % (
            row["Name"],row["Date_date"],row["Date_month"],row["Date_year"],row["JerseyNum"],row["Age"],row["AllRounder"],row["Player_teamid"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def UpdateResult():
   
    try:
        matchid=int(input("Match ID:"))
        teamwon=int(input("Id of winner team:"))

        query = "UPDATE MATCHES SET Teamwon=%d WHERE Match_ID=%d"%(teamwon,matchid)

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return

def DeleteStadium():

    try:
        # Takes emplyee details as input
        row = {}
        print("Enter stadium's details to be deleted: ")
        row["Name"] = input("Name :")

        query = "DELETE FROM STADIUM WHERE Name='%s'"%(row["Name"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        AddPlayer()
    elif(ch == 2):
        AddStadium()
    elif(ch == 3):
        DeleteStadium()
    elif(ch == 4):
        UpdateResult()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="xforce",
                              db='IPL',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Add player")  # Hire an Employee
                print("2. Add stadium")  # Fire an Employee
                print("3. Delete Stadium")  # Promote Employee
                print("4. Update result")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
