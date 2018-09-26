#!/usr/bin/python3

from board_util import GoBoardUtil
from gtp_connection import GtpConnection
from mcts import TreeNode
import operator

class PolicyMaxPlayer(object):
    """
        Plays according to the Go6 playout policy.
        No simulations, just random choice among current policy moves
    """

    version = 0.1
    name = "PolicyMaxPlayer"
    def __init__(self):
        pass

    def get_move(self, board, color, pattern, selfatari):
        policy_moves, type_of_move = GoBoardUtil.generate_all_policy_moves(board,
                                                pattern,
                                                selfatari)
        result = TreeNode.return_moves_prob(TreeNode(self), board, policy_moves, color)
        sorted_moves = []
        for point, prob in result.items():
            sorted_moves.append(tuple([ self.board.point_to_string(point),prob])) 
        a1 = sorted(sorted_moves, key=lambda x: x[0])
        sorted_moves = sorted(a1, key=lambda x: x[1], reverse = True)
        #print(sorted_moves[0][0])
        #print(GoBoardUtil.generate_move_with_filter(board,pattern,selfatari))

        return sorted_moves[0][0]



    def get_properties(self):
        return dict(
            version=self.version,
            name=self.__class__.__name__,
        )

    def reset(self):
        pass

    def update(self, move):
        pass

def createPolicyPlayer():
    con = GtpConnection(PolicyMaxPlayer())
    con.start_connection()

if __name__=='__main__':
    createPolicyPlayer()
