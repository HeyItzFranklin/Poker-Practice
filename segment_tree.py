class SegmentTree:
    def __init__(self, arr) -> None:

        self.nodes = [0 for _ in range(len(arr) * 2)]

        for i in range(len(arr)):
            self.nodes[i + len(arr)] = arr[i]
        
        start = len(arr)
        end = len(arr) * 2 - 1
        while start < end:
            for i in range(start, end, 2):
                p = int(i // 2)
                print(i, i + 1, p)
                self.nodes[p] = self.nodes[i] + self.nodes[i + 1]
            start = int(start / 2)
            end = int(end / 2)

        print(self.nodes)

    def compute(self, a, b):
        print(n1, n2, )
        mid = n1 // 2
        self.nodes[mid] = self.nodes[n1] + self.nodes[n2]
        self.build_parent_nodes(self, mid, mid + 1)

    def add(self):
        pass

def main():
    arr = [7,2,4,10,1,2,3,4]
    seg_tree = SegmentTree(arr)


if __name__ == '__main__':
    main()