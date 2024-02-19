class Dia:
    # Constructor de la clase por defecto
    def __init__(self, anyo=1998, mes=9, dia=10):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.dia_semana = self.calcular_dia_semana()

    # método para calcular día de la semana
    def calcular_dia_semana(self):
        # diccionario para el día según el indicativo en número
        weekDay = {0: 'SABADO', 1: 'DOMINGO', 2: 'LUNES', 3: 'MARTES', 4: 'MIERCOLES', 5: 'JUEVES', 6: 'VIERNES'}

        # Ajustar el año y el mes y F por efectos de un día de diferencia del algoritmo cuando el mes se ajusta
        anyo = self.anyo
        mes = self.mes
        F = 0
        if mes < 3:
            anyo -= 1
            mes += 12
            F = -1

        # Calcular los valores necesarios
        A = anyo % 100
        B = anyo // 100
        C = 2 - B + (B // 4)
        D = A // 4
        E = 13 * (mes + 1) // 5
        F = A + C + D + E + self.dia + F

        # Obtener el día de la semana
        dia_semana = (F) % 7  # Ajuste para que 0 sea sábado, 1 domingo, etc.

        return weekDay[dia_semana]

    # Método para calcular si el año es bisiesto
    def es_bisiesto(self):
        # Un año es bisiesto si cumple las siguientes condiciones:
        # - Debe ser divisible entre 4.
        # - No será bisiesto si es divisible entre 100, a menos que también sea divisible entre 400.
        # Retorna verdadero 1 si es bisiesto o falso 0 si no es bisiesto
        return (self.anyo % 4 == 0) and (self.anyo % 100 != 0 or self.anyo % 400 == 0)

    # Método para validar si la fecha es correcta
    def validar_fecha(self):
        # Verificar que el mes tenga el valor correcto
        if not 1 <= self.mes <= 12:
            raise ValueError("El mes debe estar entre 1 y 12.")

        # Verificar que el día tenga el valor correcto para el mes y año dados
        dias_por_mes = [31, 28 + self.es_bisiesto(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not 1 <= self.dia <= dias_por_mes[self.mes - 1]:
            raise ValueError("Día inválido para el mes y año dados.")

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anyo} (Día de la semana: {self.dia_semana})"


def main():
    try:
        d = Dia(2024, 2, 1)
        print(d)
    except ValueError as e:
        print(e)

    try:
        d = Dia()
        print(d)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()