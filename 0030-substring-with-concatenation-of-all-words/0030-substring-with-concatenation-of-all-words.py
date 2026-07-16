from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = Counter(words)
        result = []

        for offset in range(word_len):

            left = offset
            right = offset
            current = {}
            count = 0

            while right + word_len <= len(s):

                word = s[right:right + word_len]
                right += word_len

                if word in word_count:

                    current[word] = current.get(word, 0) + 1
                    count += 1

                    while current[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    current.clear()
                    count = 0
                    left = right

        return result