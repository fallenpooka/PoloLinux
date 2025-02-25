from utils.init import *

async def accinfo(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    user_info_url = "https://discord.com/api/v9/users/@me"
    billing_info_url = "https://discord.com/api/v9/users/@me/billing/subscriptions"
    try:
        user_info = requests.get(user_info_url, headers=headers).json()
        if "id" not in user_info:
            print("Invalid token or unauthorized access.")
            return
        user_id = user_info.get("id", "N/A")
        username = f"{user_info.get('username', 'N/A')}#{user_info.get('discriminator', '0000')}"
        email = user_info.get("email", "N/A")
        phone = user_info.get("phone", "N/A")
        fa = user_info.get("mfa_enabled", False)
        billing_info = requests.get(billing_info_url, headers=headers).json()
        nitro = any(item['type'] == 1 for item in billing_info)
        print(f"                                             {ldb}[{lc}NITRO{ldb}]    {lc}→ {w}{'True' if nitro else 'False'}")
        print(f"                                             {ldb}[{lc}USERID{ldb}]   {lc}→ {w}{user_id}")
        print(f"                                             {ldb}[{lc}USERNAME{ldb}] {lc}→ {w}{username}\n")
        print(f"                                             {ldb}[{lc}MAIL{ldb}]     {lc}→ {w}{email}")
        print(f"                                             {ldb}[{lc}PHONE{ldb}]    {lc}→ {w}{phone}")
        print(f"                                             {ldb}[{lc}2FA{ldb}]      {lc}→ {w}{'True' if fa else 'False'}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

async def infomain():
    clear()
    logo()
    token = input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Token{ldb}]{lc} → ")
    clear()
    logo()
    await accinfo(token)
    input(f"\n                                             {ldb}[{lc}POLO{ldb}] {s}| {ldb}[{lc}INPUT{ldb}] {lc}→ {w}Press Enter ")
    os.system('python polo.py')