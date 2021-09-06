def test_case():
    with open('246.csv') as file:
        cases = [line.strip().replace('\ufeff', '') for line in file.readlines()]
    return cases


class Solution2:
    """
    This did not pass all test cases
    """
    def __init__(self):
        for case in test_case():
            self.isStrobogrammatic(case)

    @staticmethod
    def isStrobogrammatic(num: str) -> bool:
        # 0, 1, 8
        # 00, 11, 88, 96, 69
        # 101, 808
        num_len = len(num)
        h = num[0:2]  # hash
        h2 = num[0:3]  # 2nd hash
        h3 = num[0:5]  # 3rd hash
        stro = {
            '0': True,
            '1': True,
            '8': True,
            '00': True,
            '11': True,
            '8118': True,
            '88': True,
            '96': True,
            '69': True,
            '101': True,
            '808': True,
            '181': True,
            '60809': True,
            '90806': True,
            '90006': True,
            '61119': True,
            '16191': True,
            '86198': True
        }

        if num_len == 1 and num in stro:
            return True
        elif num_len >= 2:
            if h in stro and num.count(h) == num_len / 2:
                return True
            elif h2 in stro and num.count(h2) == num_len / 3:
                return True
            elif h3 in stro and num.count(h3) == num_len / 5:
                return True
            else:
                return False
        else:
            return False


class Solution:
    @staticmethod
    def isStrobogrammatic(num: str) -> bool:
        sb = []  # string builder

        for c in reversed(num):
            if c in {'0', '1', '8'}:
                sb.append(c)
            elif c == '6':
                sb.append('9')
            elif c == '9':
                sb.append('6')
            else:
                return False

        return ''.join(sb) == num

for line in test_case():
    Solution.isStrobogrammatic(line)

# end of file
