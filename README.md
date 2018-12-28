# Chess-Game
Chess game written in Python3 (for terminal execution)

Game is based off a dictiornay called 'Game_board'

Each player is a class object, that stores values such as:
  1. turn ('w', 'b')
  2. King_loaction (key of Game_board where player's king is the value)
  3. pieces (all key values of Game_board that have the player's turn)
  4. check_threat (dictionary of lists)
    4a. key: Opponents piece that threatens king
    4b. Value: spaces inbetween threat and king
  5. in_check (bool) weather or not player's king in simple check.
  6. in_check_mate (bool) weather or not player's king is in check mate (game over)
  7. Capture (list of pieces that player has taken durring game.
    7a. will be used to save game in later versions program

Game is called, and starts in start_move(). Based on the outcome of simple_check_from_class() 
input of two pieces is required (choose_piece, direction).
The two pieces are evaluated based what type of piece (pawn, rook, bishop etc.) choose_piece is.
If the mve is legal the return value is a class objct called ReturnVal

All evaluations will return to start_move(). 
The value of move_return.p_ass is evaluted in the game() scope. 
  if "yes" the while loop is exited
  if "no" the while loop is continued.

