from Agents.agent_func import *
import numpy as np
from Environment.env_func import noble_cards_infor, normal_cards_infor

def in_ban_choi(p_state):
    # print('----------------------------------------------------------------------------------------------------')
    # print('Thứ tự nguyên liệu được in là: Đỏ, Lam, Lục, Đen, Trắng, Vàng')
    temp_lst = ['Đỏ', 'Lam', 'Lục', 'Đen', 'Trắng', 'Vàng']
    print('Các thẻ trên bàn chơi:')
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('ID', 'Điểm', 'Đỏ', 'Lam', 'Lục', 'Đen', 'Trắng', 'Type'))
    print('Cấp I')
    c_I = [i_ for i_ in range(40) if p_state[i_] == 5]
    for i in c_I:
        _ = normal_cards_infor[i]
        print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format(i, _[0], _[2], _[3], _[4], _[5], _[6], temp_lst[_[1]]))
    
    print('Cấp II')
    c_II = [i_ for i_ in range(40,70) if p_state[i_] == 5]
    for i in c_II:
        _ = normal_cards_infor[i]
        print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format(i, _[0], _[2], _[3], _[4], _[5], _[6], temp_lst[_[1]]))

    print('Cấp III')
    c_III = [i_ for i_ in range(70,90) if p_state[i_] == 5]
    for i in c_III:
        _ = normal_cards_infor[i]
        print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format(i, _[0], _[2], _[3], _[4], _[5], _[6], temp_lst[_[1]]))

    print('Thẻ Noble:')
    c_IV = [i_ for i_ in range(90,100) if p_state[i_] == 5]
    for i in c_IV:
        _ = noble_cards_infor[i-90]
        print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format(i, 3, _[0], _[1], _[2], _[3], _[4], 'None'))
    
    c_V = [i_ for i_ in range(90) if p_state[i_] == -1]
    if len(c_V) != 0:
        print('Thẻ đang úp')
    for i in c_V:
        _ = normal_cards_infor[i]
        print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format(i, _[0], _[2], _[3], _[4], _[5], _[6], temp_lst[_[1]]))

    print()
    print('Nguyên liệu và nguyên liệu vĩnh cửu:')
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'', 'Đỏ', 'Lam', 'Lục', 'Đen', 'Trắng', 'Vàng'))
    _ = p_state[100:106]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'Board', _[0], _[1], _[2], _[3], _[4], _[5]))

    _ = p_state[106:112]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'Self', _[0], _[1], _[2], _[3], _[4], _[5]))
    _ = p_state[112:117]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'Self_C', _[0], _[1], _[2], _[3], _[4], 0))

    _ = p_state[118:124]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'BOT1', _[0], _[1], _[2], _[3], _[4], _[5]))
    _ = p_state[124:129]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'BOT1_C', _[0], _[1], _[2], _[3], _[4], 0))

    _ = p_state[130:136]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'BOT2', _[0], _[1], _[2], _[3], _[4], _[5]))
    _ = p_state[136:141]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'BOT2_C', _[0], _[1], _[2], _[3], _[4], 0))

    _ = p_state[142:148]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'BOT3', _[0], _[1], _[2], _[3], _[4], _[5]))
    _ = p_state[148:153]
    print('    {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7} {: >7}'.format('' ,'BOT3_C', _[0], _[1], _[2], _[3], _[4], 0))
    
    print()
    print('Thẻ đang sở hữu:')
    print('Self:', [i_ for i_ in range(90) if p_state[i_] == 1])
    print('BOT1:', [i_ for i_ in range(90) if p_state[i_] == 2])
    print('BOT2:', [i_ for i_ in range(90) if p_state[i_] == 3])
    print('BOT3:', [i_ for i_ in range(90) if p_state[i_] == 4])

    print()
    print('Điểm theo thứ tự:', p_state[117], p_state[129], p_state[141], p_state[153])
    print()

def in_hanh_dong(p_state):
    list_action = get_list_action(p_state)
    phase = p_state[160]
    if phase == 0:
        print('Lựa chọn hành động tiếp theo:')
        temp_lst = ['Kết thúc lượt', 'Lấy nguyên liệu', 'Úp thẻ', 'Mua thẻ']
        for i in list_action:
            print(str(i) + '. ' + temp_lst[i])
        
        if 3 in list_action:
            temp_state = p_state.copy()
            temp_state[160] = 3
            temp_lst_act = get_list_action(temp_state)
            print('List thẻ mua được:', np.array(temp_lst_act)-102)
    
    elif phase == 1:
        print('Lấy nguyên liệu:')
        temp_lst = ['Đỏ', 'Lam', 'Lục', 'Đen', 'Trắng']
        for i in list_action:
            if i == 0:
                print(str(i) + '. ' + 'Kết thúc lấy nguyên liệu')
            else:
                print(str(i) + '. Lấy ' + temp_lst[i-4])
    
    elif phase == 2:
        print('Úp thẻ:')
        for i in list_action:
            if i >= 99:
                print(str(i) + '. Úp thẻ ẩn cấp ' + str(i-98))
            else:
                print(str(i) + '. Úp thẻ ' + str(i-9))
    
    elif phase == 3:
        print('Mua thẻ:')
        for i in list_action:
            print(str(i) + '. Mua thẻ ' + str(i-102))
    
    else: # phase == 4
        print('Trả nguyên liệu:')
        temp_lst = ['Đỏ', 'Lam', 'Lục', 'Đen', 'Trắng']
        for i in list_action:
            print(str(i) + '. Trả ' + temp_lst[i-192])

def action(p_state, temp_file, per_file):
    in_ban_choi(p_state)
    in_hanh_dong(p_state)
    list_action = get_list_action(p_state)
    act = input('\nNhập action được chọn: ')
    check_valid = False
    while not check_valid:
        try:
            act = int(act)
            if act in list_action:
                check_valid = True
            else:
                act = input('\nNhập sai, mời nhập lại! Nhập action được chọn: ')
        except:
            act = input('\nNhập sai, mời nhập lại! Nhập action được chọn: ')
    
    return int(act), temp_file, per_file