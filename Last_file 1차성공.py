import subprocess
from time import sleep
import os

# 리스트를 만드는 작업
from winreg import *
import sys

varSubkey = ""  # 서브레지스트리 목록 지정
varSubkey7 = "Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun"  # 서브레지스트리 목록 지정

varReg = ConnectRegistry(None, HKEY_USERS)  # 루트 레지스트리 핸들 객체 얻기
# print(varReg)
# print("-----------------------------------00")
varKey = OpenKey(varReg, None)  # 레지스트리 핸들 객체 얻기 여기서 문제가 되네.. 기존 키값과
# print(varKey)
# print("-----------------------------------0")
li = []


for i in range(6):  # 이중 포문이 필요할듯 .. 허미 3번째가 그값인데 그값에다 . 넣어주어야 하기때문에 항상 1개빢에 안됨
    for z in range(4):
        try:
            keyname = EnumKey(varKey, i)  # 지정한 레지스트리의 하위 키값 조회
            # print(keyname)
            # print("-----------------------------------1")
            # 하위 레지스트리 목록 생성 : 상위 레지스트리 목록과 하위 키값 결합
            str1 = 'REG ADD HKEY_USERS'
            str2 = '\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun'
            if (z == 0):
                varSubkey2 = str1 + \
                    "%s\\%s" % (varSubkey, keyname) + str2 + ' /v ' + \
                    "windows /d hellow2 /f"
                li.append(varSubkey2)
                # print(varSubkey2)
            else:
                varSubkey2 = str1 + \
                    "%s\\%s" % (varSubkey, keyname) + str2 + ' /v ' + \
                    str(z) + " /d hellow2 /f"
                # print(str+varSubkey2)
                # print(varSubkey2)
                z = z+1
                li.append(varSubkey2)
            # print(li)
            # with open(wichi, 'w') as f:

            # a.append(varSubkey2) #리스트에 저장하기 ..

            # print("-----------------------------------2")
            # varKey2 = OpenKey(varReg, a[i])  # 레지스트리 핸들 객체 얻기
            # print(varKey2)
            # print("-----------------------------------3")
            # try:
            #     for j in range(1024):
            #         # 레지스트리 가진 데이터 얻기 : 값이름, 데이터형, 데이터 조회
            #         n, v, t = EnumValue(varKey2, j)
            #         if ("DisallowRun" in n and "windows" in v):  # 사용자 계정 정보 추출
            #             print(v)
            # except:
            #     errorMsg = "Exception Inner:", sys.exc_info()[0]
            #     # print errorMsg
            # CloseKey(varKey2)
        except:
            errorMsg = "Exception Outter:", sys.exc_info()[0]
            break

CloseKey(varKey)  # 핸들 객체 반환
CloseKey(varReg)
# for y in range(len(li)):
#     print(li[y])

# 리스트 만드는 작업 끝


# li = ['REG ADD HKEY_USERS\S-1-5-21-2018056800-1039841730-2809374972-1002\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /v 1 /d hellow2 /f',
#       'REG ADD HKEY_USERS\S-1-5-21-2018056800-1039841730-2809374972-1002\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /v 2 /d hellow2 /f',
#       'REG ADD HKEY_USERS\S-1-5-21-2018056800-1039841730-2809374972-1002\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /v windows /d haha /f']

for k in range(len(li)):
    current_machine_id = subprocess.check_output(li[k])
# len(li)
# print(len(li))
# print(li[k])

# REG ADD HKEY_USERS\S-1-5-21-2018056800-1039841730-2809374972-1002\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /v 1 /d hellow2 /f
# pyinstaller -w --uac-admin --onefile Last_file.py
# d여기까지 ok


# ================= 디폴트 레지 넣기 ================= 바로 li 초기값으로 넣기


'REG DELECT "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\$hgstarterjp.exe" /f',
'REG DELECT "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\AVG SecureVPN.exe" /f',
'REG DELECT "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Vpn.exe" /f',
'REG DELECT HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\avg_vpn_online_setup.exe /f'
