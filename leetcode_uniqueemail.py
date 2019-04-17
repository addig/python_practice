class Solution(object):
    def numUniqueEmails(self,emails):
        num = 0
        newemail = []

        for address in emails:
            localname =address.split("@")[0]
            domain = address.split("@")[1]
            if "." in localname:
                localname = localname.replace(".","")
            if "+" in localname:
                localname = localname.split("+")[0]

            newemail = newemail+[localname+"@"+domain]

        num = len(set(newemail))
        return num





def main():
    emails = [u'test.email+alex@leetcode.com', u'test.e.mail+bob.cathy@leetcode.com', u'testemail+david@lee.tcode.com']
    ret = Solution().numUniqueEmails(emails)


if __name__=='__main__':
    main()