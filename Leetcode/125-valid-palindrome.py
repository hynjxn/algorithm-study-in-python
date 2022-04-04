import collections
import re

class Solution:
    # 1. 리스트로 변환
    def isPalindrome1(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                # isalnum() : 영문자, 숫자 여부를 판별하는 함수.
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                # pop(0)은 리스트 맨 앞의 값, pop()는 리스트 맨 뒤의 값을 pop. 앞 뒷 값 같은지 매칭
                return False

        return True


    # 2. 덱(deque) 이용 -> 리스트 성능 개선
    def isPalindrome2(self, s: str) -> bool:
        strs = collections.deque();
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    # 3. 슬라이싱 사용
    def isPalindrome3(self, s:str) ->bool:
        s = s.lower()
        # re 사용하여 불필요한 문자 제거
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1] # [::-1] 사용하면 배열, 리스트 등 뒤집을 수 있음

if __name__ == "__main__":
    answer = Solution()
    print(answer.isPalindrome3("A man, a plan, a canal: Panama"))