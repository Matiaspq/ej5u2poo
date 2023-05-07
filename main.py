from claseManejadorPlanAhorro import ManejadorPlanAhorro

if __name__=='__main__':
    p=ManejadorPlanAhorro()
    p.archivo()
    opcion=""
    while(opcion!="0"):
        print("\na. Actualizar el valor del vehículo de cada plan.")
        print("b. Ver planes cuyo valor de la cuota sea inferior al valor dado.")
        print("c. Mostrar cantidad de cuotas para licitar el vehiculo de cada plan.")
        print("d. Modificar la cantidad de cuotas para licitar.")
        opcion=input("Ingresa opcion: ")
        if opcion=="a":
            p.actualizarValor()
        elif opcion=="b":
            valor=float(input("Ingresa valor: "))
            p.planesCuotaInferior(valor)
        elif opcion=="c":
            p.cuotasLicitar()
        elif opcion=="d":
            codigo=int(input("Ingresa codigo de plan para modificar cuotas: "))
            p.modificarCuotas(codigo)
        else: p.a()
