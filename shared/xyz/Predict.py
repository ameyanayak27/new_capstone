from calvin.actor.actor import Actor, manage, condition, stateguard
import math
class Predict(Actor):

    """
    Pass on given _data_ every _tick_ seconds
    Inputs:
	inp:
	map3:
	ignore_flag5: 

    Outputs:
        ans: 
    """

    @manage(['mapp'])
    def init(self):
	self.mapp = {}
        pass

    @condition(['inp','map3','ignore_flag5'], ['ans'])
    def solution(self, dataset, attr, ignore_flag):
	if(ignore_flag == 'validate'):
	    prediction = self.predict(dataset, attr)
	    ans = None
            prob = -1
            for key, value in prediction.iteritems():
		if(ans is None or value > prob):
		    prob = value
		    ans = key
	    print('temperature = ', dataset)
            print('prediction = ', ans)
	    return (self.mapp,)
	else:
	    return ('',)

    def predict(self, dataset, mapp):
        prob = {}
        for attr,value in mapp.iteritems():
	    prob[attr] = 1
	    for i in range(len(mapp)) :
                avg = value[0]
                stddev = value[1]
                prob[attr] = prob[attr]*(1/(math.sqrt(2*math.pi)*stddev)) * math.exp(-(math.pow(dataset[0]-avg,2)/2*math.pow(stddev,2)))
        return prob
       
    action_priority = (solution,)
