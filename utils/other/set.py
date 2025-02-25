from utils.init import *

folders = {
    "output": ["duplicates.txt", "valid.txt", "test.txt"],
    "input": ["proxies.txt", "joined.txt", "tester.txt"]
}

local_version = "2.0"
pastebin_url = "https://pastebin.com/raw/9nP1VDG0"

def updcheck():
    print(f"                                        {ldb}[{w}Checking For Any Available Updates{ldb}]")
    time.sleep(1)
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        latestv = response.text.strip()
        clear()
        logo() 
        if local_version != latestv:
            print(f"                                       {ldb}[{s}{crtime}{ldb}] {s}| {g}[{w}Update Available{g}] {w}→ {latestv}")
        else:
            print(f"                                       {ldb}[{s}{crtime}{ldb}] {s}| {ldb}[{w}No Updates Available{ldb}] {w}→ {latestv}")
    except requests.RequestException:
        clear() 
        logo() 
        print(f"                                      {ldb}[{s}{crtime}{ldb}] {s}| {r}Failed To Check For Updates")
logo()
print(f"                                      {ldb}[{w}Files are missing. Press Enter to create them{ldb}]")
print("")
input(f"                                      {ldb}[{lc}POLO{ldb}] {s}| {ldb}[{lc}INPUT{ldb}] {lc}→ Press Enter ")
print("")
for folder, files in folders.items():
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"                                      {ldb}[{s}{crtime}{ldb}] {s}| {ldb}[{lc}Done{ldb}]{w} ——→ {folder}")
    else:
        print(f"                                      {ldb}[{s}{crtime}{ldb}] {s}| {ldb}[{lc}Exists{ldb}]{w} → {folder}")
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass
            print(f"                                      {ldb}[{s}{crtime}{ldb}] {s}| {ldb}[{lc}Done{ldb}]{w} ——→ {file_path}")
        else:
            print(f"                                      {ldb}[{s}{crtime}{ldb}] {s}| {ldb}[{lc}Done{ldb}]{w} ——→ {file_path}")
time.sleep(2)
clear()
logo()