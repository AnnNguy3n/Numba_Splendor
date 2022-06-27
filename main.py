from Environment.environment_functions import *
import random as rd
from time import time

from Agents.Agent_Random.Agent_Random import Agent_Random as p1

def one_game(list_player, env, lv1, lv2, lv3, print_mode):
    reset(env, lv1, lv2, lv3)

    def _print_():
        print('----------------------------------------------------------------------------------------------------')
        print('Thẻ 1:', [i_ for i_ in range(40) if env[:40][i_] == 5])
        print('Thẻ 2:', [i_ for i_ in range(40,70) if env[:70][i_] == 5])
        print('Thẻ 3:', [i_ for i_ in range(70,90) if env[:90][i_] == 5])
        print('Thẻ noble:', [i_ for i_ in range(90,100) if env[:100][i_] == 5])
        print('B_stocks:', env[100:106])
        print('P1:', env[106:118], 'P2:', env[118:130])
        print('P3:', env[130:142], 'P4:', env[142:154])
        print(env[154:])

    if print_mode:
        _print_()

    _cc = 0
    while env[154] <= 400 and _cc <= 10000:
        act = list_player[env[154]%4](get_player_state(env))
        step(act, env, lv1, lv2, lv3)
        if print_mode:
            print('Action chọn', act)
            _print_()

        if close_game(env) != 0:
            break

        _cc += 1
    
    if _cc >= 10000:
        print('Chỗ này bị lặp vô tận')
        _print_()
        input()

    turns = env[154]
    for i in range(4):
        env[154] = i
        p_state = get_player_state(env)
        p_state[154] = turns
        act = list_player[env[154]%4](p_state)
    
    env[154] = turns
    return close_game(env)

def n_games(list_player, num_games=1, print_mode=False):
    '''
    Chạy nhiều game thì tắt cái print_mode đi không lag máy
    Nếu bật print_mode thì nên chạy ở jupyter notebook để xem full output
    '''
    if len(list_player) != 4:
        print('Game chỉ cho phép có đúng 4 người chơi')
        return [-1]
    
    env, lv1, lv2, lv3 = generate_environment()
    num_won = [0,0,0,0,0]
    p_lst_idx = [0,1,2,3]
    for _n in range(num_games):
        # Shuffle người chơi
        rd.shuffle(p_lst_idx)
        if print_mode:
            print('Thứ tự người chơi (thứ tự này sẽ ứng với P1,P2,P3,P4):', p_lst_idx)
            print('Lưu ý: không phải người chơi index 0 là P1')

        winner = one_game([
            list_player[p_lst_idx[0]],
            list_player[p_lst_idx[1]],
            list_player[p_lst_idx[2]],
            list_player[p_lst_idx[3]],
        ], env, lv1, lv2, lv3, print_mode)

        if winner != 0:
            num_won[p_lst_idx[winner-1]] += 1
        else:
            num_won[4] += 1

    return num_won

if __name__ == '__main__':
    a = time()
    print(n_games([p1,p1,p1,p1], print_mode=True))
    print(time() - a)

    a = time()
    print(n_games([p1,p1,p1,p1], 1000))
    print(time() - a)
