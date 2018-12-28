

class Player:

    def __init__(self, color):
        self.turn = color
        self.king_location = str
        self.pieces = {}
        self.check_threat = {}
        self.in_check = False
        self.in_check_mate = False
        self.capture = []

    def player_info(self, bard):
        '''function locates all pieces for player based on there Player.turn var'''
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        # filling player class info
        self.pieces = {}
        for colum in letters:
            for row in range(1, 9):
                check_piece = colum + str(row)
                if bard[check_piece][0] == self.turn:  # if piece belongs to Player
                    self.pieces[check_piece] = []
                    if 'kg' in bard[check_piece]:
                        self.king_location = str(check_piece)  # fills class dic w/ location of king
                    else:
                        continue
                else:
                    continue
        self.player_possible_move(bard)
        return

    def player_possible_move(self, bard):
        """
        :param bard: Game_board
        :return: None, searches all players pieces, adds all possible pieces for each piece
        """

        # creates list to loop through letters
        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

        pawn_ = 'p'
        rook_ = 'r'
        knight_ = 'k'
        bishop_ = 'bs'
        queen_ = 'qn'
        king_ = 'kg'

        for my_piece in self.pieces.keys():         # iterates through players pieces currently on board
            mp0 = my_piece[0]                       # splits My_piece EX. A, B, C
            mp1 = int(my_piece[1])                  # splits my_piece EX. 1, 2, 3

            if king_ in bard[my_piece]:
                if mp1 == 8:
                    for letter, num in letters.items():
                        if num == (letters[mp0] - 1) or num == letters[mp0] or num == (letters[mp0] + 1):
                            insert_piece = letter + str(mp1 - 1)
                            if bard[insert_piece] != self.turn:
                                self.pieces[my_piece].append(insert_piece)
                            else:
                                continue
                elif mp1 == 1:
                    for letter, num in letters.items():
                        if num == (letters[mp0] - 1) or num == letters[mp0] or num == (letters[mp0] + 1):
                            insert_piece = letter + str(mp1 + 1)
                            if bard[insert_piece] != self.turn:
                                self.pieces[my_piece].append(insert_piece)
                            else:
                                continue
                elif 1 < mp1 < 8:
                    for letter, num in letters.items():
                        if num == (letters[mp0] - 1) or num == letters[mp0] or num == (letters[mp0] + 1):
                            for number in range((mp1 - 1), (mp1 + 2)):
                                if number == mp1:
                                    continue
                                else:
                                    insert_piece = letter + str(number)
                                    if bard[insert_piece] != self.turn:
                                        if insert_piece not in self.pieces:
                                            self.pieces[my_piece].append(insert_piece)
                                        else:
                                            continue
                                    else:
                                        continue

            elif pawn_ in bard[my_piece]:
                if bard[my_piece][0] == 'w':
                    increment = 1
                elif bard[my_piece][0] == 'b':
                    increment = -1
                for letter, num in letters.items():
                    insert_piece = letter + str(mp1 + increment)
                    if bard[insert_piece][0] == self.turn:
                        continue
                    else:
                        if mp0 == 'A':
                            if num == letters[mp0] or num == (letters[mp0] + 1):
                                self.pieces[my_piece].append(insert_piece)
                        elif mp0 == 'H':
                            if num == letters[mp0] or num == (letters[mp0] - 1):
                                self.pieces[my_piece].append(insert_piece)
                        elif 'A' != mp0 != 'H':
                                if num == (letters[mp0] - 1) or num == letters[mp0] or num == (letters[mp0] + 1):
                                    self.pieces[my_piece].append(insert_piece)

            elif rook_ in bard[my_piece]:
                for number in range(1, 9):
                    insert_piece = mp0 + str(number)
                    if bard[insert_piece][0] == self.turn:
                        continue
                    else:
                        if number == mp1:
                            continue
                        else:
                            self.pieces[my_piece].append(insert_piece)
                for letter in letters.keys():
                    insert_piece = letter + str(mp1)
                    if bard[insert_piece][0] == self.turn:
                        continue
                    else:
                        if letter == mp0:
                            continue
                        else:
                            self.pieces[my_piece].append(insert_piece)

            elif queen_ in bard[my_piece]:
                for letter, num in letters.items():

                    if letter == mp0:
                        for number in range(1, 9):
                            check_piece = letter + str(number)
                            if check_piece in self.pieces[my_piece]:
                                continue
                            else:
                                if bard[check_piece][0] == self.turn:
                                    continue
                                else:
                                    self.pieces[my_piece].append(check_piece)

                    elif num < letters[mp0]:
                        difference = (letters[mp0] - num)
                        insert_piece = letter + str(mp1 + difference)
                        insert_piece_2 = letter + str(mp1 - difference)
                        if insert_piece in bard:
                            if insert_piece in self.pieces[my_piece]:
                                continue
                            elif bard[insert_piece][0] == self.turn:
                                continue
                            else:
                                self.pieces[my_piece].append(insert_piece)
                                if insert_piece_2 in bard:
                                    if bard[insert_piece_2][0] != self.turn:
                                        if insert_piece_2 in self.pieces[my_piece]:
                                            continue
                                        else:
                                            self.pieces[my_piece].append(insert_piece_2)
                        elif insert_piece_2 in bard:
                            if bard[insert_piece_2][0] != self.turn:
                                if insert_piece_2 in self.pieces[my_piece]:
                                    continue
                                else:
                                    self.pieces[my_piece].append(insert_piece_2)
                            else:
                                continue
                    elif num > letters[mp0]:
                        difference = (num - letters[mp0])
                        insert_piece = letter + str(mp1 + difference)
                        insert_piece_2 = letter + str(mp1 - difference)
                        if insert_piece in bard:
                            if insert_piece in self.pieces[my_piece]:
                                continue
                            elif bard[insert_piece][0] == self.turn:
                                continue
                            else:
                                self.pieces[my_piece].append(insert_piece)
                                if insert_piece_2 in bard:
                                    if bard[insert_piece_2][0] != self.turn:
                                        if insert_piece_2 in self.pieces[my_piece]:
                                            continue
                                        else:
                                            self.pieces[my_piece].append(insert_piece_2)
                        elif insert_piece_2 in bard:
                            if bard[insert_piece_2][0] != self.turn:
                                if insert_piece_2 in self.pieces[my_piece]:
                                    continue
                                else:
                                    self.pieces[my_piece].append(insert_piece_2)
                            else:
                                continue
            elif knight_ in bard[my_piece]:
                for letter, num in letters.items():
                    # two block needed. 1. check when a piece is moving 2 right left. 2. when 2 up/down
                    if num == (letters[mp0] - 2) or num == (letters[mp0] + 2):
                        insert_piece = letter + str(mp1 + 1)                    # to the right
                        insert_piece_2 = letter + str(mp1 - 1)                  # to the left
                        if insert_piece in bard:
                            if bard[insert_piece][0] != self.turn:
                                self.pieces[my_piece].append(insert_piece)
                                if insert_piece_2 in bard:
                                    if bard[insert_piece_2][0] != self.turn:
                                        self.pieces[my_piece].append(insert_piece_2)
                        elif insert_piece_2 in bard:
                            if bard[insert_piece_2][0] != self.turn:             # if right fail, still check left
                                self.pieces[my_piece].append(insert_piece_2)
                            else:
                                continue
                    elif num == (letters[mp0] - 1) or num == (letters[mp0] + 1):
                        insert_piece = letter + str(mp1 + 2)
                        insert_piece_2 = letter + str(mp1 - 2)
                        if insert_piece in bard:
                            if bard[insert_piece][0] != self.turn:
                                self.pieces[my_piece].append(insert_piece)
                                if insert_piece_2 in bard:
                                    if bard[insert_piece_2][0] != self.turn:  # if right fail, still check left
                                        self.pieces[my_piece].append(insert_piece_2)
                        elif insert_piece_2 in bard:
                            if bard[insert_piece_2][0] != self.turn:             # if right fail, still check left
                                self.pieces[my_piece].append(insert_piece_2)

            elif bishop_ in bard[my_piece]:
                for letter, num in letters.items():
                    # method is same eval as queen diagonal
                    if num < letters[mp0]:
                        difference = (letters[mp0] - num)
                        insert_piece = letter + str(mp1 + difference)
                        insert_piece_2 = letter + str(mp1 - difference)
                        if insert_piece in bard:
                            if bard[insert_piece][0] != self.turn:
                                self.pieces[my_piece].append(insert_piece)
                                if insert_piece_2 in bard:
                                    if bard[insert_piece_2][0] != self.turn:  # if right fail, still check left
                                        self.pieces[my_piece].append(insert_piece_2)
                        elif insert_piece_2 in bard:
                            if bard[insert_piece_2][0] != self.turn:             # if right fail, still check left
                                self.pieces[my_piece].append(insert_piece_2)
                            else:
                                continue

                    elif num > letters[mp0]:
                        difference = (num - letters[mp0])     # number var to add and subtract based on distance from og
                        insert_piece = letter + str(mp1 + difference)
                        insert_piece_2 = letter + str(mp1 - difference)
                        if insert_piece in bard:
                            if bard[insert_piece][0] != self.turn:
                                self.pieces[my_piece].append(insert_piece)
                                if insert_piece_2 in bard:
                                    if bard[insert_piece_2][0] != self.turn:  # if right fail, still check left
                                        self.pieces[my_piece].append(insert_piece_2)
                        elif insert_piece_2 in bard:
                            if bard[insert_piece_2][0] != self.turn:             # if right fail, still check left
                                self.pieces[my_piece].append(insert_piece_2)
                            else:
                                continue
        return


