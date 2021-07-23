# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq


class Node:
    def __init__(self, data):
        self.data = data
        self.incoming_edges = 0
        self.succ = set()


N = int(input())

nodes = {}
starts_of_list = set()
parentless_nodes = set()


def binary_search(l, value):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > value:
            high = mid - 1
        elif l[mid] < value:
            low = mid + 1
        else:
            return True
    return False


def getOrCreateNode(i):
    if i in nodes:
        return nodes[i]
    nodes[i] = Node(i)
    return nodes[i]


def make_nodes(input_list):
    parent = getOrCreateNode(input_list[0])
    starts_of_list.add(parent.data)
    child = getOrCreateNode(input_list[1])
    if child.data not in parent.succ:
        child.incoming_edges += 1
        parent.succ.add(child.data)
    parentless_nodes.add(child.data)
    for i in range(1, len(input_list) - 1):
        parent = child
        child = getOrCreateNode(input_list[i + 1])
        parentless_nodes.add(child.data)
        if child.data not in parent.succ:
            child.incoming_edges += 1
            parent.succ.add(child.data)


for _ in range(N):
    K = int(input())
    make_nodes(list(map(int, input().split())))

heap = list(starts_of_list - parentless_nodes)
heapq.heapify(heap)

nums = []

while len(heap) > 0:
    smallest = heapq.heappop(heap)
    smallestNode = nodes[smallest]
    nums.append(smallest)
    for nInt in smallestNode.succ:
        n = nodes[nInt]
        n.incoming_edges -= 1
        if n.incoming_edges == 0 and not binary_search(heap, n.data):
            heapq.heappush(heap, n.data)

print(" ".join(list(map(str, nums))))
