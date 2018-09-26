#!/usr/bin/python3

from board_util import GoBoardUtil
from gtp_connection import GtpConnection
from mcts import TreeNode
import operator
import random

class PolicyProbabilisticPlayer(object):
    """
        Plays according to the Go4 playout policy.
        No simulations, just random choice among current policy moves
    """

    version = 0.1
    name = "PolicyProbabilisticPlayer"
    def __init__(self):
        pass

    def get_move(self, board, color, pattern, selfatari):
        policy_moves, type_of_move = GoBoardUtil.generate_all_policy_moves(board,
                                                pattern,
                                                selfatari)
        result = TreeNode.return_moves_prob(TreeNode(self), board, policy_moves, color)
        sorted_moves = []
        for point, prob in result.items():
            sorted_moves.append([point, prob])
        sorted_moves = sorted(sorted_moves, key=operator.itemgetter(1), reverse=True)
        #print(sorted_moves[0][0])
        #print(GoBoardUtil.generate_move_with_filter(board,pattern,selfatari))

        move = self.random_select(sorted_moves)[0]
        return move

    def get_properties(self):
        return dict(
            version=self.version,
            name=self.__class__.__name__,
        )

    def reset(self):
        pass

    def update(self, move):
        pass

    # This method is slow but simple
    def random_select(self, distribution):
        r = random.random();
        sum = 0.0
        for item in distribution:
            sum += item[0]
            if sum > r:
                return item
        return distribution[-1] # some numerical error, return last element

def createPolicyPlayer():
    con = GtpConnection(PolicyProbabilisticPlayer())
    con.start_connection()

if __name__=='__main__':
    createPolicyPlayer()
