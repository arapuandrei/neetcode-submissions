class Solution:

    def serchColumn(self, matrix, target, l, r):
        mid = (r-l)//2+l
        print(l,r,mid, matrix[mid][0])
        if r-l <= 0:
            return mid
        else:
            if target in matrix[mid]:
                return mid
            if matrix[mid][0] < target:
                l=mid+1
            else:
                r = mid-1
            return self.serchColumn(matrix,target,l,r)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(matrix[self.serchColumn(matrix,target,0,len(matrix)-1)])
        return target in matrix[self.serchColumn(matrix,target,0,len(matrix)-1)]