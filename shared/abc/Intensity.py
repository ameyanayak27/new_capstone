from calvin.actor.actor import Actor, condition, manage
from calvin.runtime.north.calvin_token import ExceptionToken


class Intensity(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        t1 :
    Output :
        out1 :
    """
    @manage([])
    def init(self, ):
        pass

    @condition(action_input=['t1'], action_output=['out1'])
    def categorize(self, intensity):
	result = ''
        if intensity < 0.33:
	    result = 'low'
	elif intensity < 0.67:
	    result = 'mid'
	else:
	    result = 'high'	
        return ([result],)
        #print(str(self.result),str(temperatures), str(self.counter))

    action_priority = (categorize,)
