"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
"""
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        total = (C-A)*(D-B) + (G-E)*(H-F)
        overlap = 0
        if E < C and F < D and G > A and H > B:
            xleft, xright = max(A,E), min(C,G)
            yleft, yright = max(B,F), min(D,H)
            overlap = (xright-xleft)*(yright-yleft)
            # x = sorted([A,C,E,G])
            # y = sorted([B,D,F,H])
            # overlap = (x[2]-x[1])*(y[2]-y[1])
        return total - overlap

def computeArea(self, A, B, C, D, E, F, G, H):
    overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
    return (A-C)*(B-D) + (E-G)*(F-H) - overlap

s = Solution()
A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2
print(s.computeArea(A,B,C,D,E,F,G,H))