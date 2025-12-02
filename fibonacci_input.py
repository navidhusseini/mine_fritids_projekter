fibonacci = []
a = 0
b = 1
for i in range (100):
    fibonacci.append(a)
    c = a + b
    a = b
    b = c

stopbesked = 'stop'
tekst = '\nSkriv et fibonnacital for at se om det er et fibonaccital.'
tekst += f'\nSkriv "{stopbesked}" for at stoppe programmet: '
besked = ''

while besked != stopbesked:
    besked = input(tekst)
    if int(besked) not in fibonacci:
        print("Det er ikke et fibonaccital")
        print(besked)
    else :
        print("Det er et fibonaccital")
        print(besked)