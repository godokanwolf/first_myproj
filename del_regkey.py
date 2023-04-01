from winreg import *

varSubkey = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"  # 서브레지스트리 목록 지정
varReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)  # 루트 레지스트리 핸들 객체 얻기
Key_Name = r'Software\Qube Cinema\QubeMaster Pro'
key = OpenKey(HKEY_USER, Key_Name, r'S-1-5-21-2018056800-1039841730-2809374972-1002\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun',
              winreg.KEY_ALL_ACCESS)
DeleteKey(key, '1')

S-1-5-21-2018056800-1039841730-2809374972-1002\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun\
