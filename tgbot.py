from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

start_text = '''Приветствую! Я ваш помощник по идену. В данный момент я могу снабдить вас гайдами на выбор спавна в 
рангах, правилами игры в блэкджэк и другие режимы, а также некоторыми сборками, которые делал вайт для персонажей. 
Приятного пользования!'''

help_text = '''Список команд:
/help - отображает список команд
/blackjack - показывает правила игры в блэкджэк
/genshin - отображает свежию информацию о 
/bd_team - информация о нас
/spawn - главные правила выбора спавна
/top - главная мета идена(мы)'''

blackjack_rules = '''В начале игры вы выбираете Выжившего, а Охотником становится один из игроков по ходу игры.
Игроки получат карты из колоды, в том числе проклятую карту, карты с очками атаки, помощи и бегства.
Каждый ход начинается с того, что игрок с наибольшим количеством очков проклятий становится Охотником и начинает 
преследование Выживших. Успешная атака Охотника передаёт свои проклятия Выжившему.
Если у вас проклятых очков больше 21, то вы превращаетесь в игральную карту и выходите из игры, отправляясь в Особняк.
Условия победы:
Набирайте не более 21 очка проклятия, чтобы выжить и выиграть игру.
Наберите 21 очко и удерживайте это число до конца раунда, чтобы уничтожить проклятие и победить.'''

bd_team_members = '''Наша команда постоянно растет, но основные ее члены - это:
    BD|white - наш отец и создатель, главный про идена. Его контрит только пинг и китайцы (что в идене одно и то же).
    BD|Icelegenda - сова сова сова
    BD|Ivydio - просто наш худший кошмар на ханте. Сложно сказать что страшнее: она на Наяде или Ися на Андеде. 
    BD|Kora - наша мама, ее стоит бояться и уважать!
    BD|neoffew - нео. просто нео. иногда кирпич. он юный физматик.
    BD|ГPEШHИK - с кем не бывает...'''


def start(update, context):
    update.message.reply_text(start_text)


def help(update, context):
    update.message.reply_text(help_text)


def blackjack(update, context):
    update.message.reply_text(blackjack_rules)


def genshin(update, context):
    update.message.reply_text('ГЕНШИН НЕ ИГРА, ПИКСЕЛИ - ЭТО ЛОЖЬ')


def bd_team(update, context):
    update.message.reply_text(bd_team_members)


def spawn(update, context):
    update.message.reply_text('Спасатель на миду, декодер под защитой кайтеров')


def top(update, context):
    update.message.reply_text('Мета идена:\nSeer,\nPriestess,\nProfessor,\nGrave Keeper,\nToy Merchant,\nBarmaid')


def answer(update, context):
    update.message.reply_text(update.message.text +
                              ' не является командой. Наберите /help, чтобы получить список команд')


updater = Updater("7108975513:AAGgiKsUmgsRYq_RJs9liqj4CVhjV1Vvtk4")

dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('blackjack', blackjack))
dp.add_handler(CommandHandler('genshin', genshin))
dp.add_handler(CommandHandler('bd_team', bd_team))
dp.add_handler(CommandHandler('spawn', spawn))
dp.add_handler(CommandHandler('top', top))

text_handler = MessageHandler(Filters.text, answer)
dp.add_handler(text_handler)

updater.start_polling()
updater.idle()