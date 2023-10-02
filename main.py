from agent import Agent
from team import Team
from soccer_game import SoccerGame
from dqnagent import DQNAgent  # Assuming you have a file for the DQNAgent class
import random
import matplotlib.pyplot as plt

def main():
    # Create agents and teams
    agent1_team1 = Agent("Agent 1", 0.5)
    agent2_team1 = Agent("Agent 2", 0.5)
    agent1_team2 = Agent("Agent 3", 0.5)
    agent2_team2 = Agent("Agent 4", 0.5)

    team1 = Team("Team1", agent1_team1, agent2_team1)
    team2 = Team("Team2", agent1_team2, agent2_team2)

    # Create a DQN agent
    dqn_agent = DQNAgent(input_size=3, output_size=2)

    # Create the SoccerGame instance with the DQN agent
    soccer_game = SoccerGame(team1, team2, dqn_agent)

    match_duration = 30
    bribe_amount = random.uniform(0,100)
    batch_size = 32  # Batch size for training the DQN agent

    for i in range(20):  # Run 10 episodes for training
        soccer_game.simulate_match(match_duration, bribe_amount, batch_size)

        # Train DQN agent at the end of each episode
        print(f"Training DQN - Episode {i+1}")
        for _ in range(10):  # Train the DQN agent multiple times within an episode
            soccer_game.dqn_agent.replay(batch_size)

        # Pay agents based on match outcome
        if team1.goals_scored > team2.goals_scored:
            soccer_game.pay_agent(agent1_team1, True)
            soccer_game.pay_agent(agent2_team1, True)
            soccer_game.pay_agent(agent1_team2, False)
            soccer_game.pay_agent(agent2_team2, False)
        elif team2.goals_scored > team1.goals_scored:
            soccer_game.pay_agent(agent1_team2, True)
            soccer_game.pay_agent(agent2_team2, True)
            soccer_game.pay_agent(agent1_team1, False)
            soccer_game.pay_agent(agent2_team1, False)

    print("FT: Team 1 vs Team 2:", team1.goals_scored, team2.goals_scored)

    print("Total Rewards")
    print("Agent 1: ", agent1_team1.reward)
    print("Agent 2: ", agent2_team1.reward)
    print("Agent 3: ", agent1_team2.reward)
    print("Agent 4: ", agent2_team2.reward)

    print("Bribes accepted: ")
    print("Agent 1: ", agent1_team1.bribes_accepted)
    print("Agent 2: ", agent2_team1.bribes_accepted)
    print("Agent 3: ", agent1_team2.bribes_accepted)
    print("Agent 4: ", agent2_team2.bribes_accepted)

    agent_data = {'Agent 1': (agent1_team1.bribes_accepted, agent1_team1.reward),
                      'Agent 2': (agent2_team1.bribes_accepted, agent2_team1.reward),
                      'Agent 3': (agent1_team2.bribes_accepted, agent1_team2.reward),
                      'Agent 4': (agent2_team2.bribes_accepted, agent2_team2.reward)}
    
    agent_bribes_rewards = []

    agent_bribes_rewards.append(agent_data)

    # Plotting
   



# Call the function to plot the data


if __name__ == "__main__":
    main()



