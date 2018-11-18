class ESArrary(list):
    def __init__(self, *lst):
        self.lst = lst
        self.length = len(self.lst)
        self.flattened = []

    def join(self, s):
        if self.length == 1:
            oneitem = self.lst[0]
            middlelist = [str(oneitem[i])+str(s) for i in range(len(oneitem)-1)]
            middlelist.append(str(oneitem[-1]))

        else:
            middlelist = [str(self.lst[i])+str(s) for i in range(self.length-1)]
            middlelist.append(str(self.lst[-1]))
        return   ("".join(middlelist))

    def every(self, func):
        check = True
        if len(self.lst) == 1:
            for item in self.lst[0]:
                if not func(item):
                    check = False
            return check
        else:
            for item in self.lst:
                if not func(item):
                    check = False
            return check

    def for_each(self,func):
        for item in self.lst[0]:
            func(item)

    def flatten(self):
        finallist = []
        def flat(longlist):
            for i in longlist:
                if isinstance(i, list):
                    flat(i)
                else:
                    finallist.append(i)
        flat(self.lst)
        return finallist



if __name__=="__main__":

    x = ESArrary([1, -3, 10, 5])
    z = ESArrary([[1,3], [2]])
    y = ESArrary([[3, 4], [5], 6, [7, [8, [9, 10]]]])

    print(x.join("**"))
    print(y.join("**"))
    print(x.every(lambda v: v > 0))
    print(z.every(lambda v: len(v) > 0))
    x.for_each(print)
    z.for_each(print)
    print(z.flatten())
