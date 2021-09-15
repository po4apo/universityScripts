import math
from report import Report
import matplotlib.pyplot as plt
import numpy as np
r = Report('исследование полупроводниковых диодов')
r.create_txt_report()
I = [0.5, 1, 2, 4, 6, 8, 10]
U=[]
k = 1.36e-23

e = 1.6e-19
T = 300
IZero = 3e-10


GE = [0.35, 0.4, 0.47, 0.52, 0.59, 0.61, 0.65]
SI = [0.8, 0.82, 0.89, 0.92, 1, 1, 1.1]
SID = [1.51, 1.58, 1.63, 1.7, 1.71, 1.75, 1.79]

Stab = [0.75, 0.79, 0.8, 0.83, 0.86, 0.88, 0.9]
StabInvers= [2.55, 2.79, 3, 3.6, 3.9, 4.08, 4.2]

#Идеальный расчёт для кремния
for i in I:
    U.append((k*T/e) * math.log((i/IZero) + 1))

r.add_text_block('Идеальный расчёт для кремния', U)
print("Идеальный расчёт для кремния:")
print(U)
print('-----------------\n')


# Построение графиков
xGE = np.array(GE)
xSI = np.array(SI)
xSID = np.array(SID)
y = np.array(I)

plt.title('Вольт амперная характеристика')
plt.xlabel('Uпр')
plt.ylabel('Iпр')
plt.grid()
plt.plot(xGE,y)
plt.text(xGE[0]-0.05, 0.15, 'GE')
plt.plot(xSI,y)
plt.text(xSI[0]-0.05, 0.15, 'SI')
plt.plot(xSID,y)
plt.text(xSID[0]-0.05, 0.15, 'SID')
plt.savefig('ВОХ.jpg')

plt.show()

# Расчитаем R0 для каждого элемента
R0GE = []
R0SI = []
R0SID = []
R0Stab = []
for i in range(5):
    R0GE.append(GE[i]/I[i])
    R0SI.append(SI[i]/I[i])
    R0SID.append(SID[i]/I[i])
    R0Stab.append(Stab[i]/I[i])

r.add_text_block('Результат расчета статического сопративления',
                 f"R0GE = {R0GE}", f"R0SI = {R0SI}", f"R0SID = {R0SID}", f"R0SID = {Stab}")
print(f"R0GE = {R0GE}")
print(f"R0SI = {R0SI}")
print(f"R0SID = {R0SID}")
print(f"R0SID = {Stab}")
print('-----------------\n')

# Расчитаем Ri для каждого элемента
RiGE = GE[4]-GE[2]/I[4]-I[2]
RiSI = SI[4]-SI[2]/I[4]-I[2]
RiSID = SID[4] - SID[2] / I[4] - I[2]
RiStab = Stab[4]-SID[2]/I[4]-I[2]

r.add_text_block('Результат расчёта статического сопративления',
                 f"RiGE = {GE[4]-GE[2]/I[4]-I[2]}", f"RiSI = {SI[4]-SI[2]/I[4]-I[2]}",
                  f"RiSID = {SID[4] - SID[2] / I[4] - I[2]}", f"RiStab = {Stab[4]-SID[2]/I[4]-I[2]}")
print(f"RiGE = {GE[4]-GE[2]/I[4]-I[2]}")
print(f"RiSI = {SI[4]-SI[2]/I[4]-I[2]}")
print(f"RiSID = {SID[4] - SID[2] / I[4] - I[2]}")
print(f"RiStab = {Stab[4]-SID[2]/I[4]-I[2]}")
print('-----------------\n')


# Расчитаем критизну диодов
SGE = 1/RiGE
SSI = 1/RiSI
SSID = 1/RiSID
SStab = 1/RiStab


r.add_text_block('Результаты расчёта крутизны диодов',
                 f"SGE = {SGE}",
                 f"SSI = {SSI}",
                 f"SSid = {SSI}",
                 f"SStab = {SStab}")

print(f"SGE = {SGE}")
print(f"SSI = {SSI}")
print(f"SSid = {SSID}")
print(f"SStab = {SStab}")
print('-----------------\n')

r.insert_all_line('a')






