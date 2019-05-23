import discord
import os
import asyncio
import random
import openpyxl


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='>>', type=1))


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    print('{} / {}: {}'.format(channel, author, content))

    if message.content == '>>33':
        if message.channel.id == "510732183099670529":
            if message.author.roles[1].name == "외부인":
                await client.send_message(message.channel, "dd 씀")
            else:
                await client.send_message(message.channel, "넌 못 씀")

    if message.content == '!안녕':
        await client.send_message(message.channel, "안녕하세요")

    if message.content == '>>리그':
        await client.send_message(message.channel, "https://www.twitch.tv/overwatchleague_kr")

    if message.content.startswith('>>골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice) - 1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, "||" + choiceresult + "||")

    if message.content.startswith('>>쟁탈추첨'):
        food = "리장 타워/일리오스/오아시스/부산/네팔"
        foodchoice = food.split("/")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('>>배그맵추첨'):
        pubg = "에란겔/미라마/사녹/비켄디"
        pubgchoice = pubg.split("/")
        pubgnumber = random.randint(1, len(pubgchoice))
        pubgresult = pubgchoice[pubgnumber - 1]
        await client.send_message(message.channel, pubgresult)

    if message.content.startswith('!메모장쓰기'):
        file = open("디스코드봇메모장.txt", "w")
        file.write("안녕하세요")
        file.close()

    if message.content.startswith('!메모장읽기'):
        file = open("디스코드봇메모장.txt")
        await client.send_message(message.channel, file.read())
        file.close()

    if message.content.startswith('!학습'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        learn = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == "-" or sheet["A" + str(i)].value == learn[1]:
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                await client.send_message(message.channel, "단어가 학습되었습니다.")
                break
        file.save("기억.xlsx")

    if message.content.startswith('!기억') and not message.content.startswith('!기억삭제'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == memory[1]:
                await client.send_message(message.channel, sheet["B" + str(i)].value)
                break

    if message.content.startswith('!기억삭제'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == str(memory[1]):
                sheet["A" + str(i)].value = "-"
                sheet["B" + str(i)].value = "-"
                await client.send_message(message.channel, "기억이 삭제되었습니다.")
                file.save("기억.xlsx")
                break

    if message.content.startswith('!팀나누기'):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, person[i] + "---->" + teamname[i])


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    delchannel = message.server.get_channel("527859699702562828")
    await client.send_message(delchannel, '{} / {}: {}'.format(channel, author, content))

@client.event
async def on_member_join(member):
    fmt = '<@332564579148103691>\n{0.mention}님이 {1.name}에 입장하였습니다.'
    channel = member.server.get_channel("516122942896078868")
    await client.send_message(channel, fmt.format(member, member.server))
    #await client.send_message(member, "디스코드 권한 부여 해 드렸고요")
    role = discord.utils.get(member.server.roles, name='외부인')
    await client.add_roles(member, role)

@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("516122942896078868")
    fmt = '{0.mention}\n{0.nick}님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
