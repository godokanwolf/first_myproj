# ssttrr = 'dndlsms'

# for i in range(5):
#     # print(str(i))

#     change_str = 'dndlsms ' + str(i) + " dndlsms"
#     print(change_str)

li = [
    'REG DELECT "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\$hgstarterjp.exe" /f',
    'REG DELECT "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\AVG SecureVPN.exe" /f',
    'REG DELECT "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Vpn.exe" /f',
    'REG DELECT HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\avg_vpn_online_setup.exe /f']

print(len(li))
for i in range(len(li)):
    print(li[i])
