import chess.pgn

def run():
    def print_moves_from_pgn(pgn_file):
        # Open the PGN file
        output = ""
        with open(pgn_file, 'r') as f:
            # Parse the PGN file
            game_number = 1
            while True:
                game = chess.pgn.read_game(f)
                if game is None:
                    break 
                info1 = f"Game Number {game_number}: {game.headers.get('Event', 'Unknown Event')}"
                info2 = f"White: {game.headers['White']}, Black: {game.headers['Black']}"
                info3 = f"Result: {game.headers['Result']}"
                print(game.headers['White'])
                output += "\\scalebox{1.5}{" + info1 + "} \\\\ \n"
                output += "\\scalebox{1.5}{" + info2 + "} \\\\ \n"
                output += "\\scalebox{1.5}{" + info3 + "} \\\\ \n"
                output +="\\hfill \\break\n"
                # Access the board and iterate through the moves
                board = game.board()
                move_number = 0
                output += "\\newchessgame \n"
                for move in game.mainline_moves():
                    if board.turn:
                        move_number += 1
                        movestr = f"{move_number}.{board.san(move)}"
                        output += "\scalebox{2}{\mainline{" + movestr + "}}\\\ \n" 
                    else:
                        movestr = f"{move_number}...{board.san(move)}"
                        output += "\scalebox{2}{\mainline{" + movestr + "}}\\\ \n" 

                    output += "\scalebox{2}{\chessboard}\n"
                    output += "\\newpage\n"
                    board.push(move)
                    # Print the move number and the move itself
                    #print(f"{move_number}. {board.san(move)}")

                # Read the next game
                print(f"Done with game {game_number}")
                game_number += 1


            return output

    pgn_file = "shuffled_games.pgn"  # Replace with the path to your PGN file
    output = "\documentclass{article}\n"
    output += "\\usepackage{xskak}\n"
    output += "\\begin{document}\n"
    output += "\\begin{center}\n"

    output += print_moves_from_pgn(pgn_file)
    output += "\\end{center}\n\\end{document}"
    f = open("./tt/output.tex","w")
    f.write(output)
    f.close()

