'''
create a state machine
then convert the number in binary and use state machine to see if the number is divisible or not
'''

def preprocess(k, table):
    for state in range(k):
        state0 = state<<1
        if state0 >= k:
            state0 -= k
        table[state][0] = state0

        state1 = (state<<1) + 1
        if state1 >= k:
            state1 -= k
        table[state][1] = state1

state = 0

def isDivisible(num, table):
    global state
    if num != 0:
        isDivisible(num >> 1, table)
        state = table[state][num & 1]

def main():
    num = 47
    k = len(bin(47))
    table = [[0,0] for x in range(k)]
    preprocess(k, table)
    isDivisible(num, table)

    print(state)

if __name__ == '__main__':
    main()