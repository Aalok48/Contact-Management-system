from tkinter import *
from tkinter import messagebox as tmsg

# Creating a basic GUI interface
root = Tk()
root.geometry("400x450")
root.resizable(False, False)
root.title("Contact Management System")
root.iconbitmap("D:\VS code projects\Contact management.py")

# frame for the "Welcome to contact management" text
main_frame = Frame(root, width=370, height=100, bg="red")
main_frame.place(x=45, y=30)
# label for the text "Welcome to contact management"
l1 = Label(main_frame, text="Welcome to Contact Management", font='comics 15')
l1.pack(anchor="center")

# frame for all the buttons
button_frame = Frame(root, width=350, height=300)
button_frame.place(x=35, y=95)


# code for the add page
def add():
    root2 = Tk()
    root2.geometry("350x300")
    root2.resizable(False, False)
    root2.title("Add contact")

    # code for name label and name entry
    name = Label(root2, text="Name:", font="comics 12")
    name.place(x=35, y=50)
    name_entry = Entry(root2, width=25, relief="groove", borderwidth=5, border=5)
    name_entry.place(x=105, y=50, )

    # code for contact label and contact entry
    contact = Label(root2, text="Contact:", font="comics 12")
    contact.place(x=35, y=90)
    contact_entry = Entry(root2, width=25, relief="groove", borderwidth=5, border=5)
    contact_entry.place(x=105, y=90)

    # code for address label and address entry
    address = Label(root2, text="Address:", font="comics 12")
    address.place(x=35, y=130)
    address_entry = Entry(root2, width=25, relief="groove", border=5, borderwidth=5)
    address_entry.place(x=105, y=130)

    # code for gmail label and gmail entry
    gmail = Label(root2, text="G-mail:", font="comics 12")
    gmail.place(x=35, y=170)
    gmail_entry = Entry(root2, width=25, relief="groove", border=5, borderwidth=5)
    gmail_entry.place(x=105, y=170)

    # code for finish button
    # first stored the value entered in entry box in their respective variables and stored them in a nested dictionary
    # if the user clicks on 'yes' in messagebox then the dictionary is changed to string and then stored in the file
    def finish():
        name_text = name_entry.get()
        contact_text = contact_entry.get()
        address_text = address_entry.get()
        gmail_text = gmail_entry.get()
        data_dict = {name_text: {"contact": contact_text, "address": address_text, "gmail": gmail_text}}
        answer = tmsg.askquestion("Ready to save", "Save changes")
        if answer == 'yes':
            with open("data.txt", "a") as file:
                dict_str = str(data_dict)
                file.write(dict_str)
                file.write('\n')
                file.close()
        root2.destroy()

    # button for the finish block
    Button(root2, text="Finish", width=10, borderwidth=0, font="comics 10", command=finish).place(x=125, y=230)

    root2.mainloop()


# code for the delete function
def delete():
    root_delete = Tk()
    root_delete.title("Delete a contact")
    root_delete.geometry("200x100")
    label4 = Label(root_delete, text="Enter name: ")
    label4.place(x=10, y=20)
    del_entry = Entry(root_delete, width=15, relief="sunken")
    del_entry.place(x=85, y=20)

    # the delete function asks for the name of the contact to be deleted and stores it in the del_entry_value variable
    # the file where the data is stored is opened in read mode and the data is stored in content variable
    # a new list is created and the content variable is iterated and checked for the contact to be deleted
    # the contact that is not matched with contact to be deleted is saved to list and stored to the file
    def delete_contact():
        del_entry_value = del_entry.get()
        with open("data.txt", "r") as file:
            content = file.readlines()

        new_content = []
        for line in content:
            if del_entry_value not in line:
                new_content.append(line)

        with open("data.txt", "w") as file:
            file.writelines(new_content)
            file.close()

        root_delete.destroy()

    # code for the delete block
    button_del = Button(root_delete, text="Delete", width=10, relief="groove", command=delete_contact)
    button_del.place(x=65, y=55)

    root_delete.mainloop()


