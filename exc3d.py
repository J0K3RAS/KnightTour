### EXC 3D ###
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:40:56 2021
@author: Charalampos Bekiaris
"""
from collections import deque

class Node: # Κόμβοι του γράφου
    # (x, y) η θέση του κόμβου με συντεταγμένες σκακιέρας
    def __init__(self, x, y, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

# Έλεγχος αν είναι εντός σκακιέρας το άλογο
def valid(x, y, n, m):
    return not (x < 1 or y < 1 or x > n or y > m)

# Κυρίως πρόγραμμα
def BFS(src, dim, illegal, k):
    x_move = [2, 2, -2, -2, 1, 1, -1, -1] # Οι κινήσεις του αλόγου
    y_move = [-1, 1, 1, -1, 2, -2, 2, -2] #
    
    visited = set() # Θα αποθηκεύουμε του κόμβους που ελέγξαμε

    q = deque()     # Θα προσθέτουμε του κόμβους προς έλεγχο
    q.append(src)   # Ξεκινάμε με τον αρχικό κόμβο
    while q:        # Όσο δεν είναι κενή η ουρά

        node = q.popleft()  # Πάρε το πρώτο στοιχείο & αφαίρεσέ το 

        x = node.x  # x-συνιστώσα
        y = node.y  # y-συνιστώσα
        d = node.dist # Απόσταση από τον αρχικό κόμβο
        if node not in visited and d<k:  # Αν δεν έχουμε επισκεφτεί τον κόμβο
            visited.add(node)    # Τον προσθέτουμε στην λίστα visited
            for i in range(8):   # Κάνουμε 8 κινήσεις
                x1 = x + x_move[i]
                y1 = y + y_move[i]

                if valid(x1, y1, dim[0], dim[1]): # Εάν δεν είμαστε εκτός σκακιέρας
                    if (x1,y1) not in illegal:    # Εάν δεν πάμε σε απαγορευμένο κόμβο
                        q.append(Node(x1, y1, d+1))    # Προσθέτουμε στην ουρά προς έλεγχο τον νέο κόμβο

    # Επιστρέφουμε false αν δεν γίνεται η μετακίνηση
    return visited

## Παράδειγμα ##
begin = Node(1, 1)   # Αρχικός κόμβος
dimensions = (3, 4)  # Διαστάσεις σκακιέρας
k = 3 # Maximum απόσταση από τον αρχικό κόμβο
illegal = [(2,2),(3,4),]  # Απαγορευμένοι κόμβοι
result=BFS(begin, dimensions, illegal, k)
for i in result:
    print("({},{})".format(i.x,i.y))
