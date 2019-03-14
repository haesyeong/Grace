import discord
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
    await client.change_presence(game=discord.Game(name='!', type=1))

@client.event
async def on_member_join(member):
    role = ""
    for i in member.server.roles:
        if i.name == "외부인":
            role = i
            break
    await client.add_roles(member, role)


@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요")
    if message.content.startswith('!이수영') and message.content.endswith('!이수영'):
        await client.send_message(message.channel,
                                  "하와와... 와타시엿던것이에요... 엣큥☆:eye: :tongue: :eye:\n-:pen_ballpoint: 클랜 마스터\n-:trophy: 제 3회 고정내전 우승팀장:crown:\n-:trophy: 제 4회 고정내전 우승자\n-:trophy: 제 15회 고정내전 우승자\n-:trophy: 제 16회 고정내전 우승자\n-:trophy: 제 17회 고정내전 우승팀장:crown:")
    if message.content.startswith('!순사'):
        await client.send_message(message.channel, "픵싄게임이다")
    if message.content == "!앙":
        await client.send_message(message.channel, "기모찌")
    if message.content.startswith('!히주'):
        await client.send_message(message.channel, "상어충")
    if message.content.startswith('!녹찻잎'):
        await client.send_message(message.channel, ":trophy: 제1회 Grace Arena 우승자")
    if message.content == "!동키":
        await client.send_message(message.channel, "당숭이 입니다 우끼끼!")


    if message.content.startswith('!주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(0, int(rolld[0]) + 1):
            dice = dice + random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('!골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice) - 1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, "||" + choiceresult + "||")

    if message.content.startswith('!쟁탈추첨'):
        food = "리장 타워/일리오스/오아시스/부산/네팔"
        foodchoice = food.split("/")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!배그맵추첨'):
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

    if message.content.startswith('!사진'):
        img = message.content.split(" ")
        imgsrc = Image.get_image(img[1])
        await client.send_message(message.channel, imgsrc)

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

    if message.content.startswith('!역할설정'):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(client.get_all_members(), id=rolename[1])
        for i in message.server.roles:
            if i.name == rolename[2]:
                role = i
                break
        await client.add_roles(member, role)



client.run('NTUyNzEwNjg3NTEyNTkyMzg2.D2DfqA.NyaRH7sNuQIkF5aLBOViVcrLbgI')
