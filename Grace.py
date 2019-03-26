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

    if message.content == ">>ddd":
        if message.author.id == "294813518191132672":
            embed = discord.Embed(title="이수영",
                                  url="https://www.youtube.com/channel/UCop9jfFqHTDYSGfCZnXgHcw",
                                  description="하와와... 와타시엿던것이에요... 엣큥☆:eye: :tongue: :eye:\n\n-:pen_ballpoint: 클랜 마스터\n-:trophy: 제 3,17회 Grace Arena 우승팀장:crown:\n-:trophy: 제 4,15,16회 Grace Arena 우승자",
                                  color=0x5c0bb7)
            embed.set_image(url="http://t1.daumcdn.net/cafeattach/mEr9/c8cf5e24bf2ff7a8d14ce6ceda4d92d8e64d49cd")
            embed.set_thumbnail(url="https://i.imgur.com/3mQ8rgC.jpg")
            embed.add_field(name='가입일', value="ㅇ", inline=True)
            await client.send_message(channel, embed=embed)
        else:
            await client.send_message(message.channel, "넌 못 씀")

    if message.content == ">>이수영":
        embed = discord.Embed(title="유튜브 바로가기",
                              url="https://www.youtube.com/channel/UCIjIggOWB1mogLXcGIsRt-g",
                              description="하와와... 와타시엿던것이에요... 엣큥☆:eye: :tongue: :eye:",
                              color=0x5c0bb7)
        embed.set_image(url="https://i.imgur.com/3mQ8rgC.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/556750351940714527/556826617595297822/KakaoTalk_20190309_001111270.png")
        embed.set_author(name='이수영#3438',
                         icon_url="https://cdn.discordapp.com/attachments/556750351940714527/556826617595297822/KakaoTalk_20190309_001111270.png")
        embed.add_field(name='직책', value=':pen_ballpoint: 클랜마스터', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 3,4,15,16,17회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>동키":
        embed = discord.Embed(title="유튜브 바로가기",
                              url="https://www.youtube.com/channel/UC68bIFKAv8v3YnwQRUDmkSA",
                              description="당숭이 입니다 우끼끼!",
                              color=0x5c0bb7)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/494464806791938068/556866615082221589/JPEG_20190201_062411.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867111016988687/925e1d10811c9f3a.png")
        embed.set_author(name='DONGKEY#31823')
        embed.add_field(name='직책', value=':construction_worker: 내전/스크림 운영진', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 19,22회 우승', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제 1회 우승(매니저)', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>히주공주":
        embed = discord.Embed(title="유튜브 바로가기",
                              url="https://www.youtube.com/channel/UCop9jfFqHTDYSGfCZnXgHcw",
                              description="﻿안녕하세요 그레이스 공주님 히주공주입니다",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/556750351940714527/556806153552789504/b0f5aaba39555b1d.png")
        embed.set_author(name='히주공주#3872')
        embed.add_field(name='직책', value=':construction_worker: 인사 운영진', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 3회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>디셈버":
        embed = discord.Embed(title="트위치 바로가기",
                              url="https://www.twitch.tv/jihee93",
                              description="셈버지",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867483638956034/a48d378f3ad741c7.png")
        embed.set_author(name='December15#31998')
        embed.add_field(name='직책', value=':construction_worker: 디자인 운영진', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 23회 우승', inline=True)
        embed.add_field(name='Grace League', value=':second_place: 제 1회 준우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>사먹배":
        embed = discord.Embed(title="한줄소개",
                              description="﻿:apple: :yum: :weary:",
                              color=0x5c0bb7)
        embed.set_author(name='사과먹고배탈#3128')
        embed.add_field(name='직책', value=':construction_worker: 내전/스크림 운영진', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>암고":
        embed = discord.Embed(title="한줄소개",
                              description="﻿절.대.트.레.해",
                              color=0x5c0bb7)
        embed.set_author(name='AMGOTOMOTAJO#3147')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 18회 우승', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제 1회 우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>또라에몽":
        embed = discord.Embed(title="한줄소개",
                              description="또라또라",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/505406881544667160/556867639046176788/3.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556877298721095691/8fe2252165136934.png")
        embed.set_author(name='또라에몽#31590')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>새벽사슴밤":
        embed = discord.Embed(title="유튜브 바로가기",
                              url="https://www.youtube.com/channel/UCy3Ru3UkYjxYAdGNRfYme-Q",
                              description="메인탱안해요",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556866355874496533/8d5b5ea5c2859aae.png")
        embed.set_author(name='새벽사슴밤#3679')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 18회 우승', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제 1회 우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>헤닉스":
        embed = discord.Embed(title="한줄소개",
                              description="맥크리 외길인생임",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556880149417820170/henix.png")
        embed.set_author(name='Henix#11959')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 2회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>워누다스":
        embed = discord.Embed(title="한줄소개",
                              description="﻿워누갓 그 자체",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867185742577694/bb42302ca8f12479.png")
        embed.set_author(name='워누다스#3583')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 20,21회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>청프로그":
        embed = discord.Embed(title="한줄소개",
                              description="﻿﻿류제홍빠",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867205447417876/549af7a072af24d5.png")
        embed.set_author(name='청프로그#3376')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 20회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>해마":
        embed = discord.Embed(title="한줄소개",
                              description="때려주세요제발..저도한대치게",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/498636211225755649/556993435207204865/image0.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867276612042752/e696a71eb4aa5116.png")
        embed.set_author(name='해마#31749')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>메이커":
        embed = discord.Embed(title="한줄소개",
                              description="﻿﻿잘부탁드립니다.",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867338742267917/maker.png")
        embed.set_author(name='Maker#31383')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace League', value=':second_place: 제 1회 준우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>카장":
        embed = discord.Embed(title="한줄소개",
                              description="﻿둠피 장인",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556878683852505088/cajang.png")
        embed.set_author(name='CaJang#3497')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 13,20회 우승', inline=True)
        embed.add_field(name='Grace League', value=':second_place: 제 1회 준우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>정자팔이소년":
        embed = discord.Embed(title="한줄소개",
                              description="﻿﻿10시 이후 게임",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556879622919421972/a76ec7c1fd38a3c3.png")
        embed.set_author(name='정자팔이소년#3958')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>민수":
        embed = discord.Embed(title="한줄소개",
                              description="﻿﻿.",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556881483164286995/b81eb078e97f800c.png")
        embed.set_author(name='민수#32816')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>싸콜":
        embed = discord.Embed(title="한줄소개",
                              description="놀아줄사람구함",
                              color=0x5c0bb7)
        embed.set_author(name='psycholila#3461')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 18,23회 우승', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제 1회 우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>자동제어시스템":
        embed = discord.Embed(title="한줄소개",
                              description=".",
                              color=0x5c0bb7)
        embed.set_author(name='자동제어시스템#3755')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제 1회 우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>루나":
        embed = discord.Embed(title="한줄소개",
                              description=".",
                              color=0x5c0bb7)
        embed.set_author(name='Luna#14668')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제 1회 우승', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content == ">>적셔":
        embed = discord.Embed(title="한줄소개",
                              description="헤헤",
                              color=0x5c0bb7)
        embed.set_author(name='적셔#31146')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 23회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>쿠로":
        embed = discord.Embed(title="한줄소개",
                              description="﻿158 ㅎㅇ",
                              color=0x5c0bb7)
        embed.set_author(name='Kulo#31693')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 23회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>신비":
        embed = discord.Embed(title="한줄소개",
                              description="﻿여러분들의 남녀친구, 신비입니다♡",
                              color=0x5c0bb7)
        embed.set_author(name='신비#31735')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 3,11회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>연필":
        embed = discord.Embed(title="한줄소개",
                              description="﻿:pencil2:",
                              color=0x5c0bb7)
        embed.set_author(name='연필#31408')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 20,23회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>리아코":
        embed = discord.Embed(title="한줄소개",
                              description="﻿뀨?",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/557208883374981122/riako.png")
        embed.set_author(name='Riako#31412')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>파덕":
        embed = discord.Embed(title="한줄소개",
                              description="﻿뀨뀨?",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/557208877264011294/paduck.png")
        embed.set_author(name='PADUCK#31473')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>옷파":
        embed = discord.Embed(title="한줄소개",
                              description="﻿:shirt: :jeans:",
                              color=0x5c0bb7)
        embed.set_author(name='옷파랑색사고싶어#3306')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 23회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>로즈라떼":
        embed = discord.Embed(title="한줄소개",
                              description=":smile:",
                              color=0x5c0bb7)
        embed.set_author(name='로즈라떼#31235')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 19회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>최성규":
        embed = discord.Embed(title="한줄소개",
                              description="같이 오-락 하실분 말걸어주세요",
                              color=0x5c0bb7)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/435618100327481345/558749388747571211/85b7294b373fa8845fc157fe10467ef2b0e745e5.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/558750740454047762/759d2122b0e684a8.png")
        embed.set_author(name='최성규#3160')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>체인스":
        embed = discord.Embed(title="한줄소개",
                              description="﻿No pain No gain",
                              color=0x5c0bb7)
        embed.set_author(name='CHAINS#21427')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제 21회 우승', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>미라클":
        embed = discord.Embed(title="한줄소개",
                              description="﻿게임은 잘 못하지만 즐기면서 하겠습니다",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/457565770784833546/559020987954495488/unknown.png")
        embed.set_author(name='MIRACLE#31776')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

    if message.content == ">>메이즈":
        embed = discord.Embed(title="한줄소개",
                              description="﻿안녕하세요 메이장인 메이즈입니다",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/457565770784833546/559054608459366400/unknown.png")
        embed.set_author(name='M4ZE#3992')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)
        
    if message.content == ">>햇콩":
        embed = discord.Embed(title="트위치 바로가기",
                              url="https://twitch.tv/haetkong",
                              description="﻿:sparkles: 슈퍼 뽀짝 탱커 유저 :sparkles:",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/558191378467651594/560111949069811713/1.png")
        embed.set_author(name='햇콩#31539')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await client.send_message(channel, embed=embed)

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
    fmt = '{0.mention}님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))


client.run('NTUyNzEwNjg3NTEyNTkyMzg2.D2DfqA.NyaRH7sNuQIkF5aLBOViVcrLbgI')
