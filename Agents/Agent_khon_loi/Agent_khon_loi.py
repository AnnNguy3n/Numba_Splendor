from Agents.agent_functions import *
import numpy as np

def Agent_khon_loi(p_state):
    list_action = get_list_action(p_state)
    if p_state[-1] == 0 and 3 in list_action:
        return 3

    act_idx = np.random.randint(0, len(list_action))
    return list_action[act_idx]