from winreg import *

key_to_read = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'

try:
    reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    k = OpenKey(reg, key_to_read)

    print("ok found")
    print(k)

except:
    print("sorry not found")
