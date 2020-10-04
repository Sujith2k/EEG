from kivy.app import App
from kivymd.theming import ThemeManager 
from kivymd.toast import toast
from kivy.properties import ObjectProperty

import socket
import threading
import time
record = False

def listen_to_socket():
    global record

    socket.setdefaulttimeout(2)

    s = socket.socket()
    s.settimeout(2)     
    s.bind(('0.0.0.0', 8090 ))
    s.listen(0)
    print('Listening Thread started')
    while True:
        time.sleep(0.01)
        try:
            while (record == True):
                client, addr = s.accept()
                while True:
                    content = client.recv(32)
                
                    if len(content) ==0:
                        break
                
                    else:
                        print(content)
                
                print("Closing connection")
                client.close()

        except Exception as e:
            print(e)

    print('Leaving Thread')

class MainApp(App):
    theme_cls = ThemeManager()

    status1 = ObjectProperty()



    def Start_recording(self):
        toast('Started Recording')
        print('[DEBUG] :Start Recording Button Pressed')
        global record
        record = True

        

    
    def Stop_recording(self):
        toast('Stopped Recording')
        print('[DEBUG] :Stop Recording Button Pressed')
        global record
        record = False


if __name__ == "__main__":
    listeing_thread = threading.Thread(target= listen_to_socket) 
    listeing_thread.start()
    MainApp().run()