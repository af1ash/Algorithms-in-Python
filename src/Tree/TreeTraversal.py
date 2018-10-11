
def preorder_indent(T, p, d):
    """ Print preorder representation of subtree of T rooted at p depth d. """
    print(2*d*' ' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d+1)

def preorder_label(T, p, d, path):
    """ Print labeled representation of subtree of T rooted at p at depth d. """
    label = ' '.join(str(j +  1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()

def parenthesize(T, p):
    """ Print parenthesized representation of subtree of T rooted at p. """
    print(p.element(), end = '')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = '(' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')