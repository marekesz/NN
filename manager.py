from test import test
import torch
import torch.nn as nn
from models.resnet import ResModel
from agents.egreedy_agent import EgreedyAgent
from agents.greedy_agent import GreedyAgent
from training_methods.monte_carlo import MonteCarlo
from model_utilis import *


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
'''
model_alpha = 0.001
model_1 = ResModel(input_shape=(3, 3), num_layers=66, kernel_size=(3,3), 
            num_of_res_layers=2, padding=(1, 1), 
            number_of_filters=256).to(device)

optimizer_1 = torch.optim.Adam(model_1.parameters(), lr=model_alpha)

model_2 = ResModel(input_shape=(3, 3), num_layers=66, kernel_size=(3,3), 
            num_of_res_layers=2, padding=(1, 1), 
            number_of_filters=256).to(device)

optimizer_2 = torch.optim.Adam(model_2.parameters(), lr=model_alpha)

criterion = nn.MSELoss()


trainer_1 = MonteCarlo(model_1, optimizer_1, criterion)
trainer_2 = MonteCarlo(model_2, optimizer_2, criterion)

player_1 = EgreedyAgent(e_value = 0.01)
player_2 = EgreedyAgent(e_value = 0.01)

train({'trainer_1': trainer_1, 'model_1': model_1, 'player_1': player_1,
        'trainer_2': trainer_2, 'model_2': model_2, 'player_2': player_2,
        'num_games': 30, 'save_model_every_n_iterations': 100, 'game_name': 'Reversi',
        'save_path': ''})
'''

model_1 = ResModel(input_shape=(3, 3), num_layers=66, kernel_size=(3,3), 
            num_of_res_layers=2, padding=(1, 1), 
            number_of_filters=256).to(device)

model_1 = load_model('/mnt/c/Users/zobni/Programming/NN/data/model/NN1VSNN2_(3, 3)_66_2_256.zip', model_1, device)

model_2 = ResModel(input_shape=(3, 3), num_layers=66, kernel_size=(3,3), 
            num_of_res_layers=2, padding=(1, 1), 
            number_of_filters=256).to(device)

model_2 = load_model('/mnt/c/Users/zobni/Programming/NN/data/model/NN1VSNN1_(3, 3)_66_2_256.zip', model_2, device)

player_1 = GreedyAgent()
player_2 = GreedyAgent()

test({ 'model_1': model_1, 'player_1': player_1, 'model_2': model_2, 'player_2': player_2,
       'num_games': 30})