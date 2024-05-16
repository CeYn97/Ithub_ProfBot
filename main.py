import telebot
from telebot import types
from flask import Flask, request, jsonify, make_response
import time
import datetime

secret = "d484237c-d2d5-408c-813b-cd3abedebadf"
bot_token = '7199097467:AAFXHjxqTOwPg-yZ3p2yxzZsY3b6yLL9xk4'

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url="https://IThubProfBot.pythonanywhere.com/{}".format(secret))

app = Flask(__name__)

question1 = {
    'question': 'Вы видите мощную дорогую машину, на что вы обращаете внимание прежде всего?',
    'importance': 0.65,
    'options': [
        {
            'text': 'А) На ее внешний вид, колёса, диски, цвет, плавность\мощность движения.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Думаете о том, какие же у нее могут быть характеристики мощности, количество л.с, объем двигателя, привод.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'В) Думаете, как же круто было бы поскорее сесть за руль, или прокатиться с друзьями на ней, подъехать красиво к дому за другом\парней\девушкой.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question2 = {
    'question': 'При выборе одежды для вас важнее:',
    'importance': 0.65,
    'options': [
        {
            'text': 'А) Сочетание цветов, ткань, как одежда на вас сидит.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Думаете куда в такой одежде вы будете ходить, универсальна ли она или для неё нужно особое мероприятие.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Насколько она будет подходить под погоду, будет теплой, насколько она будет тянущейся и прочной.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question3 = {
    'question': 'Всем нужно как-то поучаствовать в жизни школы, что для тебя ближе?',
    'importance': 0.8,
    'options': [
        {
            'text': 'А) Буду играть в КВН, придумывать шутки, ставить номера.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Буду делать Стенгазету.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Постараюсь поучаствовать в олимпиаде по математике, чтобы потом получить «отлично» по предмету.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question4 = {
    'question': 'Если будешь делать Ютуб канал, то:',
    'importance': 0.5,
    'options': [
        {
            'text': 'А) Сначала организую студию.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Буду делать видео с картинкой и закадровым голосом.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Прочитаю всё по теме, изучу всё, что есть в интернете по этому вопросу.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question5 = {
    'question': 'Выбери утверждение, которое больше тебя характеризует:',
    'importance': 0.9,
    'options': [
        {
            'text': 'А) Я – и есть творчество, не могу терпеть инструкций, буду делать на потоке энергии.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Буду действовать чётко по плану, старательно выполняя каждый пункт.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Разберусь как делать сам, если не пойму, то спрошу у друзей.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question6 = {
    'question': 'При выборе работы:',
    'importance': 0.65,
    'options': [
        {
            'text': 'А) Постараюсь заниматься тем, где мне не будут указывать, где я смогу спокойно творить.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Выберу работу, где понятна моя зона ответственности и чёткие правила.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Выберу работу, где буду руководить.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question7 = {
    'question': 'Выбери утверждение, которое тебе подойдёт:',
    'importance': 0.5,
    'options': [
        {
            'text': 'А) Рисую в свободное время, это то, что я люблю и умею.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) На ИЗО я вызывался первым помочь, когда приходили за «крепкими парнями», чтобы донести парты.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Могу порисовать, если в хорошей компании.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question8 = {
    'question': 'В детстве я любил:',
    'importance': 0.8,
    'options': [
        {
            'text': 'А) Делать подарки другим.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Собирать конструктор и играть в шахматы.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Тусоваться с друзьями во дворе.',
            'category': 'Ваше направление маркетинг: '
        }
    ]
}

question9 = {
    'question': 'Если бы сейчас предложили выбрать подарок:',
    'importance': 0.65,
    'options': [
        {
            'text': 'А) Выбрал бы графический планшет.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Крутые часы, деньги.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Клёвый онлайн-курс по тому, что тебя увлекает.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question10 = {
    'question': 'Выбери утверждение, которое тебе ближе:',
    'importance': 0.65,
    'options': [
        {
            'text': 'А) Люблю, когда в приложение или на сайте магазина всё красиво оформлено.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Главное, что всё быстро прогружалось и работало.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Бывает по-разному, порой дизайн не важен.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question11 = {
    'question': 'Какой бы вид отдыха выбрал:',
    'importance': 0.5,
    'options': [
        {
            'text': 'А) Встретиться с друзьями всегда и в любое время.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Люблю смотреть красивое кино, можно сходить в театр или музей на новую выставку.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Обожаю играть на приставке, планшете, компьютере.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

question12 = {
    'question': 'На тусовке с друзьями ты:',
    'importance': 0.9,
    'options': [
        {
            'text': 'А) Находишься в центре компании, рассказываешь истории, смеешься.',
            'category': 'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },
        {
            'text': 'Б) Разговариваешь с одним или двумя друзьями в стороне на конкретные темы, которые тебя волнуют.',
            'category': 'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        },        
        {
            'text': 'В) Предпочитаешь сидеть в телефоне, в переписке рассказывать, как тебе на этой вечеринке.',
            'category': 'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub'
        }
    ]
}

questions = [question1, question2, question3, question4, question5, question6, question7, question8, question10, question11, question12]

user_answers = {}

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('Пройти тест'))
    bot.send_message(
        message.chat.id,
        "Я - виртуальный студент колледжа IThub 👋🏼\n \nГотов ли пройти тест, чтобы узнать специальность, которая тебе ближе ?🤗",
        reply_markup=markup,
    )
    user_id = message.chat.id
    user_answers[user_id] = {
        'Ваше направление маркетинг:\n \nПрофессия для инициативных и предприимчивых. Начни зарабатывать, запуская и продвигая проекты в интернете! Ты изучишь маркетинг в разных его аспектах, раскроешь в себе потенциал лидера и овладеешь технологиями продвижения.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub': 0,
        'Ваше направление дизайн:\n \nСпециальность для визуалов, готовых творить в цифровой среде и создавать продукты, учитывающие потребности и желания пользователей. Монетизируй свою креативность и стань востребованным специалистом диджитал-сферы!\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub': 0,
        'Ваше направление кодинг:\n \nПрофессия будущего, способная изменить мир! Разрабатывай программы, сервисы и приложения, которые будут служить людям. Программисты пишут код для ПО, анализируют данные, обучают машины.\n \nЕсли хочешь узнать больше - напишите менеджеру: https://t.me/SPb_Ithub': 0,
        'index': 0
    }
    

@bot.message_handler(func=lambda message: message.text == "Пройти тест")   
def send_question(message):
    user_id = message.chat.id
    question_index = user_answers[user_id]['index']
    user_answers[user_id]['index'] += 1

    question = questions[question_index]
    options = question['options']

    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    markup.add(telebot.types.KeyboardButton('A'))
    markup.add(telebot.types.KeyboardButton('B'))
    markup.add(telebot.types.KeyboardButton('C'))


    message = question['question'] + '\n\n' + '\n\n'.join(option['text'] for option in options)

    bot.send_message(user_id, message, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    user_id = message.chat.id
    question_index = user_answers[user_id]['index'] - 1

    options = questions[question_index]['options']

    option_ix = 'ABC'.index(message.text)
    category = options[option_ix]['category']

    user_answers[user_id][category] += questions[question_index]['importance']

    if user_answers[user_id]['index'] < len(questions):
        send_question(message)
    else:
        show_result(user_id)

def show_result(user_id):
    user_responses = user_answers[user_id] 
    result = calculate_result(user_responses) 
    
    bot.send_message(user_id, f"{result}", reply_markup=types.ReplyKeyboardRemove())


def calculate_result(responses):
    max_result = sorted(responses.items(), key=lambda x: x[1], reverse=True)
    return max_result[1][0]


bot.polling()