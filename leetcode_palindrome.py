class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def checkPalindrome(ss):
            ln = len(ss)
            half = ln /2
            mid = ln%2

            if mid == 1:
                if ss[0:half] == ss[half+1:][::-1]:
                    return True
                else:
                    return False
            else:
                print ss[0:half+1] , ss[half:][::-1]
                if ss[0:half] == ss[half:][::-1]:
                    return True
                else:
                    return False
            return True
        l = len(s)
        n = l
        while n >= 0:
            for i in range(l - n + 1):
                ss = s[i:i + n]
                if checkPalindrome(ss):
                    return ss
            n = n - 1
        return ""


s = "cbbd"
ret = Solution().longestPalindrome(s)
print ret

"""
s = "cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvah" \
    "zpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrju" \
    "fvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwrib" \
    "fzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobb" \
    "ekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigg" \
    "lxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiop" \
    "hykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbj" \
    "yvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhz" \
    "spkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj"
"""