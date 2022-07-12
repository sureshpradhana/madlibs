from sample_madlibs import code,hp,hungargames,theFunPark,zombie,zoo
import random

if __name__== "__main__" :
    r=random.choice([code,hp,hungargames,theFunPark,zombie,zoo])
    r.madlib()

