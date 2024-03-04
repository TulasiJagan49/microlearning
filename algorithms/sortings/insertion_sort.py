from sort import Sort


class InsertionSort(Sort):

    def __init__(self, list):
        super().__init__(list)

    def sort(self, increasing=True):

        for i in range(1, self.length):
            
            k = self.list[i]

            j = i - 1

            while j >= 0 and (self.list[j] > k if increasing else self.list[j] < k):
                self.list[j + 1] = self.list[j]
                j -= 1

            self.list[j + 1] = k

        return self.list

a_list = [5,2,4,6,1,3]
print(InsertionSort(a_list).sort(increasing=True))
print(InsertionSort(a_list).sort(increasing=False))
