# Cache_sim

python3 csim.py -E 1 -s 4  -b 4 -t trace/dave.trace

# Test cases:

```
Linux> python3 csim.py -s 1 -E 1 -b 1 -t trace/yi2.trace
Linux> python3 csim.py -s 4 -E 2 -b 4 -t trace/yi.trace
Linux> python3 csim.py -s 2 -E 1 -b 4 -t trace/dave.trace
Linux> python3 csim.py -s 2 -E 1 -b 3 -t trace/trans.trace
Linux> python3 csim.py -s 2 -E 2 -b 3 -t trace/trans.trace
Linux> python3 csim.py -s 2 -E 4 -b 3 -t trace/trans.trace
Linux> python3 csim.py -s 5 -E 1 -b 5 -t trace/trans.trace
Linux> python3 csim.py -s 5 -E 1 -b 5 -t trace/long.trace

```