import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class DQNAgent:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.memory = []  # Experience replay memory
        self.gamma = 0.95  # Discount factor
        self.epsilon = 1.0  # Initial exploration rate
        self.epsilon_min = 0.01  # Minimum exploration rate
        self.epsilon_decay = 0.995  # Decay rate for exploration

        # Neural network to approximate Q-value function
        self.model = nn.Sequential(
            nn.Linear(input_size, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, output_size)
        )

        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

    def act(self, state, bribe_amount):
        if np.random.rand() <= self.epsilon:
            return np.random.choice(self.output_size)
        q_values = self.model(torch.Tensor(state + [bribe_amount]))  # Concatenate state and bribe_amount
        return np.argmax(q_values.detach().numpy())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return

        minibatch = np.random.choice(self.memory, batch_size, replace=False)
        states, targets = [], []

        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                next_state = torch.Tensor(next_state).unsqueeze(0)  # Add a batch dimension
                target = reward + self.gamma * np.amax(self.model(next_state).detach().numpy())

            state = torch.Tensor(state).unsqueeze(0)  # Add a batch dimension
            target_f = self.model(state).detach().numpy()
            target_f[0][action] = target
            states.append(state.squeeze(0).numpy())
            targets.append(target_f[0])

        states = np.array(states)
        targets = np.array(targets)

        self.optimizer.zero_grad()
        loss = nn.MSELoss()(self.model(torch.Tensor(states)), torch.Tensor(targets))
        loss.backward()
        self.optimizer.step()

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
