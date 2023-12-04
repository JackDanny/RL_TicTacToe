class State:

    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return(
            '\n'.join([
                self.code[0],
                self.code[1:4],
                self.code[4:7],
                self.code[7:10]
            ])
        )

    def __str__(self):
        return(
            '\n'.join([
                self.code[0],
                self.code[1:4],
                self.code[4:7],
                self.code[7:10]
            ])
        )

    def min_similar_state(self):

        state = similar_state_change_player(self.code)

        sim_state_90  = similar_state_90deg_clockwise(state)
        sim_state_180 = similar_state_90deg_clockwise(sim_state_90)
        sim_state_270 = similar_state_90deg_clockwise(sim_state_180)

        sim_state_mirror = similar_state_mirror(state)

        sim_state_mirror_90  = similar_state_90deg_clockwise(sim_state_mirror)
        sim_state_mirror_180 = similar_state_90deg_clockwise(sim_state_mirror_90)
        sim_state_mirror_270 = similar_state_90deg_clockwise(sim_state_mirror_180)

        return min([state,
                    sim_state_90,
                    sim_state_180,
                    sim_state_270,
                    sim_state_mirror,
                    sim_state_mirror_90,
                    sim_state_mirror_180,
                    sim_state_mirror_270])

    def get_actions(self):
        actions = []
        for i in range(1,len(self.code)):
            if self.code[i] == '0':
                actions.append(i)
        return actions

    def do_action(self, action):
        state = self.code
        state = list(state)

        state[action] = state[0]

        if state[0] == '1':
            state[0] = '2'
        else:
            state[0] = '1'

        return "".join(state)


def similar_state_change_player(state):

    if state[0] == '1':
        return state
    else:
        return ("".join(['1' if i == '2' else
                         '2' if i == '1' else
                         i for i in state]))

def similar_state_90deg_clockwise(state):
    '''
    0
    123
    456
    789

    0
    741
    852
    963
    '''
    permutation = [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]  # 0->0, 1->3 ...
    return ("".join([state[i] for i in permutation]))

def similar_state_mirror(state):
    '''
    0
    123
    456
    789

    0
    321
    654
    987
    '''
    permutation = [0, 3, 2, 1, 6, 5, 4, 9, 8, 7]  # 0->0, 1->3 ...
    return ("".join([state[i] for i in permutation]))

