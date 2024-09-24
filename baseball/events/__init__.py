import numpy as np

class SimpleEventGenerator:
    def __init__(self):
        pass

    def generateEvent(self, currentHitter):
        event = np.random.choice(
            a = [0,1,2,3,4,5,6],
            size = 1,
            p = [currentHitter.so_perc,
                 currentHitter.single_perc,
                 currentHitter.double_perc,
                 currentHitter.triple_perc,
                 currentHitter.hr_perc,
                 currentHitter.bb_perc,
                 currentHitter.all_other_outs_perc]
        )
        return event[0]
