def is_prime(n):
    s = 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s = 1
            break
    if s==1:
        return 0
    else:
        return 1
def resheto_eratosphena(n):
    resheto = list(range(n+1))
    resheto[1] = 0
    for i in resheto:
        if i > 1:
            for j in range(2*i, len(resheto), i):
                resheto[j] = 0
    return resheto
def circling_number(n):
    a = str(n)
    l = len(a)
    a = list(a[1::])+[a[0]]
    return sum(int(a[i])*(10**(l-i-1)) for i in range(l))
prime = list(set(resheto_eratosphena(1000000)))
prime.remove(0)
prime.sort()
list_of_circular_primes = []
for n in prime:
    if '0' in str(n):
        q=1
        continue
    q,l = 0,len(str(n))
    for i in range(l):
        n = circling_number(n)
        if is_prime(n)==0:
            q = 1
            break
    if q==0:
        list_of_circular_primes.append(n)
print(list_of_circular_primes)
print(len(list_of_circular_primes))