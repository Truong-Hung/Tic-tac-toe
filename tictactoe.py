"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    
    # return [[O, EMPTY, EMPTY],
    #         [X, O, EMPTY],
    #         [X, O, X]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    nX = sum(row.count('X') for row in board)
    nO = sum(row.count('O') for row in board)
    
    if nX > nO:
        return O
    elif nX == nO:
        return X
    else:
        raise ValueError("There must be someone cheating!")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    
    for i, x in enumerate(board):
        for j, y in enumerate(x):
            if y == None:
                actions.add((i, j))
            
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy
    
    result = copy.deepcopy(board)
    
    if not action:
        raise ValueError("The move is illegal!")
    else:
        result[action[0]][action[1]] = player(board)
    
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    winner = None
    
    i = 0
    while winner == None and i < len(board[:][0]):
        
        lst = board[i][:]
        winner = check_equal_elements(lst)
        i += 1
      
    i = 0    
    while winner == None and i < len(board[0][:]):
        
        lst = [board[0][i],board[1][i],board[2][i]]
        winner = check_equal_elements(lst)
        i += 1
        
    if winner == None:
        lst = [board[0][0],board[1][1],board[2][2]]
        winner = check_equal_elements(lst)
        
    if winner == None:
        lst = [board[2][0],board[1][1],board[0][2]]
        winner = check_equal_elements(lst)
    
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if actions(board) == set() or winner(board) != None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def maxvalue(board):
        
        v = -math.inf
        
        if terminal(board):
            return utility(board)
        else:
            for action in actions(board):
                v = max(v,minvalue(result(board,action)))
            return v

    def minvalue(board):
         
         v = math.inf
         
         if terminal(board):
             return utility(board)
         else:
             for action in actions(board):
                 v = min(v,maxvalue(result(board,action)))
             return v
         
    if player(board) == X:
        
        v = -math.inf
        nE = sum(row.count(EMPTY) for row in board)
        
        if nE == 9:
            action = (1,1) #The best first move should be at the center
        else:
            for a in actions(board):
                v_max = minvalue(result(board,a))
                if v_max >= v:
                    v = v_max
                    action = a
                
        return action
    
    elif player(board) == O:
        
        v = math.inf
        
        for a in actions(board):
            v_min = maxvalue(result(board,a))
            if v_min <= v:
                v = v_min
                action = a
                
        return action
         
    

def simple_algo(board):
    """
    Returns the action for the current player on the board using simple algo
    """
    #action = random.choice(tuple(actions(board)))
    
    list_acts = tuple(actions(board))
    list_players = ['X', 'O']
    
    opt_move = None
    opt_move_found = False
    
    #First move should be targetted at the center cell
    if (1,1) in list_acts:
        action = (1,1)
        opt_move_found = True
        
    p = player(board)
    
    i = 0
    while opt_move == None and i < len(board[:][0]):
        
        lst = board[i][:]
        opt_move = check_opt_move(lst, p)
        i += 1
        
    if opt_move != None and not opt_move_found:
        action = (i-1,opt_move)
        opt_move_found = True
      
    i = 0    
    while opt_move == None and i < len(board[0][:]):
        
        lst = [board[0][i],board[1][i],board[2][i]]
        opt_move = check_opt_move(lst, p)
        i += 1
        
    if opt_move != None and not opt_move_found:
        action = (opt_move,i-1)
        opt_move_found = True
        
    if opt_move == None:
        lst = [board[0][0],board[1][1],board[2][2]]
        opt_move = check_opt_move(lst, p)
        
    if opt_move != None and not opt_move_found:
        action = (opt_move,opt_move)
        opt_move_found = True
        
    if opt_move == None:
        lst = [board[2][0],board[1][1],board[0][2]]
        opt_move = check_opt_move(lst, p)
        
    if opt_move != None and not opt_move_found:
        action = (2-opt_move,opt_move)
        opt_move_found = True
    
    if not opt_move_found:   
    
        p = [x for i, x in enumerate(list_players) if x != p]
        p = p[0]
        
        i = 0
        while opt_move == None and i < len(board[:][0]):
            
            lst = board[i][:]
            opt_move = check_opt_move(lst, p)
            i += 1
            
        if opt_move != None and not opt_move_found:
            action = (i-1,opt_move)
            opt_move_found = True
          
        i = 0    
        while opt_move == None and i < len(board[0][:]):
            
            lst = [board[0][i],board[1][i],board[2][i]]
            opt_move = check_opt_move(lst, p)
            i += 1
            
        if opt_move != None and not opt_move_found:
            action = (opt_move,i-1)
            opt_move_found = True
            
        if opt_move == None:
            lst = [board[0][0],board[1][1],board[2][2]]
            opt_move = check_opt_move(lst, p)
            
        if opt_move != None and not opt_move_found:
            action = (opt_move,opt_move)
            opt_move_found = True
            
        if opt_move == None:
            lst = [board[2][0],board[1][1],board[0][2]]
            opt_move = check_opt_move(lst, p)
            
        if opt_move != None and not opt_move_found:
            action = (2-opt_move,opt_move)
            opt_move_found = True
    
    if opt_move == None and not opt_move_found:
        #When we don't have optimal moves, we should prioterize the move at the corners 
        list_corner = [(0,0),(2,2),(0,2),(2,0)]
        lst_inter = [value for value in list_corner if value in list_acts]
        
        if not lst_inter:
            action = random.choice(list_acts)
            print('random move')
        else:
            action = random.choice(lst_inter)
            print('random move at corners')
    
    return action
    
def check_equal_elements(myList):
    
    first_ele = myList[0]
 
    
    if first_ele == EMPTY:
        winner = None
    elif first_ele == X:
        winner = X
        # Comparing each element with first item
        for item in myList:
            if first_ele != item:
                winner = None
                break
    elif first_ele == O:
        winner = O
        # Comparing each element with first item
        for item in myList:
            if first_ele != item:
                winner = None
                break
            
    return winner


def check_opt_move(myList, player):

    nE = myList.count(EMPTY)

    if nE != 1:
        return None
    elif nE == 1: 
        for i, x in enumerate(myList):
            if x == EMPTY:
                iE = i
            
    lst = [x for i,x in enumerate(myList) if i!=iE]
    
    if lst[0] == lst[1] and lst[0] == player:
        return iE
    else:
        return None
            
    