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

inline_btn_psabr = InlineKeyboardButton(emojize('Вычисление площади фигуры'), callback_data='psabr')


inline_kb = InlineKeyboardMarkup()# Создали и загрузили инлайн клаву
inline_kb.add(inline_btn_psabr)

inline_btn_p = InlineKeyboardButton(emojize('Периметр'), callback_data='p')
inline_btn_s = InlineKeyboardButton(emojize('Площадь'), callback_data='s')
inline_btn_a = InlineKeyboardButton(emojize('Длинна'), callback_data='a')
inline_btn_b = InlineKeyboardButton(emojize('Ширина'), callback_data='b')

inline_ssf = InlineKeyboardMarkup()# Создали и загрузили инлайн клаву
inline_ssf.add(inline_btn_p,inline_btn_s,inline_btn_a,inline_btn_b)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "лялял рабоатет выбери чо решать будешь", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data == 'psabr', state=None)
async def sheessh(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбрать, что вам надо найти? (Периметр, Площадь, Длинна, Ширина) - ", reply_markup=inline_ssf)

class Form(StatesGroup):
    a = State() 
    b = State() 

@dp.callback_query_handler(lambda c: c.data == 'p')
async def sheesh(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Введите длинну: ")
    await Form.a.set()

@dp.message_handler(state=Form.a)
async def process_name(message: types.Message, state: FSMContext):

    await Form.next()
    await message.reply("Введите ширину:")
    await state.update_data(a=int(message.text))
    #await bot.send_message(message.from_user.id, "Введите ширину: ")
    #await Form.a.set()
    #ab = Form()
    #P = 2 * (ab.a + ab.b)
    #await bot.send_message(message.from_user.id, 'Периметр = ',P)

@dp.message_handler(state=Form.b) 
async def namee(message: types.Message, state: FSMContext):
    await state.update_data(b=int(message.text))
    b = message.text
    ab = Form()
    p = 2 * (ab.a + ab.b)
    await bot.send_message(message.from_user.id, text=f'Спасибо за ответ\n '
                                                  f'Тебя зовут: {p}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)