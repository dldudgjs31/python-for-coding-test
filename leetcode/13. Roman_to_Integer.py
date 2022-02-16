'''
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman=dict()
        roman={"I" : 1,"V" : 5,"X":10, "L":50, "C":100,"D":500,"M":1000}
        sum=0
        for rom in range(len(s)):
            if  len(s)>rom+1:
                if s[rom]=="I" and (s[rom+1]=="V" or s[rom+1]=="X"):
                    sum-=roman.get(s[rom])
                elif s[rom]=="X" and (s[rom+1]=="L" or s[rom+1]=="C"):
                    sum-=roman.get(s[rom])
                elif s[rom]=="C" and (s[rom+1]=="D" or s[rom+1]=="M"):
                    sum-=roman.get(s[rom])
                else:
                    sum+=roman.get(s[rom])
            else:
                sum+=roman.get(s[rom])

        return sum
        


## 다른 풀이
## 문자열 replace 문법 활용
def romanToInt(self, s: str) -> int:
	roman_dict = {
		'I' :1,
		'V' :5,
		'X' :10,
		'L' :50,
		'C' :100,
		'D' :500,
		'M' :1000
	}

	s = s.replace("IV", "IIII").replace("IX", "IIIIIIIII")
	s = s.replace("XL", "XXXX").replace("XC", "XXXXXXXXX")
	s = s.replace("CD", "CCCC").replace("CM", "CCCCCCCCC")

	res = 0
	for char in s:
		res += roman_dict[char]

	return res