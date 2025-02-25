from utils.init import *

async def tkncheck():
    clear()
    logo()
    validcount = 0
    invalidcount = 0
    countlimit = 0
    validtkns = []
    invald = []
    limited = []

    with open('tokens.txt', 'r') as file:
        tokens = [line.strip() for line in file if line.strip()]
    for token in tokens:
        halftkn = token[:len(token) // 2]
        
        headers = {
            'Authorization': token
        }
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            print(f"                                {ldb}[{s}{crtime}{ldb}] {s}| {dg}[{lg}VALID{dg}] {s}  | {w}{halftkn}")
            validcount += 1
            validtkns.append(token)
        elif response.status_code == 401:
            print(f"                                {ldb}[{s}{crtime}{ldb}] {s}| {r}[{lr}INVALID{r}] {s}| {w}{halftkn}")
            invalidcount += 1
            invald.append(token)
        elif response.status_code == 429: 
            print(f"                                {ldb}[{s}{crtime}{ldb}] {s}| {y}[{ly}LIMITED{y}] {s}| {w}{halftkn}")
            countlimit += 1
            limited.append(token)
        else:
            print(f"                                {ldb}[{s}{crtime}{ldb}] {s}| {r}[{lr}Error, while checking token{lr}] {s}| {w}{halftkn}")
    clear()
    logo()        
    print(f"{ldb}[{lc}Valid{ldb}] {lc}——→ {s}[{lc}{validcount}{s}]")
    print(f"{ldb}[{lc}Invalid{ldb}] {lc}→ {s}[{lc}{invalidcount}{s}]")
    print(f"{ldb}[{lc}Limited{ldb}] {lc}→ {s}[{lc}{countlimit}{s}]")
    input(f"\n{ldb}[{lc}POLO{ldb}] {s}| {ldb}[{lc}INPUT{ldb}] {lc}→ {w}Press Enter ")
    clear()
    logo()
    print(f"                         {w}Type {ldb}[{lc}Save{ldb}] {w}to save valid tokens or type {ldb}[{lc}Return{ldb}] {w}to return\n")
    inpt = input(f"{ldb}[{lc}POLO{ldb}] {s}| {ldb}[{lc}INPUT{ldb}] {lc}→ ").strip().lower()
    if inpt == 'save':
        clear()
        logo()
        with open('valid.txt', 'w') as vfile:
            vfile.write("\n".join(validtkns))
        print(f"                                        {ldb}[{s}{crtime}{ldb}] {s}| {lg}Saved Tokens Successfully")
        time.sleep(2)
        os.system('python polo.py')
    elif inpt == 'return':
        os.system('python polo.py')