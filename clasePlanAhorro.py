class PlanAhorro:
    __codigo=""
    __modelo=""
    __version=""
    __valorvehiculo=0.0
    __cantcuotas=60
    __cuotaslicitar=10

    def __init__(self,codigo,modelo,version,valor):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valorvehiculo=valor
        self.__cuotaslicitar=PlanAhorro.__cuotaslicitar

    def valorCuota(self):
        cuota=(self.__valorvehiculo/self.__cantcuotas) + self.__valorvehiculo * 0.10
        return cuota

    def actualizaValor(self,valor):
        self.__valorvehiculo=valor

    def __str__(self):
        return f"{self.__codigo} {self.__modelo} {self.__version} {self.__valorvehiculo} {self.__cantcuotas} {self.__cuotaslicitar}"
    
    def getCodigo(self):
        return self.__codigo
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def licitar(self):
        licitar=self.__cuotaslicitar * self.valorCuota()
        return licitar
    
    def setCuotasLicitar(self,cuotas):
        self.__cuotaslicitar=cuotas
    #@classmethod
    #def setCuotasLicitar(cls,cuotas):
    #    cls.__cuotaslicitar=cuotas