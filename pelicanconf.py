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
TAGLINE = 'Заместитель директора'
PIC = 'profile.png'

# sidebar links
EMAIL = 'nsitala@ukr.net'
PHONE = '(+38) 067-569-14-55'
WEBSITE = 'sitala.netlify.app'
LINKEDIN = 'nsitala'
GITHUB = 'sharkevolution'
TWITTER = 'nsitala'

CAREER_SUMMARY_HEAD = 'Профиль'
CAREER_SUMMARY = 'I am a full-stack developer currently working as a software developer at Zomato. I am a Google Summer of Code mentor for CLTK. I also participated in GSoC last year as a student. I have also worked at Aspiring Minds and various other startups mainly working on Web and Android.'

SOFT_SKILLS_HEAD = 'Навыки'

SOFT_SKILLS = [
    {
        'title': 'Управление',
        'level': '90'
    },
    {
        'title': 'Работа в команде',
        'level': '100'
    },
    {
        'title': 'Креативность',
        'level': '80'
    },
    {
        'title': 'Анализ',
        'level': '100'
    },
]

HARD_SKILLS_HEAD = 'Технические навыки'
HARD_SKILLS = json.dumps({"Python": 4.0,
                          "Jupyter": 4.0,
                          "Sqlite": 3.0,
                          "Excel": 5.0,
                          "VBA": 4.0,
                          "BPMN": 4.0
                          })

PROJECT_INTRO = 'You can list your side projects or open source libraries in this section. '

PROJECTS_HEAD = 'Проекты'
PROJECTS = [
    {
        'title': 'Open Source Contributions',
        'tagline': 'Active contributor in FOSSASIA, worked on the Open Event project (both server and android app).Active contributor in CLTK, worked on the CLTK Web app and API.Made valuable contributions in phpBB, implemented a live search feature.Also made a few contributions to Processing.org and phpMyAdmin.'
    },
    {
        'title': 'Music Hub',
        'tagline': 'Android app that connects multiple devices via wifi and plays music in all connected devices simultaneously to create a loud stereo-like sound effect.'
    },
    {
        'title': 'Music Timer',
        'tagline': 'Android app that monitors phone’s movement to detect whether the user’s asleep and pause music playback accordingly.'
    }
]

LANGUAGES_HEAD = 'Языки'
LANGUAGES = [
    {
        'name': 'Украинский',
        'description': 'Native'
    },
    {
        'name': 'English',
        'description': 'Professional'
    },
    {
        'name': 'Русский',
        'description': 'Amateur'
    }
]

INTERESTS_HEAD = 'Интересы'
INTERESTS = [
    'Метаэвристика',
    'Теория графов',
    'Задача коммивояжера',
    'GIS',
    'BigData',
    'Data Mining']


EXPERIENCES_HEAD = 'Опыт работы'
ACHIEVMENTS_HEAD = 'Достижения'
EXPERIENCES = [
    {
        'job_title': 'Software Development Engineer',
        'time': 'Oct 2016 - Present',
        'company': 'Zomato, Gurgaon IN',
        'details': 'Part of the web team working on developing a smart POS system for restaurants.',
        'achievments': 'ok'
    },
    {
        'job_title': 'Web developer',
        'time': 'Aug 2016 - Dec 2016',
        'company': 'Archimedes Digital, WFH',
        'details': 'Worked on developing an online catalog for museums using scans of various objects (artifacts, books etc). Developed a highly zoomable image viewer and integrated linting and test suites to be used across projects.',
        'achievments': 'ok'
    },
    {
        'job_title': 'Google Summer of Code Student',
        'time': 'May 2016 - Aug 2016',
        'company': 'Classical Language Toolkit (CLTK), WFH',
        'details': 'Worked on the CLTK webapp - a modern reading environment to study classical languages. Updated the webapp to provide definitions, translations and commentary along with the text. Added functionality to add annotations and bookmarks to enhance the reading experience for user. Working on extending user profile to include annotations, bookmarks and other social networks.',
        'achievments': 'ok'
    },
    {
        'job_title': 'Research and Development Intern',
        'time': 'May 2015 - June 2015',
        'company': 'Aspiring Minds, Gurgaon IN',
        'details': 'Developed a CRM-simulation module integrated into the employability assessment platform AMCAT. Created the frontend for the module and wrote backend code for question delivery and scoring. Designed the database schemas for the module compatible with the current platform’s database.',
        'achievments': 'ok'
    }
]

EDUCATIONS_HEAD = 'Образование'
EDUCATIONS = [
    {
        'degree': 'B.E in Information Technology',
        'meta': 'Netaji Subhas Institute of Technology (NSIT)',
        'time': '2012 - 2016'
    },
    {
        'degree': 'High School',
        'meta': 'Ludlow Castle',
        'time': '2012'
    }
]

EXTRA_HEAD = 'Дополнительно'

SITEMAP = {
    "format": "xml"
}
