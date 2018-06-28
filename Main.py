import discord
from discord.ext import commands
import math
import asyncio
import requests
import json
import aiohttp

mybot = commands.Bot(command_prefix="!MLK ")
headers = {'Authorization': 'fabbc9c207b0057d7dccade6938eb667'}


# no bot command 
async def getIdPlaftform(st) :
    url = "https://fortnite-public-api.theapinetwork.com/prod09/users/id"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data={"username": st}, headers=headers) as response:
            respon = await response.json()
    uid = respon['uid']
    platform = respon['platforms'][0]
    print (uid + " " + platform)
    return uid,platform

async def getstats(uid,platform):
    url = "https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data={"user_id":uid,"platform":platform,"window":"alltime"}, headers=headers) as response:
             respon= await response.json()
    return respon
@mybot.event
async def on_ready():
    print ("ready")
@mybot.command(pass_context=True)
async def getcommand(ctx):
    await mybot.say(" include "+mybot.command_prefix+" to call me ")
    await mybot.say("possible commands are welcome,salute,getStat,getStatSolo,getStatDuo,getStatSquad,find :sunglasses: ")    
@mybot.command(pass_context=True)
async def welcome(ctx , user : discord.Member):
    if user.name == "sword":
        await mybot.say("hi Brudou xD")
    else:
        await mybot.say(" hi dear " + user.name + " :smile:")
@mybot.command(pass_context=True)
async def salute(ctx , user : discord.Member):
    if user.name == "sword":
        await mybot.say("bay Brudou :cry:")
    else:
        await mybot.say(" by dear " + user.name + " :sleepy:")
@mybot.command(pass_context=True)
async def getPatchNote(ctx):

    #getRequest
    url = "https://fortnite-public-api.theapinetwork.com/prod09/patchnotes/get"
    headers = {'Authorization': 'fabbc9c207b0057d7dccade6938eb667'}
    response = requests.request("POST", url, headers=headers)

    patchnotes = (json.loads(response.text)['blogList'])[0]

    #embed
    embed = discord.Embed(title = patchnotes['title'],description=patchnotes['short'])
    embed.set_image (url=patchnotes['image'])
    embed.add_field(name="To Know More Check The Url",value ='https://www.epicgames.com/fortnite/fr/patch-notes/v' + patchnotes['title'][1]+'-'+patchnotes['title'][3])
    embed.add_field(name="Date",value = patchnotes['date'])
    embed.set_author(name = patchnotes['author'])
    await mybot.say(embed=embed)

@mybot.command(pass_context=True)
async def getStat(ctx ,*strr ):

    #get id and platform
    st = (' '.join(strr)).strip()
    print (st)
    uid , platform =await getIdPlaftform(st)

    #getStat
    response = (await getstats(uid,platform))['totals']

    embed = discord.Embed(title = st + "'s stat",color = 0x77abc1)
    embed.add_field(name = "Total Win"  ,value = str(response['wins']),inline= True)
    embed.add_field(name = "Total KD"  ,value = str(response['kd']),inline= True)
    embed.add_field(name = "Total Match Played"  ,value = str(response['matchesplayed']),inline= True)
    embed.add_field(name = "Total Kills"  ,value = str(response['kills']),inline= True)
    embed.add_field(name = "Total winrate"  ,value = str(response['winrate'])+"%",inline= True)
    embed.add_field(name = "Total hours Played"  ,value = str(response['hoursplayed']),inline= True)

    await mybot.say(embed=embed)

