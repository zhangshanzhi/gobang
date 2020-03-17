#!/usr/bin/env python
#/usr/local/bin/python3
# Set the path to your python3 above

from gtp_connection import GtpConnection
from board_util import GoBoardUtil, EMPTY
from simple_board import SimpleGoBoard
from GomokuMCTS import TreeNode, MCTS

import random
import numpy as np
    
def policy_value_fn(actived_features):
    
    return 100000*actived_features[0]+10000*actived_features[1]+5000*actived_features[2]+1000*actived_features[3]+500*actived_features[4]+400*actived_features[5]+100*actived_features[6]+90*actived_features[7]+50*actived_features[8]+10*actived_features[9]+9*actived_features[10]+5*actived_features[11]+2*actived_features[11]+1

def feature1(board,move,color):
    board.play_move_gomoku(move, color)
    

    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature2(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature3(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature4(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature5(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature6(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature7(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature8(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature9(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature10(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def feature11(board,move,color):
    board.play_move_gomoku(move, color)


    undo(board,move)
    actived = 1
    return actived    # 0 or 1

def undo(board,move):
    board.board[move]=EMPTY
    board.current_player=GoBoardUtil.opponent(board.current_player)

def play_move(board, move, color):
    board.play_move_gomoku(move, color)

def game_result(board):
    game_end, winner = board.check_game_end_gomoku()
    moves = board.get_empty_points()
    board_full = (len(moves) == 0)
    if game_end:
        #return 1 if winner == board.current_player else -1
        return winner
    if board_full:
        return 'draw'
    return None

class GomokuSimulationPlayer(object):
    """
    For each move do `n_simualtions_per_move` playouts,
    then select the one with best win-rate.
    playout could be either random or rule_based (i.e., uses pre-defined patterns) 
    """
    def __init__(self, n_simualtions_per_move=10, playout_policy='random', board_size=7):
        assert(playout_policy in ['random', 'rule_based'])
        self.n_simualtions_per_move=n_simualtions_per_move
        self.board_size=board_size
        self.playout_policy=playout_policy
    #——————————————————————————————————————————————————————————
    #——————————————————————————————————————————————————————
        #NOTE: pattern has preference, later pattern is ignored if an earlier pattern is found
        self.pattern_list=['Win', 'BlockWin', 'OpenFour', 'BlockOpenFour', 'Random']

        self.name="Gomoku3"
        self.version = 3.0
        self.best_move=None
    
    def set_playout_policy(self, playout_policy='random'):
        assert(playout_policy in ['random', 'rule_based'])
        self.playout_policy=playout_policy

    def _random_moves(self, board, color_to_play):
        return GoBoardUtil.generate_legal_moves_gomoku(board)
    
    def policy_moves(self, board, color_to_play):
        if(self.playout_policy=='random'):
            return "Random", self._random_moves(board, color_to_play)
        else:
            assert(self.playout_policy=='rule_based')
            assert(isinstance(board, SimpleGoBoard))
            ret=board.get_pattern_moves()
            if ret is None:
                return "Random", self._random_moves(board, color_to_play)
            movetype_id, moves=ret
            return self.pattern_list[movetype_id], moves
    
    def _do_playout(self, board, color_to_play):
        res=game_result(board)
        simulation_moves=[]
        while(res is None):
            _ , candidate_moves = self.policy_moves(board, board.current_player)
            playout_move=random.choice(candidate_moves)
            play_move(board, playout_move, board.current_player)
            simulation_moves.append(playout_move)
            res=game_result(board)
        for m in simulation_moves[::-1]:
            undo(board, m)
        if res == color_to_play:
            return 1.0
        elif res == 'draw':
            return 0.0
        else:
            assert(res == GoBoardUtil.opponent(color_to_play))
            return -1.0

    def features_get_move(self,board,color_to_play):
        moves = GoBoardUtil.generate_legal_moves_gomoku(board)
        #toplayer = board.current_player
        moves_records = {}
        for move in moves:
            actived_features = []
            actived_features.append(feature1(board,move,color_to_play))
            actived_features.append(feature2(board,move,color_to_play))
            actived_features.append(feature3(board,move,color_to_play))
            actived_features.append(feature4(board,move,color_to_play))
            actived_features.append(feature5(board,move,color_to_play))
            actived_features.append(feature6(board,move,color_to_play))
            actived_features.append(feature7(board,move,color_to_play))
            actived_features.append(feature8(board,move,color_to_play))
            actived_features.append(feature9(board,move,color_to_play))
            actived_features.append(feature10(board,move,color_to_play))
            actived_features.append(feature11(board,move,color_to_play))
            moves_records[move] = policy_value_fn(actived_features)
        best_move = 'Pass'
        highest_value = 0
        for move, value in moves_records.items():
            if value>=highest_value:
                best_move = move
        return best_move

    def MCTS_get_move(self,board,color_to_play):
        moves = GoBoardUtil.generate_legal_moves_gomoku(board)
        toplay = board.current_player
        


    def get_move(self, board, color_to_play):
        """
        The genmove function called by gtp_connection
        """
        moves=GoBoardUtil.generate_legal_moves_gomoku(board)
        toplay=board.current_player
        best_result, best_move=-1.1, None
        best_move=moves[0]
        wins = np.zeros(len(moves))
        visits = np.zeros(len(moves))
        while True:
            for i, move in enumerate(moves):
                play_move(board, move, toplay)
                res=game_result(board)
                if res == toplay:
                    undo(board, move)
                    #This move is a immediate win
                    self.best_move=move
                    return move
                ret=self._do_playout(board, toplay)
                wins[i] += ret
                visits[i] += 1
                win_rate = wins[i] / visits[i]
                if win_rate > best_result:
                    best_result=win_rate
                    best_move=move
                    self.best_move=best_move
                undo(board, move)
        assert(best_move is not None)
        return best_move

def run():
    """
    start the gtp connection and wait for commands.
    """
    board = SimpleGoBoard(7)
    con = GtpConnection(GomokuSimulationPlayer(), board)
    con.start_connection()

if __name__=='__main__':
    run()
