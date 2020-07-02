import sqlite3
try:
    con=sqlite3.connect("database_dir/contact_database.db")
    cur=con.cursor()
except:
    print("Error cannot connect to database ")

def write_to_base(name,num,address):
    global con,cur
    try:
        cur.execute(f"insert into contacts values('{name}','{num}','{address}')")
        con.commit()
        print("Called")
    except:
        print("Error!!")

def fetch_from_base():
    global con,cur
    try:
        cur.execute("select * from contacts")
        return(cur.fetchall())
    except:
        print("Error!")

def fetch_by_name(name):
    global con,cur
    try:
        cur.execute(f"select * from contacts where name='{name}'")
        return cur.fetchall()
    except:
        print("Error!!")

def del_from_base(num):
    global con,cur
    try:
        cur.execute(f"delete from contacts where number='{num}'")
        con.commit()
    except Exception as e:
        print("Error occured : ",e)

# del_from_base('232323232')
#
# print(fetch_by_name("Bivsdfkvvv"))
