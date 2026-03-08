class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        columncounter=[0]*len(mat[0])
        rowcounter=[0]*len(mat)
        answcounter=0
        for i, row in enumerate(mat):
            rowcounter[i]+=sum(row)
            for j, el in enumerate(row):
                if el==1:
                    columncounter[j]+=1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowcounter[i] == 1 and columncounter[j] == 1:
                    answcounter += 1          
        return answcounter