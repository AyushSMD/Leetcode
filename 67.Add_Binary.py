class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ia = max(len(a),len(b))-1
        output = ""
        c = 0

        if len(a)>len(b):
            b = (len(a)-len(b))*'0'+b
        else:
            a = (len(b)-len(a))*'0'+a

        while ia != -1:
            if a[ia] == '1' and b[ia] == '1':
                if c == 0:
                    output = '0'+output
                else: 
                    output = '1'+output
                c = 1
            elif a[ia] == '1' or b[ia] == '1':
                if c == 1:
                    output = '0'+output
                    c = 1
                else:
                    output = '1'+output
            else:
                if c == 1:
                    output = '1'+output
                    c = 0
                else:
                    output = '0'+output

            ia -= 1

        if c == 1:
            output='1'+output
            
        return output

Sol = Solution()
print (Sol.addBinary("11","1"))