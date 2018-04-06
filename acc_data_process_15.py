class Acc_data:

    elem_lim = 100
    per_cnt_true = 100

    val_lim = 0.3
    uplim_max = 3


    def __init__(self):
        self.xlist = []
        self.ylist = []
        self.zlist = []
        self.size = 0

        self.test1 = 1
        self.test2 = 2

        self.cnt = 0
        self.uplim_cnt = 0

    def process(self, acc_dict):

        #Bump analyzing function
        def bump_analyze(val_lim, cnt_lim):

            if abs(self.zlist[-1] - 1) > self.val_lim:
                self.uplim_cnt += 1
                if self.uplim_cnt > self.uplim_max:
                    self.test2 = sum(self.zlist) / float(len(self.zlist))
                    self.uplim_cnt = 0
                    return True
                else:
                    return False
            else:
                self.uplim_cnt = 0
                return False


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

