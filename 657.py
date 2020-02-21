class Solution:
    def judgeCircle(self, moves):
        h = {"L" : 0, "R" : 0, "U" : 0, "D" : 0}
        for move in moves:
            h[move] += 1
        if h["L"] == h["R"] and h["U"] == h["D"]:
            return True
        return False
