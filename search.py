"""
BREADTH-FIRST-SEARCH (UNINFORMED SEARCH)

 no usa información heurística para guiar su búsqueda.

 https://asimov.cloud/web/image/7670-02afbdcb/DFS.gif?access_token=9e1c3302-64db-4d2c-9a4b-7841c8bebd28

 
"""

import sys
import time
from dataclasses import dataclass, field
from copy import deepcopy
from collections import deque
from graphviz import Digraph
from __future__ import annotations



def bfs(state):
    root = Node (
        parent = None,
        state = state,
        action = None,
        depth = 0
    )
    fifo = deque([root])
    num_expansions = 0
    max_depth = -1

    while True:
        if not fifo:
            print(f'{num_expansions} expansiones')
            return None
        node = fifo.popleft()
        if node.depth > max_depth:
            max_depth = node.depth
            print(f'[profundidad = {max_depth}]
                  {start.elapse():.2f}s')
        if node.state.is_goal():
            print(f'{num_expansions} expansiones')
            return node.extract_solution()
        
        num_expansions += 1
        fifo.extend(node.expand())