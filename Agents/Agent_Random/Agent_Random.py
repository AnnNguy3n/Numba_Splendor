from Agents.agent_functions import *
import numpy as np

def Agent_Random(p_state):
    list_action = get_list_action(p_state)
    act_idx = np.random.randint(0, len(list_action))
    return list_action[act_idx]