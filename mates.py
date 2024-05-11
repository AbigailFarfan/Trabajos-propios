class PreparacionMate:
    def __init__(self):
        self.clean = False

    def lavarMate(self):
        print("Lavando el poro y la bombilla...")

    def agregarEdulcorante(self, edulcorante):
        print(f"Agregando 1 cucharadita de {edulcorante} al poro...")

    def agregarHierbaMate(self):
        print("Agregando hierba mate hasta la mitad del poro...")

    def agregarHierbasAdicionales(self, hierba):
        print(f"Agregando {hierba} al poro...")

    def agregarAgua(self):
        print("Echando agua caliente al poro hasta llenarlo...")

    def prepararMate(self, edulcorante, hierbas):
        if not self.clean:
            self.lavarMate()
        self.agregarEdulcorante(edulcorante)
        self.agregarHierbaMate()
        for hierba in hierbas:
            self.agregarHierbasAdicionales(hierba)
        self.agregarEdulcorante(edulcorante)
        self.agregarAgua()

mate = PreparacionMate()
tipoMate = input("¿Qué tipo de mate quieres preparar? (manzanilla y cola de caballo / poleo y manzanilla / cedrón y manzanilla / poleo y cedrón): ").lower()

if tipoMate == "manzanilla y cola de caballo":
    hierbas = ["manzanilla", "cola de caballo"]
elif tipoMate == "poleo y manzanilla":
    hierbas = ["poleo", "manzanilla"]
elif tipoMate == "cedrón y manzanilla":
    hierbas = ["cedrón", "manzanilla"]
elif tipoMate == "poleo y cedrón":
    hierbas = ["poleo", "cedrón"]
else:
    print("Tipo de mate no válido.")
    exit()

edulcorante = input("¿Qué edulcorante quieres usar? ")

mate.prepararMate(edulcorante, hierbas)

print("El mate ya está listo.")