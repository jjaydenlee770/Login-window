#this project isn't made for use. it is for learning new conepts with python


import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import base64
import webbrowser



#master = Tk()
root = tk.Tk()
root.geometry("400x300")

#socials 

github_url = "https://github.com/jjaydenlee770"
youtub_url = "https://www.youtube.com/@JaydenLee-i4d"
instagran_url = "https://www.instagram.com/jjaydenlee770/"
itch_url = "https://jjaydenlee770.itch.io/"


signup_check = False
users_w = []
pass_w = []


height = root.winfo_screenheight()
width = root.winfo_screenmmwidth()

def is_right():
    placeholder_s = entry_user.get()
    placeholder_p = entry_pass.get()


    check_for_p = encrypt(placeholder_p)
    check_for_u = encrypt(placeholder_s)


    if check_for_u in users_w:
         index_s = users_w.index(check_for_u)

         if pass_w[index_s] == check_for_p:
              acces_label.config(text = "Login correct", fg = "green")
              socials()
         else:
                acces_label.config(text = "incorrect password", fg = "red")
    else:
          acces_label.config(text = "wrong username", fg = "red")
          

  
    

#storage area
def encrypt(plainText):
    plain_b = plainText.encode('ascii')
    encode_byte = base64.b64encode(plain_b)
    encode_text = encode_byte.decode('ascii')
    return(encode_text) 

def decrypt(encrypt_text):
    decryptbyte =  encrypt_text.encode('ascii')
    decodedbyte = base64.b64decode(decryptbyte)
    decode_text = decodedbyte.decode('ascii')
    return decode_text

def store(a, b):
    user_s = a
    user_p = b

    check_for_special = any(char.isdigit() for char in user_p)
    check_for_num = any(not char.isalnum() for char in user_p)

    check_user = encrypt(user_s)
    check_pass = encrypt(user_p)

    option1_error = False
    option2_error = False

    if check_user in users_w:
          
                 
                 option1_error = True
                 error_window(option1_error, option2_error)
    if check_for_special == False and check_for_num == False:
                 
                 option2_error = True
                 error_window(option1_error, option2_error)
    else:
        if check_for_special == True and check_for_num == True:
            users_w.append(check_user)
            pass_w.append(check_pass)
            print(users_w, pass_w)

    
    


def signup():
        
     
        
        popup = Toplevel(root)
        popup.title("Sign Up")
        popup.geometry("400x300")


        signup_label = Label(popup, text = " Sign Up window")

        entry_s_u = tk.Entry(popup)
        entry_s_u.bind("<Return>", lambda event: store(entry_s_u.get(), entry_s_p.get()))
        entry_s_p = tk.Entry(popup)
        entry_s_p.bind("<Return>", lambda event: store(entry_s_u.get(), entry_s_p.get()))
        entry_s_u_t = Label(popup, text= "Username")
        entry_s_p_t = Label(popup, text= "Password")
        description = Label(popup, text = "Password must include a number and a special character")



        
        signup_submit = tk.Button(popup, text="submit", command = lambda: [store(entry_s_u.get(), entry_s_p.get()), popup.destroy()])
        
        signup_label.grid(row = 0, column = 1)
        entry_s_u.grid(row = 1, column= 2)
        entry_s_u_t.grid(row = 1, column= 1)

      


        entry_s_p.grid(row = 2, column= 2)
        entry_s_p_t.grid(row = 2, column= 1)

        signup_submit.grid(row = 3, column= 2)

        description.grid(row = 4, column= 2)

def error_window(a, b):
    error = Toplevel(root)
    error.geometry("400x300")
    if a == True:
          
     error_message = Label(error, text = "Sorry Username has already been used, please try again")

    if b == True:
     error_message = Label(error, text = "Must include special characters(!@#$) and numbers(1234)")
        
          


    error_message.grid(row = 0, column = 1)


def change_theme():
    if background_var.get():
          dark_bg = "#2d2d2d"
          text_colo = "white"
    else:
         dark_bg = "#f0f0f0"
         text_colo = "black"

    root.config(bg = dark_bg)

    Login_Label.config(bg=dark_bg, fg=text_colo)
    entry_user.config(bg=dark_bg, fg=text_colo)
    entry_pass.config(bg=dark_bg, fg=text_colo)
    acces_label.config(bg=dark_bg)
    button_login.config(bg=dark_bg, fg=text_colo)
    button_sign_up.config(bg=dark_bg, fg=text_colo)
    user_label.config(bg=dark_bg, fg=text_colo)
    pass_label.config(bg=dark_bg, fg=text_colo)
background_var = tk.BooleanVar()
theme_button = tk.Checkbutton(root, text = "DarkMode", variable = background_var, command = change_theme)
theme_button.grid(row = 0, column = 2, padx = 10)






def socials():



    

    social_window = Toplevel(root)
    social_window.title("Sign Up")
    social_window.geometry("400x300")

    social_label = tk.Label(social_window, text = "Check out my socials")
    social_github = tk.Button(social_window, text = "Github", width = 25, command = lambda: webbrowser.open(github_url))
    social_youtube = tk.Button(social_window, text = "Youtube", width = 25, command = lambda:webbrowser.open(youtub_url))
    social_instagram = tk.Button(social_window, text = "Instagram", width = 25,  command = lambda:webbrowser.open(instagran_url))
    social_itch = tk.Button(social_window, text = "Itch", width = 25, command = lambda:webbrowser.open(itch_url))

    top_game_projects = tk.Label(social_window, text = "Check out the game I made")
    plinko_game = tk.Button(social_window, text = "Plinko", command = lambda:webbrowser.open("https://jjaydenlee770.itch.io/plinko"))

    social_label.grid(row = 0, column = 2)
    top_game_projects.grid(row = 10, column = 3)
    plinko_game.grid(row = 12, column = 3)

    social_github.grid(row = 2, column= 3)
    social_youtube.grid(row = 4, column= 3)
    social_instagram.grid(row = 6, column = 3)
    social_itch.grid(row = 8, column = 3)




#log in

Login_Label = tk.Label(root, text = "Log In Page")

user_label = tk.Label(root, text = "User Name")
pass_label = tk.Label(root, text = "Password")



entry_user = tk.Entry(root)
entry_user.bind("<Return>", lambda event: is_right())

entry_pass = tk.Entry(root)
entry_pass.bind("<Return>", lambda event: is_right())

button_login = tk.Button(root, text = "Log In", width = 25, command = is_right)
button_sign_up = tk.Button(root, text = "Sign Up", width = 25, command = lambda:signup())

acces_label = tk.Label(root, text = "")


Login_Label.grid(row= 0, column= 1)

entry_pass.grid(row = 4, column=1)
entry_user.grid(row = 2, column = 1)

button_login.grid(row =  5, column = 1)
button_sign_up.grid(row = 9, column = 1 )

acces_label.grid(row = 7, column= 1)

user_label.grid(row = 2, column = 0)
pass_label.grid(row = 4, column = 0)

root.mainloop()
