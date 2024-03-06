from sort import Sort

class MergeSort(Sort):

    def __init__(self, list):
        super().__init__(list)

    def sort(self):
        self.merge_sort(self.list, 0, self.length - 1)
        return self.list

    def merge_sort(self, list, l, h):
        if l >= h: return
        m = (l + h) // 2
        self.merge_sort(list, l, m)
        self.merge_sort(list, m + 1, h)
        self.merge(list, l, m, h)
    
    def merge(self, list, l, m, h):
        aux_list = list[:]
        i = l
        j = m + 1
        for k in range(i,h+1):
            if j > h:
                list[k] = aux_list[i]
                i += 1
            elif i > m:
                list[k] = aux_list[j]
                j += 1
            elif aux_list[i] > aux_list[j]:
                list[k] = aux_list[i]
                i += 1
            else:
                list[k] = aux_list[j]
                j += 1


a = [5,2,1,4,6,3]
print(MergeSort(a).sort())