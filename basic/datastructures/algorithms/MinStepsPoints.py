class MinStepsPoint:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        sumX = 0
        sumY = 0
        for i in range(0..len(A) - 1):
            sumX += sum(A[i + 1] - A[i])
            sumY += sum(B[i + 1] - B[i])

        return sumX if sumX >= sumY else sumY