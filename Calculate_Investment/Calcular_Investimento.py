class Calcular_Investimento:
  def __init__(self, tempoEmAnos:int, tempoEmMeses, rentabilidadeAnual:float, montanteInicial:float):
    self.tempoEmAnos = tempoEmAnos
    self.tempoEmMeses = tempoEmMeses
    self.rentabilidadeAnual = rentabilidadeAnual
    self.rentabilidadeMensal = 1 + (rentabilidadeAnual / 12)
    self.montanteInicial = montanteInicial

  def investir_reinvestir(self, aporteMensal:float) -> float:
    montante = self.montanteInicial
    tempo = self.tempoEmAnos*12+self.tempoEmMeses
    for mes in range(tempo):
      montante = montante * self.rentabilidadeMensal + aporteMensal

    return montante

  def investir_sem_reinvestir(self, aporteMensal:float) -> float:
    tempo = self.tempoEmAnos*12+self.tempoEmMeses
    return self.montanteInicial + aporteMensal * (tempo)

  def investir_sem_aporte_mensal(self) -> float:
    tempo = self.tempoEmAnos*12+self.tempoEmMeses
    return self.montanteInicial * (self.rentabilidadeMensal)**(tempo)

  def incidir_inflacao(self, montante, taxaInflacionariaAnual):
    tempo = self.tempoEmAnos*12+self.tempoEmMeses
    return montante*(1-(taxaInflacionariaAnual/12))**(tempo)

  def renda_passiva_gerada(self, montante):
    return (self.rentabilidadeMensal - 1) * montante

  def decaimento_em_50_anos(self, montante, taxaInflacionariaAnual):
    tempo = self.tempoEmAnos*12+self.tempoEmMeses
    for i in range(5):
      tempo += 120
      print(f"Após {i+1}0 anos: {montante*(1-(taxaInflacionariaAnual/12))**tempo:.2f}")
    
  def objetivo_reinvestindo(self, objetivo, aporteMensal):
    montante = self.montanteInicial
    tempo = 0
    while montante < objetivo:
      montante = montante * self.rentabilidadeMensal + aporteMensal
      tempo += 1

    return tempo

  def objetivo_investindo(self, objetivo, aporteMensal):
    montante = self.montanteInicial
    tempo = 0
    while montante < objetivo:
      montante = montante + aporteMensal
      tempo += 1

    return tempo