import os
from pathlib import Path
import shutil
import platform
import getpass


# Linux
if platform.system() == "Linux":
    source_hotkeys = Path("/home/burny/syncthing/secrets/repos/SC2Hotkeys/Burny.SC2Hotkeys")
    # source_hotkeys2 = "/home/burny/syncthing/secrets/repos/SC2Hotkeys/BurnySteal.SC2Hotkeys"
    source_hotkeys2 = Path(
        "/home/burny/syncthing/secrets/repos/SC2Hotkeys/BurnyStealColemak.SC2Hotkeys"
    )
# Windows
else:
    source_hotkeys = r"D:\Dropbox\github\SC2Hotkeys\Burny.SC2Hotkeys"
    source_hotkeys2 = r"D:\Dropbox\github\SC2HotkeysSmurf\BurnySteal.SC2Hotkeys"

# Linux
if platform.system() == "Linux":
    user_name = getpass.getuser()
    # normal_folder = f"/home/{user_name}/Games/battlenet/drive_c/users/{user_name}/My Documents/StarCraft II/Hotkeys"
    # accounts_folder = f"/home/{user_name}/Games/battlenet/drive_c/users/{user_name}/My Documents/StarCraft II/Accounts"
    normal_folder = Path("/media/ssd480/Games/starcraft5/drive_c/users/burny/Documents/StarCraft II/Hotkeys/")
    accounts_folder = Path("/media/ssd480/Games/starcraft5/drive_c/users/burny/Documents/StarCraft II/Accounts/")
# Windows
else:
    user_name = os.environ["USERNAME"]
    normal_folder = f"C:/Users/{user_name}/Documents/StarCraft II/Hotkeys"
    accounts_folder = Path(f"C:/Users/{user_name}/Documents/StarCraft II/Accounts")

if os.path.isfile(source_hotkeys):
    # Copy hotkeys to all account folders
    for folder in accounts_folder.iterdir():
        target_folder = folder / "Hotkeys"
        if target_folder.is_dir():
            shutil.copy(source_hotkeys, target_folder)
            print(f"Copying {source_hotkeys} to {target_folder}")
            if source_hotkeys2.is_file():
                print(f"Copying {source_hotkeys2} to {target_folder}")
                shutil.copy(source_hotkeys2, target_folder)

    print(f"Copying {source_hotkeys} to {normal_folder}")
    normal_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_hotkeys, normal_folder)
    if source_hotkeys2.is_file():
        print(f"Copying {source_hotkeys2} to {normal_folder}")
        shutil.copy(source_hotkeys2, normal_folder)
else:
    print(f"Source hotkey file not found! Path: {source_hotkeys}")
