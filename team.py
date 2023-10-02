import random
from agent import Agent

class Team:
    def __init__(self, name, agent1, agent2):
        self.name = name
        self.agent1 = agent1
        self.agent2 = agent2
        self.team_rating = (agent1.skill + agent2.skill) / 2
        self.goals_scored = 0
        self.agents = [agent1, agent2]
      


    def calculate_goal_scoring_probability(self,selected_agent, min_prob=0.1, max_prob=0.9):
        # Use the selected agent's skill as the goal-scoring probability
        goal_prob = selected_agent.skill
        # Ensure the goal probability is within the specified range
        goal_prob = min(max_prob, max(min_prob, goal_prob))
        return goal_prob


    def score_goal(self):
        selected_agent = random.choice([self.agent1, self.agent2])
        goal_prob = self.calculate_goal_scoring_probability(selected_agent)
        if random.random() < goal_prob:
            goals_scored += 1 
