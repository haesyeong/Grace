import discord
import asyncio
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import random
import openpyxl
import datetime

BETA=False

intents = discord.Intents().all()

client = discord.Client(intents=intents)
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

url='https://docs.google.com/spreadsheets/d/1gfSsgM_0BVqnZ02ZwRsDniU-qkRF0Wo-B7rJhYoYXqc/edit?usp=drive_web&ouid=108946956826520256706'

current_time=lambda:datetime.datetime.utcnow()+datetime.timedelta(hours=9)

@client.event
async def on_ready():
    global grace
    await client.wait_until_ready()
    grace=client.get_guild(359714850865414144)
    print("login: Grace Main")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(activity=discord.Game(name='>>', type=1))

async def get_spreadsheet(ws_name):
    creds=ServiceAccountCredentials.from_json_keyfile_name("Grace-defe42f05ec3.json", scope)
    auth=gspread.authorize(creds)

    if creds.access_token_expired:
        auth.login()
    
    try:
        worksheet=auth.open_by_url(url).worksheet(ws_name)
    except gspread.exceptions.APIError:
        return
    return worksheet

def has_role(member, role):
    return role in map(lambda x:x.name, member.roles)

async def get_member_by_gametag(overwatch, valorant):
    global grace
    grace=client.get_guild(359714850865414144)

    for member in grace.members:
        try:
            if (overwatch!=None and member.nick.startswith(overwatch+'/OW/')):
                return overwatch, member
            if (valorant!=None and member.nick.startswith(valorant+'/VR/')):
                return valorant, member
        except:
            continue
    return None, None

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel

    if not ((BETA and channel.id == 486550288686120961) or (not BETA and channel.id == 419397742025113612)): return

    print('{} / {}: {}'.format(channel, author, content))
    
    if message.content.startswith(">>"):
        author = message.content
        author = author.split(">>")
        author = author[1]

        if author=='':
            return
        
        spreadsheet=await get_spreadsheet('responses')
        roles=spreadsheet.col_values(6)
        battletags=spreadsheet.col_values(2)
        
        if author=="운영진":
            spreadsheet=await get_spreadsheet('staff')
            data=spreadsheet.get_all_values()
            log = '\n\n'.join(map(lambda x:'\n'.join([t for t in x if t!='']), data))
            embed = discord.Embed(title=":fire: 운영진 목록\n", description=log, color=0x5c0bb7)
            await channel.send(embed=embed)
            return

        nickname = spreadsheet.col_values(2)
        
        try:
            index = nickname.index(author) + 1
            print(index)
        except gspread.exceptions.CellNotFound:
            return
        except gspread.exceptions.APIError:
            return
        
        indices = ['mention', 'command', 'overwatch', 'valorant', 'link', 'description', 'image', 'thumbnail', 'arena', 'league_first', 'league_second', 'friends']

        values = spreadsheet.row_values(index)

        while len(values)<len(indices):
            values.append('')

        data = dict(zip(indices, values))

        maintag, member=await get_member_by_gametag(data['overwatch'], data['valorant'])
        print(maintag, member)
        if maintag==data['overwatch']:
            data['maintag']='오버워치'
        elif maintag==data['valorant']:
            data['maintag']='발로란트'

        if member==None:
            return
        elif has_role(member, '클랜 마스터'):
            data['role']='클랜 마스터'
        elif has_role(member, '운영진'):
            data['role']='운영진'
        elif has_role(member, '클랜원'):
            data['role']='클랜원'
        elif has_role(member, '신입 클랜원'):
            data['role']='신입 클랜원'
        else:
            return

        if data['role'] == "클랜 마스터":
            data['roleimage'] = ":pen_ballpoint:"
        elif data['role'] == "운영진":
            data['roleimage'] = ":construction_worker:"
        elif data['role'] == "클랜원":
            data['roleimage'] = ":boy:"
        elif data['role'] == "신입 클랜원":
            data['roleimage'] = ":baby:"

        print(data)

        banned=["X", '', 'x', None]
        if data['link'] in banned:
            embed = discord.Embed(title="한줄소개", description=data['description'], color=0x5c0bb7)
        else:
            embed = discord.Embed(title="바로가기", url=data['link'], description=data['description'], color=0x5c0bb7)

        embed.set_author(name=maintag)
        embed.add_field(name="멘션", value=data['mention'], inline=True)
        embed.add_field(name="직책", value=data['roleimage'] + data['role'], inline=True)

        #if data['maintag']!='발로란트' and data['valorant'] not in banned:
        #    embed.add_field(name='발로란트', value = data['valorant'], inline=False)
        if data['maintag']!='오버워치' and data['overwatch'] not in banned:
            embed.add_field(name='오버워치', value = data['overwatch'], inline=False)

        if data['arena'] not in banned:
            embed.add_field(name="Grace Arena", value=":trophy: 제" + data['arena'] + "회 우승", inline=False)
        if data['league_first'] not in banned:
            embed.add_field(name="Grace League", value=":first_place: 제" + data['league_first'] + "회 우승", inline=False)
        if data['league_second'] not in banned:
            embed.add_field(name="Grace League", value=":second_place:제" + data['league_second'] + "회 준우승", inline=False)
        if data['friends'] not in banned:
            embed.add_field(name="우친바", value=data['friends'], inline=False)
        if data['image'] not in banned:
            embed.set_image(url=data['image'])
        if data['thumbnail'] not in banned:
            embed.set_thumbnail(url=data['thumbnail'])

        await channel.send(embed=embed)

