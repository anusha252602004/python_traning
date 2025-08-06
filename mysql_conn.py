import mysql.connector
def update_people(people_id,new_name,password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="anusha_ece"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE people SET name = %s,password = %s WHERE id = %s"
    val = (new_name,password,people_id)
    mycursor.execute(sql,val)
    mydb.commit()   
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount, "record inserted.")

id = input("enter people ID to update ")
name = input("enter new name")
password = input("enter new password")
update_people(id,name,password)