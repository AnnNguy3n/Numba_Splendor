from Agents.agent_func import *
import numpy as np
import json
import random

def action(play_state, file_temp, file_per):
    if len(file_per) < 2:
        with open('Agents/Agent_Chi_policy/reward_ucb.json') as f:
            file = json.load(f)
        file_per = np.array([file['choices'], file['point']])
    if len(file_temp) < 1:
        file_temp = np.zeros(460)
    list_action = get_list_action(play_state)
    index_action = random.randrange(len(list_action))
    score_max = 0
    action = list_action[index_action]
    if np.sum(file_per[1]) > 1000:
        policy = file_per[1]/file_per[0]
        for act in list_action:
            if policy[act] > score_max and act != 0:
                score_max = policy[act]
                action = act
    # else:
    # print(action,file_temp)
    file_temp[action] += 1
    win = check_victory(play_state)
    if win != -1:
        file_per[0] += file_temp
    if win == 1:
        file_per[1] += file_temp
    return action, file_temp, file_per