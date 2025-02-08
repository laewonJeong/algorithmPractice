class NumberContainers:
    def __init__(self):
        self.container = defaultdict(SortedSet)
        self.idx = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if self.idx[index] != 0:
            self.container[self.idx[index]].remove(index)
            if not self.container[self.idx[index]]:
                del self.container[self.idx[index]]

        self.container[number].add(index)
        self.idx[index] = number

    def find(self, number: int) -> int:
        if not self.container[number]:
            return -1
        return self.container[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)