from calvin.actor.actor import Actor, condition, manage
from sklearn import tree
from sklearn.svm import SVC
import numpy as np

class Distributed(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        input
    Output :
        temperatures :
	heat :
	flag : 
    """

    @manage(['clf_heat', 'clf_ac', 'mode'])
    def init(self):
        self.clf_heat = SVC()
	#tree.DecisionTreeClassifier()
        self.clf_ac = SVC()
	#tree.DecisionTreeClassifier()
        self.temperatures = []
        self.heat = []
        self.ac = []
        self.mode = 'train'

    @condition(action_input=['input'], action_output=['temperatures','heat','flag'])
    def tree(self, temperature):
        if(temperature[1] == 'train'):
            self.train(temperature[0])
	    return ([], [],'train',)
        else:
            if (self.mode == 'train'):
		print(self.mode)
	        self.mode = 'validate'
		return(np.array(self.temperatures), np.array(self.heat),'validate',)
            else:
		return([temperature[0]],[],'validate')

    def train(self, temperature):
        if (temperature != 'ignore'):
            self.temperatures.append([temperature])
            if (float(temperature) < 70):
                self.heat.append(1)
                self.ac.append(0)
            elif (float(temperature) < 75):
                self.heat.append(0)
                self.ac.append(0)
            else:
                self.heat.append(0)
                self.ac.append(1)


    '''def validate(self, temperature):
        if (self.mode == 'train'):

            #self.clf_heat = self.clf_heat.fit(np.array(self.temperatures), np.array(self.heat))
            #self.clf_ac = self.clf_ac.fit(np.array(self.temperatures), np.array(self.ac))
            #self.mode = 'validate'
        print("temperature = ", str(temperature))
        print('AC = ', str(self.clf_ac.predict([[temperature]])))
        print('Heat = ', str(self.clf_heat.predict([[temperature]])))'''

    action_priority = (tree,)
