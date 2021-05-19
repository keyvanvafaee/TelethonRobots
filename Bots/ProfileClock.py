############################################
### coded by @keyvanvafaee ( Keyvan Vafaee )
############################################
##----------- modules ---------
from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions
from datetime import datetime
import pytz
import aiocron
import asyncio

api_id ="your api id"
api_hash ="your api hash"

client=TelegramClient("session name", api_id, api_hash)

@aiocron.crontab('*/1 * * * *')
async def clock():
	ir=pytz.timezone("Asia/Tehran") #----- Time Zone 
	time=datetime.now(ir).strftime("%H:%M")
	await client(functions.account.UpdateProfileRequest(last_name=time))

client.start()
clock.start()
client.run_until_disconnected()
asyncio.get_event_loop().run_forever()

#------------ Usage ------------
#---- This Source Will Setup  Automatic Clock in your Profile !