class ReturnVal:

    def __init__(self, pass_, thrt_list=[], end='no'):
        self.p_ass = pass_
        self.threat = thrt_list
        self.finish = end


class LeaveTurn:
    def __init__(self, t, w_t, b_k, board, pass_, end='no'):
        self.turn = t
        self.white = w_t
        self.black = b_k
        self.board = board
        self.p_ass = pass_
        self.finish = end


def game(trn, w, b, G_board):

    def check_mate(plr, kg, tn, bard):
        '''
        :param plr: class
        :param kg: class.king_location
        :param tn: turn
        :param bard: Game_board
        :return: True if check mate, False if simple check
        '''

        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}

        not_poss = 0  # incremented weather king is blocked or eval of possible move is True for being in check
        num_of_check = 0  # incremented on every check

        kg_0 = kg[0]
        kg_1 = int(kg[1])

        for letter, lett_val in letters.items():
            if kg_1 == 1:
                for num in range(kg_1, (kg_1 + 2)):
                    if lett_val == (letters[kg_0] - 1) or lett_val == letters[kg_0] or lett_val == (
                            letters[kg_0] + 1):
                        check_piece = letter + str(num)
                        if bard[check_piece][0] == tn:
                            not_poss += 1
                            num_of_check += 1
                        else:
                            check_this = king(tn, kg, kg_0, kg_1, check_piece, letter, num, bard)
                            if check_this.p_ass == 'yes':
                                if simple_check(check_piece, tn, bard):
                                    not_poss += 1
                                    num_of_check += 1
                                else:
                                    num_of_check += 1
            elif kg_1 == 8:
                for num in range((kg_1 - 1), kg_1):
                    if lett_val == (letters[kg[0]] - 1) or lett_val == letters[kg_0] or lett_val == (
                            letters[kg_0] + 1):
                        check_piece = letter + str(num)
                        if bard[check_piece][0] == tn:
                            not_poss += 1
                            num_of_check += 1
                        else:
                            check_this = king(tn, kg, kg_1, kg_0, check_piece, letter, num, bard)
                            if check_this.p_ass == 'yes':
                                if simple_check(check_piece, trn, bard):
                                    not_poss += 1
                                    num_of_check += 1
                                else:
                                    num_of_check += 1
            else:
                for num in range((kg_1 - 1), (kg_1 + 2)):
                    if lett_val == (letters[kg_0] - 1) or lett_val == letters[kg_0] or lett_val == (letters[kg_0] + 1):
                        check_piece = letter + str(num)
                        if bard[check_piece][0] == tn:
                            not_poss += 1
                            num_of_check += 1
                        else:
                            check_this = king(tn, kg, kg_0, kg_1, check_piece, letter, num, bard)
                            if check_this.p_ass == 'yes':
                                if simple_check(check_piece, tn, bard):
                                    not_poss += 1
                                    num_of_check += 1
                                else:
                                    num_of_check += 1

        # If the number of not_pass == num_of_checks
        # means no possible moves to get out of check
        if not_poss == num_of_check:
            if super_reverse_check_mate(plr, trn, board):
                return False
            else:
                plr.in_check_mate = True
                return True
        else:
            return False

    def simple_check_from_class(kg, tn, bard):
        '''checks if play is in check from '''
        '''kg-Player class object'''
        '''returns true if player in check, Flase if not'''

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        opp_trn = str

        # when possible move is checked
        #  opp_trn is to see if the opposite player can take your king
        if tn == 'w':
            opp_trn = 'b'
        elif tn == 'b':
            opp_trn == 'w'

        player_king = kg.king_location
        kg.check_threat = {}  # empties any previous check threats from prior moves

        # target index to eval which type of move
        pawn_ = 'p'
        rook_ = 'r'
        knight_ = 'k'
        bishop_ = 'bs'
        queen_ = 'q'
        king_ = 'kg'

        count = 0
        kg_0 = player_king[0]                                      # split king to be used a p0, p1 in move call
        kg_1 = int(player_king[1])

        for colum in letters:
            for row in range(1,9):
                check_piece = colum + str(row)
                if tn in bard[check_piece][0] or bard[check_piece] == "###" or bard[check_piece] == '***':
                    continue
                else:
                    if pawn_ in bard[check_piece]:
                        this_check = pawn(opp_trn, check_piece, colum, row, player_king, kg_0, kg_1, bard)
                        if this_check.p_ass == 'yes':
                            kg.check_threat[check_piece] = this_check.threat
                            count +=1
                        else:
                            continue
                    elif rook_ in bard[check_piece]:
                        this_check = rook(opp_trn, check_piece, colum, row, player_king, kg_0, kg_1, bard)
                        if this_check.p_ass == 'yes':
                            kg.check_threat[check_piece] = this_check.threat
                            count +=1

                        else:
                            continue
                    elif king_ in bard[check_piece]:
                        continue
                    elif queen_ in bard[check_piece]:
                        this_check = queen(opp_trn, check_piece, colum, row, player_king, kg_0, kg_1, bard)
                        if this_check.p_ass == 'yes':
                            kg.check_threat[check_piece] = this_check.threat
                            count += 1

                        else:
                            continue
                    elif bishop_ in bard[check_piece]:
                        this_check = bishop(opp_trn, check_piece, colum, row, player_king, kg_0, kg_1, bard)
                        if this_check.p_ass == 'yes':
                            kg.check_threat[check_piece] = this_check.threat
                            count += 1
                        else:
                            continue
                    elif knight_ in bard[check_piece]:
                        this_check = knight(opp_trn, check_piece, colum, row, player_king, kg_0, kg_1, bard)
                        if this_check.p_ass == 'yes':
                            kg.check_threat[check_piece] = this_check.threat
                            count += 1

                        else:
                            continue
                    else:
                        continue

        if count > 0:       # if one eval is True king is in check and must move
            return True
        if count == 0:
            return False

    def simple_check(kg, tn, bard):
        """
        :param kg: string piece on board, usually king
        :param tn: turn
        :param bard: Game_board
        :return: true if in check, false if not
        """

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        opp_trn = str

        # when possible move is checked
        #  opp_trn is to see if the opposite player can take your king
        if tn == 'w':
            opp_trn = 'b'
        elif tn == 'b':
            opp_trn == 'w'

        # When func is called from move() player_ should be a class obj
        # When func is called from within check_mate()
        # or inside take_piece()using an arbitrary king location
        # player_ is a string
        # player_king is created to hold these val

        pawn_ = 'p'
        rook_ = 'r'
        knight_ = 'k'
        bishop_ = 'bs'
        queen_ = 'q'
        king_ = 'kg'

        count = 0
        kg_0 = kg[0]
        kg_1 = int(kg[1])

        for colum in letters:
            for row in range(1,9):
                check_piece = colum + str(row)

                if tn in bard[check_piece] or bard[check_piece] == "###" or bard[check_piece] == '***':
                    continue
                else:
                    if tn not in bard[check_piece]:
                            # based on board[check_space] what piece to eval
                            if pawn_ in bard[check_piece]:
                                this_check = pawn(opp_trn, check_piece, colum, row, kg, kg_0, kg_1, bard)
                                if this_check.p_ass == 'yes':
                                    count +=1
                                else:
                                    continue

                            elif rook_ in bard[check_piece]:
                                this_check = rook(opp_trn, check_piece, colum, row, kg, kg_0, kg_1, bard)
                                if this_check.p_ass == 'yes':
                                    count +=1
                                else:
                                    continue

                            elif king_ in bard[check_piece]:
                                this_check = king(opp_trn, check_piece, colum, row, kg, kg_0, kg_1, bard)
                                if this_check.p_ass == 'yes':
                                    count += 1
                                else:
                                    continue

                            if queen_ in bard[check_piece]:
                                this_check = queen(opp_trn, check_piece, colum, row, kg, kg_0, kg_1, bard)
                                if this_check.p_ass == 'yes':
                                    count += 1
                                else:
                                    continue

                            elif bishop_ in bard[check_piece]:
                                this_check = bishop(opp_trn, check_piece, colum, row, kg, kg_0, kg_1, bard)
                                if this_check.p_ass == 'yes':
                                    count += 1
                                else:
                                    continue

                            elif knight_ in bard[check_piece]:
                                this_check = knight(opp_trn, check_piece, colum, row, kg, kg_0, kg_1, bard)
                                if this_check.p_ass == 'yes':
                                    count += 1
                                else:
                                    continue

        if count > 0:       # if one eval is True king is in check and must move
            return True
        if count == 0:
            return False

    def super_reverse_check_mate(plr, tn,  bard):
        """Evaluaes every possible move for """
        '''class object, turn, Game_board'''
        '''returns true if piece can block king from check Mate. Flase if not'''

        pawn_ = 'p'
        rook_ = 'r'
        knight_ = 'k'
        bishop_ = 'bs'
        queen_ = 'qn'
        king_ = 'kg'
        kg = plr.king_location

        # or have to write all new functions
        for my_piece in plr.pieces.keys():
            m0 = my_piece[0]
            m1 = my_piece[1]

            for threat_name in plr.check_threat.keys():

                for possible in plr.pieces[my_piece]:
                    if threat_name == possible:
                        place_holder = '###'
                        temp_board = dict(bard)
                        temp_board[threat_name] = temp_board[possible]
                        temp_board[possible] = place_holder
                        if simple_check(kg, tn, temp_board):
                            continue
                        else:
                            return True
                    else:
                        continue

                for in_between in plr.check_threat[threat_name]:
                    i0 = in_between[0]
                    i1 = in_between[1]

                    if king_ in board[my_piece]:
                        continue

                    elif pawn_ in board[my_piece]:
                        this_check = pawn(tn, my_piece, m0, m1, in_between, i0, i1, bard)
                        if this_check.p_ass == 'yes':
                            place_holder = '###'
                            temp_board = dict(bard)
                            temp_board[in_between] = temp_board[my_piece]
                            temp_board[my_piece] = place_holder
                            if simple_check(kg, tn, temp_board):
                                continue
                            else:
                                return True
                        else:
                            continue

                    elif rook_ in bard[my_piece]:
                        this_check = rook(tn, my_piece, m0, m1, in_between, i0, i1, bard)
                        if this_check.p_ass == 'yes':
                            place_holder = '###'
                            temp_board = dict(board)
                            temp_board[in_between] = temp_board[my_piece]
                            temp_board[my_piece] = place_holder
                            if simple_check(kg, tn, temp_board):
                                continue
                            else:
                                return True
                        else:
                            continue

                    elif knight_ in bard[my_piece]:
                        this_check = knight(tn, my_piece, m0, m1, in_between, i0, i1, bard)
                        if this_check.p_ass == 'yes':
                            place_holder = '###'
                            temp_board = dict(board)
                            temp_board[in_between] = temp_board[my_piece]
                            temp_board[my_piece] = place_holder
                            if simple_check(kg, tn, temp_board):
                                continue
                            else:
                                return True
                        else:
                            continue

                    elif bishop_ in bard[my_piece]:
                        this_check = bishop(tn, my_piece, m0, m1, in_between, i0, i1, bard)
                        if this_check.p_ass == 'yes':
                            place_holder = '###'
                            temp_board = dict(board)
                            temp_board[in_between] = temp_board[my_piece]
                            temp_board[my_piece] = place_holder
                            if simple_check(kg, trn, temp_board):
                                continue
                            else:
                                return True
                        else:
                            continue

                    elif queen_ in board[my_piece]:
                        this_check = queen(tn, my_piece, m0, m1, in_between, i0, i1, bard)
                        if this_check.p_ass == 'yes':
                            place_holder = '###'
                            temp_board = dict(board)
                            temp_board[in_between] = temp_board[my_piece]
                            temp_board[my_piece] = place_holder
                            if simple_check(kg, trn, temp_board):
                                continue
                            else:
                                return True
                        else:
                            continue


            return False
        return False

    def start_move(t, player_1, player_2, bard):
        """
        :param t: Trun
        :param player_1: White
        :param player_2: Black
        """

        # lines 694 players turn is set up, aslo weather player in Check
        # create sing value of player based on current turn
        # used to pass through check/check mate eval
        if trn == 'w':
            player_go = player_1
            kng = player_go.king_location
        elif trn == 'b':
            player_go = player_2
            kng = player_go.king_location
        # lines 704-720 players turn is set up, aslo weather player in Check
        if simple_check_from_class(player_go, t, bard):          # if player's king is vulnerable
            player_go.in_check = True
            if check_mate(player_go, kng, t, bard):             # if player's king is in check mate
                return LeaveTurn(t, player_1, player_2, bard, 'no', 'yes')
            else:
                player_go.in_check_mate = False
                move_return = moving(t, player_1, player_2, bard)
                if move_return.p_ass == 'yes':
                    return LeaveTurn(t, player_1, player_2, bard, 'yes')
                else:
                    return LeaveTurn(t, player_1, player_2, bard, 'no')

        else:
            player_go.in_check = False
            move_return = moving(t, player_1, player_2, bard)
            if move_return.p_ass == 'yes':
                return LeaveTurn(t, player_1, player_2, bard, 'yes')
            else:
                return LeaveTurn(t, player_1, player_2, bard, 'no')

    def moving(tn, plr1, plr2, bard):
        '''
        :param tn: turn
        :param plr1: White
        :param plr2: Black
        :param bard: Game_board
        :return: if eval works, take_piece() will change board and approve move then return object.p_ass yes or no.
        '''

        pawn_ = 'p'
        rook_ = 'r'
        knight_ = 'k'
        bishop_ = 'bs'
        queen_ = 'qn'
        king_ = 'kg'
        choose_piece = input('What piece would you like to move?\n').upper()
        direction = input('Where do you want to move? \n').upper()
        try:
            if tn in bard[choose_piece][0]:
                if choose_piece in bard:
                    if direction in bard:

                        """Based on Game_board[choose_piece][1] contitional
                            will send data to corresponding functin to
                            evaluate wether possible move is legal"""

                        choose_0 = choose_piece[0]
                        choose_1 = int(choose_piece[1])
                        direction_0 = direction[0]
                        direction__1 = int(direction[1])

                        if pawn_ in bard[choose_piece]:
                            this_check = pawn(tn, choose_piece, choose_0, choose_1, direction, direction_0,
                                                  direction__1, bard)
                            if this_check.p_ass == 'yes':
                                if take_piece(tn, choose_piece, direction, plr1, plr2, bard):
                                    return ReturnVal('yes')
                                else:
                                    return ReturnVal('no')

                            else:
                                return ReturnVal('no')

                        elif rook_ in bard[choose_piece]:
                            this_check = rook(tn, choose_piece, choose_0, choose_1, direction, direction_0,
                                                direction__1, bard)
                            if this_check.p_ass == 'yes':
                                    if take_piece(tn, choose_piece, direction, plr1, plr2, bard):
                                        return ReturnVal('yes')
                                    else:
                                        return ReturnVal('no')

                            else:
                                return ReturnVal('no')

                        elif king_ in bard[choose_piece]:
                            this_check = king(trn, choose_piece, choose_0, choose_1, direction, direction_0,
                                                direction__1, bard)
                            if this_check.p_ass == 'yes':
                                if take_piece(tn, choose_piece, direction, plr1, plr2, bard):
                                    return ReturnVal('yes')
                                else:
                                    return ReturnVal('no')

                            else:
                                return ReturnVal('no')

                        elif queen_ in bard[choose_piece]:
                            this_check = queen(tn, choose_piece, choose_0, choose_1, direction, direction_0,
                                                direction__1, bard)
                            if this_check.p_ass == 'yes':
                                if take_piece(tn, choose_piece, direction, plr1, plr2, bard):
                                    return ReturnVal('yes')
                                else:
                                    return ReturnVal('no')

                            else:
                                return ReturnVal('no')

                        elif knight_ in bard[choose_piece]:
                            this_check = knight(tn, choose_piece, choose_0, choose_1, direction, direction_0,
                                                direction__1, bard)
                            if this_check.p_ass == 'yes':
                                if take_piece(tn, choose_piece, direction, plr1, plr2, bard):
                                    return ReturnVal('yes')
                                else:
                                    return ReturnVal('no')

                            else:
                                return ReturnVal('no')

                        elif bishop_ in bard[choose_piece]:
                            this_check = bishop(tn, choose_piece, choose_0, choose_1, direction, direction_0,
                                                direction__1, bard)
                            if this_check.p_ass == 'yes':
                                if take_piece(tn, choose_piece, direction, plr1, plr2, bard):
                                    return ReturnVal('yes')
                                else:
                                    return ReturnVal('no')
                            else:
                                return ReturnVal('no')

                        else:
                            return ReturnVal('no')
                    else:
                        return ReturnVal('no')
                else:
                    return ReturnVal('no')
            else:
                return ReturnVal('no')
        except KeyError:
            print('There was an error in piece or direction.\nPlease try again.\n\n')
            return ReturnVal('no')

    def take_piece(trn_, p, d, player_1, player_2, bard):
        '''
        :param trn_: turn
        :param p: choose_piece
        :param d: direction
        :param player_1: White
        :param player_2: Black
        :param bard: Game_board
        :return: True or False. Also board is chenged to complete turn if returning True
        '''

        def pawn_queen(tn, p, d, b_ard):
            '''
            :param tn: turn
            :param p: pawn
            :param d: piece at either location 1 or 8
            :param b_ard: Game_board (board)
            :return: True if piece is legal. Game_board changed. pawn become queen
            '''

            # copy of the dict Game_board is set
            # to the value of IF the move was completed
            place_holder = '###'
            temp_board = dict(b_ard)
            temp_board[d] = (tn + 'qn')
            temp_board[p] = place_holder

            star_ = ['A1', 'C1', 'E1', 'G1', 'B2', 'D2', 'F2', 'H2', 'A3', 'C3', 'E3', 'G3', 'B4', 'D4', 'F4', 'H4',
                     'A5', 'C5', 'E5', 'G5', 'B6', 'D6', 'F6', 'H6', 'A7', 'C7', 'E7', 'G7', 'B8', 'D8', 'F8', 'H8']

            hash_ = ['B1', 'D1', 'F1', 'H1', 'A2', 'C2', 'E2', 'G2', 'B3', 'D3', 'F3', 'H3', 'A4', 'C4', 'E4', 'G4',
                     'B5', 'D5', 'F5', 'H5', 'A6', 'C6', 'E6', 'G6', 'B7', 'D7', 'F7', 'H7', 'A8', 'C8', 'E8', 'G8']

            if tn == 'w':
                player_go_ = player_1
                go_king_ = player_1.king_location
            elif tn == 'b':
                player_go_ = player_2
                go_king_ = player_2.king_location

            if not simple_check(go_king_, tn, temp_board):
                if p in hash_:
                    player_go_.capture.append(b_ard[d])
                    b_ard[d] = (tn + 'qn')
                    b_ard[p] = '###'
                    return True

                elif p in star_:
                    player_go_.capture.append(b_ard[d])
                    b_ard[d] = (tn + 'qn')
                    b_ard[p] = '***'
                    return True

            else:
                return False

        if bard[p][0] == 'w' and bard[p][1] == 'p' and int(d[1]) == 8:  # if w pawn becoming queen
            if pawn(trn_, p, p[0], int(p[1]), d, d[0], int(d[1]), bard):
                return pawn_queen(trn_, p, d, bard)
        elif bard[p][0] == 'b' and bard[p][1] == 'p' and int(d[1]) == 1:  # if b pawn becoming queen
            if pawn(trn_, p, p[0], int(p[1]), d, d[0], int(d[1]), bard):
                return pawn_queen(trn_, p, d, bard)

        # copy of the dict Game_board is set
        # to the value of IF the move was completed
        place_holder = '###'
        temp_board = dict(bard)
        temp_board[d] = temp_board[p]
        temp_board[p] = place_holder

        star_ = ['A1', 'C1', 'E1', 'G1', 'B2', 'D2', 'F2', 'H2', 'A3', 'C3', 'E3', 'G3', 'B4', 'D4', 'F4', 'H4',
                'A5', 'C5', 'E5', 'G5', 'B6', 'D6', 'F6', 'H6', 'A7', 'C7', 'E7', 'G7', 'B8', 'D8', 'F8', 'H8']

        hash_ = ['B1', 'D1', 'F1', 'H1', 'A2', 'C2', 'E2', 'G2', 'B3', 'D3', 'F3', 'H3', 'A4', 'C4', 'E4', 'G4',
                'B5', 'D5', 'F5', 'H5', 'A6', 'C6', 'E6', 'G6', 'B7', 'D7', 'F7', 'H7', 'A8', 'C8', 'E8', 'G8']

        # depending on trn that is witch player is being evaled
        if trn_ == 'w':
            player_go = player_1
            go_king = player_1.king_location
        elif trn == 'b':
            player_go = player_2
            go_king = player_2.king_location

        if bard[p] == bard[go_king]:
            if not simple_check(d, trn_, temp_board):     # if move doesn't put you in check
                if p in hash_:
                    player_go.capture.append(bard[d])
                    bard[d] = bard[p]
                    bard[p] = '###'
                    return True

                elif p in star_:
                    player_go.capture.append(bard[d])
                    bard[d] = bard[p]
                    bard[p] = '***'
                    return True
            else:
                return False
        else:
            if not simple_check_from_class(player_go, trn_, temp_board):  # if move doesn't put you in check
                if p in hash_:
                    player_go.capture.append(bard[d])
                    bard[d] = bard[p]
                    bard[p] = '###'
                    return True

                elif p in star_:
                    player_go.capture.append(bard[d])
                    bard[d] = bard[p]
                    bard[p] = '***'
                    return True
            else:
                return False

    def pawn(tn, p, p0, p1, d, d0, d1, bard):
        """
        :param tn: turn
        :param p: choose_piece
        :param p0: letter @ choose_piece[0]
        :param p1: number at choose_piece[1]
        :param d: direction
        :param d0: direction[0]
        :param d1: direction[1]
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """

        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

        if tn == 'w':
            incremnt = 1        # var to be added to p to see if move is pawns first?
            dbl_inc = 2         # if p is moving 2 on its first move
            start = 2           # position to for 'w'
        elif tn == 'b':
            incremnt = -1       # var to be added to p to see if move is pawns first?
            dbl_inc = -2        # if p is moving 2 on its first move
            start = 7           # position to for 'b'

        if bard[d][0] != tn and tn == bard[p][0]:
            if p1 == start:                                             # pawn's first move can opt for 2 spaces
                if d1 == p1 + incremnt or d1 == p1 + dbl_inc:           # if piece is moving 1 or 2 spaces
                    if p0 == d0:                                        # if pawn is moving forward
                        if bard[d] == "###" or bard[d] == '***':
                            return ReturnVal('yes')

                        else:
                            return ReturnVal('no')
                    elif p0 != d0 and d1 == p1 + incremnt:                  # if pawn is taking piece on first move
                        for letter, num in letters.items():
                            if p0 == letter:
                                if letters[p0] == letters['A']:
                                    if bard[d] != '###' or bard[d] != '***':
                                        if p0 == letter and letters[d0] == (letters[p0] + 1):
                                            if bard[d][0] != tn:
                                                return ReturnVal('yes', [d])
                                            else:
                                                return ReturnVal('no')
                                        else:
                                            return ReturnVal('no')
                                    else:
                                        return ReturnVal('no')

                                elif letters[p0] == letters['H']:                        # letter is 'H'
                                    if bard[d] != '###' or bard[d] != '***':
                                        if p0 == letter and letters[d0] == (letters[p0] - 1):
                                            if bard[d][0] != tn:
                                                return ReturnVal('yes', [d])
                                            else:
                                                return ReturnVal('no')
                                        else:
                                            return ReturnVal('no')
                                    else:
                                        return ReturnVal('no')

                                elif letters[p0] != letters['A'] or letters[p0] != letters['H']:  # inside A and H range
                                    if bard[d] != '###' or bard[d] != '***':
                                        if p0 == letter and letters[d0] == (letters[p1] + 1) or \
                                                p0 == letter and letters[d0] == (letters[p0] - 1):
                                            if bard[d][0] != trn:
                                                return ReturnVal('yes', [d])
                                            else:
                                                return ReturnVal('no')
                                        else:
                                            return ReturnVal('no')
                                    else:
                                        return ReturnVal('no')
                                else:
                                    return ReturnVal('no')
                            else:
                                continue
                    else:
                        return ReturnVal('no')

                else:
                    return ReturnVal('no')
            elif p0 != d0:                                                  # piece moving diagonal
                for letter, num in letters.items():
                    if p0 == letter:
                        if '***' != bard[d] != '###':
                            if letters[p0] == letters['A']:                              # letter is 'A'
                                if letters[d0] == (letters[p0] + 1):
                                    if bard[d][0] != tn:
                                        return ReturnVal('yes', [d])
                                    else:
                                        return ReturnVal('no')
                                else:
                                    return ReturnVal('no')

                            elif letters[p0] == letters['H']:                            # letter is 'H'
                                if letters[d0] == (letters[p0] - 1):
                                    if bard[d][0] != tn:
                                        return ReturnVal('yes', [d])
                                    else:
                                        return ReturnVal('no')
                                else:
                                    return ReturnVal('no')

                            elif letters[p0] != letters['A'] or p0 != letters['H']:          # inside A and H range
                                if letters[d0] == (letters[p0] + 1) or letters[d0] == (letters[p0] - 1):
                                    if bard[d][0] != tn:
                                        return ReturnVal('yes', [d])
                                    else:
                                        return ReturnVal('no')
                                else:
                                    return ReturnVal('no')
                            else:
                                return ReturnVal('no')
                        else:
                            return ReturnVal('no')
                    else:
                        continue
            elif p0 == d0 and p1 + incremnt == d1:                                  # if pawn is moving forward
                if bard[d] == "###" or bard[d] == '***':
                    return ReturnVal('yes')
                else:
                    return ReturnVal('no')
            else:
                return ReturnVal('no')
        return ReturnVal('no')

    def rook(tn, p, p0, p1, d, d0, d1, bard):
        """
        :param tn: Turn
        :param p: choose_piece
        :param p0: choose_piece[0]
        :param p1: choose_piece[1]
        :param d: direction
        :param d0: direction[0]
        :param d1: direction[1]
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}
        if p0 == d0:                                                    # if rook is moving forward
            if p1 < d1:                                                 # if piece moving up the board
                check_this = move_forward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)
            elif p1 > d1:                                               # if rook is moving down board
                check_this = move_downward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)
            else:
                return ReturnVal('no')

        elif p1 == d1:                                                  # if rook is moving sideways
            if letters[p0] < letters[d0]:                               # if piece moving up the board
                check_this = move_forward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)
            elif letters[p0] > letters[d0]:                             # if rook is moving down board
                check_this = move_downward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)
            else:
                return ReturnVal('no')
        else:
            return ReturnVal('no')

    def knight(tn, p, p0, p1, d, d0, d1, bard):
        """
        :param tn: turn
        :param p: choose_piece
        :param p0: choose_piece[0]
        :param p1: choose_piece[1]
        :param d: direction
        :param d0: direction[0]
        :param d1: direction[1]
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        def knight_check(t, x, b_ard):                  # final check on knight eval (reduce redundancy)
            ''' turn, direction, Game_board'''
            if b_ard[x][0] != t:
                return ReturnVal('yes', [d])
            else:
                return ReturnVal('no')

        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}                                   # to evaluate letter using in base 10

        # FORWARD RIGHT
        if (p1 + 2) == d1:                                   # if piece is moving upward
            if (letters[p0] + 1) == letters[d0]:         # if the piece is moving to the right one

                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)
            elif (letters[p0] - 1) == letters[d0]:       # if the piece is moving to the left
                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)

            else:
                return ReturnVal('no')
        # FORWARD LEFT
        elif (p1 - 2) == d1:                                 # if piece is moving downward
            if (letters[p0] + 1) == letters[d0]:         # if the piece is moving to the right one
                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)

            elif (letters[p0] - 1) == letters[d0]:       # if the piece is moving to the left one
                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)

            else:
                return ReturnVal('no')
        # RIGHT
        elif (p1 + 1) == d1:                                # if piece is moving right or left and up one
            if (letters[p0] + 2) == letters[d0]:        # if piece is moving to the right two
                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)

            elif (letters[p0] - 2) == letters[d0]:      # if piece is moving to the left
                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)

            else:
                return ReturnVal('no')
        # LEFT
        elif (p1 - 1) == d1:                                # if piece is moving right or left and down one
            if (letters[p0] + 2) == letters[d0]:        # if piece is moving to the right
                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)

            elif (letters[p0] - 2) == letters[d0]:      # if piece is moving to the left
                check_this = knight_check(tn, d, bard)
                return ReturnVal(check_this.p_ass, check_this.threat)

            else:
                return ReturnVal('no')
        else:
            return ReturnVal('no')

    def bishop(tn, p, p0, p1, d, d0, d1, bard):
        """
        :param tn: turn
        :param p: choose_piece
        :param p0: choose_piece[0]
        :param p1: choose_piece[1]
        :param d: direction
        :param d0: direction[0]
        :param d1: direction[1]
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}                                      # to evaluate letter using in base 10

        if bard[p][0] == tn != bard[d][0]:
            if p1 < d1:                                         # if piece is moving forward
                if letters[p0] > letters[d0]:                   # if piece is moving to the left
                    check_this = move_left_up(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)
                elif letters[p0] < letters[d0]:                 # if piece is moving to the right
                    check_this = move_right_up(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)
                else:
                    return ReturnVal('no')
            elif p1 > d1:                                       # if piece is moving backwards (down)
                if letters[p0] > letters[d0]:                   # if piece is moving to the left
                    check_this = move_left_down(p, d, trn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)
                elif letters[p0] < letters[d0]:                 # if piece is moving to the right
                    check_this = move_right_down(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)
                else:
                    return ReturnVal('no')
            else:
                return ReturnVal('no')
        else:
            return ReturnVal('no')

    def queen(tn, p, p0, p1, d, d0, d1, bard):
        """
        :param tn: turn
        :param p: choose_piece
        :param p0: choose_piece[0]
        :param p1: choose_piece[1]
        :param d: direction
        :param d0: direction[0]
        :param d1: direction[1]
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """

        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}                                          # to evaluate letter using in base 10

        if p0 == d0:                                                # if queen is moving up or down
            if p1 < d1:                                             # if piece moving up the board
                check_this = move_forward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass,check_this.threat)

            elif p1 > d1:                                           # if piece is moving down the board
                check_this = move_downward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass,check_this.threat)

            else:
                return ReturnVal('no')
        elif p1 == d1:                                              # if queen is moving sideways
            check_this = move_sideways(p, d, tn, bard)                  # function handles both left and right
            return ReturnVal(check_this.p_ass, check_this.threat)

        elif p0 != d0 and p1 != d1:                                 # if piece is moving diagonal
            if p1 < d1:                                             # if piece is moving forward
                if letters[p0] > letters[d0]:                       # if piece is moving to left
                    check_this = move_left_up(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)

                elif letters[p0] < letters[d0]:                     # if piece is moving to the right
                    check_this = move_right_up(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)

                else:
                    return ReturnVal('no')
            elif p1 > d1:                                           # if piece is moving down board
                if letters[p0] > letters[d0]:                       # if piece is moving to the left
                    check_this = move_left_down(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)

                elif letters[p0] < letters[d0]:                     # if piece is moving to the right
                    check_this = move_right_down(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass, check_this.threat)

                else:
                    return ReturnVal('no')
            else:
                return ReturnVal('no')
        else:
            return ReturnVal('no')

    def king(tn, p, p0, p1, d, d0, d1, bard):
        """
        :param tn: turn
        :param p: choose_piece
        :param p0: choose_piece[0]
        :param p1: choose_piece[1]
        :param d: direction
        :param d0: direction[0]
        :param d1: direction[1]
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}                                                  # to evaluate letter using in base 10

        # king can only move one space at a time

        if p0 == d0:                                                        # if king is moving up or down
            if p1 + 1 == d1:                                                # if king is moving forward
                check_this = move_forward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass)
            elif p1 - 1 == d1:                                              # if king is moving down
                check_this = move_downward(p, d, tn, bard)
                return ReturnVal(check_this.p_ass)
            else:
                return ReturnVal('no')

        elif p1 == d1:                                                      # if king is moving sideways:
            if letters[p0] + 1 == letters[d0] or letters[p0] - 1 == letters[d0]:  # if king is moving one space
                check_this = move_sideways(p, d, tn, bard)
                return ReturnVal(check_this.p_ass)
            else:
                return ReturnVal('no')
        elif p1 != d1 and letters[p0] != letters[d0]:                       # if king is moving diagonally
            if p1 + 1 == d1:                                                # if piece is moving forward
                if letters[p0] - 1 == letters[d0]:                          # if piece is moving to left
                    check_this = move_left_up(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass)
                elif letters[p0] + 1 == letters[d0]:                        # if piece is moving to the right
                    check_this = move_right_up(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass)
                else:
                    return ReturnVal('no')
            elif p1 - 1 == d1:                                              # if piece is moving down board
                if letters[p0] - 1 == letters[d0]:                          # if piece is moving to the left
                    check_this = move_left_down(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass)
                elif letters[p0] + 1 == letters[d0]:                        # if piece is moving to the right
                    check_this = move_right_down(p, d, tn, bard)
                    return ReturnVal(check_this.p_ass)
                else:
                    return ReturnVal('no')
            else:
                return ReturnVal('no')

    def move_sideways(p, d, tn, bard):
        """
        :param p: choose_piece
        :param d: direction
        :param tn: turn
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters_revr = {'H': 7, 'G': 6, 'F': 5, 'E': 4, 'D': 3, 'C': 2, 'B': 1,
                        'A': 0}
        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}

        p0 = letters[p[0]]
        p1 = int(p[1])
        d0 = letters[d[0]]
        hold_in_between = []
        if p0 < d0:                                                      # if p is moving from left to right
            for letter, number in letters.items():
                check_piece = letter + str(p1)
                if number <= p0:
                    continue
                elif p0 < number <= d0:
                    if check_piece == d:
                        if bard[d][0] != tn:
                            return ReturnVal('yes', hold_in_between)
                        else:
                            return ReturnVal('no')
                    elif bard[check_piece] == '###' or bard[check_piece] == '***':      # is space is free to move
                        hold_in_between.append(check_piece)
                        continue
                    elif check_piece != d or bard[check_piece] != '###' \
                            or bard[check_piece] != '***':                               # if path is blocked
                        return ReturnVal('no')
                else:
                    return ReturnVal('no')
        elif p0 > d0:                                                   # if p is moving right to left
            for letter, number in letters_revr.items():
                check_piece = letter + str(p1)
                if number >= p0:
                    continue
                elif p0 > number >= d0:
                    if check_piece == d:  # if final check
                        if bard[d][0] != trn:  # if d is not your piece
                            return ReturnVal('yes', hold_in_between)
                        else:
                            return ReturnVal('no')
                    elif bard[check_piece] == '###' or bard[check_piece] == '***':  # is space free to move
                        hold_in_between.append(check_piece)
                        continue
                    elif check_piece != d or bard[check_piece] != '###' \
                            or bard[check_piece] != '***':  # if path is blocked
                        return ReturnVal('no')
                    else:
                        return ReturnVal('no')
                else:
                    return ReturnVal('no')
        else:
            return ReturnVal('no')

    def move_left_up(p, d, tn, bard):
        """
        :param p: choose_piece
        :param d: direction
        :param tn: turn
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters_revr = {'H': 7, 'G': 6, 'F': 5, 'E': 4, 'D': 3, 'C': 2, 'B': 1,
                        'A': 0}

        d1 = int(d[1])
        p1 = int(p[1])
        hold_in_between = []
        check_num = p1 + 1
        for letter, number in letters_revr.items():
            if number < letters_revr[p[0]]:
                check_piece = letter + str(check_num)
                if p1 < check_num <= d1:
                    if check_piece == d:
                        if bard[d][0] != tn:
                            return ReturnVal('yes', hold_in_between)
                        else:
                            return ReturnVal('no')
                    elif bard[check_piece] == "###" or bard[check_piece] == "***":
                        hold_in_between.append(check_piece)
                        check_num += 1
                    elif check_piece != d or bard[check_piece] != "###" or bard[check_piece] != "***":
                        return ReturnVal('no')
                elif number > d1:
                    return ReturnVal('no')
            else:
                continue
        return ReturnVal('no')

    def move_right_up(p, d, tn, bard):
        """
        :param p: choose_piece
        :param d: direction
        :param tn: turn
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                   'H': 7}

        d1 = int(d[1])
        p1 = int(p[1])
        hold_in_between = []
        check_num = p1 + 1
        for letter, number in letters.items():
            if number > letters[p[0]]:
                check_piece = letter + str(check_num)
                if p1 < check_num <= d1:
                    if check_piece == d:
                        if bard[d][0] != tn:
                            return ReturnVal('yes', hold_in_between)
                        else:
                            return ReturnVal('no')
                    elif bard[check_piece] == "###" or bard[check_piece] == "***":  # if space is open.. move
                        hold_in_between.append(check_piece)
                        check_num += 1
                    elif check_piece != d and bard[check_piece] != "###" and bard[check_piece] != "***":
                        return ReturnVal('no')
                elif number > d1:
                    return ReturnVal('no')
            else:
                continue
        return ReturnVal('no')

    def move_forward(p, d, tn, bard):
        """
        :param p: choose_piece
        :param d: direction
        :param tn: turn
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        p1 = int(p[1])
        d1 = int(d[1])

        hold_in_between = []
        for num in range(p1, d1 + 1):
            check_piece = p[0] + str(num)
            if num == p1:
                continue
            elif d1 >= num > p1:
                if bard[check_piece] == bard[d]:
                    if bard[d][0] != tn:
                        return ReturnVal('yes', hold_in_between)
                    else:
                        return ReturnVal('no')
                elif bard[check_piece] == "###" or bard[check_piece] == "***":  # Open space.. move
                    hold_in_between.append(check_piece)
                    continue
                elif bard[check_piece] != bard[d] and bard[check_piece] != '###' \
                        or bard[check_piece] != '***':             # if block path by your own piece
                    return ReturnVal('no')
                else:
                    return ReturnVal('no')
        return ReturnVal('no')

    def move_downward(p, d, tn, bard):
        """
        :param p: choose_piece
        :param d: direction
        :param tn: turn
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        numbers = [8, 7, 6, 5, 4, 3, 2, 1]

        p1 = int(p[1])
        d1 = int(d[1])
        hold_in_between = []
        for num in numbers:
            check_piece = p[0] + str(num)
            if num >= p1:
                continue
            elif d1 <= num < p1:
                if num == p1:
                    continue
                else:
                    if check_piece == d:
                        if bard[d][0] != tn:
                            return ReturnVal('yes', hold_in_between)
                        else:
                            return ReturnVal('no')
                    elif bard[check_piece] == "###" or bard[check_piece] == "***":  # Open space.. move
                        hold_in_between.append(check_piece)
                        continue
                    elif check_piece != d or bard[check_piece] != '###' \
                            or bard[check_piece] != '***':         # if path is blocked by your own piece

                        return ReturnVal('no')
            else:
                return ReturnVal('no')

    def move_left_down(p, d, tn, bard):
        """
        :param p: choose_piece
        :param d: direction
        :param tn: turn
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters_revr = {'H': 7, 'G': 6, 'F': 5, 'E': 4, 'D': 3, 'C': 2, 'B': 1,
                        'A': 0}

        d1 = int(d[1])
        p1 = int(p[1])
        hold_in_between = []
        check_num = p1 - 1
        for letter, number in letters_revr.items():
            if number < letters_revr[p[0]]:
                check_piece = letter + str(check_num)
                if p1 > check_num >= d1:
                    if check_piece == d:
                        if bard[d][0] != tn:
                            return ReturnVal('yes', hold_in_between)
                        else:
                            return ReturnVal('no')
                    elif bard[check_piece] == "###" or bard[check_piece] == "***":
                        hold_in_between.append(check_piece)
                        check_num -= 1
                    elif check_piece != d or bard[check_piece] != "###" or bard[check_piece] != "***":
                        return ReturnVal('no')
                elif number < d1:
                    return ReturnVal('no')
            else:
                continue
        return ReturnVal('no')

    def move_right_down(p, d, tn, bard):
        """
        :param p: choose_piece
        :param d: direction
        :param tn: turn
        :param bard: Game_board
        :return: object.p_ass yes or no if move is legal
        """
        letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,'H': 7}

        d1 = int(d[1])
        p1 = int(p[1])
        hold_in_between = []
        check_num = p1 - 1
        for letter, number in letters.items():
            if number > letters[p[0]]:
                check_piece = letter + str(check_num)
                if p1 > check_num >= d1:
                    if check_piece == d:
                        if bard[d][0] != tn:
                            return ReturnVal('yes', hold_in_between)
                        else:
                            return ReturnVal('no')
                    elif bard[check_piece] == "###" or bard[check_piece] == "***":
                        hold_in_between.append(check_piece)
                        check_num -= 1
                    elif check_piece != d and bard[check_piece] != "###" and bard[check_piece] != "***":
                        return ReturnVal('no')
                elif number > d1:
                    return ReturnVal('no')
            else:
                continue
        return ReturnVal('no')

    on_switch = True
    while on_switch:                                        # call turn until return p_ass == 'yes
        print_board()
        move_response = start_move(trn, w, b, G_board)
        if move_response.finish == 'no':                    # if player is not in check mate
            if move_response.p_ass == 'yes':                # if prior move was legal
                print("valid move.")
                if trn == 'w':
                    trn_x = 'b'
                elif trn == 'b':
                    trn_x = 'w'
                on_switch = False
            elif move_response.p_ass == 'no':               #stay in loop and recall move
                print('Invalid move. Please try again')
                on_switch = True
        elif move_response.finish == 'yes':                 # if player is nin check mate (game is over)
            return LeaveTurn(trn, w, b, G_board, 'no', 'yes')
    return LeaveTurn(trn_x, w, b, G_board, 'yes')

