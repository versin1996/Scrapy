# -*- coding: utf-8 -*-

# Scrapy settings for bianju project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bianju'

SPIDER_MODULES = ['bianju.spiders']
NEWSPIDER_MODULE = 'bianju.spiders'

COOKIE = {'UserIC': '182%2E142%2E35%2E172%2D20200708110033', 'UM_distinctid': '1732c5e1f91827-0f5fdf5a784653-4353761-144000-1732c5e1f92c6b', 'utype': '%C6%E4%CB%FB', 'username': 'versin', 'password': '0761c8bb76093e45', 'iReadArtID': '%2D27%2D', 'vipnum': '0', 'yname': '%CD%FE%C9%AD', 'RememberMe': 'ok', 'UserEduType': '', 'IfZhuanye': '', 'company': '', 'IfLockGb': '', 'ifpartner': '', 'enddate': '', 'ifvip': '', 'ASPSESSIONIDSQETSRDD': 'CONAHDNDCKAKFMDEPPAHPKPH', 'CNZZDATA2878103': 'cnzz_eid%3D282836955-1594176557-%26ntime%3D1594367720', 'CNZZDATA1274624805': '1020660856-1594175226-%7C1594367737', 'lastIP': '182%2E142%2E35%2E172', 'ComTitle': '', 'ifpass': '0', 'bname': 'versin', 'UID': 'C20200710277680988', 'lastlogin': '2020%2F7%2F10+17%3A00%3A32', 'lastlogintime': '2020%2F7%2F10+17%3A00%3A32', 'UserID': '100981', 'face': '%2Fimg%5Fuserface%2Fdefault%2Dboy%2Fboy6%2Epng', 'LoginOK': '1bianju%2Ecom', 'loginnum': '6', 'ifpass%5Femail': '1', 'CurrentBannerNo': '2', 'ComeUrl': 'http%3A%2F%2Fwww%2E1bianju%2Ecom%3A443%2FArt%5Flist%2Easp%3Fid%3D27%26CType%3Dcontent', 'BannerOrderID%5FLast': '1%2E5', 'ReadADID': '5', 'ReadADID2': '5', 'ViewPages': '28'}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bianju (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARN'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 30
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bianju.middlewares.BianjuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bianju.middlewares.BianjuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'bianju.pipelines.BianjuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
