'''
Date: 03/14/2020
Class: CS5541
Assignment: Cache Simulator
Author: Anubhav Rawal
'''

from Cache_block import Cache_block

class Cache:
    #inilize the Cache based on the command line args
    def __init__(self, s, E, b):
        self.E  = E
        self.s = s
        self.b = b
        self.mem = [ [ Cache_block( ) for _ in range(E) ] for __ in range(2**s)]
    
    def load(self, address, program_time):
        s = self.s
        b = self.b
        E = self.E

        #Lets find the tag, set_index and byte offset based on the bitwise operators
        byte_offset = address & ((2**b) - 1) 
        address = address // ((2**b))
        set_index = address & ((2**s) - 1)
        tag = address // ((2**s))

        free_space_count = E # Maximum avilable space will alwasy be number of lines avilable
        avilable_index = -1

        #Look throught the cache for the given set index
        for x in range(E):
            if (self.mem[set_index][x].valid == True):
                if (self.mem[set_index][x].tag == tag):
                    return 1
                else:
                    free_space_count -= 1 
            else:
                avilable_index = x
            
        #No hits??
        #Do we have invalid spaces?
        if free_space_count > 0:
            self.mem[set_index][avilable_index].update(program_time, tag)
            return 0
        
        #NO free space call for eviction
        else:
            self.cache_eviction(tag, set_index, program_time)
            return 2
    
    #Method to evicit the oldest valid information
    def cache_eviction(self, tag, set_index, program_time):
        E = self.E

        oldest_time = program_time
        oldest_index = -1

        #look through the index and search for the oldest time 
        for line in range(0,E):
             #update each variable according if older information is found
            if self.mem[set_index][line].time < oldest_time:
                oldest_index =  line
                oldest_time = self.mem[set_index][line].time
        
        #Updated the information at the oldest index
        self.mem[set_index][oldest_index].update(program_time,tag)