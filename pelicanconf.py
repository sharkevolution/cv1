import json

AUTHOR = 'Sitala'
SITENAME = 'CV'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = "resume"
CSS_FILE = 'main-3.css'

# Profile information
NAME = 'Сітала Микола'
TAGLINE = 'Продюсер Digital-проектів'
PIC = 'profile.png'

# sidebar links
EMAIL = 'nsitala@ukr.net'
PHONE = '(+38) 067-569-14-55'
WEBSITE = 'sitala.netlify.app'
LINKEDIN = 'nsitala'
GITHUB = 'sharkevolution'
TWITTER = 'nsitala'


CAREER_SUMMARY_HEAD = 'Профіль'
CAREER_SUMMARY = 'Фахівець у галузі логістики та обробки даних. Маю гарні аналітичні здібності та ' \
'досвід створення унікальних рішень у логістиці, та досвід оцінки вартості володіння ресурсами.' \
'<br> Допомагаю клієнтам із зовнішніми ресурсами, підбирати найбільш підходяще рішення, закриття завдань під ключ, пошук релевантних фахівців для посилення команд.'


SOFT_SKILLS_HEAD = 'Ключові навички'

SOFT_SKILLS = [
    {
        'title': 'Командна праця',
        'level': '90'
    },
    {
        'title': 'Креативність',
        'level': '90'
    },
    {
        'title': 'Аналіз даних',
        'level': '90'
    },
    {
        'title': 'Управління персоналом',
        'level': '90'
    },
]

HARD_SKILLS_HEAD = 'Технічні навички'
HARD_SKILLS = json.dumps({"Python": 4.0,
                          "Jupyter": 4.0,
                          "Django": 3.0,
                          "Sql": 3.0,
                          "Lua": 3.0,
                          "HTML/CSS": 3.0,
                          "BPMN": 4.0,
                          "linux": 3.0
                          })

PROJECT_INTRO = 'Частковий список реалізованих проектів'

PROJECTS_HEAD = 'Проекти'
PROJECTS = [
    {
      'title': 'Сховище даних',
        'tagline': 'Оцінка та розрахунок вартості володіння на періоді 2років (OpEx/CapEx) Data Warehouse | Data Lake.'
    },
    {
        'title': 'Система обліку та планування транспорту',
        'tagline': 'Cтворення БТ та ТЗ, розробка системи обліку та планування на підприємстві з нуля'
    },
    {
        'title': 'Інструменти для роботи з геоданими',
        'tagline': 'Створив з використанням Jupyter інструменти для роботи з геоданими, GPS треками'
    },
    {
        'title': 'Simple Chat',
        'tagline': 'Навички роботи з Django, Channel layers, DRF, JWT. Реалізував простий чат з можливістю використовувати API, створення або видалення, '
                   'статуси повідомлення, останні непрочитані, використаня адмін панели, пагінация',
    },
    {
        'title': 'Telegram Bot',
        'tagline': 'Розробив бот для фіксації часу прибуття товару в точки видачі, з можливістю вибору перевізника, '
                   'міста, часу.'
    },
    {
        'title': 'Система оптимального розкрою матеріалу',
        'tagline': 'Розробив оптимальний алгоритм розкрою штрипсу та додав можливість зміни налаштувань на сайт'
    },
]

LANGUAGES_HEAD = 'Мови'
LANGUAGES = [
    {
        'name': 'Український',
        'description': 'Native'
    },
    {
        'name': 'English',
        'description': 'Intermediate'
    },
    {
        'name': 'Російська',
        'description': 'Native'
    }
]

INTERESTS_HEAD = 'Інтереси'
INTERESTS = [
    'Алгоритми',
    'Метаевристика',
    'Теорія графів',
    'Задача комівояжера',
    'GIS',
    'BigData',
    'Data Mining',
    'Data Warehouse',
    'Web scraping']


EXPERIENCES_HEAD = 'Досвід роботи'
ACHIEVMENTS_HEAD = 'Досягнення'
EXPERIENCES = [
    {
        'job_title': 'Team Lead of Data Engineering',
        'time': '2023 - 2024',
        'company': 'Ferm',
        'details': 'Створення команди з аналізу даних та парсінгу даних з різних джерел (50+); <br>'
                   'Організація ресурсного планування та процесів у команді; <br>'
                    'Впровадження управлінських рішень для досягнення цілей компанії.',

        'achievments': 'Проведено комплекс заходів щодо пошуку та залучення підрядників виконання робіт з розробки сховища даних; <br>'
        'Проведено оцінку та розрахунок вартості володіння Data Warehouse/Data Lake, OpEx/CapEx.'
    },
    {
        'job_title': 'Заступник директора з логістики',
        'time': '2019 - 2022',
        'company': 'Розетка',
        'details': 'Організація та управління магістральними перевезеннями; <br>'
                   'Планування потреб у транспорті; <br>'
                   'Розрахунок рентабельності доставки у регіонах (last mile); <br>'
                   'Формування бізнес-вимог, технічних завдань.',
        'achievments': 'Впроваджено систему вартості підйомів на поверх B2C та розраховано її вартість; <br>'
                    'Проведено оцінку та розрахунок вартості володіння транспортром від 2т до 20т на періоді 5 років; <br>'
    },
    {
        'job_title': 'Начальник відділу',
        'time': '2009 - 2019',
        'company': 'ТОВ БаДМ',
        'details': 'Організація роботи відділу 7чол; <br>'
                   'Оптимізація та облік транспортних витрат, KPI; <br>'
                   'Формування бізнес-вимог, технічних завдань; <br>'
                   'Аналіз, розуміння, розробка систем планування із нуля.',
        'achievments': 'Скорочено витрати на 5% за рахунок створення та впровадження системи обліку та планування транспорту, GPS; <br>'
                    'Реалізована система автоматичного разрахунку витрат без участі людини, скорочено час на 200%'
    },
    {
        'job_title': 'Начальник сектора',
        'time': '2000 - 2009',
        'company': 'ТОВ АТБ-Маркет',
        'details': 'Планування та управління диспетчерською службою 27чол; <br>'
                   'Планування потреби рухомого складу >200од; <br>'
                   'Розробка вимог щодо диспетчеризації; <br>'
                   'Автоматизація розрахунків, розробка алгоритму пошуку найкоротших відстаней.',
        'achievments': 'Впроваджено систему мотивації диспетчерів; <br>'
                   'Скорочено витрати та збільшено обсяги завантаження транспорту на 7%;'
    },
]

EDUCATIONS_HEAD = 'Освіта'
EDUCATIONS = [
    {
        'degree': 'Товарознавство та комерційна діяльність; Облік і аудит',
        'meta': 'Харківський університет харчування та торгівлі',
        'time': '2001 - 2006'
    },
    {
        'degree': 'Компанія SkillsUp',
        'meta': 'Навчання Бізнес аналіз у дії',
        'time': '2018'
    },
    {
        'degree': 'Бізнес тренер Сергей Жарков',
        'meta': 'Бізнес-тренінг «Розвиток управлінських навичок»',
        'time': '2015'
    }
]

EXTRA_HEAD = 'Додатково'

SITEMAP = {
    "format": "xml"
}

if __name__ == '__main__':
    print(CAREER_SUMMARY)