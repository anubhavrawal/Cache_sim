'''
Date: 03/14/2020
Class: CS5541
Assignment: Cache Simulator
Author: Anubhav Rawal

'''
import sys
import numpy as np

from Cache import Cache

#prints usage
def usage():
    print('Usage: python3 cache2.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>')
    print("-h: Optional help flag that prints usage info")
    print("-v: Optional verbose flag that displays trace info")
    print("-s <s>: Number of set index bits (S = 2 s is the number of sets)")
    print("-E <E>: Associativity (number of lines per set)")
    print("-b <b>: Number of block bits (B = 2 b is the block size)")
    print("-t <tracefile>: Name of the valgrind trace to replay")

#Calls the load method and incremetn the hit miss and eviction counter based on the return
#value
def selection(flow, hme_count):
    flag = ''

    if(flow == 1):
        flag = 'hit'
        hme_count[0] +=1
    
    elif (flow == 0):
        flag = 'miss'
        hme_count[1] +=1
    
    elif (flow == 2):
        flag = "miss eviction"
        hme_count[1] +=1
        hme_count[2] +=1
    
    return hme_count, flag

#Driver function
def main():
    program_time = 0

    # ./csim-ref -E 1 -s 4  -b 4 -t traces/yi.trace

    #input flags set to deafult
    h = False
    v = False
    s = None
    E = None
    b = None

    #Pasrse the command line args and assign respective values
    for _e in range(len(sys.argv)):
        try: 
            if sys.argv[_e] == '-h':
                h = True
                break

            elif sys.argv[_e] == '-v':
                v = True

            elif sys.argv[_e] == '-s':
                s = int( sys.argv[_e +1]) 

            elif sys.argv[_e] == '-E':
                E =  int (sys.argv[_e +1])

            elif sys.argv[_e] == '-b':
                b = int ( sys.argv[_e +1] )
        
        except:
            usage()
            return
        
    #If help then just print usage
    if h == True:
        usage()
        return

    #If not enough arguments print usage
    if (s == None) or (E == None) or (b == None):
        usage()
        return
    
    try:
        fname = sys.argv[ sys.argv.index('-t') + 1]
    
    except:
        print("Bad File Name")
        usage()
        return
    
    #cache initilizer
    cache = Cache(s,E,b)

    hme_count = [0,0,0] #hit,miss,eviction counter initilized to all zeros

    #attempt to open the file
    try:
        with open(fname, 'r') as trace:
            trace_vals = trace.readlines()

    except:
        print("Bad File Name")
        usage()
        return


    for command in trace_vals:

        program_time += 1 # Increase the program time for each new line

        if command == '\n':
            break

        tmp_trace = command.split(' ')
        

        if tmp_trace[0] == '':
            instruction =  tmp_trace[1]
        else:
            instruction =  tmp_trace[0]

        address = int(tmp_trace[-1].split(',')[0], base =16) #Extracting the hex

        #Call the load method based on the instruction demands
        # Instruction I is being ignored
        if instruction == "L" or instruction == "S":
            hme_count, hme_flag =  selection(cache.load( address, program_time), hme_count)

            #Print only on the case of verbosity
            if v == True:
                 print(str(instruction), str(hex(address))[2:] +str(command[-3:-1]), hme_flag)
            
        elif instruction == "M":
            hme_count, hme_flag_1 =  selection(cache.load( address, program_time), hme_count)
            hme_count, hme_flag_2 =  selection(cache.load( address, program_time), hme_count)

            #Print only on the case of verbosity
            if v == True:
                 print(str(instruction), str(hex(address))[2:] +str(command[-3:-1]), hme_flag_1, hme_flag_2)
            

    print("hits:"+ str(hme_count[0]) ,"misses:"+ str(hme_count[1]) ,"evictions:"+ str(hme_count[2]))


if __name__ == '__main__':
    main()
