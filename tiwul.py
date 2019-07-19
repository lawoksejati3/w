# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
#import pyimgflip
from googletrans import Translator
import youtube_dl

#CREATOR BY sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ  

botStart = time.time()
mulai = time.time()
#tokenOpen = codecs.open("boyfira.json","r","utf-8")
#token = json.load(tokenOpen)

print  ("Welcome login self")  
boy = LineClient()
#boy = LineClient(authToken="EH8WAd3vvRgV9od8aoZ8./evnxlhBFZc5xEvz0BGnsa.290dPIpEUUKYQfMRA7vXNXBKtZNAuhCgDtwNJ/YueHQ=")
channel = LineChannel(boy,boy.server.CHANNEL_ID['LINE_TIMELINE'])
boy.log("Auth Token : " + str(boy.authToken))

print ("sᴇʟғʙᴏᴛ ʙʏ : ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ")

#ubah mid di dalem admin,owner,creator.json dengan mid kalian
poll = LinePoll(boy)
call = boy
creator = ["u059095aa0cc2f6ef02d8ae72c3430163"]
owner = ["uf8454d5cb1db7f30b95de559d1b80d48"]
admin = ["uf8454d5cb1db7f30b95de559d1b80d48"]
staff = ["udb300701d1c35494134ced718a21e9b8"]
mid = boy.getProfile().mid
KAC = [boy]
ABC = [boy]
Bots = [mid]
Boy = admin + staff + creator

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

boyProfile = boy.getProfile()
myProfile["displayName"] = boyProfile.displayName
myProfile["statusMessage"] = boyProfile.statusMessage
myProfile["pictureStatus"] = boyProfile.pictureStatus

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.01)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        backupData()
        time.sleep(0,1)
        restartBot()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "ᴛᴏᴛᴀʟ ᴘᴇɴɢʜᴜɴɪ ʀᴜᴍᴀʜ「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "═══════════════════════                      ≈ᴀᴜᴛᴏ ᴄʏᴅᴜᴋ≈                   ═══════════════════════         ╠❂͜͡☬➣ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "╔═══════════════════════╗ ╠❂͜͡☬➣       WELCOME            ║ ╚═══════════════════════╝ ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ sᴇʟᴀᴍᴀᴛ ʙᴇʀɢᴀʙᴜɴɢ ᴅᴀʟᴀᴍ ᴋᴇʟᴜᴀʀɢᴀ ᴋᴀᴍɪ...(-‿◦) ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ sᴀʟᴀᴍ ᴋᴇɴᴀʟ ᴅᴀɴ sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ʙᴇʀsᴀᴍᴀ ᴋᴀᴍɪ....(*^ω^*) ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ ᴅᴀɴ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴜɴᴛᴜᴋ ᴄᴇᴋ ɴᴏᴛᴇ ᴜɴᴛᴜᴋ ɪɴғᴏ ᴛᴇʀʙᴀʀᴜ ᴛᴇɴᴛᴀɴɢ ɢʀᴏᴜᴘ ᴋɪᴛᴀ ɪɴɪ...(^_^)ノ ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ ╔═══════════════════════╗ ╠❂͜͡☬➣              ɴᴀʜ ɢᴀɴ ɪɴɪ ᴅɪᴀ               ║ ╠❂͜͡☬➣          ғᴏᴛᴏ ᴄᴀᴋᴇᴘɴʏᴀ         ║ ╠❂͜͡☬➣        ʏᴀɴɢ ʙᴀʀᴜ ɴʏᴜɴɢsᴇᴘ        ║ ╚═══════════════════════╝ ╠❂͜͡☬➣ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boy.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\n๔ī งг๏มр "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        boy.sendMessage(op.param1, None, contentMetadata={"STKID":"12842273","STKPKGID":"1318245","STKVER":"1"}, contentType=7)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "╔═══════════════════════╗ ╠❂͜͡☬➣    SELAMAT JALAN SOBAT'      ║ ╚═══════════════════════╝ ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ รєใค๓คҭ  вєг♩มคกง ใมคг รคกค ๔ī ҭє๓рคҭ ұคกง вคгม ๔คก ใєвīђ ҭєกคกง...(-‿◦) ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ вұє вұє รคม๔คгคкม รєใค๓คҭ ♩คใคก....(*^ω^*) ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ รє๓๏งค кīҭค вєгҭє๓ม кє๓вคใī ๔ī ใมคг รคกค กคกҭī...(^_^)ノ ╔═══════════════════════╗ ║  ☫☫☫☫☫☫☫εïзεïзεïз❁❁❁❁❁❁❁  ║ ╚═══════════════════════╝ ╔═══════════════════════╗ ╠❂͜͡☬➣              กคђ īกī ๔īค กīђ               ║ ╠❂͜͡☬➣          ғ๏ҭ๏ кєใมคгงค кīҭค          ║ ╠❂͜͡☬➣         ұคกง вคгม รค♩ค рєгงī        ║ ╚═══════════════════════╝ ╠❂͜͡☬➣ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boy.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nᴅᴀʀɪ ɢʀᴏᴜᴘ "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(boy.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        boy.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        boy.sendMessage(op.param1, None, contentMetadata={"STKID":"12690685","STKPKGID":"1314362","STKVER":"1"}, contentType=7)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,10,7)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = boy.getAllContactIds()
        gid = boy.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"❂͜͡☬➣ ⌚ᴊᴀᴍ : "+datetime.strftime(timeNow,'%H:%M:%S')+" ᴡɪʙ\n❂͜͡☬➣ 📕ɢʀᴏᴜᴘ : "+str(len(gid))+"\n❂͜͡☬➣ 🚶ᴛᴇᴍᴀɴ : "+str(len(teman))+"\n❂͜͡☬➣ 📠ᴋᴀᴅᴀʟᴜᴀʀsᴀ : In "+hari+"\n❂͜͡☬➣ 📖ᴠᴇʀsɪ : ᴘʏᴛʜᴏɴ3\n❂͜͡☬➣ 📅ᴛᴀɴɢɢᴀʟ : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n❂͜͡☬➣ 📆ʀᴜɴᴛɪᴍᴇ : \n • "+bot
        boy.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boy.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷  " + "\n" + \
                  "╚═══════════════════════╝" + "\n" + \
                  "╔═══════════════════════╗" + "\n" + \
                  "     📃ᴍᴇɴᴜ📃 " + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Help\n" + \
                  "╠❂͜͡☬➣ " + key + "Help 2\n" + \
                  "╠❂͜͡☬➣ " + key + "Help bot\n" + \
                  "╠❂͜͡☬➣ " + key + "Meme\n" + \
                  "╠❂͜͡☬➣ " + key + "Me\n" + \
                  "╠❂͜͡☬➣ " + key + "Mymid\n" + \
                  "╠❂͜͡☬➣ " + key + "Mid「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Info 「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "K 「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Stat\n" + \
                  "╠❂͜͡☬➣ " + key + "Abo\n" + \
                  "╠❂͜͡☬➣ " + key + "Poin\n" + \
                  "╠❂͜͡☬➣ " + key + "Run\n" + \
                  "╠❂͜͡☬➣ " + key + "Creat\n" + \
                  "╠❂͜͡☬➣ " + key + "Speed/Sp\n" + \
                  "╠❂͜͡☬➣ " + key + "Sr\n" + \
                  "╠❂͜͡☬➣ " + key + "Pa/hai\n" + \
                  "╠❂͜͡☬➣ " + key + "Gin\n" + \
                  "╠❂͜͡☬➣ " + key + "Opn\n" + \
                  "╠❂͜͡☬➣ " + key + "Clo\n" + \
                  "╠❂͜͡☬➣ " + key + "Url\n" + \
                  "╠❂͜͡☬➣ " + key + "Rjt\n" + \
                  "╠❂͜͡☬➣ " + key + "Gl\n" + \
                  "╠❂͜͡☬➣ " + key + "Igp「angka」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ime「angka」\n" + \
                  "╠❂͜͡☬➣ " + key + "Lur「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Lu\n" + \
                  "╠❂͜͡☬➣ " + key + "Sider「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Uf\n" + \
                  "╠❂͜͡☬➣ " + key + "Ugr\n" + \
                  "╠❂͜͡☬➣ " + key + "Bc:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mykey\n" + \
                  "╠❂͜͡☬➣ " + key + "Resetkey\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╔═══════════════════════╗" + "\n" + \
                  "     🎡ʜɪʙᴜʀᴀɴ🎡" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Stag:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Stag「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Scall:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Scall\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage1

