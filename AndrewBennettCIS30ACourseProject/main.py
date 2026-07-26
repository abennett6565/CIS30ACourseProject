import keyLog
import fileHandling as fh

user1 = fh.UserFileHandler()
user1.takeUserInput()
fh.UserFileHandler.handleUserData(user1, user1.userInfo["name"], user1.userInfo["age"], user1.userInfo["phone"],
                         user1.userInfo["marital"], user1.userInfo["country"], user1.userInfo["number"])

print("The data you entered was: ")
print(user1.userInfo["name"], user1.userInfo["age"], user1.userInfo["phone"], user1.userInfo["marital"],
       user1.userInfo["country"], user1.userInfo["number"])

keyLog.startLog()