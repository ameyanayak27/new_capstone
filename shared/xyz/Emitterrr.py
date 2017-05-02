from calvin.actor.actor import Actor, manage, condition, stateguard
import random

class Emitterrr(Actor):

    """
    Pass on given _data_ every _tick_ seconds
    Inputs:

    Outputs:
        data2
    """

    @manage(['tick', 'started', 'timer'])
    def init(self):
        self.tick = 0.01
        self.data = []
        self.timer = None
        self.started = False
        self.type = 'train'
        self.setup()

    def setup(self):
        self.use('calvinsys.events.timer', shorthand='timer')

    def start(self):
        self.timer = self['timer'].repeat(self.tick)
        self.started = True

    def will_migrate(self):
        if self.timer:
            self.timer.cancel()

    # div.temp1
    # div.result >
    #div : Math.AverageActor()
    def did_migrate(self):
        self.setup()
        if self.started:
            self.start()

    @stateguard(lambda self: not self.started)
    @condition([], ['data2'])
    def start_timer(self):
        self.start()
        result = random.random()
        return ([result, self.type],)

    @stateguard(lambda self: self.timer and self.timer.triggered)
    @condition([], ['data2'])
    def trigger(self):
        result = random.uniform(0, 1)
        self.started = False
        return ([result, self.type],)

    action_priority = (start_timer, trigger)
    requires = ['calvinsys.events.timer']