def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╔═══════════════════════╗" + "\n" + \
                  "     📝ᴘʀᴏᴛᴇᴄᴛ📝" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Nt「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Tl「ᴏɴ/ᴏғғ」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·sᴇᴛᴛɪɴɢ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Un「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Jointicket「on/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Str「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Res「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Rg「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Contact「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ajo「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autoadd「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Wl「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Simi「ᴏɴ/ᴏғғ」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autoleave「ᴏɴ/ᴏғғ」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·ᴀᴅᴍɪɴ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Fresh\n" + \
                  "╠❂͜͡☬➣ " + key + "Lb\n" + \
                  "╠❂͜͡☬➣ " + key + "La\n" + \
                  "╠❂͜͡☬➣ " + key + "Lp\n" + \
                  "╠❂͜͡☬➣ ᴋᴇᴛɪᴋ「 ғʀᴇsʜ」ᴊɪᴋᴀ sᴜᴅᴀʜ\n╠❂͜͡☬➣ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ᴅɪᴀᴛᴀs\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝" 
    return helpMessage2
    boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
    
  
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╔═══════════════════════╗" + "\n" + \
                  "     📱sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ📱" + "\n" + \
                  "╚═══════════════════════╝" + "\n" + \
                  "╔═══════════════════════╗" + "\n" + \
                  "     🔧·ʙᴏᴛ·🔧" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Mytoken\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek sider\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek spam\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek pesan\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek respon\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek welcome\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek leave\n" + \
                  "╠❂͜͡☬➣ " + key + "Set si:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set spam:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set pesan:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set re:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set wl:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set leave:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mme:「Nama」\n" + \
                  "╠❂͜͡☬➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
				  "╠❂͜͡☬➣ " + key + "Stag:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Stag「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Scall:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Scall\n" + \
				  "╠❂͜͡☬➣ " + key + "Uf\n" + \
                  "╠❂͜͡☬➣ " + key + "Ugr\n" + \
                  "╠❂͜͡☬➣ " + key + "Bc:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mykey\n" + \
                  "╠❂͜͡☬➣ " + key + "Resetkey\n" + \
				  "╠❂͜͡☬➣ " + key + "Self「ᴏɴ/ᴏғғ」\n" + \
				  "╠❂͜͡☬➣ " + key + "Hc\n" + \
				  "╠❂͜͡☬➣ " + key + "Leave:「Namagrup」\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "     ◄]·✪·ʙʟᴀᴄᴋʟɪsᴛ·✪·[►" + "\n" + \
                  "╠═══════════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Blc\n" + \
                  "╠❂͜͡☬➣ " + key + "Ban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Unban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Ban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Unban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Untalkban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Untalkban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Banlist\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkbanlist\n" + \
                  "╠❂͜͡☬➣ " + key + "Cb\n" + \
                  "╠❂͜͡☬➣ " + key + "Fresh\n" + \
                  "╠═══════════════════════╗" + "\n" + \
                  "      📷sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ📷" + "\n" + \
                  "╚═══════════════════════╝"
    return helpMessage3
    boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
    
def infomeme():
    helpMessage4 = """
╔═══════════════════════╗
       👙sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ👙
╚═══════════════════════╝
╔═══════════════════════╗
    ◄]·✪·ʟɪsᴛ ᴍᴇᴍᴇ·✪·[►
╠═══════════════════════╝
╠❂͜͡☬➣ Buzz
╠❂͜͡☬➣ Spongebob
╠❂͜͡☬➣ Patrick
╠❂͜͡☬➣ Doge
╠❂͜͡☬➣ Joker
╠❂͜͡☬➣ Xzibit
╠❂͜͡☬➣ You_tried
╠❂͜͡☬➣ cb
╠❂͜͡☬➣ blb
╠❂͜͡☬➣ wonka
╠❂͜͡☬➣ keanu
╠❂͜͡☬➣ cryingfloor
╠❂͜͡☬➣ disastergirl
╠❂͜͡☬➣ facepalm
╠❂͜͡☬➣ fwp
╠❂͜͡☬➣ grumpycat
╠❂͜͡☬➣ captain
╠❂͜͡☬➣ mmm
╠❂͜͡☬➣ rollsafe
╠❂͜͡☬➣ sad-obama
╠❂͜͡☬➣ sad-clinton
╠❂͜͡☬➣ aag
╠❂͜͡☬➣ sarcasticbear
╠❂͜͡☬➣ sk
╠❂͜͡☬➣ sparta
╠❂͜͡☬➣ sad
╠❂͜͡☬➣ contoh:
╠❂͜͡☬➣ Meme@buzz@lu tau?@gatau
╠═══════════════════════╗
      📷sᴇʟғʙᴏᴛ ʙʏ ᴀʀᴇᴢᴀ📷
╚═══════════════════════╝
"""
    return helpMessage4
    boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait['leaveRoom'] == True:
                boy.leaveRoom(op.param1)   
        if op.type == 24:
            if wait['leaveRoom'] == True:
                boy.leaveRoom(op.param1)        
                
        if op.type == 5:
              if wait["autoAdd"] == True:
                  boy.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "ʜᴀʟʟᴏ ", ", ᴛʜᴀɴᴋs ᴜᴅᴀʜ ᴀᴅᴅ sᴀʏᴀ")
                  boy.sendText(op.param1, wait["message"])
                  boy.sendContact(op.param1,"u059095aa0cc2f6ef02d8ae72c3430163")
                                                
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"sᴇʟᴀᴍᴀᴛᴛɪɴɢɢᴀʟ\n Group " +str(ginfo.name))
                        boy.leaveGroup(op.param1)
                    else:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Hai " + str(ginfo.name))
                        
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boy.acceptGroupInvitation(op.param1)                     
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        boy.acceptGroupInvitation(op.param1)
                        ginfo = boy.getGroup(op.param1)
                        boy.sendMessage(op.param1,"Haii " + str(ginfo.name))

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        boy.sendMessage(op.param1, wait["message"])

