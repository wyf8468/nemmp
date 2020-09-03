# --^_^-- coding:utf-8 --^_^--
# @Remark:日志模块

import logging
from logging.handlers import TimedRotatingFileHandler
import datetime
from nmmp_manage.common import dir_config

fmt = "%(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
# 获取当前时间
now_time = datetime.datetime.now().strftime('%Y-%m-%d')
# 把当前时间转换成str
now_time_str = str(now_time)

handler_1 = logging.StreamHandler()
handler_2 = TimedRotatingFileHandler(dir_config.logs_dir + "/" + now_time_str + "_Web.log",
                                     when='D',
                                     interval=10,
                                     backupCount=0,
                                     encoding='utf-8')

# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])