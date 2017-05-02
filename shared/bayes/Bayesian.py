from calvin.actor.actor import Actor, condition, manage
from sklearn import tree
import numpy as np
class Bayesian(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        temp :
	intensity :
    Output :
        out2 :
    """

    @manage(['clf_blinds'])
    def init(self):
        self.clf_blinds = tree.DecisionTreeClassifier()
        self.blinds = [] 
        self.temperatures = []   
        self.mode = 'train'

    @condition(action_input=['temp', 'intensity'], action_output=['out2'])
    def tree(self, temperature, inten):
	print(inten)
        if(temperature[1] == 'train'):
            self.train(temperature[0], inten)
            self.mode = 'train'
        else:
            self.validate(temperature[0], inten)
        return ('',)

    def train(self, temperature, inten):
        if (temperature != 'ignore'):
            self.temperatures.append([temperature, inten])
            if (inten == 'low'):
                self.blinds.append('open')
            elif (float(temperature) < 70 and inten == 'mid'):
                self.blinds.append('open')
            elif (float(temperature) < 70 and inten == 'high'):
                self.blinds.append('close')
            elif (float(temperature) > 70 and inten == 'mid'):
                self.blinds.append('half')
            elif (float(temperature) > 70 and inten == 'high'):
                self.blinds.append('close')


    def validate(self, temperature, inten):
        if (self.mode == 'train'):
            self.clf_blinds = self.clf_blinds.fit(np.array(self.temperatures), np.array(self.blinds))
            self.mode = 'validate'
        print("temperature = ", str(temperature))
        print("inten = ", str(inten))
        print('Blind = ', str(self.clf_ac.predict([[temperature, inten]])))

    action_priority = (tree,)
