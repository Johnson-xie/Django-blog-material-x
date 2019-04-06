"""
Django settings for www project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nrnen$7n$+(sm7qtu808qryubv$0)x$)y3)w9-84s)_#cjr2(l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['localhost','.bgods.cn','bgods.cn']
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog.apps.BlogConfig', # 注册blog应用
    'ckeditor', # 注册富文本编辑器
    'ckeditor_uploader', # 文件上传
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'www.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'www.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, "static") # 部署时用

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
   '/var/www/static/',
]

MEDIA_URL = '/media/'
# 放在django项目根目录，同时也需要创建media文件夹
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 富文本CKEDITOR插件上传文件存放位置
CKEDITOR_UPLOAD_PATH = 'upload/'
# 富文本CKEDITOR插件工具栏配置
CKEDITOR_CONFIGS = {
    # 配置名是default时，django-ckeditor默认使用这个配置
    'default': {
        # 使用简体中文
        'language':'zh-cn',
        # 编辑器的宽高请根据你的页面自行设置
        'width':'auto',
        'height':'500px',
        'image_previewText':' ',
        'tabSpaces': 4,
        'toolbar': 'Custom',
        # 添加按钮在这里
        'toolbar_Custom': [
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'CodeSnippet'],
        ],
        # 插件
        'extraPlugins': ','.join(['codesnippet','uploadimage','prism','widget','lineutils',]),
    }
}



# 站点配置
SITE_CONFIGS = {
    'Name': 'Bgods', # 站点名称
    'Title': '人生苦短,我用Python', # 站点标题

    # 站点底部footer配置
    'Footer': {
        'Email': 'bgods@qq.com', # 邮箱
        'Weibo': 'http://weibo.com/songzhilian22', # 新浪微博
        'Music': 'https://music.163.com/#/user/home?id=1534745920', # 音乐地址
        'Twitter': 'http://blog.csdn.net/songzhilian22', # Twitter
        'GitHub': 'https://github.com/Bgods', # GitHub
        'Beian': '粤ICP备17050010号', # 备案号
    },

    # 侧边栏网易云音乐插件配置
    'Music': {
        'home': 'https://music.163.com/#/user/home?id=1534745920', # 网易云用户主页，点击会跳转到你的主页
        'id': '2700450552', # 播放歌单id，获取方法自行百度。比如我的id就是链接后面的id，https://music.163.com/#/playlist?id=2700450552
    },

    # 第三方评论Gitalk插件配置，关于下面的参数获取自己百度：(参考链接:https://www.jianshu.com/p/78c64d07124d)
    'Gitalk': {
        'clientID': '*************', # Github Application clientID
        'clientSecret': '*************', # Github Application clientSecret
        'repo': '*************', # 存储你评论 issue 的 Github 仓库名
        'owner': '*************', # Github 用户名
        'admin': '*************', # Github 用户名
    },

    # 百度统计,代码获取方法自行百度,不需要的话可以留空
    'BaiduTj': '''
    <script>
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?*************";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();
    </script>''',

}