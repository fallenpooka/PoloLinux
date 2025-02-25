import os
import webbrowser
import asyncio
import discord
import requests
import threading
import time
import ctypes
import aiohttp
import json
from discord.ext import tasks
from datetime import datetime
from colorama import Fore, init
from pystyle import System

d = Fore.BLACK       
w = Fore.WHITE       
r = Fore.RED          
g = '\x1b[38;5;2m'    
y = "\x1b[38;5;178m"   
b = "\x1b[38;5;69m"   

sx, sxs, sxsx = 20, 20, 20  
l = f"\033[38;2;{sx};{sxs};{sxsx}m"  

s = Fore.LIGHTBLACK_EX  
lr = Fore.LIGHTRED_EX  
lg = '\x1b[38;5;10m'   
ly = '\x1b[38;5;220m'  
lb = Fore.LIGHTBLUE_EX

dg = '\x1b[38;5;28m'

ldb = "\x1b[38;5;67m"  
ldc = "\x1b[38;5;44m" 
ldg = "\x1b[38;5;28m"  
ldm = "\x1b[38;5;125m"  

vdb = "\x1b[38;5;18m"  
llb = "\x1b[38;5;153m"  
vdg = "\x1b[38;5;22m"  
lgr = "\x1b[38;5;120m" 
dp = "\x1b[38;5;54m"   
lp = "\x1b[38;5;183m"  
lc = "\x1b[38;5;195m" 
vdr = "\x1b[38;5;52m"  

fb1 = "\x1b[38;5;18m"    
fb2 = "\x1b[38;5;19m"   
fb3 = "\x1b[38;5;20m"  
fb4 = "\x1b[38;5;25m"   
fb5 = "\x1b[38;5;32m"   
fb6 = "\x1b[38;5;39m"   
fb7 = "\x1b[38;5;45m"   
fb8 = "\x1b[38;5;51m"    

fc1  = "\x1b[38;5;159m"  
fc2  = "\x1b[38;5;123m" 
fc3  = "\x1b[38;5;81m"  

p = "\x1b[38;5;93m"   
dp = "\x1b[38;5;55m"  
lp = "\x1b[38;5;139m" 

fp1 = "\x1b[38;5;201m" 
fp2 = "\x1b[38;5;199m" 
fp3 = "\x1b[38;5;13m" 
fp4 = "\x1b[38;5;55m"  
fp5 = "\x1b[38;5;93m"  

with open('tokens.txt', 'r') as file:
    tokens = [line.strip() for line in file if line.strip()]

for token in tokens:
    halftkn = token[:len(token) // 2]

def ctime():
    return datetime.now().strftime("%H:%M:%S")
crtime = ctime()

System.Size(120, 22)

def logo():
    logo = fr"""
{lc}                                            ________      ______      
{fc1}                                            ___  __ \________  /_____ 
{fc2}                                            __  /_/ /  __ \_  /_  __ \
{fc3}                                            _  ____// /_/ /  / / /_/ /
{ldb}                                            /_/     \____//_/  \____/ 
    """
    print(logo)
 
def clear():
    os.system("cls" if os.name == "nt" else "clear")