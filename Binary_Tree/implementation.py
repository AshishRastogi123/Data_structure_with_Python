""""
Binary Tree Structure:
        Drink
       
    Water    Cock
   
Bislari Simple Fanta Thumpshup
"""


class Binary_Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

if __name__=="__main__":
    drink=Binary_Node("Drink")
    water=Binary_Node("water")
    cock=Binary_Node("Cock")
    bislari=Binary_Node("Bislary")
    simple=Binary_Node("Simple")
    fanta=Binary_Node("Fanta")
    thumsup=Binary_Node("Thumpshup")

    drink.left=water
    drink.right=cock

    water.left=bislari
    water.right=simple

    cock.left=fanta
    cock.right=thumsup

    print(drink.left)
    print(water)
    print(drink.left.left.val)
    print(drink.left.left.left.val)
#If node does not create
#AttributeError: 'NoneType' object has no attribute 'val'