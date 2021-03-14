import sys
import numpy as np

from Cache import Cache


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
            print('Usage: python3 cache2.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>')
            return
        
        

    if h == True:
        print('Usage: python3 cache2.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>')
        return
    
    if v == True:
        print('Print everything!!')

    if (s == None) or (E == None) or (b == None):
        print("Insufficent variables!!!")
        print('Usage: python3  cache2.py [-hv] -s <s> -E <E> -b <b> -t <tracefile>')
        return
    
    
    tmp = cache(s,E,b)

    hme_count = [0,0,0]

    try:
        with open(fname, 'r') as trace:
            trace_vals = trace.readlines()

    except:
        print("Invalid file!!!!!")
        return

    
    print("Hit:", hme_count[0] ," Miss", hme_count[1] ," eviction:", hme_count[2] )


if __name__ == '__main__':
    main()
