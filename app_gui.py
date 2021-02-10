'''App Name: Interactive Dictionary(GUI)
Authour : Felender
Version : 1.0
python Version: 3
'''
import json
import tkinter as tk


#load json data
data = json.load(open("data.json"))


window = tk.Tk()
window.title("Interactive Dictionary GUI")
window.geometry("600x300")



# declaring string variables
# for storing user input
user_input_var = tk.StringVar()


def translate():
    user_input = user_input_var.get().lower()
    results =  data[user_input]
    if user_input in results and user_input !='':
        print(user_input)
        lbl_result["text"] =  results
    else:
        lbl_result["text"] =  "Word don't exist. Please double check"
       


#creating a label for user input suing widget label
search_label = tk.Label(window, text="Search for word", font=('calibre',10, 'bold'))

#creating a entry for user input using widget entry
user_input_entry = tk.Entry(window, textvariable=user_input_var)


sub_btn = tk.Button(text="Search", command=translate)

#creating a button using the widget 
#button that will call the submit function 
sub_btn=tk.Button(window,text = 'Search', command = translate)

lbl_result = tk.Label()



sub_btn.grid(row=0, column=0, sticky="nsew")

lbl_result.grid(row=1, column=0)


# placing the label and entry in the required position using grid method
search_label.grid(row=0,column=0)
user_input_entry.grid(row=0,column=1)

window.mainloop()
