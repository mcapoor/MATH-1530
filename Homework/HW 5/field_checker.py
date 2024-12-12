def field_check(n):
    #Checks if all elements of Z/nZ have inverses

    fail_list = []
    for candidate in range(1, n):
        mod_list = []
        for factor in range(1, n):
            mod_list.append((candidate * factor) % n)

        if 1 not in mod_list:
            fail_list.append(candidate)               

    if len(fail_list) != 0:
        print(f"These elements of Z/{n}Z do not have inverses: {fail_list}")
    else:
        print(f"Z/{n}Z is a field")

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
primes_squared = list(map(lambda x: x**2, primes))

for p in primes_squared:
    field_check(p)