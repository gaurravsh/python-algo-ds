# Leetcode Problem # 733. Flood Fill
# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        oldColor = image[sr][sc]
        
        def fill(r: int, c: int):
            if r>=0 and r<rows and c>=0 and c<cols and image[r][c]==oldColor and image[r][c]!=newColor:
                image[r][c] = newColor
                fill(r-1,c)
                fill(r+1,c)
                fill(r,c-1)
                fill(r,c+1)
        
        fill(sr,sc)
        
        return image