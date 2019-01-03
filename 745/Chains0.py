class Chains0:

    def getProperSubset(self, x, y):
        # [x, x + 1) is always a proper subset of [x, y]
        # when y >= (x + 2).
        return (x, x + 1)
