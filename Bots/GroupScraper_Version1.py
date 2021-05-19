############################################
### coded by @keyvanvafaee ( Keyvan Vafaee )
############################################
##----------- modules ---------
from telethon.sync import TelegramClient,functions,types,events,errors
from telethon.tl.custom import Button
import sqlite3 , telethon 
import datetime
import time
from time import sleep
import sys,requests,random,os,json,string,time
from lxml import html
import socks , logging   , asyncio , random
import requests
from telethon import types as telethon_types
from telethon.tl import types as tl_telethon_types

### --- DEBUG 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

#--------- Starting Bot

bot = TelegramClient('when',1753946,'ba6b9d9fa75d4bbb6f09224e6cae8200')
bot.start()
info = bot.get_me()

#--------- Create Directories

for item in ['Database']:
    if not os.path.exists(item):
        os.mkdir(item)


#---------alert

print(f'Bot Connected on {info.username}  Successfully !')


#-------- Only Get  Online / Last Seen Recently Members.

def online_within(participant):
    status = participant.status

    if isinstance(status, tl_telethon_types.UserStatusOnline): #------ Online Members
        return True


    if isinstance(status, tl_telethon_types.UserStatusRecently): #------ Last Seen Members
        return True

    return False

#------- Replace 282199711 to your Admins Chat Ids
#------- ping 
@bot.on(events.NewMessage(from_users=[282199711] , pattern="[pP]ing"))
async def handler(msg):

    await msg.reply("`Online` !")

# ----- help
@bot.on(events.NewMessage(from_users=[282199711 ] , pattern="[hH]elp"))
async def handler(msg):
    await msg.reply('''

▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬

▭ **help** : `for showing help message `  


▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬

▭ **get** link :  `for getting usernames from link`

▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬

        ''')

#------- get yourLink 
@bot.on(events.NewMessage(from_users=[282199711] , pattern="get"))
async def handler(msg):

    link = msg.raw_text.split('get ')[1]
    keu  = link
    m    = await msg.reply("● please wait ")
    
    if '@' in link:
        keu = link.split('@')[1]

    elif 'joinchat' in link:
       keu = link.split('/')[-1]
       
    fl = open(f'Database/{keu}.txt','w')
    counter = 0
    if not '@' in link:
        link = f'https://t.me/joinchat/{keu}'
    async def join(ls): 
        try:
            if '@' in ls:
                    await bot(functions.channels.JoinChannelRequest(channel=ls))
            else:
                    await bot(functions.messages.ImportChatInviteRequest(hash=ls.split('/')[-1]))
            return True
        except errors.UserAlreadyParticipantError:
            return True 
        except errors.rpcerrorlist.AuthKeyDuplicatedError:
            return -3
        except errors.UserDeactivatedBanError:
            return -1
        except errors.UserDeactivatedError:
            return -1
        except errors.SessionExpiredError:
            return -2
        except errors.SessionRevokedError:
            return -2
        except errors.rpcerrorlist.ChannelPrivateError:
            return -4
        except errors.rpcerrorlist.InviteHashExpiredError:
            await msg.reply("** link is invalid ! **")

        except errors.rpcerrorlist.FloodWaitError as e :
            x = [int(s) for s in str(e).split() if s.isdigit()][0]
            await log_msg.edit(f"❌🎗 [**join**] Wait for   ** {x} ** secounds")
            await asyncio.sleep(x)
            return None

        except Exception as e :
            print (e.__class__ , str(e))
            return -1

    ww = await join(link)
    if (ww == None):
        ww = await join(link)
    if (ww == -4 ):
        await msg.reply(" ** I Baned from this chat ! **")
    if (ww == -2 ):
        await msg.reply(" **Session SessionRevokedError /  SessionExpiredError **")
    if (ww == -3) :
        await msg.reply(" **  AuthKeyDuplicatedError  **")
    if ww == True:
        await m.edit(f"Join to {link} Completed \n please wait for leaching  ")
        async for item in bot.iter_participants(link , aggressive =True):
            if item.username != None:
                if  online_within(item):
                    fl.write(str(item.username) + '\n')
                    counter+=1
        fl.close()
        await bot.send_file(msg.chat_id, f'Database/{keu}.txt', caption=f"🎗 Total `{counter}` Leached Users.\n ")


loop = asyncio.get_event_loop()
loop.run_forever()

## ------------- Usage -------------------
## Replace all 282199711 with your chat id 
## get @YourGoupLink
## After that Bot will Save all members that are Online Or last Seen Recently in the File