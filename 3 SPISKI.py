sp1=['бананы','apple','tomato','potatos','ananas']
print(sp1[2])
sp1[2]='mandarin'
print(sp1)
sp1.append('cheese')
print(sp1)

del sp1[1]
print(sp1)

sp2=[2,45,457,746,34,74,465]
sp3=[567,45,873,'sdf',36,'rthrr4']
sp4=[sp2,sp3,sp1]
print(sp4)
print(sp4[1][1])

''' 2
sp5=[1,2,3]
sp6=[4,5,6]
sp7=sp5+sp6
print(sp7)
'''