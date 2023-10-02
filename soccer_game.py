import random
from agent import Agent 
class SoccerGame:
    def __init__(self, team1, team2, dqn_agent):
        self.team1 = team1
        self.team2 = team2
        self.current_time = 0 
        self.cash_prize = 200
        self.dqn_agent = dqn_agent

    def step(self):
        self.current_time += 1
        
   
    def simulate_actions(self, bribe_amount):
         for team in [self.team1, self.team2]:
            for agent in team.agents:
                state = [agent.skill, bribe_amount, self.cash_prize]  # State: [skill, bribe amount, cash prize]
                action = self.dqn_agent.act(state,bribe_amount)

                # Simulate a goal scoring attempt
                goal_prob = agent.skill
                if action == 0:  # Accepting the bribe
                    agent.accept_bribe(bribe_amount)
                    print(f"Bribe of ${bribe_amount} accepted by {agent.name}.") 
                else: 
                      print(f"{agent.name} rejected the bribe offer of ${bribe_amount}.")

                
                if random.random() < goal_prob: 
                    team.goals_scored += 1

    def simulate_match(self, match_duration, bribe_amount, batch_size):
     self.total_time = match_duration
     while self.current_time < self.total_time:
        self.step()  # Simulate each step (1-second intervals)
        # Simulate actions during the match
        self.simulate_actions(bribe_amount)  # Pass bribe_amount
        print("Team 1 vs Team 2:", self.team1.goals_scored, self.team2.goals_scored)

        # Train DQN agent by replaying experiences
        self.dqn_agent.replay(batch_size)
                        
   


    def offer_bribe(self):
        # Simulate sending a bribe to a randomly chosen team
        bribe_amount = random.uniform(0,100)  # Bribe amount to offer to each agent
        for team in [self.team1, self.team2]:
            for agent in team.agents:
                agent_bribe_accepted = agent.receive_bribe(bribe_amount)
                if agent_bribe_accepted:
                    print(f"Bribe of ${bribe_amount} accepted by {agent.name}.")
                else:
                    print(f"{agent.name} rejected the bribe offer of ${bribe_amount}.")
    
    def pay_agent(self, agent, match_won):
        if match_won:
            agent.reward += 200  # Reward for winning the match
            if agent.bribe_accepted:
                agent.reward += 50  # Additional reward for accepting the bribe
        
    
    
            ####
        ###elif  agent.bribe_accepted == True & match_won == False:
         ###   agent.reward = 50  # for accepting the bribbe 
       ### elif agent.bribe_accepted == False & match_won == True:
         ###    agent.reward = 200

        


        
              

   
      

 

   
   

