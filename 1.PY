import winreg


def delete_sub_key(key0, current_key, arch_key=0):

    open_key = winreg.OpenKey(key0, current_key, 0,
                              winreg.KEY_ALL_ACCESS | arch_key)
    info_key = winreg.QueryInfoKey(open_key)
    for x in range(0, info_key[0]):
        # NOTE:: This code is to delete the key and all sub_keys.
        # If you just want to walk through them, then
        # you should pass x to EnumKey. sub_key = winreg.EnumKey(open_key, x)
        # Deleting the sub_key will change the sub_key count used by EnumKey.
        # We must always pass 0 to EnumKey so we
        # always get back the new first sub_key.
        sub_key = winreg.EnumKey(open_key, 0)
        try:
            winreg.DeleteKey(open_key, sub_key)
            print("Removed %s\\%s " % (current_key, sub_key))
        except OSError:
            delete_sub_key(key0, "\\".join([current_key, sub_key]), arch_key)
            # No extra delete here since each call
            # to delete_sub_key will try to delete itself when its empty.

    winreg.DeleteKey(open_key, "")
    open_key.Close()
    print("Removed %s" % current_key)
    return


# Allows to specify if operating in redirected 32 bit mode or 64 bit, set arch_keys to 0 to disable
arch_keys = [winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY]

# Base key
root = winreg.HKEY_LOCAL_MACHINE

# List of keys to delete
keys = ['SOFTWARE\MyInstalledApp', 'SOFTWARE\SomeKey\SomeOtherKey']

for key in keys:
    for arch_key in arch_keys:
        try:
            delete_sub_key(root, key, arch_key)
        except OSError as e:
            print(e)
