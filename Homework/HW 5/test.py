import random 
def p_test(n, m):
    trials = 1000000
    questions = 4

    total = 0
    real_trial = 0

    for i in range(trials):
       qs = set((random.randint(1, questions), random.randint(1, questions)))
       if len(qs) == 2:
          real_trial += 1
        
          if (n in qs) or (m in qs):
            total += 1

    print(real_trial, total / real_trial)

p_test(1, 2)
p_test(3, 4)
p_test(2, 3)
p_test(1, 4)
