class User():

    userInfo = {
        "name": "",
        "age": "",
        "phone": "",
        "marital": "",
        "country": "",
        "number": ""
    }

    #prompt the user for their information
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

    #validate the information that the user provided
    def validateUserData(self, name:str, age:str, phone:str, marital:str, country:str, number:str):
        validName = False
        validAge = False
        validPhone = False
        validMarital = False
        validCountry = False
        validNumber = False

        if name.isalpha():
            validName = True

        if age.isdigit():
            validAge = True

        if phone.isdigit():
            validPhone = True

        if marital.isalpha():
            validMarital = True

        if country.isalpha():
            validCountry = True

        if number.isdigit():
            validNumber = True

        if validName and validAge and validPhone and validMarital and validCountry and validNumber:
            return True
        else:
            return False

    #store the user's data into a text file
    def storeUserData(self, name:str, age:str, phone:str, marital:str, country:str, number:str):
        with open("user_info.txt", "w") as file:
            file.write("Name: " + name + "\n")
            file.write("Age: " + age + "\n")
            file.write("Phone Number: " + phone + "\n")
            file.write("Marital Status: " + marital + "\n")
            file.write("Home Country: " + country + "\n")
            file.write("Favorite Number: " + number + "\n")

    #read the user's data from the text file
    def readUserData(self, name:str, age:str, phone:str, marital:str, country:str, number:str):
        with open("user_info.txt", "r") as file:
                for line in file:
                    print(line)

    #runs the various other functions related to user data
    def handleUserData(self, name:str, age:str, phone:str, marital:str, country:str, number:str):
        if self.validateUserData(name, age, phone, marital, country, number):
            self.storeUserData(name, age, phone, marital, country, number)
            self.readUserData(name, age, phone, marital, country, number)
        else:
            print("Invalid data was entered, please try again.")

