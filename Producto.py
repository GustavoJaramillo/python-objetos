class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    #Metodo get para _id_producto
    @property
    def id_producto(self):
        return self._id_producto

    #Metodo set para _id_producto
    @id_producto.setter
    def id_producto(self,id_producto):
        self._id_producto = id_producto

    #Metodo get para _nombre
    @property
    def nombre(self):
        return self._nombre

    #Método set para nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    #Método get para precio
    @property
    def precio(self):
        return self._precio

    #Metodo set para preico
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa',100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 200.50)
    print(producto2)