# Game_board is dict containing
# key: space name on board
# val: player's piece or open space occupying key


Game_board = {    'A8': 'br1','B8': 'bk1','C8': 'bbs','D8': 'bkg','E8': 'bqn','F8': 'bbs','G8': 'bk2','H8': 'br2',
                  'A7': 'bp1','B7': 'bp2','C7': 'bp3','D7': 'bp4','E7': 'bp5','F7': 'bp6','G7': 'bp7','H7': 'bp8',
                  'A6': '###','B6': '***','C6': '###','D6': '***','E6': '###','F6': '***','G6': '###','H6': '***',
                  'A5': '***','B5': '###','C5': '***','D5': '###','E5': '***','F5': '###','G5': '***','H5': '###',
                  'A4': '###','B4': '***','C4': '###','D4': '***','E4': '###','F4': '***','G4': '###','H4': '***',
                  'A3': '***','B3': '###','C3': '***','D3': '###','E3': '***','F3': '###','G3': '***','H3': '###',
                  'A2': 'wp1','B2': 'wp2','C2': 'wp2','D2': 'wp4','E2': 'wp5','F2': 'wp6','G2': 'wp7','H2': 'wp8',
                  'A1': 'wr1','B1': 'wk1','C1': 'wbs','D1': 'wkg','E1': 'wqn','F1': 'wbs','G1': 'wk2','H1': 'wr2' }