@mybot.command(pass_context=True)
async def getStatSolo(ctx ,*strr ):

    #get id and platform
    st = (' '.join(strr)).strip()
    print (st)
    uid , platform = await getIdPlaftform(st)

    #getStat
    response = (await getstats(uid,platform))['stats']

    embed = discord.Embed(title = st + "'s stat",color = 0x77abc1)
    embed.add_field(name = "Solo Win"  ,value = str(response['placetop1_solo']),inline= True)
    embed.add_field(name = "Solo KD"  ,value = str(response['kd_solo']),inline= True)
    embed.add_field(name = "Solo Match Played"  ,value = str(response['matchesplayed_solo']),inline= True)
    embed.add_field(name = "Solo Kills"  ,value = str(response['kills_solo']),inline= True)
    embed.add_field(name = "Solo winrate"  ,value = str(response['winrate_solo'])+"%",inline= True)
    embed.add_field(name = "Solo hours Played"  ,value = str(int(response['minutesplayed_solo'])//60),inline= True)

    await mybot.say(embed=embed)

@mybot.command(pass_context=True)
async def getStatDuo(ctx ,*strr ):

    #get id and platform
    st = (' '.join(strr)).strip()
    print (st)
    uid , platform = await getIdPlaftform(st)

    #getStat
    response = (await getstats(uid,platform))['stats']

    embed = discord.Embed(title = st + "'s stat",color = 0x77abc1)
    embed.add_field(name = "Duo Win"  ,value = str(response['placetop1_duo']),inline= True)
    embed.add_field(name = "Duo KD"  ,value = str(response['kd_duo']),inline= True)
    embed.add_field(name = "Duo Match Played"  ,value = str(response['matchesplayed_duo']),inline= True)
    embed.add_field(name = "Duo Kills"  ,value = str(response['kills_duo']),inline= True)
    embed.add_field(name = "Duo winrate"  ,value = str(response['winrate_duo'])+"%",inline= True)
    embed.add_field(name = "Duo hours Played"  ,value =str(int(response['minutesplayed_duo'])//60),inline= True)

    await mybot.say(embed=embed)
@mybot.command(pass_context=True)
async def getStatSquad(ctx ,*strr ):

    #get id and platform
    st = (' '.join(strr)).strip()
    print (st)
    uid , platform = await getIdPlaftform(st)

    #getStat
    response = (await getstats(uid,platform))['stats']

    embed = discord.Embed(title = st + "'s stat",color = 0x77abc1)
    embed.add_field(name = "Squad Win"  ,value = str(response['placetop1_squad']),inline= True)
    embed.add_field(name = "Squad KD"  ,value = str(response['kd_squad']),inline= True)
    embed.add_field(name = "Squad Match Played"  ,value = str(response['matchesplayed_squad']),inline= True)
    embed.add_field(name = "Squad Kills"  ,value = str(response['kills_squad']),inline= True)
    embed.add_field(name = "Squad winrate"  ,value = str(response['winrate_squad'])+"%",inline= True)
    embed.add_field(name = "Squad hours Played"  ,value = str(int(response['minutesplayed_squad'])//60),inline= True)
    await mybot.say(embed=embed)

@mybot.command(pass_context =True)
async def find(ctx,*strr):
    #get id and platform
    strr=list(strr)
    a=int(strr[0])
    z=float(strr[1])
    print(a)
    print (z)
    strr.pop(0)
    strr.pop(0)
    #get id and platform
    st = (' '.join(strr)).strip()
    print (st)
    uid , platform = await getIdPlaftform(st)

    #getStat
    response = (await getstats(uid,platform))['stats']

    x=  math.ceil((int(response['kills_solo']) - z * int(response['matchesplayed_solo']))/(z-a))
    await mybot.say(" if you kill " + str(a) +" each game,you'll need " + str(x) + " game at a row with that kill number to reach " + str(z)+ " KD :smile:")

@mybot.command(pass_context =True)
async def spam(ctx,user: discord.Member,a=10,*strr):
    st = (' '.join(strr)).strip()
    i = 0
    while i < a:
       await mybot.say(st + " <@"+user.id+">")
       i+=1
       await asyncio.sleep(10)

@mybot.command(pass_context =True)

mybot.run("NDYxNjYwNzM1NDYyNzAzMTE2.DhWj0g.GQ4e4XVNRzklWpUblEHTKaPksgY")
