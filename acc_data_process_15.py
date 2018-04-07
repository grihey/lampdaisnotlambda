class Acc_data:

    elem_lim = 100
    per_cnt_true = 100

    val_lim = 0.2
    uplim_max = 4
    lowlim_max = 4


    def __init__(self):
        self.xlist = []
        self.ylist = []
        self.zlist = []
        self.size = 0

        self.test1 = 1
        self.test2 = 2

        self.cnt = 0
        self.uplim_cnt = 0

        #complicated processing
        self.lowlim_cnt = 0
        self.is_up = False

    def process(self, acc_dict):

        #Bump analyzing function
        def bump_analyze(val_lim, cnt_lim):
            if abs(self.zlist[-1] - 1) > self.val_lim:
                self.uplim_cnt += 1
                if self.uplim_cnt > self.uplim_max:
                    # self.test1 = sum(self.zlist) / float(len(self.zlist))
                    self.uplim_cnt = 0
                    return True
                else:
                    return False
            else:
                self.uplim_cnt = 0
                return False

        def send_and_clear():
            self.test1 = sum(self.zlist)
            self.test2 = self.uplim_cnt - self.lowlim_max

            # Clear data
            self.uplim_cnt = 0
            self.lowlim_cnt = 0
            self.is_up = False

        #Bump analyzing function
        def bump_analyze2():

            if self.is_up == False:
                if abs(self.zlist[-1] - 1) > self.val_lim:
                    self.uplim_cnt += 1
                    if self.uplim_cnt >= self.uplim_max:
                        self.is_up = True
                        return False
                    else:
                        return False
                else:
                    self.uplim_cnt = 0
                    return False
            else:
                self.uplim_cnt += 1
                #If more, than our memory list size, we finish and send data
                if (self.uplim_cnt >= self.elem_lim):
                    #Data to send
                    self.test1 = sum(self.zlist)
                    self.test2 = self.uplim_cnt
                    #Clear data
                    self.uplim_cnt = 0
                    self.lowlim_cnt = 0
                    self.is_up = False

                    print("Got full list of upper elements\n")
                    print("Sum: %f\n", self.test1)
                    print("Cnt: %d\n", self.test2)
                    return True
                elif abs(self.zlist[-1] - 1) < self.val_lim:
                    self.lowlim_cnt += 1
                    if self.lowlim_cnt > self.lowlim_max:
                        #Data to send
                        total_up_cnt = self.uplim_cnt - self.lowlim_cnt
                        self.test1 = sum(self.zlist[-total_up_cnt:])
                        self.test2 = total_up_cnt
                        #Clear data

                        print("Sum: %f\n", self.test1)
                        print("Cnt: %d\n", self.test2)
                        self.uplim_cnt = 0
                        self.lowlim_cnt = 0
                        self.is_up = False
                        return True
                    else:
                        return False
                else:
                    self.lowlim_cnt = 0
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

        # if bump_analyze(self.val_lim, self.uplim_max):
        #     self.test1 = sum(self.zlist) / float(len(self.zlist))
        #     self.test2 += 2
        #     res = True
        # else:
        #     res = False
        #
        # return res

        return bump_analyze2()


    def stat_get(self):
        return self.test1, self.test2

