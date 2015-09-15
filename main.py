#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading, os

def run_server():
    print 'Started server..'
    thread = threading.Thread(target = lambda: os.system('python server.py'))
    thread.start()

def update():
    print 'Started PSI Daemon..'
    os.system("python scrape.py")
    threading.Timer(5,update).start()

if  __name__ == '__main__':
    run_server()
    update()
