import chess.pgn
import random
def run():
    def shuffle_pgn(input_pgn, output_pgn):
        # Open the input PGN file
        with open(input_pgn, "r") as pgn_file:
            games = []
            
            # Read all the games from the PGN file
            while True:
                game = chess.pgn.read_game(pgn_file)
                if game is None:
                    break
                games.append(game)
            
            # Shuffle the list of games randomly
            random.shuffle(games)
            
            # Open the output PGN file
            with open(output_pgn, "w") as output_file:
                # Write the shuffled games to the output PGN file
                for game in games:
                    game.accept(chess.pgn.StringExporter(headers=True, variations=True))
                    output_file.write("\n" + str(game) + "\n")

# Example usage
    input_pgn_file = "input.pgn"  # Path to the input PGN file
    output_pgn_file = "shuffled_games.pgn"  # Path to save the shuffled PGN

    shuffle_pgn(input_pgn_file, output_pgn_file)
    print("Games shuffled and saved to", output_pgn_file)

