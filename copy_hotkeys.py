import sys
import os
import shutil
import platform
import getpass


# Linux
if platform.system() == "Linux":
    source_hotkeys = "/home/burny/Dropbox/github/SC2Hotkeys/Burny.SC2Hotkeys"
    source_hotkeys2 = "/home/burny/Dropbox/github/SC2HotkeysSmurf/BurnySteal.SC2Hotkeys"
# Windows
else:
    source_hotkeys = r"D:\Dropbox\github\SC2Hotkeys\Burny.SC2Hotkeys"
    source_hotkeys2 = r"D:\Dropbox\github\SC2HotkeysSmurf\BurnySteal.SC2Hotkeys"

# Linux
if platform.system() == "Linux":
    user_name = getpass.getuser()
    normal_folder = f"/home/{user_name}/Games/battlenet/drive_c/users/{user_name}/My Documents/StarCraft II/Hotkeys"
    accounts_folder = f"/home/{user_name}/Games/battlenet/drive_c/users/{user_name}/My Documents/StarCraft II/Accounts"
# Windows
else:
    user_name = os.environ["USERNAME"]
    normal_folder = f"C:/Users/{user_name}/Documents/StarCraft II/Hotkeys"
    accounts_folder = f"C:/Users/{user_name}/Documents/StarCraft II/Accounts"

if os.path.isfile(source_hotkeys):
    # Copy hotkeys to all account folders
    for folder in os.listdir(accounts_folder):
        target_folder = os.path.join(accounts_folder, folder, "Hotkeys")
        if os.path.isdir(target_folder):
            shutil.copy(source_hotkeys, target_folder)
            print(f"Copying {source_hotkeys} to {target_folder}")
            if os.path.isfile(source_hotkeys2):
                print(f"Copying {source_hotkeys2} to {target_folder}")
                shutil.copy(source_hotkeys2, target_folder)

    print(f"Copying {source_hotkeys} to {normal_folder}")
    shutil.copy(source_hotkeys, normal_folder)
    if os.path.isfile(source_hotkeys2):
        print(f"Copying {source_hotkeys2} to {normal_folder}")
        shutil.copy(source_hotkeys2, normal_folder)
else:
    print(f"Source hotkey file not found! Path: {source_hotkeys}")
