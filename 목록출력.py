# -*- coding: utf-8 -*-

from winreg import *
import sys

varSubkey = ""  # 서브레지스트리 목록 지정
varSubkey7 = "Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"  # 서브레지스트리 목록 지정

varReg = ConnectRegistry(None, HKEY_USERS)  # 루트 레지스트리 핸들 객체 얻기
# print(varReg)
# print("-----------------------------------00")
varKey = OpenKey(varReg, None)  # 레지스트리 핸들 객체 얻기 여기서 문제가 되네.. 기존 키값과
# print(varKey)
# print("-----------------------------------0")
wichi = 'c:\\test\\unilog32.txt'

for i in range(5):
    try:
        keyname = EnumKey(varKey, i)  # 지정한 레지스트리의 하위 키값 조회
        # print(keyname)
        # print("-----------------------------------1")
        # 하위 레지스트리 목록 생성 : 상위 레지스트리 목록과 하위 키값 결합
        varSubkey2 = "%s\\%s" % (keyname, varSubkey7)
        print(varSubkey2)

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

# for j in range(a):
#     n, v, t = EnumValue(a, j)  # 레지스트리 가진 데이터 얻기 : 값이름, 데이터형, 데이터 조회
#     if ("DisallowRun" in n and "windows" in v):  # 사용자 계정 정보 추출
#         print(v)

CloseKey(varKey)  # 핸들 객체 반환
CloseKey(varReg)
