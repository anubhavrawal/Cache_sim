'''
Date: 03/14/2020
Class: CS5541
Assignment: Cache Simulator
Author: Anubhav Rawal

'''
class Cache_block:
    def __init__(self):
        self.time = 0
        self.valid = False
        self.tag = None

    def update(self, time, tag):
        self.time= time
        self.tag = tag
        self.valid = True