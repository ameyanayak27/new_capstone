from calvin.actor.actor import Actor, condition, stateguard
from calvin.runtime.north.calvin_token import ExceptionToken


class AverageActor(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        temp3 :
    Output :
        result2:
    """

    def init(self, window_size):
        self.counter = 0
        self.result = []
        self.type = ''
	self.window_size = window_size

    @stateguard(lambda self: self.counter <= self.window_size)
    @condition(action_input=['temp3'], action_output=['result2'])
    def divide(self, temperatures):
        self.result.append(temp1)
        self.counter += 1
        self.type = temperatures[1]
        return (['ignore','train'],)
        #print(str(self.result),str(temperatures), str(self.counter))

    @stateguard(lambda self: self.counter > self.window_size)
    @condition(action_input=[], action_output=['result2'])
    def answer(self):
        result = self.result
        self.counter = 0
        self.result = []
        return ([result, self.type],)

    action_priority = (divide,answer)
