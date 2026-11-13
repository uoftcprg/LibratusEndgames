#!/usr/bin/env python3

def main():
    game = {}
    status = True

    while status:
        try:
            line = input()
        except EOFError:
            status = False
        else:
            key, value = line[1:].strip().split(' ', 1)
            game[key] = value

    pot = int(game['pot'])
    board_cards = game['board']
    hand_reaches = game['reach']
    name = (
        'universal_poker('
        'betting=nolimit,'
        'numPlayers=2,'
        'numRounds=4,'
        f'blind={pot // 2} {pot // 2},'
        'firstPlayer=2 1 1 1,'
        'numSuits=4,'
        'numRanks=13,'
        'numHoleCards=2,'
        'numBoardCards=0 3 1 1,'
        'stack=20000 20000,'
        f'boardCards={board_cards},'
        f'handReaches={hand_reaches})'
    )

    print(name)


if __name__ == '__main__':
    main()
