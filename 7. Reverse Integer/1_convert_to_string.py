class Solution(object):
    def reverse(self, x):
        c = []
        if x < 0:
            postivie_x = x*-1
            b = str(postivie_x)
        else:    
            b = str(x)

        for digit in b[::-1]:
            c.append(int(digit))    
        res = int("".join(map(str, c))) 
          
        if res > (2**31) - 1:
            return 0
        elif x < 0:
            return (-1*res)
        else:
            return(res)
