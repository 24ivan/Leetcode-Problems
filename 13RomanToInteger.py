class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = s
        output = 0
        romanList = ['I','V','X','L','C','D','M']
        conversionList = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
            }
        currentIndex = 0
        currentChar = ''

        while currentIndex < len(s):
            currentChar = s[currentIndex]
            indexOfC = romanList.index(currentChar)
            if currentIndex + 1 < len(s):
                print(len(s))
                print(currentChar)
                print('Current index is: ')
                print(currentIndex)
                if (currentChar == 'I' or currentChar == 'X' or currentChar == 'C') and (s[currentIndex+1] == romanList[indexOfC+1] or s[currentIndex+1] == romanList[indexOfC+2]):
                    currentChar += s[currentIndex+1]
                    currentIndex+=2
                else:
                    currentIndex+=1
            else:
                currentIndex += 1
            print(currentChar)
            output += conversionList[currentChar]

        return output
        

p = Solution()
print(p.romanToInt('I'))
