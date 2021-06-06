import discord
import asyncio
import json
import gspread
import datetime
from bisect import bisect
from oauth2client.service_account import ServiceAccountCredentials

intents = discord.Intents().all()
client = discord.Client(intents=intents)

channels={
    '렙업알림':850685514041917440,
    '봇실험실':486550288686120961,
}

roles={
    '신입':457568290370486292,
    '클랜원':359739346485772289,
}

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
url='https://docs.google.com/spreadsheets/d/1gfSsgM_0BVqnZ02ZwRsDniU-qkRF0Wo-B7rJhYoYXqc/edit?usp=drive_web&ouid=108946956826520256706'

current_time=lambda:datetime.datetime.utcnow()+datetime.timedelta(hours=9)

#시트 관리
indices = ['mention', 'command', 'overwatch', 'valorant', 'link', 'description', 'image', 'thumbnail', 'arena', 'arena_lost', 'league_first', 'league_second', 'friends', 'supporters', 'joined', 'exp', 'checkin', 'exp_get', 'awards']
indicates = ['멘션','커맨드','오버워치','발로란트','바로가기','한줄소개','이미지 링크','썸네일 링크','아레나','아레나 패배','리그 우승','리그 준우승','우친바','서포터즈','최초 가입일','경험치', '출석', '경험치받기', '어워즈']
indicate_to_indice=dict(zip(indicates, indices))

#레벨 관리
level_to_exp=[0,200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3400,3800,4200,4600,5000,5400,5800,6200,6600,7000,7800,8600,9400,10200,11000,11800,12600,13400,14200,15000,16600,18200,19800,21400,23000,24600,26200,27800,29400,31000,34200,37400,40600,43800,47000,50200,53400,56600,59800,63000,69400,75800,82200,88600,95000,101400,107800,114200,120600,127000]
level=lambda exp: bisect(level_to_exp, exp)

def get_worksheet(ws_name):
    creds=ServiceAccountCredentials.from_json_keyfile_name("Grace-defe42f05ec3.json", scope)
    auth=gspread.authorize(creds)

    if creds.access_token_expired:
        auth.login()
    
    try:
        worksheet=auth.open_by_url(url).worksheet(ws_name)
    except gspread.exceptions.APIError:
        return
    return worksheet

def get_col_order(ws):
    cols=ws.row_values(1)
    vals=[]
    for i in cols:
        vals.append(indicate_to_indice[i])
    return vals

def search(ws, key, val, *, cols=None):
    if key not in ['mention', 'command', 'overwatch']:
        raise Exception
    if cols==None:
        cols=get_col_order(ws)
    col_idx=cols.index(key)+1
    rows=ws.col_values(col_idx)
    try:
        return rows.index(val)+1
    except:
        raise Exception

def get_row(ws, idx, *, cols=None):
    if cols==None:
        cols=get_col_order(ws)
    vals = ws.row_values(idx)

    while len(vals)<len(cols):
            vals.append('')

    data = {}
    for col, val in zip(cols, vals):
        data[col]=val

    return data

def fetch(ws, key, val, *, cols=None):
    if cols==None:
        cols=get_col_order(ws)
    idx=search(ws, key, val, cols=cols)
    return get_row(ws, idx, cols=cols)

async def give_exp(ws, exp, client, *, key=None, val=None, row_idx=None, cols=None, update_date=False, add_giver=False, arena_record=False, arena_result=None):
    if cols==None:
        cols=get_col_order(ws)
    if row_idx==None:
        row_idx=search(ws, key, val, cols=cols)
    row=get_row(ws, row_idx, cols=cols)
    col_idx=cols.index('exp')+1
    old_exp=int(row['exp'])
    new_exp=old_exp+exp
    ws.update_cell(row_idx, col_idx, new_exp)
    if update_date:
        col_idx=cols.index('checkin')+1
        ws.update_cell(row_idx, col_idx, current_time().strftime("%Y%m%d"))
    if add_giver:
        col_idx=cols.index('exp_get')+1
        ws.update_cell(row_idx, col_idx, add_giver)
    if arena_record:
        if arena_result:
            col_idx=cols.index('arena')+1
            row_content=row['arena']
        else:
            col_idx=cols.index('arena_lost')+1
            row_content=row['arena_lost']
        ws.update_cell(row_idx, col_idx, row_content+(',' if row_content else '')+f'{arena_record}')
    old_level=level(old_exp)
    new_level=level(new_exp)
    if old_level!=new_level:
        return await levelup(client, row, new_level)

async def levelup(client, row, new_level):
    try:
        await client.wait_until_ready()
        grace=client.get_guild(359714850865414144)
        sendstr='{}님이 레벨 {}로 레벨업하셨습니다!'.format(row['mention'], new_level)
        if new_level==10:
            newbie=grace.get_role(roles['신입'])
            clan=grace.get_role(roles['클랜원'])
            member=grace.get_member(int(row['mention'][3:-1]))
            await member.add_roles(clan, atomic=True)
            await member.remove_roles(newbie, atomic=True)
            sendstr+='\n정식 클랜원이 되신 것을 축하드립니다!'
        notice=grace.get_channel(channels['봇실험실'])#'렙업알림'
        await notice.send(sendstr)
        return True
    except Exception as e:
        print(e)
        return False

if __name__=='__main__':
    #ws=get_worksheet('responses')
    #give_exp(ws, 100, key='overwatch', val='nonenone#3447')
    print(level(200))
