class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        
        for word in strs:
            counts = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                counts[index] += 1
            key = tuple(counts)
            if key in my_dict:
                my_dict[key].append(word)
            else:
                my_dict[key] = [word]
        return list(my_dict.values())
