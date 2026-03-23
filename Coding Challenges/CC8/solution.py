class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compute_formula_tree(tree):
    """
    Evaluate the arithmetic expression represented by the formula tree.

    Leaf nodes contain non-negative integers. Internal nodes contain operator
    codes: -1 (add), -2 (subtract), -3 (divide, truncate toward zero), -4 (multiply).
    Internal nodes always have two children. The tree is never empty.

    Parameters
    ----------
    tree : BinaryTree
        Root of the formula tree.

    Returns
    -------
    int
        The computed value of the expression.

    TODO
    ----
    Implement this function.
    """
    if tree.left is None and tree.right is None:
        return tree.value

    left_value = compute_formula_tree(tree.left)
    right_value = compute_formula_tree(tree.right)

    if tree.value == -1:
        return left_value + right_value
    if tree.value == -2:
        return left_value - right_value
    if tree.value == -3:
        return int(left_value / right_value)
    if tree.value == -4:
        return left_value * right_value

    raise NotImplementedError
