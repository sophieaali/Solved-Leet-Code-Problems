class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        strings = {}
        for i in range(numRows):
            var_name = "var%d" % i
            strings[var_name] = ''

        try:
            while len(s)>0:
                for i in range(numRows):
                    var_name = "var%d" % i
                    strings[var_name] += s[0]
                    s = s[1:]

                for i in range(numRows-2, 0, -1):
                    var_name = "var%d" % i
                    strings[var_name] += s[0]
                    s = s[1:]
        except:
            pass



        newString = ''
        for i in range(numRows):
            var_name = "var%d" % i
            newString += strings[var_name]
        return newString


s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows))