import  autoit
import   time

def  provide_credentials():
    autoit.send("test")
    time.sleep(2)
    autoit.send("{TAB}")
    time.sleep(3)
    autoit.send("password")

provide_credentials()

