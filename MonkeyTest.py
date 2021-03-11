# -*- coding:utf-8 -*-

import os
import datetime

now_time = datetime.datetime.now()
nowtime = now_time.strftime('%Y-%m-%d-%H-%M-%S')

cmd = os.system("adb shell monkey -p com.zzkko --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 1000 -v -v 500 > E:\\monkeyLog\\monkeyLogs\\"+nowtime+"Monkey_log.txt")
