from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(combination: str, index: int) -> None:
            # Base case: we've processed all digits
            if index == len(digits):
                result.append(combination)
                return

            # Try all possible letters for the current digit
            for letter in phone[digits[index]]:
                backtrack(combination + letter, index + 1)

        backtrack("", 0)
        return result
