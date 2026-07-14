class chatbook:
    #Attributes
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    #Fuction/Method
    def menu(self):
        user_input = input(""""Welcome to chatbook !! How would you like to proceed?
                       1. Press 1 to signup
                       2. Press 2 to signin
                       3. Press 3 to write a post
                       4. press 4 to message friend
                       5. press any other key to exit
                       ->""")     
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter your emanil: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("You have signed up Sucessfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("please singup first by pressing in the main menu")
        else:
            uname = input("Enter your emanil/Usename: ")
            pwd = input("Enter your password: ")
            if self.username==uname and self.password==pwd:
                print("you have signed in sucessfully")
                self.loggedin = True
            else:
                print("Please input correct credential...")
        print("\n")
        self.menu()

    def  my_post(self):
        if self.loggedin==True:
            txt=input("Enter your message here-->")
            print(f"following content has been posted-->{txt}")
        else:
            print("you need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your message here-->")
            frnd=input("whom to send the msg?-->")
            print(f"your message has been sent to {frnd}")
        else:
            print("you need to signin first to post something...")
        print("\n")
        self.menu()

obj = chatbook() 