def print_board():
    print(
        Game_board['A8'] + '|' + Game_board['B8'] + '|' + Game_board['C8'] + '|' + Game_board['D8'] + '|' +
        Game_board[
            'E8'] + '|' + Game_board['F8'] + '|' + Game_board['G8'] + '|' + Game_board['H8'])
    print(
        Game_board['A7'] + '|' + Game_board['B7'] + '|' + Game_board['C7'] + '|' + Game_board['D7'] + '|' +
        Game_board[
            'E7'] + '|' + Game_board['F7'] + '|' + Game_board['G7'] + '|' + Game_board['H7'])
    print(
        Game_board['A6'] + '|' + Game_board['B6'] + '|' + Game_board['C6'] + '|' + Game_board['D6'] + '|' +
        Game_board[
            'E6'] + '|' + Game_board['F6'] + '|' + Game_board['G6'] + '|' + Game_board['H6'])
    print(
        Game_board['A5'] + '|' + Game_board['B5'] + '|' + Game_board['C5'] + '|' + Game_board['D5'] + '|' +
        Game_board[
            'E5'] + '|' + Game_board['F5'] + '|' + Game_board['G5'] + '|' + Game_board['H5'])
    print(
        Game_board['A4'] + '|' + Game_board['B4'] + '|' + Game_board['C4'] + '|' + Game_board['D4'] + '|' +
        Game_board[
            'E4'] + '|' + Game_board['F4'] + '|' + Game_board['G4'] + '|' + Game_board['H4'])
    print(
        Game_board['A3'] + '|' + Game_board['B3'] + '|' + Game_board['C3'] + '|' + Game_board['D3'] + '|' +
        Game_board[
            'E3'] + '|' + Game_board['F3'] + '|' + Game_board['G3'] + '|' + Game_board['H3'])
    print(
        Game_board['A2'] + '|' + Game_board['B2'] + '|' + Game_board['C2'] + '|' + Game_board['D2'] + '|' +
        Game_board[
            'E2'] + '|' + Game_board['F2'] + '|' + Game_board['G2'] + '|' + Game_board['H2'])
    print(
        Game_board['A1'] + '|' + Game_board['B1'] + '|' + Game_board['C1'] + '|' + Game_board['D1'] + '|' +
        Game_board[
            'E1'] + '|' + Game_board['F1'] + '|' + Game_board['G1'] + '|' + Game_board['H1'])
    print("\n\n\n")


turn = 'w'                              # White starts turn
White = Player('w')                     # creat Player class for Black and White
Black = Player('b')
White.player_info(Game_board)
Black.player_info(Game_board)

first_move = game(turn, White, Black, Game_board)


if first_move.p_ass == 'yes':
    game_on = True
    White_ = first_move.white
    Black_ = first_move.black
    turn = first_move.turn
    board = first_move.board

    while game_on:
        White.player_info(board)
        Black.player_info(board)
        turn_result = game(turn, White, Black, board)
        if turn_result.p_ass == 'yes':
            White_ = turn_result.white
            Black_ = turn_result.black
            turn = turn_result.turn
            board = turn_result.board
            print('\n\n Turn is now {}'.format(turn))
        elif turn_result.finish == 'yes':
            if White.in_check_mate:
                print('White has lost the game')
                game_on = False
            elif Black.in_check_mate:
                    print('Black has lost the game')
                    game_on = False




exit(0)


