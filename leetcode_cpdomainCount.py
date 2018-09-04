class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dct = {}
        fnl_lst = []
        for cpname in cpdomains:
            cp = cpname.split(" ")
            cpcount = int(cp[0])
            cnum = len(cp[1].split("."))
            cpup = cp[1]
            for i in range(cnum):
                key = cpup
                value = cpcount
                if key not in dct.keys():
                    dct[key] = value
                else:
                    dct[key] +=cpcount
                if "." in cpup:
                    cpup = cpup.split(".",1)[1]

        for key in dct.keys():
            fnl_lst =fnl_lst +[str(dct[key]) + " " + key]
        return fnl_lst



def main():

    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

    ret = Solution().subdomainVisits(cpdomains)

    print ret


if __name__ == '__main__':
    main()