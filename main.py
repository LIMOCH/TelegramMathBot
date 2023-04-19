import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import math
from telegram import KeyboardButton, ReplyKeyboardMarkup
TOKEN = '5836886917:AAFCzT6SGLfY9Q34xWnvi03l7Ad25fOxrJI'  # вставьте свой токен

def start(update, context):
    update.message.reply_text('Здравствуйте! Я бот-калькулятор и могу Вам помочь с вычислениями: найти периметр квадрата, его площадь, объем куба, разность квадратов, квадрат разности и прочие. \nДля помощи нажмите сюда -> /help.')


def help(update, context):
    update.message.reply_text('Для вычислений нужно ввести: \n /команда <первое число> <второе число> (через пробел). \n Для подсказки по каждой задачe, нажмите на нужную команду из списка. \n\nВычисления для геометрических фигур: \n/square - найти периметр квадрата\n/volume - найти объем куба\n/rectangle - найти периметр и площадь прямоугольника\n/spherevolume - найти объём сферы\n/circle - найти площадь круга\n/densitys - найти плотность фигуры\n------------\nДействия с числами: \n/stepen - возвести число в степень\n/plus – сложить 2 числа\n/minus – найти разность 2-х чисел\n/multiply – умножить 2 числа\n-------------\nФормулы сокращенного умножения: \n/sq_sum – Квадрат суммы (a + b)^2 \n/sq_min - Квадрат разности (a - b)^2 \n/sq_dif - Разность квадратов a^2 - b^2 \n/cube_sum - Куб суммы ( a + b )^3 \n/cube_raz - Куб разности ( a − b )^3 \n/sum_cube - Сумма кубов a^3 + b^3 \n/raz_cube - Разность кубов a^3 - b^3')

#----геометрические--задачи-----
def perimeter(update, context):
    args = context.args
    if len(args) < 1 or len(args) > 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления периметра и площади квадрата скопируйте команду и через пробел введите длину одной стороны квадрата: /square <число равное длине 1 стороны квадрата>")
        return
    try:
        side = float(context.args[0])
        p = 4 * side
        s = side ** 2
        update.message.reply_text(f'Периметр квадрата со стороной {side} = {p}\nПлощадь квадрата со стороной {side} = {s}')
    except (IndexError, ValueError):
        update.message.reply_text('Вы ввели неверные значения, попробуйте /square <число равное длине 1 стороны квадрата>')
