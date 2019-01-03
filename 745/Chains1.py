class Chains1:

    def countMaximalChains(self, n):
        if n == 1:
            return 1
        return 2 * self.countMaximalChains(n - 1)
