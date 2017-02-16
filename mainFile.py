__author__ = "eshan"
__date__ = "$Jul 29, 2016 2:08:09 AM$"

import random
import Node
import collections
import itertools


class mainFile(object):

    def consume(self, iterator, n):
        collections.deque(itertools.islice(iterator, n))

    def graphSetup(self, parent, depth, limit, minVal, maxVal, notes):
        set = []
        if depth == limit:
            n = random.randint(int(minVal), int(maxVal))
            set.append(n)
            node = Node.Node(n, parent)
            node.terminal = True
            parent.addChild(node)
        else:
            for a in range(int(notes)):
                node = Node.Node(0, parent)
                parent.addChild(node)
                value = self.graphSetup(
                    node, depth + 1, limit, minVal, maxVal, notes)
                set.extend(value)
        return set

    def minMax(self, node, maximize):
        if node.terminal:
            return node.value
        if maximize:
            bestValue = -float("inf")
            for a in range(len(node.children)):
                v = self.minMax(node.children[a], False)
                bestValue = max(bestValue, v)
            return bestValue
        else:
            bestValue = +float("inf")
            for a in range(len(node.children)):
                v = self.minMax(node.children[a], True)
                bestValue = min(bestValue, v)
            return bestValue

    def alphaBeta(self, node, alpha, beta, maximize, depth, limit):
        if node.terminal:
            return node.value
        if maximize:
            v = -float("inf")
            for a in range(len(node.children)):
                v = max(v, self.alphaBeta(
                    node.children[a], alpha, beta, False, depth + 1, limit))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v
        else:
            v = +float("inf")
            for a in range(len(node.children)):
                v = min(v, self.alphaBeta(
                    node.children[a], alpha, beta, True, depth + 1, limit))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v

    def minMaxTurns(self, notes, turns):
        return pow(int(notes), pow(2, int(turns)))

    def alphaBetaTurns(self, list, notes):
        count = 0
        loop = 0
        minimum = +float("inf")
        iterator = range(len(list)).__iter__()
        for a in iterator:
            if a < int(notes):
                count += 1
                minimum = min(minimum, list[a])
            elif loop < int(notes):
                if list[a] < minimum:
                    minimum = list[a]
                    self.consume(iterator, int(notes) - (loop + 1))
                loop += 1
                count += 1
                if loop == int(notes) - 1:
                    loop = 0
        return count


def main():
    task = mainFile()
    root = Node.Node(-float("inf"), None)
    valSet = task.graphSetup(root, 0, 2 * int(turns), minVal, maxVal, notes)
    bestVal = task.minMax(root, True)
    abVal = task.alphaBeta(root, -float("inf"), +
                           float("inf"), True, 0, pow(2, int(turns)))

    print("Depth:"),
    print(pow(2, int(turns)))
    print("Branch:"),
    print(notes)
    print("Set:"),
    print(valSet)
    print("Maximum Collected Amount Using MinMax:"),
    print(bestVal)
    print("Comparisons Using MinMax Algorithm:"),
    print(task.minMaxTurns(notes, turns))
    print("Maximum Collected Amount Using AlphaBeta:"),
    print(abVal)
    print("Comparisons Using Alpha Beta Pruning:"),
    print(task.alphaBetaTurns(valSet, notes))

if __name__ == "__main__":
    turns = raw_input()
    notes = raw_input()
    string = raw_input()
    list = string.split()
    minVal = list[0]
    maxVal = list[1]
    main()
