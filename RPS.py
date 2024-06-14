def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    
    # Use a default move initially
    guess = "R"
    
    # Implement a simple strategy based on the opponent's most recent move
    if len(opponent_history) > 0:
        # Counter the opponent's last move
        last_move = opponent_history[-1]
        if last_move == "R":
            guess = "P"  # Paper beats Rock
        elif last_move == "P":
            guess = "S"  # Scissors beats Paper
        elif last_move == "S":
            guess = "R"  # Rock beats Scissors
    
    return guess
  
