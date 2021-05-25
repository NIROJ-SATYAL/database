from tkinter import *
import sqlite3



root=Tk()
root.title("database")
#create a database or connect to one
conn=sqlite3.connect("hello.db")
#create a curser 
c=conn.cursor()


'''c.execute("""CREATE TABLE HELLO(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    phone_number int
    )""")'''

#create submit function for database

def sumbit():
    #global f_name,l_name,address,city,state,phone_number
    #create a database or connect to one
    conn=sqlite3.connect("hello.db")
    #create a curser 
    c=conn.cursor()
    #insert into table
    c.execute("INSERT INTO HELLO VALUES (:f_name, :l_name, :address, :city, :state, :phone_number)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'phone_number': phone_number.get()
                })
    #COMMIT CHANGES
    conn.commit()

    #connection close
    conn.close()
    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    phone_number.delete(0,END)

def query():
    conn=sqlite3.connect("hello.db")
    #create a curser 
    c=conn.cursor()
    #insert into table
    c.execute("SELECT *, oid FROM HELLO")
    hi=c.fetchall()
    print(hi)

    print_record=" "
    for i in hi:
        print_record+=str(i[0]) + " " + str(i[1]) + " " + str(i[6])+ "\n"
    
    query_label=Label(root,text=print_record)
    query_label.grid(row=12,column=1,columnspan=2)




    #COMMIT CHANGES
    conn.commit()

    #connection close
    conn.close()

def delete():
    conn=sqlite3.connect("hello.db")
    #create a curser 
    c=conn.cursor()
    #delete database from table
    c.execute("DELETE FROM HELLO WHERE oid=" + delete_box.get())
    delete_box.delete(0,END)



    conn.commit()

    #connection close
    conn.close()
     

#create text box
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=4,column=1)

phone_number=Entry(root,width=30)
phone_number.grid(row=5,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=8,column=1)
#cretae text box label


f_label=Label(root,text="first_name:")
f_label.grid(row=0,column=0)

l_label=Label(root,text="last_name:")
l_label.grid(row=1,column=0)

a_label=Label(root,text="address:")
a_label.grid(row=2,column=0)

c_label=Label(root,text="city:")
c_label.grid(row=3,column=0)

s_label=Label(root,text="state:")
s_label.grid(row=4,column=0)

p_label=Label(root,text="phone_number:")
p_label.grid(row=5,column=0)

delete_label=Label(root,text="delete database")
delete_label.grid(row=8,column=0)
#create a sumbit button
sumbit_button=Button(root,text="sumbit",command=sumbit)
sumbit_button.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
#create a query button
query_button=Button(root,text="query",command=query)
query_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
# create a delete button
delete_button=Button(root,text="delete",command=delete)
delete_button.grid(row=9,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
#COMMIT CHANGES
conn.commit()
#connection close
conn.close()
root.mainloop()
