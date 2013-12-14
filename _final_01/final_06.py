__author__ = 'Sabinu'


class Member(object):
    def __init__(self, founder):
        """
        founder: string
        Initializes a member.
        Name is the string of name of this node,
        parent is None, and no children
        """
        self.name = founder
        self.parent = None
        self.children = []

    def __str__(self):
        return self.name

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent

    def is_parent(self, mother):
        """
        mother : Member
        Returns: Boolean, whether or not `mother` is the
                 parent of this Member
        """
        return self.parent == mother

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children


class Family(object):
    def __init__(self, founder):
        """
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """
        self.names_to_nodes = {}
        self.root = Member(founder)
        self.names_to_nodes[founder] = self.root

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother.

        Keyword arguments:
        mother           -- mother's name as a string
        list_of_children -- children names as strings
        """

        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]
        for c in list_of_children:
            c_member = Member(c)
            self.names_to_nodes[c] = c_member
            c_member.add_parent(mom_node)
            mom_node.add_child(c_member)

    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid.

        Keyword arguments:
        mother -- string of mother's name
        kid    -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother.

        Keyword arguments:
        kid    -- string of kid's name
        mother -- string of mother's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def path(self, node):
        n = self.names_to_nodes[node]
        path = [n]

        while n.get_parent() is not None:
            path.append(n.get_parent())
            n = n.get_parent()

        return path

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed)

        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendant
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common
        ancestor as described in the exercises above.

        degree removed is the distance to the common ancestor

        Keyword arguments:
        a -- string that is the name of a
        b -- string that is the name of b
        """
        right  = self.names_to_nodes[a]
        left   = self.names_to_nodes[b]
        r_list = self.path(a)
        l_list = self.path(b)

        #   Same Object - Same Path
        if r_list == l_list:
            return -1, 0
        #   One Object is a Direct Descendant of the Other
        if right in l_list or left in r_list:
            e1 = max(len(r_list), len(l_list))
            e2 = min(len(r_list), len(l_list))
            return -1, e1 - e2

        r_list.reverse()
        l_list.reverse()

        #   Remove all - except different
        while r_list[0] == l_list[0]:
            e = r_list[0]
            r_list.remove(e)
            l_list.remove(e)

        if len(r_list) == len(l_list):              # Zero Degree Removed
            return len(r_list) - 1, 0
        else:                                       # Calculate Removed Degree
            out1 = min(len(r_list), len(l_list))
            out2 = len(r_list) - len(l_list)
            return out1 - 1, abs(out2)


f = Family("a")
f.set_children("a", ["b", "c"])
f.set_children("b", ["d", "e"])
f.set_children("c", ["f", "g"])

f.set_children("d", ["h", "i"])
f.set_children("e", ["j", "k"])
f.set_children("f", ["l", "m"])
f.set_children("g", ["n", "o", "p", "q"])

words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]


##   These are your test cases.
test_cases = [('b', 'c'), ('d', 'f'),
              ('i', 'n'), ('q', 'e'),
              ('h', 'c'), ('h', 'a'),
              ('h', 'h'), ('a', 'a')]

for i, j in test_cases:
    t, r = f.cousin(i, j)
    if t == -1:
        print '%s_%s %s - %s' % (i, j, t, r)
    else:
        print '%s_%s  %s - %s' % (i, j, t, r)

# b_c  0 - 0
# d_f  1 - 0
# i_n  2 - 0
# q_e  1 - 1
# h_c  0 - 2
# h_a -1 - 3
# h_h -1 - 0
# a_a -1 - 0