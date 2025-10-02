class Carrera:
    def __init__(self, nombre, grado, rama):
        self.setNombre(nombre)
        self.setGrado(grado)
        self.setRama(rama)
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setGrado(self, grado):
        self.__grado = grado

    def setRama(self, rama):
        self.__rama = rama

    def getNombre(self):
        return self.__nombre
    
    def getGrado(self):
        return self.__grado
    
    def getRama(self):
        return self.__rama