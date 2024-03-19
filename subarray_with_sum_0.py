def subArrayExists(self,arr,n):
    prefix_sum_set = set()
    prefix_sum = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in prefix_sum_set:
            return True
        prefix_sum_set.add(prefix_sum)

    return False