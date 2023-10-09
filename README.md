# MultiAgentSafetyHackathonProject
<ins>**Balancing Objectives: Ethical Dilemmas and AI's Temptation for Immediate Gains in Team Environments**</ins> 


**Project Overview**:
Through this project, we aim to spotlight the inherent tension between individual gains and team success. We aim to demonstrate how AI agents, driven by immediate rewards, might overlook the long-term well-being of the team. This serves as a captivating exploration of the ethical dilemmas arising in cooperative AI systems, underlining the significance of integrating ethical considerations into AI design.

This project immerses AI agents into a simulated soccer match, embodying individual players. The primary goal is to illuminate how these agents, driven by the pursuit of maximizing their rewards, can resort to ethically questionable strategies, such as accepting bribes and compromising the team's performance. 

**Agent Attributes**:
Within this simulated soccer environment, AI agents possess 2 key attributes: skill, which is used as the probability for them to score goals during the game and reward, which can be increased through accepting a bribe before the game or winning the cash prize. Each time an agent accepts a bribe, their skill level decreases by 0.1. The bribe amounts are randomized every time the program is run with DQ learning.

**Ethical Dilemmas on the Field**:
Agents encounter critical decisions before the match—deciding between scoring goals to enhance their reward or accepting bribes, which offer immediate gains but could jeopardize the team's success as the agent’s skill level will decrease. Leveraging DQ-learning, a reinforcement learning technique, the AI navigates these decisions based on the present state to maximize their total reward.

**Project Findings**: 
Generally, there has been a mix of results. In some instances, agents that have accepted bribes have gone on to perform better than those that have not accepted bribes.. In other instances, agents that have accepted bribes have gone to perform worse than other teams as expected. 

**Project Paper**:
This is the link to my project paper: [Project Paper](https://docs.google.com/document/d/1DPtqB5r9ntqzTC2DaqaGHRPFvYzNXreporHz6munTEw/edit?usp=sharing)







