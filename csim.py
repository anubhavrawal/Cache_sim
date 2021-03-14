import sys
import numpy as np

import struct

from Cache import Cache

def usage():
    print('Usage: python3 cache2.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>')
    print("-h: Optional help flag that prints usage info")
    print("-v: Optional verbose flag that displays trace info")
    print("-s <s>: Number of set index bits (S = 2 s is the number of sets)")
    print("-E <E>: Associativity (number of lines per set)")
    print("-b <b>: Number of block bits (B = 2 b is the block size)")
    print("-t <tracefile>: Name of the valgrind trace to replay")


def main():
    program_time = 0
    try:
        fname = sys.argv[ sys.argv.index('-t') + 1]
    
    except:
        print('Usage: python3 cache2.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>')
        return

    # ./csim-ref -E 1 -s 4  -b 4 -t traces/yi.trace

    h = False
    v = False
    s = None
    E = None
    b = None

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
        
        

    if h == True:
        usage()
        return
    
    if v == True:
        print('Print everything!!')

    if (s == None) or (E == None) or (b == None):
        usage()
        return
    
    
    tmp = Cache(s,E,b)

    hme_count = [0,0,0]

    try:
        with open(fname, 'r') as trace:
            trace_vals = trace.readlines()

    except:
        print("Sorry! Invalid file was supplied!")
        usage()
        return


    for command in trace_vals:

        if command == '\n':
            break

        tmp_trace = command.split(' ')
        program_time += 1


        if tmp_trace[0] == '':
            instruction =  tmp_trace[1]
        else:
            instruction =  tmp_trace[0]


        address = int(tmp_trace[-1].split(',')[0], base =16)

        print(str(instruction), str(hex(address))[2:] +str(command[-3:-1]))

    
    print("hits:", hme_count[0] ,"misses", hme_count[1] ,"evictions:", hme_count[2])


if __name__ == '__main__':
    main()
