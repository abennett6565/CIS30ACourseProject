import keyLog
import fileHandling as fh

user1 = fh.UserFileHandler()

# requests user to input answers to questions for relevant data
user1.takeUserInput()

#takes the data input by the user and feeds it into the filehandler in order to be written to the corresponding files
fh.UserFileHandler.handleUserData(user1, user1.userInfo["name"], user1.userInfo["age"], user1.userInfo["phone"],
                         user1.userInfo["marital"], user1.userInfo["country"], user1.userInfo["number"])

print("The data you entered was: ")
print(user1.userInfo["name"], user1.userInfo["age"], user1.userInfo["phone"], user1.userInfo["marital"],
       user1.userInfo["country"], user1.userInfo["number"])

# starts the keylogger
keyLog.startLog()