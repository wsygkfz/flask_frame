# -*- coding: UTF-8 -*- 
'''
Created on 2016-7-7

@author: yuzhongfu
'''


import os

import time

              
def start():

    str_find_process = "ps -ef | grep 'uwsgi taryuapi.ini'"
    os.system(str_find_process)

    str_kill_process = "ps -ef | grep 'uwsgi taryuapi.ini' |awk '{print $2}'| xargs kill -9"
    os.system(str_kill_process)
    time.sleep(0.1)

    str_start_process = "uwsgi taryuapi.ini"
    os.system(str_start_process)
    time.sleep(1)

    os.system(str_find_process)

if __name__ == '__main__':
    
    start()




