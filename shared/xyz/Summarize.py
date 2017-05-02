from calvin.actor.actor import Actor, manage, condition, stateguard
import math 
class Summarize(Actor):

    """
    Pass on given _data_ every _tick_ seconds
    Inputs:
	dataset:
	attributes:
	ignore_flag1: 

    Outputs:
	dataset2:
        mapp:
	ignore_flag2: 
    """

    @manage(['mapp'])
    def init(self):
	self.mapp = {}
        pass

    @condition(['dataset','attributes','ignore_flag1'], ['dataset2','mapp','ignore_flag2'])
    def aggregate(self, dataset, attr, ignore_flag):
	if(ignore_flag == 'validate'):
	    if(self.mapp == {} ):
	    	self.mapp = self.mappify(dataset,attr)
	    return ([dataset[-1]], self.mapp, 'validate',)
	else:
	    return ([], self.mapp, 'train',)

    def mappify(self, dataset, attr):
        unique = list(set(attr))
	map_attr = {}
        for i in range(len(dataset)):
	    item = dataset[i]
            if (attr[i] not in map_attr):
                map_attr[attr[i]] = []
            map_attr[attr[i]].append(item)

        return map_attr
       
    action_priority = (aggregate,)
