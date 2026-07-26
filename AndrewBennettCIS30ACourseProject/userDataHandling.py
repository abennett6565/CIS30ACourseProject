class User():

    userInfo = {
        "name": "",
        "age": "",
        "phone": "",
        "marital": "",
        "country": "",
        "number": ""
    }

    #prompt the user for their information, validate type
    def takeUserInput(self):
        try:
            self.userInfo["name"] = input("Please enter your name: ")
            self.userInfo["age"] = input("Please enter your age: ")
            self.userInfo["phone"] = input("Please enter your phone number: ")
            self.userInfo["marital"] = input("Please enter your marital status: ")
            self.userInfo["country"] = input("Please enter what country you live in: ")
            self.userInfo["number"] = input("Please enter your favorite number: ")
        except(TypeError):
            print("Some of the input was the wrong type! Please try again")
