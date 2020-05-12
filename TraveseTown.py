import random as rand

class Node:
    def _init_(self, name):
        self.name = name
        self.neighbors = []


class Graph:
    def _init_(self):
        self.nodeList = []

    def addNode(self, name):
        self.nodeList.append(self.Node(name))

    def addUndirectedEdge(self, first, second):
        first.neighbors.append(second)
        second.neighbors.append(first)

    def removeUndirectedEdge(self, first, second):
        first.neighbors.remove(second)
        second.neighbors.remove(first)

    def getAllNodes(self):
        return self.nodeList

    def createRandomUnweightedGraph(n):

    def createLinkedList(n):

    def DFSRec(self, start, end):

    def DFSIter(self, start, end):

    def DFTRec(graph):

    def DFTIter(graph):

    def BFTRecLinkedList(graph):

    def BFTIterLinkedList(graph):
