class Solution:
    def isIsomorphic(self, s, t):

        map_st = {}
        map_ts = {}

        for i in range(len(s)):

            if s[i] in map_st:

                if map_st[s[i]] != t[i]:
                    return False

            else:
                map_st[s[i]] = t[i]

            if t[i] in map_ts:

                if map_ts[t[i]] != s[i]:
                    return False

            else:
                map_ts[t[i]] = s[i]

        return True
