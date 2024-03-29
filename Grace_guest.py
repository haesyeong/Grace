import discord
from discord.ext.commands import Bot
import random
import datetime
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import asyncio

intents = discord.Intents().all()

client=Bot(command_prefix=('>>',), intents=intents)

content=lambda message:message.content
author=lambda message:message.author
channel=lambda message:message.channel.id
current_time=lambda:datetime.datetime.utcnow()+datetime.timedelta(hours=9)

grace=None

BETA=False
BETA_TESTLAB=486550288686120961

channels={
    '가입상담':    510732183099670529,
    '출입로그':   516122942896078868,
    }

roles={
    '외부인':      510731224654938112,
    '손님':        510497018213564426,
}

if BETA:
    for _ in channels:
        channels[_]=BETA_TESTLAB

def is_moderator(member):
    return "운영진" in map(lambda x:x.name, member.roles) or "스태프" in map(lambda x:x.name, member.roles)

def has_role(member, role):
    return role in map(lambda x:x.name, member.roles)

@client.event
async def on_message(message):
    global grace
    grace=client.get_guild(359714850865414144)

    if channel(message)!=channels['가입상담']:
        return

    if content(message).startswith(">>손님"):
        enter=author(message)
        reference=' '.join(content(message).split()[1:])

        if not has_role(enter, '외부인'):
            await message.delete()
            return

        if not reference:
            await message.delete()
            return

        outsider=grace.get_role(roles['외부인'])
        guest=grace.get_role(roles['손님'])
        logchannel=grace.get_channel(channels['출입로그'])
        
        await logchannel.send("{}님이 {}님의 손님으로 들어오셨습니다.".format(enter.mention, reference))

        await enter.add_roles(guest, atomic=True)
        await enter.remove_roles(outsider, atomic=True)

    await message.delete()

@client.event
async def on_ready():
    global grace
    await client.wait_until_ready()
    grace=client.get_guild(359714850865414144)
    print("login: Grace Guest")
    print(client.user.name)
    print(client.user.id)
    print("---------------")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)