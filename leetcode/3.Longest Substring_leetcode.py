"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        1. 입력된 문자열 받기
        2. 임시 저장 리스트 생성
        3. 중복체크
        - 중복인 경우 중복된 문자열 인덱스까지 문자열 제거
        - 
        4. 체크 완료시 문자열 길이 max에 담기
        """
        inputstring=list(s)
        valid=list()
        maxnum=0
        temp=0
        temp2=0
        ##1차 필터링
        ## 0글자 입력시 0 반환
        if len(inputstring)==0:
            maxnum=0
            return maxnum
        ## 1글자 입력시 1 반환
        elif len(inputstring)==1:
            maxnum=1
            return maxnum
        else:
            ## 2글자 이상부터 검증 스타트
            for i in inputstring:
                ##중복성 체크
                ##중복인 경우
                if valid.count(i)!=0:
                    ## 중복인 인덱스 찾기
                    dupnum=valid.index(i)
                    ## 중복 제거 이전에 문자열 길이 저장
                    temp=len(valid)
                    if temp>temp2:
                      temp2=temp
                    ## 중복 인덱스 이하 제거
                    del valid[:dupnum+1]
                    ## 중복 제거후 해당 문자열 추가
                    valid.append(i)
                    #print("중복인경우 :",valid," temp :",temp," temp2 :",temp2)
                ## 중복이 아닌경우
                else:
                    valid.append(i)
                    if len(valid)>temp2:
                      temp2=len(valid)
                    #print("중복 아닌 경우 :",valid," temp :",temp," temp2 :",temp2)
        maxnum=temp2
        return maxnum
      
                    
                
        