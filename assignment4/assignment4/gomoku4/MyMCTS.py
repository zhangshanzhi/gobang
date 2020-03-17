import numpy as np 
import copy
from simple_board import SimpleGoBoard

class TreeNode(object):

    def __init__(self,parent,board):
        self.board = board  #board is the board 
        self.parent = parent  #parent is a tree node
        self.children = {}
        self.num_visits = 0
        self.Q = 0

    def expand(self, moves):
        for move in moves:
            next_board = self.board.play(move) ##假设board有一个funtion play
            if next_board not in self.children:
                self.children[move] = TreeNode(self,next_board)
            self.board.undo()  ## 假设board you一个funtion undo
    
    def update(self,leaf_value):
        self.num_visits +=1

        self.Q += leaf_value
    
    def update_ancestor(self,leaf_value):
        if self.parent:
            self.parent.updata(-leaf_value)
        self.update(leaf_value)
    
    def select(self):
        pass

    def get_value(self,):
        pass
    
    def is_leaf(self):
        return len(self.children) == 0

    def is_roof(self):
        return self.parent is None

    
class MCTS(object):

    def __init__(self, value_fn, n_playout = 10000):
        self.root = TreeNode(None, SimpleGoBoard(7))
        self.value_fn = value_fn
        self.n_playout = n_playout

    def playout(self,board):
        node = self.root
        while True:
            if node.is_leaf():
                break
            moves, node = node.select()

