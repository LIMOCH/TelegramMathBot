import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import math
from telegram import KeyboardButton, ReplyKeyboardMarkup
TOKEN = 'token'  # вставьте свой токен

def start(update, context):
    update.message.reply_text('Здравствуйте! Я бот-калькулятор. Я могу помочь найти периметр квадрата, его площадь и объем куба. Введите /help для списка команд.')


def help(update, context):
    update.message.reply_text('Что бы воспользоваться функциями вводите данные так: /команда <первое число> <второе число>. Некоторые функции требуют всего 1 число\n\n/square - найти периметр квадрата\n/volume - найти объем куба\n/rectangle - найти периметр, площадь прямоугольника\n/spherevolume - найти объём сферы\n/circle - найти площадь круга\n/densitys - найти пплотность фигуры\n------------\n/stepen - возвести в степень\n/plus - сложить 2 числа\n/minus - разность 2 чисел\n/multiply - умножить 2 числа\n-------------\n/sq_sum - Квадрат суммы\n/sq_min - Квадрат разности\n/sq_dif - Разность квадратов\n/cube_sum - Куб суммы\n/cube_raz - Куб разности\n/sum_cube - Сумма кубов\n/raz_cube - Разность кубов')

#----геометрические--задачи-----
def perimeter(update, context):
    args = context.args
    if len(args) < 1 or len(args) > 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для данной операции требуеться только 1 число")
        return
    try:
        side = float(context.args[0])
        p = 4 * side
        s = side ** 2
        update.message.reply_text(f'Периметр квадрата со стороной {side} = {p}\nПлощадь квадрата со стороной {side} = {s}')
    except (IndexError, ValueError):
        update.message.reply_text('Вы ввели неверные значения, попробуйте /perimeter <1 число>')
def rectangle(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для данной операции требуеться 2 числа \n1.Длинна 2.Ширина")
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для данной операции требуеться 1 число - длинна 1 стороны куба")
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения объёма сферы требуеться 1 число - радиус")
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения площади круга требуеться 1 число - радиус")
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения степени требуеться 2 числа\n1.Число 2.Степень")
        return
    try:
        num = int(context.args[0])
        sp = int(context.args[1])
        result = num ** sp
        update.message.reply_text(f'число {num} в степени {sp} = {result}')
    except (IndexError, ValueError):
        update.message.reply_text('Вы ввели неверные значения, попробуйте /stepen <1 число> <2 число>')
def plus(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения суммы слагаемых требуеться 2 числа\n1.Первое слагаемое 2.Второе слагаемое")
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения разности чисел требуеться 2 числа\n1.Уменьшаемое 2.Вычитаемое")
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения произведеня чисел требуеться 2 числа\n1.Первый множитель 2.Второй множитель")
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения квадрата суммы требуеться 2 числа\n1.Число 2.Число")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a + b) ** 2
        update.message.reply_text(f'({a} + {b})^2 = {a}^2 + 2 * {a}*{b} + {b}^2  = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /sq_sum <1 число> <2 число>')
def sq_raz(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения квадрата разности требуеться 2 числа\n1.Число 2.Число")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a - b) ** 2
        update.message.reply_text(f'({a} - {b})^2 = {a}^2 - 2 * {a}*{b} + {b}^2 = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /sq_raz <1 число> <2 число>')
def difference_of_sq(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения разности квадратов требуеться 2 числа\n1.Число 2.Число")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a + b) * (a - b)
        update.message.reply_text(f'({a} + {b})({a} - {b}) = {a}^2 - {b}^2 =  {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /difference_of_sq <1 число> <2 число>')
def densitys(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения плотности фигуры требуеться 2 числа\n1.Масса 2.Радиус")
        return
    try:
        mass = float(context.args[0])
        volume = float(context.args[1])
        density = mass / volume
        update.message.reply_text(f"Плотность фигуры с массой {mass} и радиусом {volume} = {density}")
        pass
    except (IndexError, ValueError):
        update.message.reply_text("Вы ввели неверные значения, попробуйте /density <1 число> <2 число>")

def cube_sum(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения куба суммы требуеться 2 числа\n1.Число 2.Число")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = a + b
        update.message.reply_text(f'({a} + {b})^3 = {a}^3 + 3*{a}^2 * {b} + 3 * {a} * {b}^2 + {b}^4 = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /cube_sum <1 число> <2 число>')
def cube_raz(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения куба разности требуеться 2 числа\n1.Число 2.Число")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = (a - b) ** 3
        update.message.reply_text(f'({a} - {b})^3 = {a}^3 + 3*{a}^2 * {b} + 3 * {a} * {b}^2 - {b}^4 = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /cube_raz <1 число> <2 число>')
def sum_cube(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения суммы кубов требуеться 2 числа\n1.Число 2.Число")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = a ** 3 + b** 3
        update.message.reply_text(f'{a}^3 + {b}^3 = ({a} + {b})({a}^2 - {a}*{b} + {b}^2) =  {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /sum_cube <1 число> <2 число>')
def raz_cube(update, context):
    args = context.args
    if len(args) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Для нахождения суммы кубов требуеться 2 числа\n1.Число 2.Число")
        return
    try:
        a = int(context.args[0])
        b = int(context.args[1])
        result = a ** 3 - b ** 3 
        update.message.reply_text(f'{a}^3 - {b}^3 = ({a} + {b})({a}^2 + {a}*{b} + {b}^2) = {result}')
    except:
        update.message.reply_text('Вы ввели неверные значения, попробуйте /raz_cube <1 число> <2 число>')



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

