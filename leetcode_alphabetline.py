import string
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 1
        acc = 0
        alpha = list(string.ascii_lowercase)
        dct = dict(zip(alpha,widths))
        for letter in S:
            acc+=dct[letter]
            if acc > 100:
                line+=1
                acc = dct[letter]
        return [line,acc]



def main():

    widths = [7, 5, 4, 7, 10, 7, 9, 4, 8, 9, 6, 5, 4, 2, 3, 10, 9, 9, 3, 7, 5, 2, 9, 4, 8, 9]#[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

    #S =  "bbbcccdddaaa"

    S = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"

    ret = Solution().numberOfLines(widths, S)


    print ret


if __name__ == '__main__':
    main()