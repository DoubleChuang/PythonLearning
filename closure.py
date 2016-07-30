def gen_power(base):
    def power(exp):
        return base ** exp
    return power

power2=gen_power(2)
power3=gen_power(3)

print power2(3)
print power3(2)
