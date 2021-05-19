
#### ------------------- COpyBot (faker bot) -----------------###
#### -------------- Coded By : @keyvanvafaee  ---- ###

import sys,random,os,logging,asyncio,telethon,re,time
from telethon import TelegramClient, events , utils , functions, types , connection
from telethon import errors , functions
from telethon.tl.functions.account import UpdateProfileRequest , UpdateUsernameRequest,UpdateStatusRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import InputUser
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import InputPeerChat





num = '+19094069563'
api_id = 855178
api_hash = 'd4b8d0a8494ab6043f0cfdb1ee6383d3'
client = TelegramClient("keyvanVafaee" , api_id , api_hash )
client.start()

@client.on(events.NewMessage(pattern='[Cc]opy', forwards=False))
async def handler(event):

        m = await event.reply("🛡️ Copy process started ...  \n '□□□□□□□□□□□' ")
        await client(UpdateProfileRequest(last_name=' '))
        await m.edit("🛡️ Copy process started ... \n '■□□□□□□□□□□' ")
        await asyncio.sleep(1)
        await client(UpdateProfileRequest(about=' '))
        await m.edit("🛡️ Copy process started ... \n '■■□□□□□□□□□' ")
        me = await client(GetFullUserRequest("me"))
        profile_pic = me.profile_photo
        while me.profile_photo:
            await client(DeletePhotosRequest([profile_pic]))
            me = await client(GetFullUserRequest("me"))
            profile_pic = me.profile_photo
            asyncio.sleep(1)
        asyncio.sleep(2)
        await m.edit("🛡️ Copy process started ... \n '■■■□□□□□□□□' ")
        me = await client.get_me()
        try:
                item = ((event.raw_text).split(' '))[1]
                id = await client.get_input_entity('{}'.format(item))
                id = (id.user_id)
                info = (await client.get_entity(id))
                bio = (await client(GetFullUserRequest(item))).about
                result = await client(functions.photos.GetUserPhotosRequest(user_id=item , offset= 0 , max_id = 0 , limit=100))
                c=0
                for pic in result.photos:
                    print(await client.download_file((result.photos)[c]  , file= str(item)+str(c)+'.jpg'))
                    c+=1
                for i in range(0,c):
                    await client(UploadProfilePhotoRequest(await client.upload_file(str(item)+str((c-1)-i)+".jpg")))
                await m.edit("🛡️ Copy process started ... \n '■■■■■■□□□□□' ")
                await asyncio.sleep(2)
                await client(UpdateProfileRequest(
about=bio
))
                await client(UpdateProfileRequest(first_name=info.first_name))
                await asyncio.sleep(2)
                await m.edit("🛡️ Copy process started ... \n '■■■■■■■■□□□' ")
                await client(UpdateProfileRequest(last_name=info.last_name))
                await asyncio.sleep(2)
                re= ''.join(random.choice('abcdefghi1234567890jklmnopqrstuvwxyz') for _ in range(3))
                await client(UpdateUsernameRequest(info.username+re))
                await asyncio.sleep(2)
                await m.edit("🛡️ Copy process started ... \n '■■■■■■■■■■' ")
                await asyncio.sleep(30)
                os.system("rm -rf *.jpg")
        except Exception as e :
                await event.reply(" Log: "+str(e))

loop = asyncio.get_event_loop()
loop.run_forever()

##### ---- usage 
#### ----- copy @UserWhoYouWantCopyItsProfile 
#### Wowa you copied all images / bio / name / last name OF the user