from Agents.agent_functions import *
import numpy as np

def action(p_state, temp_file, pernament_file):
    list_action = get_list_action(p_state)
    act_idx = np.random.randint(0, len(list_action))
    return list_action[act_idx], temp_file, pernament_file