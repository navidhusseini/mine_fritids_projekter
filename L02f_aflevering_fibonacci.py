

# De første 100 Fibonacci-tal

n = 100
fibonacci = [1] * n     # En smart måde at lave en liste med 100
                        # 1-taller
for i in range(2,n):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

print("\nFibonaccitallene:")
print(fibonacci)


# Ekstra
# Tværsummen af Fibonacci-tallene
tvaersum = [0] * n
for i in range(n):
    fibo_str = str(fibonacci[i])    # Jeg caster det i-te tal som
                                    # en streng
    fibo_list = list(fibo_str)      # Jeg laver en liste med tallets
                                    # cifre
    for ciffer in fibo_list:
        tvaersum[i] += int(ciffer)  # Jeg adderer cifrene og får tværsum
    
print("\nTværsum:")
print(tvaersum)
    

# Ekstra ekstra
# Totaltværsummen af Fibonacci-tallene
totaltvaersum = tvaersum[:]         # Jeg starter med en kopi af
                                    # tvaersum

for i in range(n):
    for j in range(10): 	            # Jeg gætter på, at 10 gange
                                            # tværsum er nok (for jeg  
					    # kender ikke while endnu)
        fibo_str = str(totaltvaersum[i])    # det i-te tal som en streng
        fibo_list = list(fibo_str)          # liste med tallets cifre
        sum = 0
        for ciffer in fibo_list:
            sum += int(ciffer)              # tværsum af tallet
        totaltvaersum[i] = sum              # ny midlertidig totaltvær-
                                            # sum
#        print("i=" + str(i) + " tal=" + fibo_str + " sum=" + str(sum))
        
print("\nTotaltværsum:")
print(totaltvaersum)



