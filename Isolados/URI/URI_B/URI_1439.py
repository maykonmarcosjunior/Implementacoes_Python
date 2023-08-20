def main():
    while True:
        P, M, N = map(int, input().split())
        if P == 0 and M == 0 and N == 0:
            break

        players = [[] for _ in range(P)]
        for i in range(P * M):
            value, suit = input().split()
            players[(i // M) % P].append((int(value), suit))

        initial_card = input().split()
        discard_pile = [(int(initial_card[0]), initial_card[1])]
        draw_pile = [tuple(input().split()) for _ in range(N - (P * M) - 1)]

        direction = 'clockwise'
        current_player = 0
        winner = None

        while True:
            top_value, top_suit = discard_pile[-1]

            has_valid_card = False
            for idx, (value, suit) in enumerate(players[current_player]):
                if value == top_value or suit == top_suit:
                    discard_pile.append((value, suit))
                    players[current_player].pop(idx)
                    has_valid_card = True
                    break

            if not has_valid_card:
                if draw_pile:
                    drawn_card = draw_pile.pop(0)
                    players[current_player].append(drawn_card)

            if not players[current_player]:
                winner = current_player + 1
                break

            if discard_pile[-1][0] == 12:
                direction = 'anticlockwise' if direction == 'clockwise' else 'clockwise'
            elif discard_pile[-1][0] == 7:
                if draw_pile:
                    drawn_card = draw_pile.pop(0)
                    players[current_player].append(drawn_card)
                    if draw_pile:
                        drawn_card = draw_pile.pop(0)
                        players[current_player].append(drawn_card)
                current_player = get_next_player(current_player, direction, P)
                continue
            elif discard_pile[-1][0] == 1:
                if draw_pile:
                    drawn_card = draw_pile.pop(0)
                    players[current_player].append(drawn_card)
                current_player = get_next_player(current_player, direction, P)
                continue
            elif discard_pile[-1][0] == 11:
                current_player = get_next_player(current_player, direction, P)

            current_player = get_next_player(current_player, direction, P)

        print(winner)


def get_next_player(current_player, direction, num_players):
    if direction == 'clockwise':
        return (current_player + 1) % num_players
    else:
        return (current_player - 1 + num_players) % num_players


main()
