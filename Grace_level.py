import discord
from discord.ext.commands import Bot
import random
import datetime
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import asyncio

import worksheet_funcs as ws_f

intents = discord.Intents().all()

level_to_exp=[0,200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3400,3800,4200,4600,5000,5400,5800,6200,6600,7000,7800,8600,9400,10200,11000,11800,12600,13400,14200,15000,16600,18200,19800,21400,23000,24600,26200,27800,29400,31000,34200,37400,40600,43800,47000,50200,53400,56600,59800,63000,69400,75800,82200,88600,95000,101400,107800,114200,120600,127000]
checkin_exp=10
hello_exp=50
hello_limit=10

client=Bot(command_prefix=('!',), intents=intents)

content=lambda ctx:ctx.message.content
author=lambda ctx:ctx.message.author
channel=lambda ctx:ctx.message.channel.id
current_time=lambda:datetime.datetime.utcnow()+datetime.timedelta(hours=9)

def is_moderator(member):
    return "운영진" in map(lambda x:x.name, member.roles)

def has_role(member, role):
    return role in map(lambda x:x.name, member.roles)

addr='https://docs.google.com/spreadsheets/d/1gfSsgM_0BVqnZ02ZwRsDniU-qkRF0Wo-B7rJhYoYXqc/edit?usp=drive_web&ouid=108946956826520256706'
scope=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
grace=None
    
@client.command()
async def 출석(message):
    user=author(message)
    ws=ws_f.get_worksheet('responses')
    cols=ws_f.get_col_order(ws)
    row_idx=ws_f.search(ws, 'mention', user.mention, cols=cols)
    row=ws_f.get_row(ws, row_idx, cols=cols)
    if row['checkin']!=current_time().strftime("%Y%m%d"):
        await ws_f.give_exp(ws, checkin_exp, client, row_idx=row_idx, cols=cols, update_date=True)
        await message.channel.send(f'{user.mention}님의 {current_time().strftime("%Y년 %m월 %d일")} 출석체크가 완료되었습니다.')
    else:
        await message.channel.send(f'{user.mention}님은 이미 출석체크를 하셨습니다.')

@client.command()
async def 안녕(message):
    user=author(message)
    targets=content(message).split()[1:]
    replies=[]
    await message.message.delete()
    for target in targets:
        ws=ws_f.get_worksheet('responses')
        cols=ws_f.get_col_order(ws)
        row_idx=ws_f.search(ws, 'mention', target, cols=cols)
        row=ws_f.get_row(ws, row_idx, cols=cols)
        print(row)
        if target==user:
            reply=await message.channel.send(f'본인에게는 사용할 수 없습니다.')
        elif ws_f.level(int(row['exp']))>=10:
            print(ws_f.level(int(row['exp'])))
            reply=await message.channel.send(f'신입 클랜원에게만 사용할 수 있습니다.')
        elif user.mention in row['exp_get'].split():
            reply=await message.channel.send(f'이미 경험치를 한번 지급했습니다.')
        elif len(row['exp_get'].split(','))>=hello_limit:
            await ws_f.give_exp(ws, 0, client, row_idx=row_idx, cols=cols, add_giver=user.mention)
            reply=await message.channel.send(f'{user.mention}님이 {target}님께 인사합니다.')
        else:
            await ws_f.give_exp(ws, hello_exp, client, row_idx=row_idx, cols=cols, add_giver=user.mention)
            reply=await message.channel.send(f'{user.mention}님이 {target}님께 인사하며 경험치를 줍니다.')
        replies.append(reply)
    await asyncio.sleep(0.5)
    for reply in replies:
        await reply.delete()

############################################################
#자동 기록(이벤트)
@client.event
async def on_ready():
    print("login: Grace Level")
    print(client.user.name)
    print(client.user.id)
    print("---------------")

############################################################
#실행
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
