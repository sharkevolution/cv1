import json

AUTHOR = 'Sitala'
SITENAME = 'CV'

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'Russian'

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
NAME = 'Ситала Николай'
TAGLINE = 'junior Python developer'
PIC = 'profile.png'

# sidebar links
EMAIL = 'nsitala@ukr.net'
PHONE = '(+38) 067-569-14-55'
WEBSITE = 'sitala.netlify.app'
LINKEDIN = 'nsitala'
GITHUB = 'sharkevolution'
TWITTER = 'nsitala'

CAREER_SUMMARY_HEAD = 'Профиль'
CAREER_SUMMARY = 'Имею опыт некоммерческой разработки на Python. Использую Jupyter, Heroku, QGIS, telegram api. ' \
                 'Имею хорошие аналитические способности, написание БТ и ТЗ, создание транспортных учетных систем. ' \
                 'Быстро обучаюсь, стремлюсь стать частью профессиональной команды, ' \
                 'в которой я мог бы развивать свои навыки для достижения командных результатов. ' \
                 'Накопленный опыт привел к желанию сменить сферу деятельности.'


SOFT_SKILLS_HEAD = 'Ключевые навыки'

SOFT_SKILLS = [
    {
        'title': 'Работа в команде',
        'level': '100'
    },
    {
        'title': 'Креативность',
        'level': '80'
    },
    {
        'title': 'Анализ данных',
        'level': '100'
    },
    {
        'title': 'Управление персоналом',
        'level': '90'
    },
]

HARD_SKILLS_HEAD = 'Технические навыки'
HARD_SKILLS = json.dumps({"Python": 4.0,
                          "Jupyter": 4.0,
                          "Sql": 3.0,
                          "Lua": 3.0,
                          "HTML": 3.0,
                          "CSS": 2.0,
                          "BPMN": 4.0,
                          "linux": 3.0
                          })

PROJECT_INTRO = 'Частичный список реализованных проектов'

PROJECTS_HEAD = 'Проекты'
PROJECTS = [
    {
        'title': 'Telegram Bot',
        'tagline': 'Разработал бот для фиксации времени прибытия товара в точки выдачи, с возможностью выбора перевозчика, города, времени'
    },
    {
        'title': 'Система оптимального раскроя материала',
        'tagline': 'Разработал оптимальный алгоритм раскроя штрипса и добавил возможность изменения настроек на сайт'
    },
    {
        'title': 'Инструменты для работы с геоданными',
        'tagline': 'Создал с использованием Jupyter инструменты для работы с геоданными'
    },
    {
        'title': 'Система учета и планирования транспорта',
        'tagline': 'Участвовал в создании, написании, разработке системы учета и планирования на предприятии с нуля'
    },
]

LANGUAGES_HEAD = 'Языки'
LANGUAGES = [
    {
        'name': 'Украинский',
        'description': 'Native'
    },
    {
        'name': 'English',
        'description': 'Intermediate'
    },
    {
        'name': 'Русский',
        'description': 'Native'
    }
]

INTERESTS_HEAD = 'Интересы'
INTERESTS = [
    'Алгоритмы',
    'Метаэвристика',
    'Теория графов',
    'Задача коммивояжера',
    'GIS',
    'BigData',
    'Data Mining',
    'Love2D framework']


EXPERIENCES_HEAD = 'Опыт работы'
ACHIEVMENTS_HEAD = None  # 'Достижения'
EXPERIENCES = [
    {
        'job_title': 'Заместитель директора по логистике',
        'time': '2019 - 2022',
        'company': 'Розетка',
        'details': 'Организация и управление магистральными перевозками; <br>'
                   'Планирование потребности в транспорте; <br>'
                   'Оценка и расчет стоимости владения транспортром 2т, 5т, 20т; <br>'
                   'Расчет рентабельности доставки в регионах (last mile); <br>'
                   'Расчет стоимости подъемов на этаж B2C; <br>'
                   'Формирование бизнес требований, технических заданий.',
        'achievments': 'ok'
    },
    {
        'job_title': 'Начальник отдела',
        'time': '2009 - 2019',
        'company': 'ООО БаДМ',
        'details': 'Организация работы отдела 7чел; <br>'
                   'Оптимизация и учет транспортных затрат, KPI; <br>'
                   'Сокращены затраты на 5% за счет создания и внедрения системы учета и планирования транспорта, GPS; <br>'
                   'Формирование бизнес требований, технических заданий; <br>'
                   'Анализ, понимание, разработка систем планирования с нуля.',
        'achievments': 'ok'
    },
    {
        'job_title': 'Начальник сектора',
        'time': '2000 - 2009',
        'company': 'ООО АТБ-Маркет',
        'details': 'Внедрение системы мотивации диспетчеров; <br>'
                   'Увеличены объемы загрузки транспорта на 7%; <br>'
                   'Планирование и управление диспетчерской службой 27чел; <br>'
                   'Планирование потребности подвижного состава >200ед; <br>'
                   'Разработка требований к диспетчеризации; <br>'
                   'Автоматизация расчетов, разработка алгоритма поиска кратчайших расстояний.',
        'achievments': 'ok'
    },
]

EDUCATIONS_HEAD = 'Образование'
EDUCATIONS = [
    {
        'degree': 'Товароведение и коммерческая деятельность; Учет и Аудит',
        'meta': 'Харьковский университет питания и торговли',
        'time': '2001 - 2006'
    },
    {
        'degree': 'Компания SkillsUp',
        'meta': 'Обучение Бизнес анализ в действии',
        'time': '2018'
    },
    {
        'degree': 'Бизнес-тренер Сергей Жарков',
        'meta': 'Бизнес-тренинг «Развитие управленческих навыков»',
        'time': '2015'
    }
]

EXTRA_HEAD = 'Дополнительно'

SITEMAP = {
    "format": "xml"
}
