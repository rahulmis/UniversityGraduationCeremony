from sys import setrecursionlimit
setrecursionlimit(10**6)

class UniversityGraduationCeremony:
    def __init__(self, n, m):
        # n: number of academic days
        # m: cannot miss m or more classes consecutevly
        if n < m or n < 0 or m < 0:
            raise Exception("Invalid Inputs")
        self.n = n
        self.m = m

    def solution(self):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m)
        We are solving this problem using Dynamic Programming Tabulation approach with Space Optimization
        """

        n, m = self.n, self.m
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        x1 = dp[0]  # total number of valid way to attend classes
        x2 = temp[1]  # total number of way to miss last day

        return f"{x2}/{x1}"

    def run(self):
        print('Solution = ', self.solution())

if __name__ == "__main__":
    """
    Here we have to pass list of tuples where the first value is the days and the second
    value is the number of consecutive days that is not allowed to miss
    """
    inputs = [(5, 4), (10, 4)]
    for n, m in inputs:
        ceremony_obj = UniversityGraduationCeremony(n, m)
        ceremony_obj.run()
