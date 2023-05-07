from clasePlanAhorro import PlanAhorro
import csv

class ManejadorPlanAhorro:
    def __init__(self):
        self.__planes=[]

    def a(self):
        for i in self.__planes:
            print(i)

    def agregarPlan(self,plan):
        self.__planes.append(plan)

    def archivo(self):
        archivo = open('planes.csv')
        reader = csv.reader (archivo, delimiter = ';')
        for fila in reader:
            plan=PlanAhorro(int(fila[0]),fila[1],fila[2],float(fila[3]))
            self.agregarPlan(plan)
        print(self.__planes[1])

    def actualizarValor(self):
        for plan in self.__planes:
            print(f"Codigo:{plan.getCodigo()} Modelo:{plan.getModelo()} Version:{plan.getVersion()}")
            valor=float(input("Ingresa valor actual del vehiculo para modificar:"))
            plan.actualizaValor(valor)

    def planesCuotaInferior(self,valor):
        for plan in self.__planes:
            print(plan.valorCuota())
            if plan.valorCuota()<valor:
                print(f"Codigo:{plan.getCodigo()} Modelo:{plan.getModelo()} Version:{plan.getVersion()}")

    def cuotasLicitar(self):
        for plan in self.__planes:
            print(f"Codigo:{plan.getCodigo()} Modelo:{plan.getModelo()} Version:{plan.getVersion()} Cantidad de cuotas para licitar:{round(plan.licitar(),2)}")
    
    def modificarCuotas(self,cod):
        i=0
        while i<len(self.__planes) and self.__planes[i].getCodigo()!=cod:
            i+=1
        cuotas=int(input("Ingresa cantidad de cuotas: "))
        self.__planes[i].setCuotasLicitar(cuotas)

