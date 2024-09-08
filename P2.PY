from abc import ABC, abstractmethod

class EstrategiaEnvio(ABC):
    @abstractmethod
    def calcular_costo_envio(self, precio_producto, peso_producto):
        """
        Método abstracto para calcular el costo de envío.
        
        Args:
            precio_producto (float): El precio del producto.
            peso_producto (float): El peso del producto en kilogramos.
        
        Returns:
            float: El costo de envío calculado.
        """
        pass

class EnvioEstadosUnidos(EstrategiaEnvio):
    def calcular_costo_envio(self, precio_producto, peso_producto):
        # Tarifa fija de $10 más un 5% del precio del producto
        tarifa_fija = 10.0
        porcentaje_precio = 0.05
        return tarifa_fija + (precio_producto * porcentaje_precio)

class EnvioCanada(EstrategiaEnvio):
    def calcular_costo_envio(self, precio_producto, peso_producto):
        # $1 por cada kilogramo de peso
        costo_por_kg = 1.0
        return peso_producto * costo_por_kg

class EnvioBrasil(EstrategiaEnvio):
    def calcular_costo_envio(self, precio_producto, peso_producto):
        # Tarifa fija de $15
        return 15.0
class Tienda:
    def __init__(self, estrategia_envio):
        self.estrategia_envio = estrategia_envio

    def calcular_costo_total(self, precio_producto, peso_producto):
        costo_envio = self.estrategia_envio.calcular_costo_envio(precio_producto, peso_producto)
        return precio_producto + costo_envio
def main():
    precio_producto = 100.0
    peso_producto = 2.0

    # Crear instancias de las estrategias de envío
    envio_eeuu = EnvioEstadosUnidos()
    envio_canada = EnvioCanada()
    envio_brasil = EnvioBrasil()

    # Crear instancias de la tienda con las estrategias específicas
    tienda_eeuu = Tienda(envio_eeuu)
    tienda_canada = Tienda(envio_canada)
    tienda_brasil = Tienda(envio_brasil)

    # Calcular y mostrar el costo total para cada país
    costo_total_eeuu = tienda_eeuu.calcular_costo_total(precio_producto, peso_producto)
    costo_total_canada = tienda_canada.calcular_costo_total(precio_producto, peso_producto)
    costo_total_brasil = tienda_brasil.calcular_costo_total(precio_producto, peso_producto)

    


    print("precio del producto:",precio_producto)
    print("peso del producto:",peso_producto)
    print("costo de envio a estados unidos:$15")
    print(f"Costo total en Estados Unidos: ${costo_total_eeuu:.2f}")
    print("costo de envio a estados unidos:$2")
    print(f"Costo total en Canadá: ${costo_total_canada:.2f}")
    print("costo de envio a estados unidos:$15")
    print(f"Costo total en Brasil: ${costo_total_brasil:.2f}")

if __name__ == "__main__":
    main()
