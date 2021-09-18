import math

# to enumulate the API call in leetcode
first_bad_version = 4


def isBadVersion(v):
    if v >= first_bad_version:
        return True
    return False


class Solution:
    @staticmethod
    def firstBadVersion(n):
        """
        https://leetcode.com/problems/first-bad-version/
        Which app version is the 1st bad version?
        :param n: the number of app versions there are
        :return: the 1st bad app version
        """
        left = 1
        right = n
        while left < right:  # why < ?
            mid = math.floor(left + (right - left) / 2)  # magic formula
            if isBadVersion(mid):
                right = mid
            else:  # else ?
                left = mid + 1
        return left


print(Solution.firstBadVersion(10))

#
