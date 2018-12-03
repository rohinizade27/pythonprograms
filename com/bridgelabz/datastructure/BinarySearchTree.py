
"""
purpose   :find the number of possible binary trees of given number of nodes
@Author   : Rohini Zade
@version  : 1.0
@since    : 1-12-2018

"""

from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

if __name__ == "__main__":
    utility_obj = Utility()
    bst_obj=BinarySearchTree()
    nodelist=[]
    print("Enter the no of nodes in BST:")
    no_of_nodes=utility_obj.inputIntiger()
    bst_obj.countBinaryTree(no_of_nodes)


