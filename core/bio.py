from utils.init import *

with open('tokens.txt') as f:
    tokens = f.read().splitlines()
async def biomain(token, nbio):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        'Authorization': token,
        'Content|Type': 'application/json'
    }
    data = {
        'bio': nbio
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(fr"                                          {ldb}[{s}{crtime}{ldb}] {s}| {lg}Updated Succesfully")
    else:
        print(fr"                                          {ldb}[{s}{crtime}{ldb}] {s}| {r} Failed")
async def bio():
    while True:
        nbio = input(fr"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Bio{ldb}]{lc} → ")
        if nbio.strip():
            for token in tokens:
                await biomain(token, nbio)
        else:
            print(fr"                                          {ldb}[{s}{crtime}{ldb}] {s}| {r} This was unexpected 😪🧐")
            break