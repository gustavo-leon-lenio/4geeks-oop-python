class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_salario(self):
        return "Un Salario"


class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, salario, beneficios):
        super().__init__(nombre, salario)
        self.beneficios = beneficios

    def obtener_salario(self):
        return self.salario + self.beneficios


class EmpleadoPartTime(Empleado):
    def __init__(self, nombre, salario, horas_trabajo):
        super().__init__(nombre, salario)
        self.horas_trabajo = horas_trabajo

    def obtener_salario(self):
        salario_tiempo_completo = 40
        salario_medio_tiempo = (self.salario / salario_tiempo_completo) * self.horas_trabajo
        return salario_medio_tiempo
