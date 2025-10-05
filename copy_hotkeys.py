import os
from pathlib import Path
import shutil
import platform
import getpass


# Linux
if platform.system() == "Linux":
    source_hotkeys = [
         Path("/home/burny/syncthing/secrets/repos/SC2Hotkeys/BurnySteal_QWERTZ.SC2Hotkeys"),
         Path("/home/burny/syncthing/secrets/repos/SC2Hotkeys/BurnySteal_QWERTY.SC2Hotkeys"),
         Path("/home/burny/syncthing/secrets/repos/SC2Hotkeys/BurnySteal_Colemak.SC2Hotkeys"),
         Path("/home/burny/syncthing/secrets/repos/SC2Hotkeys/BurnyArcade_Colemak.SC2Hotkeys"),
    ]
# Windows
else:
    source_hotkeys = [
         Path(r"D:\Dropbox\github\SC2Hotkeys\Burny.SC2Hotkeys"),
         Path(r"D:\Dropbox\github\SC2HotkeysSmurf\BurnySteal.SC2Hotkeys"),
    ]

# Linux
if platform.system() == "Linux":
    user_name = getpass.getuser()
    # normal_folder = f"/home/{user_name}/Games/battlenet/drive_c/users/{user_name}/My Documents/StarCraft II/Hotkeys"
    # accounts_folder = f"/home/{user_name}/Games/battlenet/drive_c/users/{user_name}/My Documents/StarCraft II/Accounts"
    normal_folder = Path("/media/ssd250/Games/StarCraft/pfx/drive_c/users/burny/Documents/StarCraft II/Hotkeys/")
    accounts_folder = Path("/media/ssd250/Games/StarCraft/pfx/drive_c/users/burny/Documents/StarCraft II/Accounts/")
# Windows
else:
    user_name = os.environ["USERNAME"]
    normal_folder = Path(f"C:/Users/{user_name}/Documents/StarCraft II/Hotkeys")
    accounts_folder = Path(f"C:/Users/{user_name}/Documents/StarCraft II/Accounts")

# Copy hotkeys to all account folders
normal_folder.mkdir(parents=True, exist_ok=True)
for source_file in source_hotkeys:
    target2_file = normal_folder / source_file.name
    print(f"Copying {source_hotkeys} to {normal_folder}")
    shutil.copy(source_file, target2_file)

    for folder in accounts_folder.iterdir():
        target_folder = folder / "Hotkeys"
        if target_folder.is_dir():
            target1_file = target_folder / source_file.name
            print(f"Copying {source_file} to {target_folder}")
            shutil.copy(source_file, target1_file)
else:
    print(f"Source hotkey file not found! Path: {source_hotkeys}")
