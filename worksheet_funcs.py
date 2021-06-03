import asyncio
import json
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

current_time=lambda:datetime.datetime.utcnow()+datetime.timedelta(hours=9)

url='https://docs.google.com/spreadsheets/d/1gfSsgM_0BVqnZ02ZwRsDniU-qkRF0Wo-B7rJhYoYXqc/edit?usp=drive_web&ouid=108946956826520256706'

indices = ['mention', 'command', 'overwatch', 'valorant', 'link', 'description', 'image', 'thumbnail', 'arena', 'arena_lost', 'league_first', 'league_second', 'friends', 'supporters', 'joined', 'exp', 'checkin', 'exp_get']
indicates = ['멘션','커맨드','오버워치','발로란트','바로가기','한줄소개','이미지 링크','썸네일 링크','아레나','아레나 패배','리그 우승','리그 준우승','우친바','서포터즈','최초 가입일','경험치', '출석', '경험치받기']

indicate_to_indice=dict(zip(indicates, indices))

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

def fetch(ws_name, key, val, *, cols=None):
    ws=get_worksheet(ws_name)
    if cols==None:
        cols=get_col_order(ws)
    idx=search(ws, key, val)
    return get_row(ws, idx, cols=cols)

def give_exp(ws_name, exp, *, key, val, row_idx=None, cols=None, update_date=False):
    ws=get_worksheet(ws_name)
    if cols==None:
        cols=get_col_order(ws)
    if row_idx==None:
        row_idx=search(ws, key, val, cols=cols)
    row=get_row(ws, row_idx, cols=cols)
    col_idx=cols.index('exp')+1
    new_exp=int(row['exp'])+exp
    ws.update_cell(row_idx, col_idx, new_exp)
    if update_date:
        col_idx=cols.index('checkin')+1
        ws.update_cell(row_idx, col_idx, current_time().strftime("%Y%m%d"))
    return True


if __name__=='__main__':
    give_exp('res_bak_210527', 100, key='mention', val='<@!320235433181315073>', update_date=True)