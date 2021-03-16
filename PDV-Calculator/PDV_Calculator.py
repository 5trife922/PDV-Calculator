Bases = ["10Base-5","10Base-2","10Base-T","10Base-FB","10Base-FL","FOIRL","AUI"]
LBase = [11.8,11.8,15.3,0,12.3,7.8,0.0]
RBase = [169.5,169.5,165,0,156.5,152,0]
GapBase = [46.5,46.5,42,24,33.5,29,0]
Delay = [0.0866,0.1026,0.113,0.1,0.1,0.1,0.1026]
SelBaseGap = []
SelLengthGap = []
GapOTV = []

def baseprint():
    print(f"Базы: \n 1) {Bases[0]} \n 2) {Bases[1]} \n 3) {Bases[2]} \n 4) {Bases[3]} \n 5) {Bases[4]} \n 6) {Bases[5]} \n 7) {Bases[6]} \n" )


CoutGap = int(input("Введите кол-во промежуточных сегментов >_ "))


baseprint();
SelBaseL = int(input("Выбери базу левого сегента >_ ")) - 1
LengthL = float(input("Длина левого сегмента >_ "))
LOTV = LBase[SelBaseL] + LengthL * Delay[SelBaseL]
PDV = LOTV

baseprint();
SelBaseR = int(input("Выбери базу правого сегента >_ ")) - 1
LengthR= float(input("Длина правого сегмента >_ "))
ROTV = RBase[SelBaseL] + LengthR * Delay[SelBaseL]
PDV += ROTV

if(CoutGap != 0):
    for i in range(0, CoutGap):
        baseprint();
        SelBaseGap.insert(len(SelBaseGap) + 1, int(input("Выбери базу промежуточного сегмента >_ ")) - 1)
        SelLengthGap.insert(len(SelLengthGap) + 1, float(input("Длина промежуточного сегмента >_ ")))
        GapOTV.insert(len(GapOTV) + 1, GapBase[SelBaseGap[i]] + SelLengthGap[i] * Delay[SelBaseGap[i]])
        PDV += GapOTV[i]

print (round(PDV, 3))

if PDV < 575:
    print("Сеть проходит по критерию времени двойного оборота сигнала (PDV < 575)")
else:
    print("Сеть не проходит по критерию времени двойного оборота сигнала (PDV > 575)")
