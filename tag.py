from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from pycbrf import ExchangeRates
from emoji import emojize
from aiogram.dispatcher.filters.state import State, StatesGroup
import requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "5836886917:AAFCzT6SGLfY9Q34xWnvi03l7Ad25fOxrJI"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

inline_btn_psabr = InlineKeyboardButton(emojize('Вычисление площади, периметра, длинны, ширины фигуры'), callback_data='psabr')
inline_btn_vstr = InlineKeyboardButton(emojize('Вычисление скорости, расстояния, времени'), callback_data='vstr')

inline_kb = InlineKeyboardMarkup()# Создали и загрузили инлайн клаву
inline_kb.add(inline_btn_psabr, inline_btn_vstr)

#===================Площадь==================================
inline_btn_p = InlineKeyboardButton(emojize('Периметр'), callback_data='p')
inline_btn_s = InlineKeyboardButton(emojize('Площадь'), callback_data='s')
inline_btn_a = InlineKeyboardButton(emojize('Длинна'), callback_data='a')
inline_btn_b = InlineKeyboardButton(emojize('Ширина'), callback_data='b')

inline_ssf = InlineKeyboardMarkup()# Создали и загрузили инлайн клаву
inline_ssf.add(inline_btn_p,inline_btn_s,inline_btn_a,inline_btn_b)
#=============================================================
#===================VST==========================================
inline_btn_v = InlineKeyboardButton(emojize('Скорость'), callback_data='v')
inline_btn_t = InlineKeyboardButton(emojize('Время'), callback_data='t')
inline_btn_s = InlineKeyboardButton(emojize('Расстояние'), callback_data='s')
inline_ssd = InlineKeyboardMarkup()# Создали и загрузили инлайн клаву
inline_ssd.add(inline_btn_v,inline_btn_t,inline_btn_s)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "лялял рабоатет выбери чо решать будешь", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data == 'psabr', state=None)
async def sheessh(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбрать, что вам надо найти? (Периметр, Площадь, Длинна, Ширина)", reply_markup=inline_ssf)

@dp.callback_query_handler(lambda c: c.data == 'vst', state=None)
async def sheessh(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбрать, что вам надо найти? (Скорость(м/c), время(с) путь(м))", reply_markup=inline_ssd)

class Form(StatesGroup):
    a = State() 
    b = State() 


#====================Периметр=================================
@dp.callback_query_handler(lambda c: c.data == 'p')
async def sheesh(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Введите длинну: ")
    await Form.a.set()

@dp.message_handler(state=Form.a)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a'] = int(message.text)

    await Form.next()
    await message.reply("Введите ширину:")
    await state.update_data(a=int(message.text))
@dp.message_handler(state=Form.b) 
async def namee(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await state.update_data(b=int(message.text))
        data['b'] = int(message.text)
        p = 2 * (data['a'] + data['b'])
    await bot.send_message(message.from_user.id, text=f'Периметр = {p}')
    await state.finish()



@dp.callback_query_handler(lambda c: c.data == 's')
async def sheeesh(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Введите длинну: ")
    await Form.a.set()

@dp.message_handler(state=Form.a)
async def processs_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a'] = int(message.text)

    await Form.next()
    await message.reply("Введите ширину:")
    await state.update_data(a=int(message.text))

@dp.message_handler(state=Form.b) 
async def nameee(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await state.update_data(b=int(message.text))
        data['b'] = int(message.text)
        s = data['a'] * data['b']
    await bot.send_message(message.from_user.id, text=f'Площадь = {p}')
    await state.finish()



@dp.callback_query_handler(lambda c: c.data == 'a')
async def sheeshas(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Введите площадь: ")
    await Form.a.set()

@dp.message_handler(state=Form.a)
async def process_nameas(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a'] = int(message.text)

    await Form.next()
    await message.reply("Введите ширину:")
    await state.update_data(a=int(message.text))

@dp.message_handler(state=Form.b) 
async def nameeds(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await state.update_data(b=int(message.text))
        data['b'] = int(message.text)
        s = data['a'] / data['b']
    await bot.send_message(message.from_user.id, text=f'Длинна = {p}')
    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'b')
async def sheeshas(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Введите длинну: ")
    await Form.a.set()

@dp.message_handler(state=Form.a)
async def process_namdse(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a'] = int(message.text)

    await Form.next()
    await message.reply("Введите площадь:")
    await state.update_data(a=int(message.text))

@dp.message_handler(state=Form.b) 
async def namease(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await state.update_data(b=int(message.text))
        data['b'] = int(message.text)
        s = data['b'] / data['a']
    await bot.send_message(message.from_user.id, text=f'Длинна = {p}')
    await state.finish()
#=============================================================


#======================VST===================================


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)