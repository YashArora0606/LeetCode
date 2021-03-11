class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        out = []
        for lst in A:
            flipped = lst[::-1]
            inverted = [0 if elem == 1 else 1 for elem in flipped]
            out.append(inverted)
        return out
