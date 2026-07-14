class chatmax:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    
    def menu(self):
        user_input = input("""Enter your input
                            1.Press 1 to Signup
                            2.Press 2 to Signin
                            3.Press 3 to write post
                            4.Press 4 to message friend""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.msg()
        else:
            exit()

    
    def signup(self):
        email=input("Enter the email")
        pwd=input("Enter the password")
        self.username=email
        self.password=pwd
        print("Your id sucessfully signup")
        print("\n")
        self.menu()
    

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first to signin")
        else:
            use=input('enter username')
            pwd=input('enter the password')
            if self.username==use and self.password==pwd:
                print('you have successfully signin')
                self.loggedin=True
            else:
                print("Please add correct userid and password")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter your post here")
            print(f"following content has been posted {txt}")
        else:
            print("Please add correct userid and password")
        print("\n")
        self.menu()

    
    def msg(self):
        if self.loggedin==True:
            txt=input("Enter your post here")
            print(f"following content has been posted {txt}")
        else:
            print("Please add correct userid and password")
        print("\n")
        self.menu()

obj = chatmax()