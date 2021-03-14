from Cache_block import Cache_block

class Cache:
    def __init__(self, s, E, b):
        self.E  = E
        self.s = s
        self.b = b
        self.mem = [ [ Cache_block( ) for _ in range(E) ] for __ in range(2**s)]
    
    def load(self, address, program_time):
        pass