

def binary_search_practice1():
    def binary_search(array: list, target: int) -> int:
        """ leetcode problem 704 """
        left = 0
        right = len(array) - 1
        while left <= right:
            idx = left + (right - left)  # +? or -?
            if array[idx] == target:
                return idx
            if target < array[idx]:
                right = idx - 1  # +? or -?
            else:
                left = idx + 1  # +? or -?
        return -1





# end of file
