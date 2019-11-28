class Node:
    __slots__ = ('elem', 'children', 'status')

    def __init__(self, elem):
        self.children = []
        self.status = True
        self.elem = elem
        # True for haven't been traversed

    def depth_traversal(self):
        results = []

        stack = [self]
        self.status = False

        while len(stack) > 0:
            if len(stack[-1].children) > 0:
                for child in stack[-1].children:
                    if child.status:
                        child.status = False
                        stack.append(child)
                        break

                    if child == stack[-1].children[-1]:
                        stack.pop()

            else:
                results.append(list(node.elem for i, node in enumerate(stack)))
                stack.pop()

        return results


def construct(seq):
    tree_stack = []
    root = Node(seq[0])
    tree_stack.append(root)

    for i, elem in enumerate(seq):
        if i == 0:
            continue
        else:
            if elem == '#':
                tree_stack.pop()
            else:
                cur = Node(elem)
                tree_stack[-1].children.append(cur)
                tree_stack.append(cur)

    return root


if __name__ == '__main__':
    sequence = 'ABC#D##E#'
    tree = construct(sequence)
    path_set = tree.depth_traversal()
    print(path_set)
