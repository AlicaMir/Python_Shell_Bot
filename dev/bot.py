from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from replics import *
from data import *
from Shell import Shell

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
shell = Shell()

def private_chat(message: types.Message):
    return message.chat.type == 'private'

@dp.message_handler(private_chat, commands='authorize')
async def authorize(message: types.Message):
    if not registred(message.from_user.id):
        try: password = message.text.split()[1]
        except: password = ''
        if (password == PASSWORD):
            users.append({'id' : message.from_user.id})
            await message.answer(welcome_message)
        else:
            await message.answer(wrong_password)
    else:
        await message.answer(already_authorized)

@dp.message_handler(private_chat, commands='unauthorize')
async def unauthorize(message: types.Message):
    try:
        users.remove({'id':message.from_user.id})
        await message.answer(unauthrization_complete)
    except ValueError as e:
        await message.answer(not_authorized)
    

@dp.message_handler(private_chat, commands=['help','start'])
async def help(message: types.Message):
    if registred(message.from_user.id):
        await message.answer(help_registered)
    else:
        await message.answer(help_not_registered)
 
@dp.message_handler(private_chat)
async def handler(message: types.Message):
    if registred(message.from_user.id):
        answer = shell.handler(message.text)
        if answer != None:
            await message.answer(answer)

async def shutdown(dispatcher):
    save_data(users, path_to_users)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
