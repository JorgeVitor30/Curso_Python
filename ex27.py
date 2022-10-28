from collections import deque

fila = deque()
fila.append('João')
fila.append('Arthur')
fila.append('Vitor')
fila.append('Felipe')
fila.popleft()

for valor in fila:
    print(valor)
    
    
fila2 = deque(maxlen=10)
fila2.extend([1,2,3,4,5,6])
fila2.insert(2,'Vitor')
print(fila2)

fila2.rotate(2) # 2 ULTIMOS VEM PROS PRIMEIROS

print(fila2)
