from __future__ import print_function

class MySup(object):
    raw = True
    def __init__(self, rec, args):
        print(rec, rec.field('VAL').fieldinfo())
        self.args = args
        print('VAL', rec.VAL)
    def process(self, rec, reason):
        rec.VAL = rec.VAL+1.3
        print(rec.VAL)
    def detach(self, rec):
        print('test1 detach',rec.name())

def build(rec, args):
    print('test1 build for',rec.name())
    return MySup(rec, args)
