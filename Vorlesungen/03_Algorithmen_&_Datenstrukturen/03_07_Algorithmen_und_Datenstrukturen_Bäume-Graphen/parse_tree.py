#%%

class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return F"{self.data}"

    def insert_left(self, data=None):
        tree.left = Node(data)
        tree.left.parent = self
        return tree.left

    def insert_right(self, data=None):
        tree.right = Node(data)
        tree.right.parent = self
        return tree.right
    
    def print_as_tree(self, level=0):
        spaces = " " * (level * 3 - 2)
        prefix = spaces + "└──" if level != 0 else ""
        print(F"{prefix} {self}")
        
        children = []
        children.append(self.left if self.left else None)
        children.append(self.right if self.right else None)
    
        for child in children:
            if child:
                child.print_as_tree(level+1)

    def as_expr(self):
        result = ""
        if self:
            if self.left:
                result += ('(' + self.left.as_expr())
            result += str(self.data)
            if self.right:
                result += (self.right.as_expr() + ')')
        return result

#%%
# Fully parenthesized expressions in infix notation can also be computed using a tree

import operator

#expr = "((3 * (4 + 5)) + 6)"
expr = "((5 + 3) * (5 + 1))"
ops = {
       '+': operator.add,
       '-': operator.sub,
       '*': operator.mul
      }

tree = Node()
root = tree

for c in expr:
    if c == "(":
        tree = tree.insert_left()
    elif c in ops:
        tree.data = c
        tree = tree.insert_right()
    elif c.isdigit():
        tree.data = int(c)
        tree = tree.parent
    elif c == ")":
        tree = tree.parent

root.print_as_tree()

# %%

def evaluate(tree: Node):
    if tree.left and tree.right:
        # if both children a set then the current node must be an operator
        fn = ops[tree.data]
        return fn(evaluate(tree.left), evaluate(tree.right))
    else:
        return tree.data

result = evaluate(root)
print(result)

#%%

print(root.as_expr())