def rectangle(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления периметра и площади прямоугольника скопируйте команду и через пробел введите длину одной стороны прямоугольника, затем через пробел введите длину другой стороны прямоугольника: /rectangle <1 число> <2 число>")
        return
    try:
        length = float(args[0])
        width = float(args[1])
    except ValueError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Вы ввели неверные значения, попробуйте /rectangle <1 число> <2 число>")
        return

    area = length * width
    perimeter = 2 * (length + width)

    text = f"Периметр прямоугольника = {perimeter:.2f}\nПлощадь прямоугольника = {area:.2f}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
def volume(update, context):
    args = context.args
    if len(args) < 1 or len(args) > 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления объема куба скопируйте команду и через пробел введите длину стороны куба: /volume <1 число>")
        return
    try:
        side = float(context.args[0])
        result = side ** 3
        update.message.reply_text(f'Объем куба со стороной {side} = {result}')
    except (IndexError, ValueError):
        update.message.reply_text('Вы ввели неверные значения, попробуйте /volume <1 число>')
def spherevolume(update, context):
    args = context.args
    if len(args) < 1 or len(args) > 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления объёма сферы скопируйте команду и через пробел введите длину радиуса: /spherevolume <1 число>")
        return
    try:
        r = float(context.args[0])
        result = (4 / 3) * math.pi * (r ** 3)
        update.message.reply_text(f"Объем сферы с радиусом {r} равен {round(result, 2)}")
    except (IndexError, ValueError):
        update.message.reply_text("Вы ввели неверные значения, попробуйте /spherevolume <1 число>")
def circle(update, context):
    args = context.args
    if len(args) < 1 or len(args) > 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления площади круга скопируйте команду и через пробел введите длину радиуса: /circle <1 число>")
        return
    try:
        pi = math.pi
        radius = float(context.args[0])
        s = pi * (radius ** 2)
        perimeter = 2 * pi * radius
        update.message.reply_text(f"Площадь круга с радиусом {radius} равна {round(s, 3)}\nПериметр круга равен {round(perimeter, 3)}")
    except (IndexError, ValueError):
        update.message.reply_text("Вы ввели неверные значения, попробуйте /circle <1 число>")


#----Классические--операторы-----
def stepen(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления степени скопируйте команду и через пробел введите число, пробел и значение степень: /stepen <число – возводимое в степень> <значение степени>")
        return
    try:
        num = int(context.args[0])
        sp = int(context.args[1])
        result = num ** sp
        update.message.reply_text(f'число {num} в степени {sp} = {result}')
    except (IndexError, ValueError):
        update.message.reply_text('Вы ввели неверные значения, попробуйте /stepen <<число – возводимое в степень> <значение степени>')
def plus(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления суммы слагаемых скопируйте команду и через пробел введите первое слагаемое, пробел и второе слагаемое: /plus <1 число> <2 число>")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = a + b
        update.message.reply_text(f'число {a} + {b} = {result}')
    except(IndexError, ValueError):
        update.message.reply_text('Вы ввели неверные значения, попробуйте /plus <1 число> <2 число>')
def minus(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления разности чисел скопируйте команду и через пробел введите Уменьшаемое число, пробел и Вычитаемое число: /minus <1 число> <2 число>")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = a - b
        update.message.reply_text(f'{a} - {b} = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /minus <1 число> <2 число>')
def multiply(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления произведения 2х чисел скопируйте команду и через пробел введите первое число, пробел и второе число: /multiply <1 число> <2 число>")
        return
    try: 
        a = int(context.args[0])
        b = int(context.args[1])
        result = a * b
        update.message.reply_text(f'{a} * {b} = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /multiply <1 число> <2 число>')

#----Формулы-----
def sq_sum(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления квадрата суммы (a + b)^2 скопируйте команду и через пробел введите число a, пробел и число b: /sq_sum <число а> <число b >")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a + b) ** 2
        update.message.reply_text(f'({a} + {b})^2 = {a}^2 + 2 * {a}*{b} + {b}^2  = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /sq_sum <число а> < число b >')
def sq_raz(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления квадрата разности (a - b)^2 скопируйте команду и через пробел введите число a, пробел и число b: /sq_raz <число а> <число b>")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a - b) ** 2
        update.message.reply_text(f'({a} - {b})^2 = {a}^2 - 2 * {a}*{b} + {b}^2 = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /sq_min <число а> <число b >')
def difference_of_sq(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления разности квадратов a^2 - b^2 скопируйте команду и через пробел введите число a, пробел и число b: /sq_dif <число а> <число b >")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a + b) * (a - b)
        update.message.reply_text(f'({a} + {b})({a} - {b}) = {a}^2 - {b}^2 =  {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /sq_dif <число а> <число b >')
def densitys(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для вычисления плотности плотности фигуры скопируйте команду и через пробел введите значение массы, пробел и значение радиуса: /densitys < Масса > < Радиус >")
        return
    try:
        mass = float(context.args[0])
        volume = float(context.args[1])
        density = mass / volume
        update.message.reply_text(f"Плотность фигуры с массой {mass} и радиусом {volume} = {density}")
        pass
    except (IndexError, ValueError):
        update.message.reply_text("Вы ввели неверные значения, попробуйте /densitys < Масса > < Радиус >")

def cube_sum(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения куба суммы ( a + b )^3 скопируйте команду и через пробел введите число a, пробел и число b: /cube_sum <число а> <число b >")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a + b) ** 3
        update.message.reply_text(f'({a} + {b})^3 = {a}^3 + 3*{a}^2 * {b} + 3 * {a} * {b}^2 + {b}^4 = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /cube_sum <число а> <число b >')
def cube_raz(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения куба разности ( a − b )^3 скопируйте команду и через пробел введите число a, пробел и число b: /cube_raz <число а> <число b >")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a - b) ** 3
        update.message.reply_text(f'({a} - {b})^3 = {a}^3 + 3*{a}^2 * {b} + 3 * {a} * {b}^2 - {b}^4 = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /cube_raz <число а> <число b >')
def sum_cube(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения суммы кубов a^3 + b^3 скопируйте команду и через пробел введите число a, пробел и число b: /sum_cube <число а> <число b >")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = a ** 3 + b** 3
        update.message.reply_text(f'{a}^3 + {b}^3 = ({a} + {b})({a}^2 - {a}*{b} + {b}^2) =  {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /sum_cube <число а> <число b >')
def raz_cube(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения разности кубов a^3 - b^3 скопируйте команду и через пробел введите число a, пробел и число b: /raz_cube <число а> <число b >")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = a ** 3 - b ** 3 
        update.message.reply_text(f'{a}^3 - {b}^3 = ({a} + {b})({a}^2 + {a}*{b} + {b}^2) = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /raz_cube <число а> <число b >')



def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('square', perimeter))#Периметр
    dp.add_handler(CommandHandler('volume', volume))#обьём
    dp.add_handler(CommandHandler('rectangle', rectangle))#площадь прямоугольника   
    dp.add_handler(CommandHandler('spherevolume', spherevolume))#обьём сферы
    dp.add_handler(CommandHandler('circle', circle))#площадь круга
    dp.add_handler(CommandHandler('densitys', densitys))#плотность
    
    dp.add_handler(CommandHandler('stepen', stepen))#возвести в степень
    dp.add_handler(CommandHandler('plus', plus))#плюс
    dp.add_handler(CommandHandler('minus', minus))#минус
    dp.add_handler(CommandHandler('multiply', multiply))#умножить

    dp.add_handler(CommandHandler('sq_sum', sq_sum))#Квадрат суммы
    dp.add_handler(CommandHandler('sq_min', sq_raz))#Квадрат разности
    dp.add_handler(CommandHandler('sq_dif', difference_of_sq))#Разность квадратов
    dp.add_handler(CommandHandler('cube_sum', cube_sum))#Куб суммы
    dp.add_handler(CommandHandler('cube_raz', cube_raz))#Куб разности
    dp.add_handler(CommandHandler('sum_cube', sum_cube))#Сумма кубов
    dp.add_handler(CommandHandler('raz_cube', raz_cube))#Разность кубов
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

