from calvin.actor.actor import Actor, manage, condition, stateguard
import math

class StdDeviation(Actor):

    """
    Pass on given _data_ every _tick_ seconds
    Inputs:
	dataset3:
	attr_map:
	ignore_flag3:

    Outputs:
	dataset4:
        map2:
	ignore_flag4:
    """

    @manage(['mapp'])
    def init(self):
        self.mapp = {}

    @condition(['dataset3', 'attr_map', 'ignore_flag3'], ['dataset4', 'map2', 'ignore_flag4'])
    def stddeviation(self, dataset, mean_map, ignoreflag3):
        if(ignoreflag3 == 'train'):
	    return ([], {},'train')
	else:
	    if(self.mapp == {}):
	    	self.mapp = self.calc_stddeviation(mean_map)
	    return ([dataset[-1]], self.mapp, 'validate')

    def calc_stddeviation(self, mean_map):
	mapp = {}
        for attr, values in mean_map.iteritems():
            mean = sum(values)/ float(len(values))
            std_dev = sum([pow(x - mean, 2) for x in values])/float(len(values) - 1)
            mapp[attr] = [mean,math.sqrt(std_dev)]
	return mapp

    action_priority = (stddeviation,)
