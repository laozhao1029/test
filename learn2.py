import random as rd
seq_1 = []
seq_random = [rd.randint(10,80) for i in range(10) ]
seq_2 = [ i for i in range(10) ]

print( seq_random )
print( seq_2 )

seq_1 = list(map(lambda x,y:x+y, seq_2,seq_random))
seq_filter1 = list(filter( lambda x:x>50,seq_random))
seq_filter2 = list(filter( lambda x:x%2==0,seq_random))
# seq_11 = list(seq_1)
# seq_3 = list(seq_filter1)
# seq_4 = list(seq_filter2)

print( '两个列表元素求和:',seq_1)
print( '大于50的随机数: ',seq_filter1)
print( '随机数列表中的偶数: ',seq_filter2 )

# seq_11 = list(seq_1)
# seq_3 = list(seq_filter1)
# seq_4 = list(seq_filter2)
print('second time=')
print( '两个列表元素求和:',seq_1 )
print( '大于50的随机数: ',seq_filter1 )
print( '随机数列表中的偶数: ',seq_filter2 )