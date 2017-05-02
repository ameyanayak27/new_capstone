from calvin.actor.actor import Actor, condition, manage
from calvin.runtime.north.calvin_token import ExceptionToken

class AverageMultipleIn(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        tem1 :
        tem2 :
        tem3 :
    Output :
        ip:
    """
    @manage([])
    def init(self):
        pass

    @condition(action_input=['tem1','tem2','tem3'], action_output=['ip'])
    def avg(self, temperature1, temperature2, temperature3):
        if(temperature1[0] != 'ignore' and temperature2[0] !='ignore' and temperature3[0]!='ignore'):
            self.result = (temperature1[0]+temperature2[0]+temperature3[0])/ 3
            self.type = temperature3[1]
        else:
            self.result = 'ignore'
            self.type = 'train'
        return ([self.result, self.type],)

    action_priority = (avg,)
