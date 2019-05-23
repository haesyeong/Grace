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
    await client.change_presence(activity=discord.Game(name='>>', type=1))


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    print('{} / {}: {}'.format(channel, author, content))

    if message.content == '>>33':
        if message.channel.id == "510732183099670529":
            if message.author.roles[1].name == "외부인":
                await channel.send("dd 씀")
            else:
                await channel.send("넌 못 씀")

    if message.content == ">>이수영":
        embed = discord.Embed(title="유튜브 바로가기",
                              url="https://www.youtube.com/channel/UCIjIggOWB1mogLXcGIsRt-g",
                              description="하와와... 와타시엿던것이에요... 엣큥☆:eye: :tongue: :eye:",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/528180606165712906/567377736247541761/Elmo-elmo-21675732-500-333.png")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/556750351940714527/556826617595297822/KakaoTalk_20190309_001111270.png")
        embed.set_author(name='이수영#3438',
                         icon_url="https://cdn.discordapp.com/attachments/556750351940714527/556826617595297822/KakaoTalk_20190309_001111270.png")
        embed.add_field(name='직책', value=':pen_ballpoint: 클랜마스터', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제3,4,15,16,17회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>히주공주":
        embed = discord.Embed(title="유튜브 바로가기",
                              url="https://www.youtube.com/channel/UCop9jfFqHTDYSGfCZnXgHcw",
                              description="﻿안녕하세요 그레이스 공주님 히주공주입니다",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/474961920223346699/567374986939990043/2.png")
        embed.set_author(name='히주공주#3872')
        embed.add_field(name='직책', value=':construction_worker: 인사 운영진', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제3회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>디셈버":
        embed = discord.Embed(title="트위치 바로가기",
                              url="https://www.twitch.tv/jihee93",
                              description="셈버지",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867483638956034/a48d378f3ad741c7.png")
        embed.set_author(name='December15#31998')
        embed.add_field(name='직책', value=':construction_worker: 디자인 운영진', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제23,24회 우승', inline=True)
        embed.add_field(name='Grace League', value=':second_place: 제1회 준우승', inline=False)
        await channel.send(embed=embed)

    if message.content == ">>파덕":
        embed = discord.Embed(title="한줄소개",
                              description="﻿뀨뀨?",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/557208877264011294/paduck.png")
        embed.set_author(name='PADUCK#31473')
        embed.add_field(name='직책', value=':construction_worker: 인사 운영진', inline=True)
        await channel.send(embed=embed)
        
    if message.content == ">>싸콜":
        embed = discord.Embed(title="한줄소개",
                              description="빌리 팬입니다",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/528180606165712906/567376011759583250/wp2382523-billie-eilish-wallpapers.jpg")
        embed.set_author(name='psycholila#3461')
        embed.add_field(name='직책', value=':construction_worker: 내전/스크림 운영진', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제18,23,26,29회 우승', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제1회 우승', inline=False)
        await channel.send(embed=embed)
        
    if message.content == ">>김청하":
        embed = discord.Embed(title="한줄소개",
                              description="관종",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/534809208642732040/556866375273152537/1d971ab6518df40c.png")
        embed.set_author(name='김청하#31888')
        embed.add_field(name='직책', value=':construction_worker: 내전/스크림 운영진', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제17,19,20,27,29회 우승', inline=True)
        await channel.send(embed=embed)
        
    if message.content == ">>화이트피피":
        embed = discord.Embed(title="한줄소개",
                              description="피피",
                              color=0x5c0bb7)
        embed.set_author(name='Whitepp#3802')
        embed.add_field(name='직책', value=':construction_worker: 개발 운영진', inline=True)
        await channel.send(embed=embed)
        
    if message.content == ">>논":
        embed = discord.Embed(title="한줄소개",
                              description="뭐라고 부르실지 모르시겠다면, None(논)이라고 불러주시면 됩니다 :smile:",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/457565770784833546/566586131735379998/unknown.png")
        embed.set_author(name='nonenone#3447')
        embed.add_field(name='직책', value=':construction_worker: 개발 운영진', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>사먹배":
        embed = discord.Embed(title="한줄소개",
                              description="﻿:apple: :yum: :weary:",
                              color=0x5c0bb7)
        embed.set_author(name='사과먹고배탈#3128')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>동키":
        embed = discord.Embed(title="유튜브 바로가기",
                              url="https://www.youtube.com/channel/UC68bIFKAv8v3YnwQRUDmkSA",
                              description="당숭이 입니다 우끼끼!",
                              color=0x5c0bb7)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/494464806791938068/556866615082221589/JPEG_20190201_062411.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867111016988687/925e1d10811c9f3a.png")
        embed.set_author(name='DONGKEY#31309')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제19,22,25회 우승', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제1회 우승(매니저)', inline=False)
        await channel.send(embed=embed)

    if message.content == ">>또라에몽":
        embed = discord.Embed(title="한줄소개",
                              description="또라또라",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/505406881544667160/556867639046176788/3.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556877298721095691/8fe2252165136934.png")
        embed.set_author(name='또라에몽#31590')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제28회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>워누":
        embed = discord.Embed(title="한줄소개",
                              description="﻿워누갓 그 자체",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867185742577694/bb42302ca8f12479.png")
        embed.set_author(name='WorNoo#1545')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제20,21,25회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>청프로그":
        embed = discord.Embed(title="한줄소개",
                              description="﻿﻿:frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867205447417876/549af7a072af24d5.png")
        embed.set_author(name='청프로그#3376')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제20회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>유로노예":
        embed = discord.Embed(title="한줄소개",
                              description="때려주세요제발..저도한대치게",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/498636211225755649/556993435207204865/image0.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556867276612042752/e696a71eb4aa5116.png")
        embed.set_author(name='유로노예#3271')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>카장":
        embed = discord.Embed(title="한줄소개",
                              description="﻿둠피 장인",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556878683852505088/cajang.png")
        embed.set_author(name='CaJang#3497')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제13,20,25회 우승', inline=True)
        embed.add_field(name='Grace League', value=':second_place: 제1회 준우승', inline=False)
        await channel.send(embed=embed)

    if message.content == ">>정자팔이소년":
        embed = discord.Embed(title="한줄소개",
                              description="﻿﻿10시 이후 게임",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/540560340350402581/576058723525591040/1557410743615.jpg")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556879622919421972/a76ec7c1fd38a3c3.png")
        embed.set_author(name='정자팔이소년#3958')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제29회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>민수":
        embed = discord.Embed(title="한줄소개",
                              description="﻿﻿.",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/556881483164286995/b81eb078e97f800c.png")
        embed.set_author(name='민수#32816')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>자동제어시스템":
        embed = discord.Embed(title="한줄소개",
                              description=".",
                              color=0x5c0bb7)
        embed.set_author(name='자동제어시스템#3755')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace League', value=':first_place: 제1회 우승', inline=False)
        await channel.send(embed=embed)

    if message.content == ">>쿠로":
        embed = discord.Embed(title="한줄소개",
                              description="﻿백수짱",
                              color=0x5c0bb7)
        embed.set_author(name='Kulo#31693')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제23,24,26회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>신비":
        embed = discord.Embed(title="한줄소개",
                              description="﻿여러분들의 남녀친구, 신비입니다♡",
                              color=0x5c0bb7)
        embed.set_author(name='신비#31735')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제3,11회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>연필":
        embed = discord.Embed(title="한줄소개",
                              description="﻿:pencil2:",
                              color=0x5c0bb7)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/494458119707951114/570256628298022923/21313.png")
        embed.set_author(name='연필#31408')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제20,23,27회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>아코":
        embed = discord.Embed(title="한줄소개",
                              description="﻿뀨?",
                              color=0x5c0bb7)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/534809208642732040/557208883374981122/riako.png")
        embed.set_author(name='AKO#31389')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>로즈라떼":
        embed = discord.Embed(title="한줄소개",
                              description=":smile:",
                              color=0x5c0bb7)
        embed.set_author(name='로즈라떼#31235')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제19회 우승', inline=True)
        await channel.send(embed=embed)

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
        await channel.send(embed=embed)

    if message.content == ">>체인스":
        embed = discord.Embed(title="한줄소개",
                              description="﻿No pain No gain",
                              color=0x5c0bb7)
        embed.set_author(name='CHAINS#21427')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제21,24,25,26,28회 우승', inline=True)
        await channel.send(embed=embed)
        
    if message.content == ">>햇콩":
        embed = discord.Embed(title="트위치 바로가기",
                              url="https://twitch.tv/haetkong",
                              description="﻿:sparkles: 슈퍼 뽀짝 탱커 유저 :sparkles:",
                              color=0x5c0bb7)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/558191378467651594/564500095765184522/asdsasd.png")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/558191378467651594/560111949069811713/1.png")
        embed.set_author(name='햇콩#31539')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>룸나인":
        embed = discord.Embed(title="한줄소개",
                              description="﻿한줄 소개 할게없내요",
                              color=0x5c0bb7)
        embed.set_author(name='room9philps#3151')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>능인스멜":
        embed = discord.Embed(title="한줄소개",
                              description="탱커유저",
                              color=0x5c0bb7)
        embed.set_author(name='능인스멜#3202')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제29회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>페이트":
        embed = discord.Embed(title="한줄소개",
                              description="안녕하세요 옵치닉은 fate지만 레랜이라고 불러주세요!",
                              color=0x5c0bb7)
        embed.set_author(name='fate#12983')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>행복":
        embed = discord.Embed(title="한줄소개",
                              description="행복해지고 싶은 그레이스 행복 입니다",
                              color=0x5c0bb7)
        embed.set_author(name='행복#32146')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제25,26,27,28회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>올리브":
        embed = discord.Embed(title="한줄소개",
                              description="학수학수",
                              color=0x5c0bb7)
        embed.set_author(name='olive#31397')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제24,28회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>악마":
        embed = discord.Embed(title="한줄소개",
                              description="안녕하세요 그레이스 악마입니다",
                              color=0x5c0bb7)
        embed.set_author(name='악마#34650')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제26,28회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>두부":
        embed = discord.Embed(title="한줄소개",
                              description="안녕하세요 그레이스 두부입니다",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/457565770784833546/563906500314005505/831024038bc673c2.png")
        embed.set_author(name='DUBU#21590')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>뒤통수갈기기":
        embed = discord.Embed(title="한줄소개",
                              description="뒤통수 조심해",
                              color=0x5c0bb7)
        embed.set_author(name='뒤통수갈기기#3910')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제26,27,29회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>유로":
        embed = discord.Embed(title="한줄소개",
                              description="유노해",
                              color=0x5c0bb7)
        embed.set_author(name='유로#31358')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>꽃이피면너에게":
        embed = discord.Embed(title="한줄소개",
                              description="그레이스 최고 꽃미녀",
                              color=0x5c0bb7)
        embed.set_image(url="https://cdn.discordapp.com/attachments/457565770784833546/570978414765408286/unknown.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/562967466813423616/571754411852955649/image0.jpg")
        embed.set_author(name='꽃이피면너에게#3470')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제27,29회 우승', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>메르시":
        embed = discord.Embed(title="한줄소개",
                              description="오늘 당직은 메르시 입니다",
                              color=0x5c0bb7)
        embed.set_author(name='메르시#31643')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>힙노틱":
        embed = discord.Embed(title="한줄소개",
                              description="힙노힙노",
                              color=0x5c0bb7)
        embed.set_author(name='Hypnotic#31217')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        embed.add_field(name='Grace Arena', value=':trophy: 제28회 우승', inline=True)
        await channel.send(embed=embed)
        
    if message.content == ">>진땅이":
        embed = discord.Embed(title="한줄소개",
                              description="또라에몽 담당 일찐",
                              color=0x5c0bb7)
        embed.set_author(name='진땅이#3539')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == ">>김동률":
        embed = discord.Embed(title="한줄소개",
                              description="위도우는 진땅보다 필수",
                              color=0x5c0bb7)
        embed.set_author(name='김동률#31585')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)
        
    if message.content == ">>사노":
        embed = discord.Embed(title="한줄소개",
                              description="안녕하세요",
                              color=0x5c0bb7)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/580798796993396736/581079802551730177/55390147_p0.png")
        embed.set_author(name='sano#31836')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)
        
    if message.content == ">>이븐폴":
        embed = discord.Embed(title="소개영상",
                              url="https://youtu.be/2ibftiGpots",
                              description="즐거워.. 짜릿해..",
                              color=0x5c0bb7)
        embed.set_author(name='Evenfall#31117')
        embed.add_field(name='직책', value=':boy: 클랜원', inline=True)
        await channel.send(embed=embed)

    if message.content == '!안녕':
        await channel.send("안녕하세요")

    if message.content == '>>리그':
        await channel.send("https://www.twitch.tv/overwatchleague_kr")

    if message.content.startswith('>>골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice) - 1)
        choiceresult = choice[choicenumber]
        await channel.send("||" + choiceresult + "||")

    if message.content.startswith('>>쟁탈추첨'):
        food = "리장 타워/일리오스/오아시스/부산/네팔"
        foodchoice = food.split("/")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await channel.send(foodresult)

    if message.content.startswith('>>배그맵추첨'):
        pubg = "에란겔/미라마/사녹/비켄디"
        pubgchoice = pubg.split("/")
        pubgnumber = random.randint(1, len(pubgchoice))
        pubgresult = pubgchoice[pubgnumber - 1]
        await channel.send(pubgresult)

    if message.content.startswith('!메모장쓰기'):
        file = open("디스코드봇메모장.txt", "w")
        file.write("안녕하세요")
        file.close()

    if message.content.startswith('!메모장읽기'):
        file = open("디스코드봇메모장.txt")
        await channel.send(file.read())
        file.close()

    if message.content.startswith('!학습'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        learn = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == "-" or sheet["A" + str(i)].value == learn[1]:
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                await channel.send("단어가 학습되었습니다.")
                break
        file.save("기억.xlsx")

    if message.content.startswith('!기억') and not message.content.startswith('!기억삭제'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == memory[1]:
                await channel.send(sheet["B" + str(i)].value)
                break

    if message.content.startswith('!기억삭제'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == str(memory[1]):
                sheet["A" + str(i)].value = "-"
                sheet["B" + str(i)].value = "-"
                await channel.send("기억이 삭제되었습니다.")
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
            await channel.send(person[i] + "---->" + teamname[i])


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    delchannel = message.guild.get_channel(527859699702562828)
    await delchannel.send('{} / {}: {}'.format(channel, author, content))

@client.event
async def on_member_join(member):
    fmt = '<@332564579148103691>\n{0.mention}님이 {1.name}에 입장하였습니다.'
    channel = member.guild.get_channel(516122942896078868)
    await channel.send(fmt.format(member, member.guild))
    role = discord.utils.get(member.guild.roles, name='외부인')
    await client.add_roles(member, role)

@client.event
async def on_member_remove(member):
    channel = member.guild.get_channel(516122942896078868)
    fmt = '{0.mention}\n{0.nick}님이 서버에서 나가셨습니다.'
    await channel.send(fmt.format(member, member.guild))


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
