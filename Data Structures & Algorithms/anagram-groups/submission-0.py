class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for str in strs:
            key = tuple(sorted(str))
            if key not in seen:
                seen[key] = [str]
            else:
                seen[key].append(str)

        return list(seen.values())

        