#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
#===========Accepet===========#

            if op.param3 in mid:
                if op.param2 in Bots:
                    boy.acceptGroupInvitation(op.param1)

#===========Cancel============#
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "BERHASIL LIKE BY ⊰์◉⊱sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ◉⊱"
                            boy.sendMessage(to, str(ret_))
                            boy.sendMessage(msg.to, None, contentMetadata={"STKID":"17225909","STKPKGID":"1456919","STKVER":"1"}, contentType=7) 
                            channel.like(url[25:58], url[66:], likeType=1001)
                            channel.comment(url[25:58], url[66:], wait["message"])

#___________________________________________________
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = boy.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            boy.sendMessage(msg.to, "「ᴀᴡᴀs ᴋɪᴋɪʟ ʙᴏss... ђคрมร вใ ᴅᴜʟᴜ ʙᴀʀᴜ ɪɴᴠɪᴛᴇ ʟᴀɢɪ ʙᴏss...!!!」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                fira = boy.getContact(target)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Sukses Invite 」\nNama "
                                ret_ = "「Ketik Invite off jika sudah done」"
                                fa = str(fira.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':fira.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                wait["invite"] = False
                                break
                            except:
                                boy.sendText(msg.to,"ʟɪᴍɪᴛ ʙᴏss...!!!")
                                wait["invite"] = False
                                break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            boy.sendText(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                boy.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    boy.sendText(msg.to,"ᴇʀʀᴏʀ")
                                    wait["invite"] = False
                                    break

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["AFreadPoint"]:
                   if op.param2 in Setmain["AFreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["AFreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = boy.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = boy.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        boy.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 UNSEND MESSAGE 」\n❂➣ Pengirim : "
                                ret_ = "❂➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n❂➣ sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ◉⊱"
                                ry = str(Boy.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Boy.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 UNSEND MESSAGE 」\n"
                                ret_ += "❂➣ Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n❂➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n❂➣Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n❂➣ sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ◉⊱"
                                boy.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "❂➣ Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n❂➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n❂➣ sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ◉⊱"
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                boy.sendMessage(at, str(ret_))
                                boy.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               boy.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass
                   
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   contact = boy.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, wait["Respontag"])
                           boy.sendImageWithURL(msg.to,image)
                           boy.sendMessage(msg.to, None, contentMetadata={"STKID":"65871427","STKPKGID":"4160181","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           boy.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           boy.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, "Jangan tag saya....")
                           boy.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"「Cek ID Sticker」\n❂͜͡☬➣ STKID : " + msg.contentMetadata["STKID"] + "\n❂͜͡☬➣ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n❂͜͡☬➣ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"\n❂͜͡☬➣ Nama : " + msg.contentMetadata["displayName"] + "\n❂͜͡☬➣ MID : " + msg.contentMetadata["mid"] + "\n❂͜͡☬➣ Status : " + contact.statusMessage + "\n❂͜͡☬➣ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)


        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = boy.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n❂͜͡☬➣ Sticker ID : {}".format(stk_id)
                   ret_ += "\n❂͜͡☬➣ Sticker Version : {}".format(stk_ver)
                   ret_ += "\n❂͜͡☬➣ Sticker Package : {}".format(pkg_id)
                   ret_ += "\n❂͜͡☬➣ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\n❂͜͡☬➣ sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = boy.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"\n❂͜͡☬➣ Nama : " + msg.contentMetadata["displayName"] + "\n❂͜͡☬➣ MID : " + msg.contentMetadata["mid"] + "\n❂͜͡☬➣ Status : " + contact.statusMessage + "\n❂͜͡☬➣ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)
#===========ADD BLACKLIST============#
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di Talkban")


#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = boy.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            boy.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ғᴏᴛᴏ")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = boy.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     boy.updateGroupPicture(msg.to, path)
                     boy.sendMessage(msg.to, "sᴜᴄᴄᴇs ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ғᴏᴛᴏ ɢʀᴏᴜᴘ")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["AFfoto"]:
                            path = boy.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][mid]
                            boy.updateProfilePicture(path)
                            boy.sendMessage(msg.to,"ғᴏᴛᴏ ʙᴇʀʜᴀsɪʟ ᴅɪɢᴀɴᴛɪ")               

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        boy.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage = help()
                               helpMessage1 = help1()
                               boy.sendMessage(msg.to, "Help \nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to,str(helpMessage))
                               boy.sendMessage(msg.to,str(helpMessage1))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~jackyeza✪·[► \n╚═══════════════════════╝")
                               boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                boy.sendMessage(msg.to, "sᴇʟғʙᴏᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                boy.sendMessage(msg.to, "sᴇʟғʙᴏᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage2 = help2()
                               boy.sendMessage(msg.to, "🔗ʜᴇʟᴘ ʙᴏᴛs🔗\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage2))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~jackyeza✪·[► \n ╚═══════════════════════╝")
                               boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage3 = helpbot()
                               boy.sendMessage(msg.to, "🔗ʜᴇʟᴘ ʙᴏᴛs🔗\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage3))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~jackyeza✪·[► \n ╚═══════════════════════╝")
                               boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
                               
                               
                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage4 = infomeme()
                               boy.sendMessage(msg.to, "Help Fun\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                               boy.sendMessage(msg.to, str(helpMessage4))
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n◄]·✪line.me/R/ti/p/~jackyeza✪·[► \n╚═══════════════════════╝")
                               boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")

                        if cmd == "uns on":
                            if msg._from in admin:
                                wait["unsend"] = False
                                boy.sendMessage(msg.to, "ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴏɴ")
                                
                        if cmd == "uns off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                boy.sendMessage(msg.to, "ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴏғғ")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ┏━━━━━━━━━━━━━━━━━\n┃┃          ❂͜͡☬➣sᴛᴀᴛᴜs❂͜͡☬➣\n┃┣━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["unsend"] == True: md+="┃┃❂͜͡☬➣ √ ᴜɴsᴇɴᴅ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴜɴsᴇɴᴅ「ᴏғғ」\n"                                
                                if wait["sticker"] == True: md+="┃┃❂͜͡☬➣ √ sᴛɪᴄᴋᴇʀ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ sᴛɪᴄᴋᴇʀ「ᴏғғ」\n"
                                if wait["contact"] == True: md+="┃┃❂͜͡☬➣ √ ᴄᴏɴᴛᴀᴄᴛ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴄᴏɴᴛᴀᴄᴛ「ᴏғғ」\n"
                                if wait["talkban"] == True: md+="┃┃❂͜͡☬➣ √ ᴛᴀʟᴋʙᴀɴ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴛᴀʟᴋʙᴀɴ「ᴏғғ」\n"
                                if wait["Mentionkick"] == True: md+="┃┃❂͜͡☬➣ √ ɴᴏᴛᴀʟ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ɴᴏᴛᴀʟ「ᴏғғ」\n"
                                if wait["detectMention"] == True: md+="┃┃❂͜͡☬➣ √ ʀᴇsᴘᴏɴ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ʀᴇsᴘᴏɴ「ᴏғғ」\n"
                                if wait["Mentiongift"] == True: md+="┃┃❂͜͡☬➣ √ ʀᴇsᴘᴏɴsɪғ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ʀᴇsᴘᴏɴsɪғ「ᴏғғ」\n"                                
                                if wait["autoJoin"] == True: md+="┃┃❂͜͡☬➣ √ ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴀᴜᴛᴏᴊᴏɪɴ「ᴏғғ」\n"
                                if settings["autoJoinTicket"] == True: md+="┃┃❂͜͡☬➣ √ ᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏғғ」\n"                                
                                if wait["autoAdd"] == True: md+="┃┃❂͜͡☬➣ √ ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴀᴜᴛᴏᴀᴅᴅ「ᴏғғ」\n"                                
                                if wait["Timeline"] == True: md+="┃┃❂͜͡☬➣ √ ᴛɪᴍᴇʟɪɴᴇ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴛɪᴍᴇʟɪɴᴇ「ᴏғғ」\n"
                                if msg.to in welcome: md+="┃┃❂͜͡☬➣ √ ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴡᴇʟᴄᴏᴍᴇ「ᴏғғ」\n"
                                if msg.to in simisimi: md+="┃┃❂͜͡☬➣ √ sɪᴍɪsɪᴍɪ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ sɪᴍɪsɪᴍɪ「ᴏғғ」\n"                                
                                if wait["autoLeave"] == True: md+="┃┃❂͜͡☬➣ √ ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ」\n"
                                else: md+="┃┃❂͜͡☬➣ ✖ ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏғғ」\n"                                      
                                boy.sendMessage(msg.to, md+"┃┣━━━━━━━━━━━━━━━━━━━━\n┃┃❧ 📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃┃❧ ⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ┗━━━━━━━━━━━━━━━━━")
                                boy.sendMessage(msg.to,"╔═══════════════════════╗\n ◄]·✪line.me/R/ti/p/~jackyeza✪·[► \n╚═══════════════════════╝"
)
                                boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")

                                
                        elif cmd == "creat" or text.lower() == 'creat':
                            if msg._from in admin:
                                boy.sendMessage(msg.to,"❂͜͡☬➣ ɪɴɪ ʙʀᴏ ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛɴʏᴀ...!!!") 
                                ma = ""
                                for i in creator:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "abo" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「sᴇʟғʙᴏᴛ ʙʏ : ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ ᴛᴇᴀᴍ」\n")
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd.startswith('penyewa'):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2025
                                bln = 12    #isi bulannya yg sewa
                                hr = 11    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = boy.getContact(mid)
                                favoritelist = boy.getFavoriteMids()
                                grouplist = boy.getGroupIdsJoined()
                                contactlist = boy.getAllContactIds()
                                blockedlist = boy.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                sw.sendText("u059095aa0cc2f6ef02d8ae72c3430163", 'Cek dulu')
                                elapsed_time = time.time() - start
                                ryan = boy.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɪɴғᴏʀᴍᴀsɪ sᴇʟғʙᴏᴛ 」\n• User : "
                                ret_ = "• Group : {} Group".format(str(len(grouplist)))
                                ret_ += "\n• Friend : {} Friend".format(str(len(contactlist)))
                                ret_ += "\n• Blocked : {} Blocked".format(str(len(blockedlist)))
                                ret_ += "\n• Favorite : {} Favorite".format(str(len(favoritelist)))
                                ret_ += "\n• Version : 「Self Bots 」"
                                ret_ += "\n• Expired : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• In days : {} again".format(days)
                                ret_ += "\n「 Speed Respon 」\n• {} detik".format(str(elapsed_time))
                                ret_ += "\n「 Selfbot Runtime 」\n• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               boy.sendMessage1(msg)

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "❂͜͡☬➣Nama : "+str(mi.displayName)+"\n❂͜͡☬➣MID : " +key1)
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "❂͜͡☬➣ 📖ɴᴀᴍᴀ : "+str(mi.displayName)+"\n❂͜͡☬➣ 📋ᴍɪᴅ : " +key1+"\n❂͜͡☬➣ 📝sᴛᴀᴛᴜs : "+str(mi.statusMessage))
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(boy.getContact(key1)):
                                   boy.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   boy.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               boy.sendMessage1(msg)

                        elif text.lower() == "hc":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   boy.removeAllMessages(op.param2)
                                   boy.sendText(msg.to,'🚮ᴄʜᴀᴛ ᴅɪʜᴀᴘᴜs ʙᴏssǫɪᴜ...!!!')
                               except:
                                   pass

                        elif cmd.startswith("bc: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = boy.getGroupIdsJoined()
                               for group in saya:
                                   boy.sendMessage(group,"=======[ʙʀᴏᴀᴅᴄᴀsʜ]=======\n\n"+pesan+"\n\nCreator : ◄]·✪line.me/R/ti/p/~jackyeza✪·[►")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   boy.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   boy.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               boy.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "poin":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               boy.sendMessage(msg.to, "ʀᴇsᴛᴀʀᴛ...!!!")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "run":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "ʙᴏᴛ ᴛᴇʟᴀʜ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ" +waktu(eltime)
                               boy.sendMessage(msg.to,bot)
                               boy.sendMessage(msg.to,"╔═══════════════════════╗\n ◄]·✪line.me/R/ti/p/~jackyeza✪·[► \n╚═══════════════════════╝")
                               boy.sendContact(to, "u059095aa0cc2f6ef02d8ae72c3430163")
                            
                        elif cmd == "gin":
                          if msg._from in admin:
                            try:
                                G = boy.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                boy.sendMessage(msg.to, "❂͜͡☬➣ ʙᴏᴛ ɢʀᴏᴜᴘ ɪɴғᴏ\n\n ❂͜͡☬➣ ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(G.name)+ "\n❂͜͡☬➣ ɪᴅ ɢʀᴏᴜᴘ : {}".format(G.id)+ "\n❂͜͡☬➣ ᴘᴇᴍʙᴜᴀᴛ : {}".format(G.creator.displayName)+ "\n❂͜͡☬➣ ᴡᴀᴋᴛᴜ ᴅɪʙᴜᴀᴛ : {}".format(str(timeCreated))+ "\n❂͜͡☬➣ ᴊᴜᴍʟᴀʜ ᴍᴇᴍʙᴇʀ : {}".format(str(len(G.members)))+ "\n❂͜͡☬➣ ᴊᴜᴍʟᴀʜ ᴘᴇʀᴅɪɴɪ : {}".format(gPending)+ "\n❂͜͡☬➣ ɢʀᴏᴜᴘ ǫʀ : {}".format(gQr)+ "\n❂͜͡☬➣ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket))
                                boy.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                boy.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd.startswith("igr "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "❂͜͡☬➣ ʙᴏᴛ ɢʀᴏᴜᴘ ɪɴғᴏ\n"
                                ret_ += "\n❂͜͡☬➣ 📖ɴᴀᴍᴀ : {}".format(G.name)
                                ret_ += "\n❂͜͡☬➣ 📃ɪᴅ : {}".format(G.id)
                                ret_ += "\n❂͜͡☬➣ 📝ᴄʀᴇᴀᴛᴏʀ : {}".format(gCreator)
                                ret_ += "\n❂͜͡☬➣ ⏰ᴄʀᴇᴀᴛᴇᴅ ᴛɪᴍᴇ : {}".format(str(timeCreated))
                                ret_ += "\n❂͜͡☬➣ 👪ᴍᴇᴍʙᴇʀ : {}".format(str(len(G.members)))
                                ret_ += "\n❂͜͡☬➣ 🚶ᴘᴇɴᴅɪʀɪ : {}".format(gPending)
                                ret_ += "\n❂͜͡☬➣ 👙ǫʀ : {}".format(gQr)
                                ret_ += "\n❂͜͡☬➣ 📠ᴛɪᴄᴋᴇᴛ : {}".format(gTicket)
                                ret_ += ""
                                boy.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("ime "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "❂͜͡☬➣ "+ str(no) + ". " + mem.displayName
                                boy.sendMessage(to,"❂͜͡☬➣ ɴᴀᴍᴀ ɢʀᴏᴜᴘ : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「ᴛᴏᴛᴀʟ %i ᴍᴇᴍʙᴇʀ」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = boy.getGroup(i)
                                if ginfo == group:
                                    k1.leaveGroup(i)
                                    k2.leaveGroup(i)
                                    k3.leaveGroup(i)
                                    k4.leaveGroup(i)
                                    k5.leaveGroup(i)
                                    k6.leaveGroup(i)
                                    k7.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    k10.leaveGroup(i)
                                    boy.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴏᴜᴘ " +str(ginfo.name))

                        elif cmd == "fl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getAllContactIds()
                               for i in gid:
                                   G = boy.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ ʟɪsᴛ ᴛᴇᴍᴀɴ ]\n┃┃\n"+ma+"┃┃\n┗━━[ ᴛᴏᴛᴀʟ「"+str(len(gid))+"」ғʀɪᴇɴᴅs ]")

                        elif cmd == "gl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getGroupIdsJoined()
                               for i in gid:
                                   G = boy.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ ʟɪsᴛ ɢʀᴏᴜᴘ ]\n┃┃\n"+ma+"┃┃\n┗━━[ ᴛᴏᴛᴀʟ「"+str(len(gid))+"」ɢʀᴏᴜᴘs ]")

                        elif cmd == "gl1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"┏━━[ ʟɪsᴛ ɢʀᴏᴜᴘ ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")


                        elif cmd == "opn":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "ᴜʀʟ ᴛᴇʟᴀʜ ᴅɪʙᴜᴋᴀ")

                        elif cmd == "clo":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "ᴜʀʟ ᴛᴇʟᴀʜ ᴅɪᴛᴜᴛᴜᴘ")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = k1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      k1.updateGroup(x)
                                   gurl = k1.reissueGroupTicket(msg.to)
                                   k1.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "rjt":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = boy.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      boy.rejectGroupInvitation(gid)
                                  boy.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ ".format(str(len(ginvited))))
                              else:
                                  boy.sendMessage(to, "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ᴛᴇʀᴛᴜɴᴅᴀ")

#===========BOT UPDATE============#
                        elif cmd == "ugp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                boy.sendMessage(msg.to,"ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ......")
                                
                        elif cmd == "uf":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["AFfoto"][mid] = True
                                boy.sendMessage(msg.to,"ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ......")
                                
                        elif cmd.startswith("mme: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = boy.getProfile()
                                profile.displayName = string
                                boy.updateProfile(profile)
                                boy.sendMessage(msg.to,"ɴᴀᴍᴀ ᴅɪɢᴀɴᴛɪ ᴊᴀᴅɪ" + string + "")

#===========BOT UPDATE============#
                        elif cmd == "pa" or text.lower() == 'hai':
                          if msg._from in admin:
                               group = boy.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)
                                
                        elif cmd == "bme":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                G = boy.getGroup(msg.to)
                                boy.sendText(msg.to, "╠❂͜͡☬➣ Bye bye fams "+str(G.name))
                                boy.leaveGroup(msg.to)
                                
                        elif cmd == "sr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = boy.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = boy.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                boy.sendMessage(msg.to, " ❧ ʙᴏᴛ sᴘᴇᴇᴅ ʀᴇsᴘᴏɴ \n\n - ɢᴇᴛ ᴘʀᴏғɪʟᴇ\n   %.10f\n - ɢᴇᴛ ᴄᴏɴᴛᴀᴄᴛ\n   %.10f\n - ɢᴇᴛ ɢʀᴏᴜᴘ\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               boy.sendMessage(msg.to, "💿[ʟᴏᴀᴅɪɴɢ] sᴘᴇᴇᴅ...!!!")
                               elapsed_time = time.time() - start
                               boy.sendMessage(msg.to, "{} ᴅᴇᴛɪᴋ".format(str(elapsed_time)))
                               boy.sendMessage(msg.to," [sᴜᴄᴄᴇs]... sᴘᴇᴇᴅ ᴅᴏɴᴇ √...!!!")

                        elif cmd == "lur on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['AFreadPoint'][msg.to] = msg_id
                                 Setmain['AFreadMember'][msg.to] = {}
                                 boy.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lur off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['AFreadPoint'][msg.to]
                                 del Setmain['AFreadMember'][msg.to]
                                 boy.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lu":
                          if msg._from in admin:
                            if msg.to in Setmain['AFreadPoint']:
                                if Setmain['AFreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['AFreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(boy.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        boy.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['AFreadPoint'][msg.to]
                                        del Setmain['AFreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['AFreadPoint'][msg.to] = msg.id
                                    Setmain['AFreadMember'][msg.to] = {}
                                else:
                                    boy.sendMessage(msg.to, "User kosong...")
                            else:
                                boy.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  boy.sendMessage(msg.to, "ᴄᴇᴋ sɪᴅᴇʀ ᴅɪᴀᴋᴛɪғᴋᴀɴ\n\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  boy.sendMessage(msg.to, "ᴄᴇᴋ sɪᴅᴇʀ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n\n📅ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  boy.sendMessage(msg.to, "sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ")

                        elif cmd.startswith("stag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["AFlimit"] = num
                                boy.sendMessage(msg.to,"ᴛᴏᴛᴀʟ sᴘᴀᴍᴛᴀɢ ᴅɪᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("scall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                boy.sendMessage(msg.to,"ᴛᴏᴛᴀʟ sᴘᴀᴍᴄᴀʟʟ ᴅɪᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("stag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["AFlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                boy.sendMessage1(msg)
                                            except Exception as e:
                                                boy.sendMessage(msg.to,str(e))
                                    else:
                                        boy.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "scall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = boy.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                boy.sendMessage(msg.to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢɪʀɪᴍ {} ᴜɴᴅᴀɴɢᴀɴ ᴄᴀʟʟ ɢʀᴏᴜᴘ ".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        boy.sendMessage(msg.to,str(e))
                                else:
                                    boy.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, str(Setmain["AFmessage1"]))                                                                       
                        elif 'Mbt' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               boy.sendMessage(msg.to,"📷sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ📷\n"+boy.authToken)

#==============================================================================# 
                       

#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs) 
                                    
                        elif 'Wl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Wl ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "ᴘᴇɴʏᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴀᴋᴛɪғ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ ᴅɪᴀᴋᴛɪғᴋᴀɴ\n ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「ᴅɪᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ\nᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "ᴘᴇɴʏᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ"
                                    boy.sendMessage(msg.to, "「ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)
                                    
#===========KICKOUT============#
                        elif ("!?? " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = boy.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           boy.updateGroup(G)
                                           invsend = 0
                                           Ticket = boy.reissueGroupTicket(msg.to)
                                           boy.kickoutFromGroup(msg.to, [target])
                                           X = boy.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           boy.updateGroup(X)
                                       except:
                                           pass

                        elif ("!!/ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                
                        elif  text.lower() == "virus" or text.lower () == "Crash":
                          if wait["selfbot"] == True:
                        #    if msg._from in admin:
                              dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash!","Kamu asu ngecrash terus!","crash cresh crash cresh, bikin hp orang lag anjing!")
                              ngkol = random.choice(dia)
                              random.choice(ABC).sendText(msg.to,ngkol)
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                              random.choice(ABC).sendText(msg.to,"Mampus!")
                              if msg.text in ["!cipok",".desah","!makan","!","?","!kickall",".kickall","Nuke","Cleanse","Ratakan","Mayhem","MB Mayhem","Kick all","kickall","!rata","play","sory","sorry","maaf","sexi",".",","]:
                              	Peringatan = ("Manual kek jangan pake bot.","Cupu lu! Ratain pake bot!","Lain kali liat liat dulu~","ＴＥＲＣＹＤＵＣＫ")
                              Vonis = random.choice(Peringatan)
                              random.choice(ABC).sendText(msg.to, Vonis)
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                              
                               #for x in key["MENTIONEES"]:
                                    #targets.append(x["M"])
                           #    for target in targets:
                               #    if target not in Bots:
                                   #    try:
                                        #   random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                      # except:
                                        #   pass
                                        
                        elif cmd == "fresh" or text.lower() == 'fresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                wait["invite"] = False
                                boy.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴅɪʀᴇғʀᴇsʜ....!!!")

                        elif cmd == "ca" or text.lower() == 'ca':
                                ma = ""
                                for i in admin:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "nt on" or text.lower() == 'nt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                boy.sendMessage(msg.to,"ɴᴏᴛᴀɢ ᴅɪᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "nt off" or text.lower() == 'nt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                boy.sendMessage(msg.to,"ɴᴏᴛᴀɢ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "tl on" or text.lower() == 'tl on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                boy.sendMention(msg.to, "「 Status Timeline 」\nUser \nSilahkan kirim postingannya\nKetik timeline off jika sudah slesai")

                        elif cmd == "tl off" or text.lower() == 'tl off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                boy.sendMention(msg.to, "「 Status Timeline 」\nUser ", " \nDeteksi timeline dinonaktifkan")
                                
                        elif cmd == "invi on" or text.lower() == 'invi on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                boy.sendMention(msg.to, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invi off" or text.lower() == 'invi off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                boy.sendMention(msg.to, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                boy.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                boy.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "res on" or text.lower() == 'res on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "res off" or text.lower() == 'res off':
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
                                
                        elif cmd == "rg on" or text.lower() == 'rg on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ɢɪғᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "rg off" or text.lower() == 'rg off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                boy.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ɢɪғᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")                                

                        elif cmd == "ajo on" or text.lower() == 'ajo on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                boy.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "ajo off" or text.lower() == 'ajo off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                boy.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                boy.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                boy.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                boy.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                boy.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "str on" or text.lower() == 'str on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                boy.sendMessage(msg.to,"ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪᴀᴋᴛɪғᴋᴀɴ...!!!")

                        elif cmd == "str off" or text.lower() == 'str off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                boy.sendMessage(msg.to,"ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪᴍᴀᴛɪᴋᴀɴ...!!!")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                boy.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                boy.sendMessage(msg.to,"Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"⏩ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"⏩ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = boy.getContact(i)
                                        boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'cb':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = boy.getContacts(wait["blacklist"])
                              mc = "���%i」User Blacklist" % len(ragets)
                              boy.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set wl: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set re: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["AFmessage1"] = spl
                                  boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  boy.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["AFmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = boy.findGroupByTicket(ticket_id)
                                     boy.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     boy.sendMessage(msg.to, "💻sᴇʟғʙᴏᴛ ʙʏ ᴊᴀᴄᴋʏ ᴀʀᴇᴢᴀ💻📲 OTW MASUK KE GROUP : %s" % str(group.name))

    except Exception as error:
        print (error)

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
