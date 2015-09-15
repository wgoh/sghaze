#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading, os, sys

def run_server(target):
    print 'Started server..'
    thread = threading.Thread(target = lambda: os.system('python server.py ' + target))
    thread.start()

def update():
    print 'Started PSI Daemon..'
    os.system("python scrape.py")
    threading.Timer(60 * 15,update).start()

if  __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) == 2 else ''
    run_server(target)
    update()
