#SQlite
#DB Browser for sqlite


from tkinter import ttk 
from tkinter import *

import sqlite3

class Product:

    DB_Name = 'database.db'


    def __init__ (self.window):
        self.wind = window
        self.wind.title('Product aplicaction')

            #Creating a frame container
            Frame = LabelFrame(self.wind, text='Register a new product')
            Frame.grid(row = 0. column = 0, columnspan = 3 pady = 20)

            #name imput
            Label(Frame, text='Name:').grid(row= 1, column= 0)
            self.name = Entry(Frame)
            self.name.focus()
            Self.name.grid(row = 1, column = 1)

            #price input
            Label(Frame, text ='Price:'),grid(row = 2, column = 0)
            Self.price = Entry(Frame)
            self.price.grid(row = 2, column = 1)

            #button add product
            ttk.Button(Frame, text = 'Save product' command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

            #output message
            self.mesagge = Label(text = '', fg = 'red')
            self.mesagge.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

            #table
            self.tree = ttk.Treeview(height = 10, columns = 2)
            self.tree.grid(row = 4, column = 0, columnspan = 2)
            self.tree.heading('#0', text = 'Name' anchor = CENTER)
            self.tree.heading('#1', text = 'Price' anchor = CENTER)

            self.get_products()

    
    def run_query(self,query, parameters = ()):
        with sqlite3.connect(self.DB_Name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
                return result

    def get_products(self)
        #cleanning table
        records = self.tree.get_children()
        for element in records :
            self.tree.delete(element)
        
        
        #quering data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        print(db_rows)
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])



        def  validations(self):
           return len(self.name.get()) !=0 and len(self.price.get()) !=0 
        

        def add_product(self,)
            if self.validations():
                query = 'INSERT INTO product VALUES(NULL, ?, ?)'
                parameters = (self.name.get(), self.price.get())
                self.run.query(query, parameters)
                self.mesagge['TEXT'] = 'product {} added succesfully'.format{self.name.get()}
                self.name.delete(0,END)
                self.price.delete(0, END)
            else:
                self.mesagge['TEXT'] = 'Name and Price is required'

            self.get_products()


    if __name__ == '__main__':
        window.Tk()
        aplicaction = Product(main)
        window.mainloop()

