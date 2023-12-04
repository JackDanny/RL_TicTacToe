from State import State
import pandas as pd

def compute_all_state():
    code = '1000000000'
    set_code_to_explore = {code}
    set_explored_code = set()

    while len(set_code_to_explore) > 0:
        code = set_code_to_explore.pop()
        current_state = State(code)
        actions = current_state.get_actions()
        for act in actions:
            next_code = State(current_state.do_action(act)).min_similar_state()
            if next_code not in set_explored_code:
                set_code_to_explore.add(next_code)
        set_explored_code.add(code)
        pass

    pass


    #df = pd.DataFrame(columns = ['visited'])
    #df.loc[code] = [False]


def main():
    list_state_j1 = []
    list_state_j2 = []

    code = '1000000000'

    df = pd.DataFrame(columns=['visited'])

    df.loc[code] = [False]

    current_state = State(code)
    print(current_state)
    print("min similar state")
    print(State(current_state.min_similar_state()))

    actions = current_state.get_actions()
    while len(actions) > 0:
        print(actions)
        current_state = State(current_state.do_action(actions[0]))
        if current_state[0] == '1':
            pass
        if current_state[0] == '2':
            pass
        print(current_state)
        print("min similar state")
        print(State(current_state.min_similar_state()))
        actions = current_state.get_actions()

if __name__ == '__main__':
    compute_all_state()





    
