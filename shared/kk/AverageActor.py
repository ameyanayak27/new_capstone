from calvin.actor.actor import Actor, condition, stateguard, manage
from calvin.runtime.north.calvin_token import ExceptionToken


class AverageActor(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        temp1 :
    Output :
        result:
    """
    @manage(['counter', 'result', 'types', 'window_size'])
    def init(self, window_size):
        self.counter = 0
        self.result = 0
        self.types = ''
	self.window_size = window_size

    @stateguard(lambda self: self.counter <= self.window_size)
    @condition(action_input=['temp1'], action_output=['result'])
    def divide(self, temperatures):
        self.result = (( self.result * self.counter ) + temperatures[0] )/ (self.counter + 1)
        self.counter += 1
        self.types = temperatures[1]
        return (['ignore','train'],)
        #print(str(self.result),str(temperatures), str(self.counter))

    @stateguard(lambda self: self.counter > self.window_size)
    @condition(action_input=[], action_output=['result'])
    def answer(self):
        result = self.result
        self.counter = 0
        self.result = 0
        return ([result, self.types],)

    action_priority = (divide,answer)