@client.event
async def on_message_delete(message):
    if BETA: return

    create = str(message.created_at).split('.')[0]
    if message.edited_at:
    	create+='(최종수정 {})'.format(str(message.edited_at+datetime.timedelta(hours=9)).split('.')[0])
    author = message.author
    content = message.clean_content
    channel = message.channel
    delchannel = message.guild.get_channel(527859699702562828)
    await delchannel.send('{} - {} / {}: {}'.format(create, channel, author, content))

@client.event
async def on_member_join(member):
    if BETA: return

    fmt = '<@&617396702005035024>\n{0.mention}님이 {1.name}에 입장하였습니다.'
    channel = member.guild.get_channel(516122942896078868)
    role = member.guild.get_role(510731224654938112)
    await member.add_roles(role)
    await channel.send(fmt.format(member, member.guild))

@client.event
async def on_member_remove(member):
    if BETA: return

    channel = member.guild.get_channel(516122942896078868)
    fmt = '{0.mention}\n{0.nick}님이 서버에서 나가셨습니다.'
    await channel.send(fmt.format(member, member.guild))

async def periodic_sweep():
    if BETA: pass#return

    global grace
    await client.wait_until_ready()
    cur=current_time()
    next_notify=datetime.datetime(cur.year, cur.month, cur.day, 1, 0, 0)+datetime.timedelta(days=1)
    while True:
        await asyncio.sleep((next_notify-current_time()).seconds)
        next_notify+=datetime.timedelta(days=1)
        print('next sweep:', next_notify)
        
        creds=ServiceAccountCredentials.from_json_keyfile_name("Grace-defe42f05ec3.json", scope)
        auth=gspread.authorize(creds)
        
        if creds.access_token_expired:
            auth.login()

        sheet=auth.open_by_url("https://docs.google.com/spreadsheets/d/1gfSsgM_0BVqnZ02ZwRsDniU-qkRF0Wo-B7rJhYoYXqc/edit#gid=174260089")
        try:
            worksheet=sheet.worksheet('responses')
        except gspread.exceptions.APIError:
            print('spreadsheet error; trying tomorrow.')
        
        grace=client.get_guild(359714850865414144)
        res=worksheet.get_all_values()
        nicks={*map(lambda x:x.nick.split('/')[0:1] if (x.nick!=None and '/' in x.nick) else '', grace.members)}

        print("Command sweep")
        for i in range(1,len(res)):
            print(res[i][2], res[i][3], (((res[i][2],'O') not in nicks) or ((res[i][3],'V') not in nicks)), res[i][1]!="")
            if (((res[i][2],'O') not in nicks) or ((res[i][3],'V') not in nicks)) and res[i][1]!="":
                worksheet.update_cell(i+1,2,"")

        print("Record sweep")
        to_be_deleted=[]
        for i in range(1,len(res)):
            print(res[i][2], res[i][3], (((res[i][2],'O') not in nicks) or ((res[i][3],'V') not in nicks)), ''.join((res[i][8:])).strip()=="")
            if (((res[i][2],'O') not in nicks) or ((res[i][3],'V') not in nicks)) and ''.join((res[i][8:])).strip()=="":
                to_be_deleted.append(i)

        print(to_be_deleted)
        for i in reversed(sorted(to_be_deleted)):
            worksheet.delete_rows(i+1)

        print('sweep finished')

access_token = os.environ["BOT_TOKEN"]
#client.loop.create_task(periodic_sweep())
client.run(access_token)