# code for the edit function to edit the existing contact
def edit():
    # GUI for the entry of contact to be searched
    root_edit = Tk()
    root_edit.title("Edit contact")
    root_edit.geometry("225x90")
    label_edit = Label(root_edit, text="Enter name:", font="comics 12")
    label_edit.place(x=5, y=5)
    # entry box for the contact to be searched
    entry_edit = Entry(root_edit, width=15, borderwidth=3, border=3, relief="ridge")
    entry_edit.place(x=100, y=5)

    def edit2():
        edit2_var = entry_edit.get()
        root_edit.destroy()
        with open("data.txt", "r") as file:
            content = file.readlines()
            for line in content:
                if edit2_var in line:
                    info_list = []
                    line2 = eval(line)
                    for name, info in line2.items():
                        contact_number = info['contact']
                        address = info['address']
                        gmail = info['gmail']
                        info_list.append([contact_number, address, gmail])
                    a = info_list[0]
                    root_edit_view = Tk()
                    root_edit_view.geometry("350x300")
                    root_edit_view.title("Edit contact")
                    # code for name label and name entry
                    name = Label(root_edit_view, text="Name:", font="comics 12")
                    name.place(x=35, y=50)
                    name_entry = Entry(root_edit_view, width=25, relief="groove", borderwidth=5, border=5)
                    name_entry.insert(END, edit2_var)
                    name_entry.place(x=105, y=50, )

                    # code for contact label and contact entry
                    contact = Label(root_edit_view, text="Contact:", font="comics 12")
                    contact.place(x=35, y=90)
                    contact_entry = Entry(root_edit_view, width=25, relief="groove", borderwidth=5, border=5)
                    contact_entry.insert(END, a[0])
                    contact_entry.place(x=105, y=90)

                    # code for address label and address entry
                    address = Label(root_edit_view, text="Address:", font="comics 12")
                    address.place(x=35, y=130)
                    address_entry = Entry(root_edit_view, width=25, relief="groove", border=5, borderwidth=5)
                    address_entry.insert(END, a[1])
                    address_entry.place(x=105, y=130)

                    # code for gmail label and gmail entry
                    gmail = Label(root_edit_view, text="G-mail:", font="comics 12")
                    gmail.place(x=35, y=170)
                    gmail_entry = Entry(root_edit_view, width=25, relief="groove", border=5, borderwidth=5)
                    gmail_entry.insert(END, a[2])
                    gmail_entry.place(x=105, y=170)

                    def save_changes():
                        new_name = name_entry.get()
                        new_contact_number = contact_entry.get()
                        new_address = address_entry.get()
                        new_gmail = gmail_entry.get()
                        root_edit_view.destroy()
                        new_info = {'contact': new_contact_number, 'address': new_address.capitalize(),
                                    'gmail': new_gmail}
                        new_line = {new_name.capitalize(): new_info}
                        try:
                            content.remove(line)
                        except ValueError:
                            tmsg.showinfo("Error", "Contact not found")
                            return
                        content.append(str(new_line) + "\n")
                        with open("data.txt", "w") as file1:
                            file1.writelines(content)
                        tmsg.showinfo("Success", "Contact updated successfully")

                    # button for the finish block
                    Button(root_edit_view, text="Save changes", width=10, borderwidth=0, font="comics 11",
                           command=save_changes).place(x=125,
                                                       y=230)
                    file.close()
                    root_edit_view.mainloop()
                    break

            else:
                tmsg.showerror("ERROR", "Contact searched is not saved ")

    # button call the edit2 function to initiate the edit process
    button_edit = Button(root_edit, text="Next", borderwidth=0, border=0, font="comics 12", command=edit2)
    button_edit.place(x=85, y=50)
    root_edit.mainloop()


# code for the view function to view the list of all the contacts
def view():
    root3 = Tk()
    root3.title("Contacts")
    text = Text(root3)
    text.grid(row=0, column=0, sticky='nsew')

    # scrollbar for the view interface to scroll if there are many contacts
    scrollbar = Scrollbar(root3, orient="vertical", command=text.yview, width=20)
    scrollbar.grid(row=0, column=1, sticky='ns')
    text.config(yscrollcommand=scrollbar.set)
    # Open the file in read mode
    with open('data.txt', 'r') as f:
        # Loop through each line of the file
        for line in f:
            # Convert the line to a dictionary using eval()
            my_dict = eval(line)
            contents = f'Name: {list(my_dict.keys())[0]}\nContact: {my_dict[list(my_dict.keys())[0]]["contact"]}\nAddress: {my_dict[list(my_dict.keys())[0]]["address"]}\nGmail: {my_dict[list(my_dict.keys())[0]]["gmail"]}\n\n---\n\n '
            text.insert(END, contents)
        f.close()


# code for the search function
# root_search is the GUI for taking the contact to be searched
# root_search_view is the GUI for viewing the details of the contact searched
def search():
    root_search = Tk()
    root_search.geometry("200x75")
    root_search.title("Search Contact")
    Label(root_search, text="Enter contact: ").place(x=5, y=5)
    # entry box for the contact to be searched
    search_entry = Entry(root_search, width=15, relief="solid")
    search_entry.place(x=90, y=5)

    # code that searches the contact in file and shows in a new interface
    def search2():
        search_text = search_entry.get()
        with open("data.txt", "r") as file:
            content = file.readlines()
            found_match = False
            for line in content:
                if search_text in line:
                    my_dict = eval(line)
                    contents = f'Name: {list(my_dict.keys())[0]}\nContact: {my_dict[list(my_dict.keys())[0]]["contact"]}\nAddress: {my_dict[list(my_dict.keys())[0]]["address"]}\nGmail: {my_dict[list(my_dict.keys())[0]]["gmail"]}'
                    root_search_view = Tk()
                    root_search_view.geometry("300x100")
                    root_search_view.title("Contacts")
                    root_search_view.resizable(False, False)
                    Label(root_search_view, text=contents).pack()
                    root_search.destroy()
                    found_match = True
                    root_search_view.mainloop()
                    break

            # code that shows error if non-existing contact is searched
            if not found_match:
                root_search.destroy()
                tmsg.showerror("ERROR", "Contact not found")
        file.close()

    # button that calls the search function
    Button(root_search, text="Search", border=0, borderwidth=0, font="comics 10", command=search2).place(x=65, y=45)
    root_search.mainloop()


# creating first button named add a contact
b1 = Button(button_frame, text="1. Add a contact", command=add, borderwidth=0, font="15")
b1.pack(fill=X)

# creating second button named delete a contact
b2 = Button(button_frame, text="    2. Delete a Contact", command=delete, borderwidth=0, font=15)
b2.pack(fill=X, pady=5)

# creating third button named edit a contact
b3 = Button(button_frame, text="3. Edit a contact", command=edit, borderwidth=0, font=15)
b3.pack(pady=5)

# creating forth button named see all contacts
b4 = Button(button_frame, text="    4. View all contacts", borderwidth=0, command=view, font=15)
b4.pack(pady=5)

# creating fifth button named search contacts
b5 = Button(button_frame, text="    5. Search a contact", command=search, borderwidth=0, font="15")
b5.pack(pady=5)

root.mainloop()
