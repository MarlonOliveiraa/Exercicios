class Imovel:
    def __init__(self,inscriçaoMunicipal,Valor_aluguel,IPTU):
        self.inscricaoMunicipal = inscriçaoMunicipal
        self.Valor_aluguel = Valor_aluguel
        self.IPTU = IPTU

    def obter_parcela_IPTU(self):
        return self.IPTU
    
    def set_valor_aluguel(self):
        return self.Valor_aluguel
    
class Casa(Imovel):
    def __init__(self, inscriçaoMunicipal, Valor_aluguel, IPTU,piscina,sala_de_estar,quartos):
        super().__init__(inscriçaoMunicipal, Valor_aluguel, IPTU)
        self.piscina = piscina
        self.sala_de_estar = sala_de_estar
        self.quartos = quartos

class Condominio(Imovel):
    def __init__(self, inscriçaoMunicipal, Valor_aluguel, IPTU,area_de_lazer,aluguel_condominio):
        super().__init__(inscriçaoMunicipal, Valor_aluguel, IPTU)
        self.area_de_lazer = area_de_lazer
        self.aluguel_condominio = aluguel_condominio

class Apartamento(Imovel):
    def __init__(self, inscriçaoMunicipal,Valor_aluguel, IPTU,elevador,andar,):
        super().__init__(inscriçaoMunicipal, Valor_aluguel, IPTU)
        self.elevador = elevador
        self.andar = andar

class Terreno(Imovel):
    def __init__(self, inscriçaoMunicipal, Valor_aluguel, IPTU,area_m2):
        super().__init__(inscriçaoMunicipal, Valor_aluguel, IPTU)
        self.area_m2 = area_m2

class Chacara(Imovel)
      

        