import sys

def parse_input(input_path):
    # load input file
    data = []
    with open(input_path) as f:
        for line in f:
            data.append(line[:-1])

    games = []
    opponent = ["A", "B", "C"]
    myself = ["X", "Y", "Z"]
    for s in data:
        letters = s.split(" ")
        games.append((opponent.index(letters[0]), myself.index(letters[1])))

    return games

def sum_of_games(games):
    # rows are choice of opponent, columns are choice of player
    point_matrix = [[3, 6, 0],
                    [0, 3, 6],
                    [6, 0, 3]]
    total_score = 0
    for game in games:
        score = point_matrix[game[0]][game[1]]
        # print(game)
        # print(score+ game[1] + 1)
        total_score += score + game[1] + 1

    return total_score

def sum_of_games_inversed_info(games):
    point_matrix = [[3, 4, 8],
                    [1, 5, 9],
                    [2, 6, 7]]
    total_score = 0
    for game in games:
        score = point_matrix[game[0]][game[1]]
        total_score += score

    return total_score

if __name__ == "__main__":
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    games = parse_input(input_file_path)
    ANSWER = sum_of_games(games)
    print(ANSWER)

    games = parse_input(input_file_path)
    ANSWER = sum_of_games_inversed_info(games)
    print(ANSWER)

