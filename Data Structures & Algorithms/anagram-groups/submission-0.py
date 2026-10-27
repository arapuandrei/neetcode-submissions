class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i in strs:
            if ''.join(sorted(i)) in m.keys():
                m[''.join(sorted(i))].append(i)
            else:
                m[''.join(sorted(i))]=[i]

        return [m[x] for x in m.keys()]

