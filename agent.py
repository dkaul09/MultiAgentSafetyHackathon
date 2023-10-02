import random



class Agent: # Agent class implementation - Bribe is offered before the game 
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill #Skill level
        self.bribe_accepted = False
        self.reward = 0
        self.bribes_accepted = 0

    def accept_bribe(self, bribe_amount):
        self.skill -= 0.1
        self.bribes_accepted += bribe_amount
        #self.skill -= random.uniform(0,1)
        self.skill = max(0, min(1, self.skill))
        self.bribe_accepted = True
        self.reward += bribe_amount
        print(f"New skill level: {self.skill}")

    def receive_bribe(self,bribe_amount):
        acceptance_probability = 0.5  # Adjust this probability as needed
        if random.random() < acceptance_probability:
            self.accept_bribe(bribe_amount)
            return True
        else:
            return False

       