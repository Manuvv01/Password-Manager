from tkinter import *
from tkinter import messagebox
import random, pyperclip, json

def main():

    #Password function
    def password_gen():

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        #Ranges of the characters
        num_letters = random.randint(8, 10)
        num_symbols = random.randint(4, 6)
        num_numbers = random.randint(3, 4)

        password_letters = [random.choice(letters) for char in range(num_letters)]
        password_symbols = [random.choice(symbols) for char in range(num_symbols)]
        password_numbers = [random.choice(numbers) for char in range(num_numbers)]

        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)

        password = "".join(password_list)
        password_input.insert(0, password)#Ends function

    def copy():
        pyperclip.copy(password_input.get())


    def store():
        #Variables storing the entries inputs
        website_data = website_input.get()
        user_data = user_input.get()
        password_data = password_input.get()
        data_dict = {
            website_data: {
                "Email/User": user_data,
                "Password": password_data
            }
        }

        #Input Validation(Fields blank)
        if len(website_data) == 0 or len(user_data) == 0 or len(password_data) == 0:
            error_msg = messagebox.showerror(title="Error", message= "Fields don't need to be empty") #Error box
        else:
            try:
                with open("secret.json", "r") as json_data:
                    py_data = json.load(json_data) #converts the json data as py dict named py_data
                    py_data.update(data_dict) #Appends the new dict data with the py_data dictionary

                #Write the new data in the json file
                with open("secret.json", "w") as json_data:
                    json.dump(py_data, json_data, indent= 4)
            #If dile doesn't exist
            except FileNotFoundError:
                with open("secret.json", "w") as json_data:
                    json.dump(data_dict, json_data, indent= 4)

            finally:
                message_box = messagebox.showinfo(title="Confirmation", message="Data stored")   #Confirmation Box
                website_input.delete(0, END)
                user_input.delete(0, END)
                password_input.delete(0, END)
                json_data.close()

    def search_password():
        web = website_input.get()
        with open("secret.json") as data_file:
            data = json.load(data_file)
            if web in data:
                website_search = data[web]["Email/User"]
                password_search = data[web]["Password"]
                messagebox.showinfo(title = "Search box", message= f" Email/User: {website_search}\n Password: {password_search}\n")

    #Window layout
    window = Tk()
    window.title("Password Generator")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=200, height=200)
    logo = PhotoImage(file = "logo.png")
    canvas.create_image(100,100, image = logo)
    canvas.grid(row = 0, column= 2)

    website = Label(text= "Website:")
    website.grid(row = 1, column = 0)

    email = Label(text= "Email/Username:")
    email.grid(row = 2, column = 0)

    password_label = Label(text= "Password:")
    password_label.grid(row = 3, column = 0)

    website_input = Entry(width=35)
    website_input.grid(row = 1, column = 1, columnspan= 2)
    website_input.focus()  #To start typing on website entry

    search_button = Button(text = "Search", command= search_password)
    search_button.grid(row = 1, column = 3)

    user_input = Entry(width=35)
    user_input.grid(row = 2, column = 1, columnspan= 2)

    password_input = Entry(width=35)
    # password_input = Entry(width=21)
    password_input.grid(row = 3, column = 1, columnspan= 2)

    copy_button = Button(text= "Copy", command= copy)
    copy_button.grid(row=3, column= 3)
    # copy_button.place(x= 240, y= 243)

    generate_button = Button(text="Generate Password", command= password_gen)
    generate_button.grid(row=3, column=4)
    # generate_button.place(x= 280, y= 243)


    add_button = Button(text="Add", width=36, command= store)
    add_button.grid(row=4, column= 1, columnspan= 2)

    window.mainloop()

if __name__ == "__main__":
    main()
