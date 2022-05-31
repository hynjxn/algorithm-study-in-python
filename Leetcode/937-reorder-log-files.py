from typing import List

class Solution:
    def reorderLogFiles(self, logs:List[str]) ->List[str]:
        let, dig = [], []
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                let.append(log)

        # 람다 표현식 사용 -> 문자 비교, 문자 동일할 경우 식별자 순
        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let + dig

if __name__ == "__main__":
    answer = Solution()
    print(answer.reorderLogFiles(["dig1 8 1 5 1","let art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))