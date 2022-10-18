class PhysicalStream:
    def __init__(self, mass, heat_capacity, temperature):
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.temperature = temperature


about_p_s_1 = input("Введите информацию о первом потоке в формате:\nмасса теплоёмкость температура\n").split()
about_p_s_2 = input("Введите информацию о втором потоке в формате:\nмасса теплоёмкость температура\n").split()

p_s_1 = PhysicalStream(float(about_p_s_1[0]), float(about_p_s_1[1]), float(about_p_s_1[2]))
p_s_2 = PhysicalStream(float(about_p_s_2[0]), float(about_p_s_2[1]), float(about_p_s_2[2]))

tm = (p_s_1.mass * p_s_1.heat_capacity * p_s_1.temperature + p_s_2.mass * p_s_2.heat_capacity * p_s_2.temperature) / \
     (p_s_1.mass * p_s_1.heat_capacity + p_s_2.mass * p_s_2.heat_capacity)
print('Температура смеси: ', tm)
