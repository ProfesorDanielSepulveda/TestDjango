class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, servicio):
        id = str(servicio.idServicio)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "idServicio": servicio.idServicio,
                "nombre": servicio.nombreServicio,
                "acumulado": servicio.precioServicio,
                "cantidad":1,        
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += servicio.precioServicio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self,servicio):
        id = str(servicio.idServicio)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, servicio):
        id = str(servicio.idServicio)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -=1
            self.carrito[id]["acumulado"] -= servicio.precioServicio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(servicio)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True