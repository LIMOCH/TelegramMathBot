import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import math
TOKEN = '5836886917:AAFCzT6SGLfY9Q34xWnvi03l7Ad25fOxrJI'  # вставьте свой токен


def start(update, context):
    update.message.reply_text('Здравствуйте! Я бот-калькулятор. Я могу помочь найти периметр квадрата, его площадь и объем куба. Введите /help для списка команд.')


def help(update, context):
    update.message.reply_text('/square - найти периметр квадрата\n/volume - найти объем куба\n/rectangle - найти периметр, площадь, объем фигуры')

#----геометрические--задачи-----
def perimeter(update, context):
    try:
        side = float(context.args[0])
        p = 4 * side
        s = side ** 2
        update.message.reply_text(f'Периметр квадрата со стороной {side} равен {p}\nПлощадь квадрата со стороной {side} равна {s}')
    except (IndexError, ValueError):
        update.message.reply_text('Использование: /square сторона')
def rectangle(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Неверное количество аргументов. Введите два числа через пробел.")
        return
    try:
        length = float(args[0])
        width = float(args[1])
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Введите числа.")
        return

    area = length * width
    perimeter = 2 * (length + width)
    volume = 0.0

    text = f"Периметр прямоугольника: {perimeter:.2f}\nПлощадь прямоугольника: {area:.2f}"
    if length > 0 and width > 0:
        volume = length * width * 1
        text += f"\nОбъем прямоугольника: {volume:.2f}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
def volume(update, context):
    try:
        side = float(context.args[0])
        result = side ** 3
        update.message.reply_text(f'Объем куба со стороной {side} равен {result}')
    except (IndexError, ValueError):
        update.message.reply_text('Использование: /volume сторона')
def spherevolume(update, context):
    try:
        r = float(context.args[0])
        result = (4 / 3) * math.pi * (r ** 3)
        update.message.reply_text(f"Объем сферы с радиусом {r} равен {result}")
    except (IndexError, ValueError):
        update.message.reply_text("Неверный формат ввода. Пожалуйста, введите радиус сферы в числовом формате.")
def circle(update, context):
    try:
        pi = math.pi
        radius = float(context.args[0])
        s = pi * (radius ** 2)
        perimeter = 2 * pi * radius
        update.message.reply_text(f"Площадь круга с радиусом {radius} равна {s}\nПериметр круга равен {perimeter}")
    except (IndexError, ValueError):
        update.message.reply_text("Неверный формат ввода. Пожалуйста, введите радиус круга в числовом формате.")

#----Классические--операторы-----
def stepen(update, context):
    try:
        num = int(context.args[0])
        sp = int(context.args[0])
        result = num ** sp
        update.message.reply_text(f'число {num} в степени {sp} = {result}')
    except (IndexError, ValueError):
        update.message.reply_text('Error')
def plus(update, context):
    try:
        a = int(context.args[0])
        b = int(context.args[0])
        result = a + b
        update.message.reply_text(f'число {a} + {b} = {result}')
    except(IndexError, ValueError):
        update.message.reply_text('Error')
def minus(update, context):
    try:
        a = int(context.args[0])
        b = int(context.args[0])
        result = a - b
        update.message.reply_text(f'число {a} - {b} = {result}')
    except:
        update.message.reply_text('Error')
def multiply(update, context):
   try:
       a = int(context.args[0])
       b = int(context.args[0])
       result = a * b
       update.message.reply_text(f'число {a} * {b} = {result}')
   except:
       update.message.reply_text('Error')

#----Формулы-----
def sq_sum(update, context):
    try:
        a = int(context.args[0])
        b = int(context.args[0])
        result = (a + b) ** 2
        update.message.reply_text(f'число {a} * {b} = {result}')
    except:
        update.message.reply_text('Error')
def sq_raz(update, context):
    try:
        a = int(context.args[0])
        b = int(context.args[0])
        result = (a - b) ** 2
        update.message.reply_text(f'число {a} * {b} = {result}')
    except:
        update.message.reply_text('Error')
def difference_of_sq(update, context):
    try:
        a = int(context.args[0])
        b = int(context.args[0])
        result = (a + b) * (a - b)
        update.message.reply_text(f'число {a} * {b} = {result}')
    except:
        update.message.reply_text('Error')



def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('square', perimeter))
    dp.add_handler(CommandHandler('volume', volume))
    dp.add_handler(CommandHandler('rectangle', rectangle))
    dp.add_handler(CommandHandler('spherevolume', spherevolume))
    dp.add_handler(CommandHandler('circle', circle))
    
    dp.add_handler(CommandHandler('stepen', stepen))
    dp.add_handler(CommandHandler('plus', plus))
    dp.add_handler(CommandHandler('minus', minus))
    dp.add_handler(CommandHandler('multiply', multiply))

    dp.add_handler(CommandHandler('sq_sum', sq_sum))
    dp.add_handler(CommandHandler('sq_min', sq_raz))
    dp.add_handler(CommandHandler('sq_dif', difference_of_sq))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

