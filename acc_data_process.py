class Acc_data:

    elem_lim = 100
    per_cnt_true = 100


    def __init__(self):
        self.xlist = []
        self.ylist = []
        self.zlist = []
        self.size = 0

        self.test1 = 1
        self.test2 = 2

        self.cnt = 0


    def process(self, acc_dict):

        self.xlist.append(acc_dict['x'])
        self.ylist.append(acc_dict['y'])
        self.zlist.append(acc_dict['z'])
        self.size += 1

        if len(self.xlist) > self.elem_lim:
            del(self.xlist[0])
            del(self.ylist[0])
            del(self.zlist[0])
            self.size -= 1

#DEBUG: Imitating False and True sequences
        self.cnt += 1
        if self.cnt == self.per_cnt_true:
            self.cnt = 0
            res = True
            self.test1 = sum(self.zlist) / float(len(self.zlist))
            self.test2 += 2
        else:
            res = False

        return res


    def stat_get(self):
        return self.test1, self.test2

