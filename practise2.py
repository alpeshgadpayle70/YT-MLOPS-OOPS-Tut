#create class
class chatgpt:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.main()
    
    #create a method
    def main(self):
        user=input("""Enter your query
                      1.Press to 1 Signup
                      2.Press to 2 Signin
                      3.Press to 3 write a post
                      4.Press to 4 message friend
                        Press any key to quit""")
        if user=="1":
            self.signup()
        elif user=="2":
            self.signin()
        elif user=="3":
            self.post()
        elif user=="4":
            self.msg()l
        else:
            quit()

    
    def signup(self):
        email=input("enter the email id")
        pwd=input("enter the password")
        self.username=email
        self.password=pwd
        print("\n")
        self.main()

    
    def signin(self):
        if self.username=='' and self.password=='':
            print("please add correct id/password")
        else:
            use=input("enter your mail")
            pwd=input("Enter the password")
            if self.username==use and self.password==pwd:
                print("you have signin sucessfully")
                self.loggedin=True
        print("\n")
        self.main()

    
    def post(self):
        if self.loggedin==True:
            txt=input("write a post")
            print(f"your post has to be posted {txt}")
        else:
            print("password\id incorrect")
        print("\n")
        self.main()



    def msg(self):
        if self.loggedin==True:
            txt=input("write a friend name")
            print(f"your msg send to {txt}")
        else:
            print("password\id incorrect")
        print("\n")
        self.main()
     


#obj=chatgpt()