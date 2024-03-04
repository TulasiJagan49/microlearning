from sort import Sort

class SelectionSort(Sort):

    def __init__(self, list):
        super().__init__(list)
    
    def sort(self, increasing=True):

        for i in range(self.length - 1):
            key = self.list[i]
            index = i
            for j in range(i+1, self.length):
                if (self.list[j] < key if increasing else self.list[j] > key):
                    key = self.list[j]
                    index = j
            self.list[index] = self.list[i]
            self.list[i] = key
                    
        return self.list

a = [5,2,1,4,6,3]
print(SelectionSort(a).sort())
print(SelectionSort(a).sort(increasing=False))
