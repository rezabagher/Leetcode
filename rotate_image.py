# -*- coding: utf-8 -*-
"""Rotate Image.ipynb

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution(object):
    def rotate(self, matrix):
      import numpy as np
      matrix = np.array(matrix)
      matrix = matrix.T
      return np.fliplr(matrix)

s = Solution()

r=s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

r
