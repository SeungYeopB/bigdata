###############################################################
# class화 작업
#expense[0]['date']
#expense[0]['coffee']
tot_coffee  = 0
tot_traffic = 0
tot_bab     = 0
class Pay:
    def __init__(self, date, coffee, traffic,bab):
        self.date = date
        self.coffee = coffee
        self.traffic = traffic
        self.bab = bab
    def make_total(self):
        return  self.coffee + self.traffic +\
                 self.bab
    def make_nujuk(self):
        global tot_coffee
        global tot_traffic
        global tot_bab
        tot_coffee += self.coffee
        tot_traffic += self.traffic
        tot_bab +=     self.bab

    def make_print(self):
        return "{}\t{}\t{}\t{}\t{}".format(
            self.date,
            self.coffee,
            self.traffic,
            self.bab,
            self.make_total()
    )
    def make_g_total(self):
        global tot_coffee
        global tot_traffic
        global tot_bab
        return "{}\t{}\t{}\t{}".format(
            '합계',
            tot_coffee,
            tot_traffic,
            tot_bab
    )

expense = [
    Pay("3/1", 8700, 9800, 8800),
    Pay("3/2", 5700, 9700, 6700),
    Pay("3/3", 8700, 9800, 9800),
    Pay("3/4", 5700, 9500, 6700),
    Pay("3/5", 8700, 6800, 8800),
    Pay("3/6", 6700, 9100, 6600),
    Pay("3/7", 8300, 9800, 4800),
    Pay("3/8", 5700, 9500, 9700),
]
#expense[0].date
#expense[0].coffee

# 타이틀 출력
print("   ===================")
print("      용돈 사용  리스트 ")
print("   ===================")
print("=======================================")
print("일자  음료대   교통비    식대    합계   ")
print("=======================================")
# tot_coffee  = 0
# tot_traffic = 0
# tot_bab     = 0
for exp in expense:
    exp.make_nujuk()
    print(exp.make_print())
print("=======================================")
#print("합 계:", tot_coffee, " ", tot_traffic, " ", tot_bab)
print(expense[0].make_g_total())
print("=======================================")


