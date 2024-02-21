# Data de Criação: xx/xx/2023 - Meio do curso.
# Alguns Cálculos de Renda Fixa, não é muito útil para renda váriavel.

import Calcular_Investimento as CI

TEMPOEMANOS = 30
TEMPOEMMESES = 0
RENTABILIDADEANUAL = 0.12
MONTANTEINICIAL = 0
APORTEMENSAL = 245
OBJETIVO = 6200
INFLACAODECENAL = 0.65 # Uso 65% pensando em um caso provavel, 95% em um caso ruim e 45% pensando em um bom.
INFLACAOANUAL = INFLACAODECENAL/10

Calcular_Investimento = CI.Calcular_Investimento(TEMPOEMANOS, TEMPOEMMESES, RENTABILIDADEANUAL, MONTANTEINICIAL)

investindoEReinvestindo = Calcular_Investimento.investir_reinvestir(APORTEMENSAL)
investindoSemReinvestir = Calcular_Investimento.investir_sem_reinvestir(APORTEMENSAL)
investindo = Calcular_Investimento.investir_sem_aporte_mensal()
tempoParaOObjetivoIR = Calcular_Investimento.objetivo_reinvestindo(OBJETIVO, APORTEMENSAL)
tempoParaOObjetivoI = Calcular_Investimento.objetivo_investindo(OBJETIVO, APORTEMENSAL)
objetivoMesesIR = tempoParaOObjetivoIR%12
objetivoAnosIR = int((tempoParaOObjetivoIR - objetivoMesesIR) / 12)
objetivoMesesI = tempoParaOObjetivoI%12
objetivoAnosI = int((tempoParaOObjetivoI - objetivoMesesI) / 12)

rendaPassivaInvestindoEReinvestindo = Calcular_Investimento.renda_passiva_gerada(investindoEReinvestindo)
rendaPassivaInvestindoSemReinvestir = Calcular_Investimento.renda_passiva_gerada(investindoSemReinvestir)
rendaPassivaInvestindo = Calcular_Investimento.renda_passiva_gerada(investindo)

print("Os valores são aproximações dos valores reais, os valores podem ser maiores ou menores que os resultados reais.")

print("\n")

print(f"Investindo e reinvestindo: {investindoEReinvestindo:.2f}")
print(f"Incidindo a inflação: {Calcular_Investimento.incidir_inflacao(investindoEReinvestindo ,INFLACAOANUAL):.2f}")
print(f"Renda passiva mensal gerada: {rendaPassivaInvestindoEReinvestindo:.2f}")
print(f"Incidindo a inflação: {Calcular_Investimento.incidir_inflacao(rendaPassivaInvestindoEReinvestindo ,INFLACAOANUAL):.2f}")
Calcular_Investimento.decaimento_em_50_anos(rendaPassivaInvestindoEReinvestindo, INFLACAOANUAL)

print("\n")

print(f"Investindo sem reinvestir: {investindoSemReinvestir:.2f}")
print(f"Incidindo a inflação: {Calcular_Investimento.incidir_inflacao(investindoSemReinvestir ,INFLACAOANUAL):.2f}")
print(f"Renda passiva mensal gerada: {rendaPassivaInvestindoSemReinvestir:.2f}")
print(f"Incidindo a inflação: {Calcular_Investimento.incidir_inflacao(rendaPassivaInvestindoSemReinvestir ,INFLACAOANUAL):.2f}")
Calcular_Investimento.decaimento_em_50_anos(rendaPassivaInvestindoSemReinvestir, INFLACAOANUAL)

print("\n")

print(f"Investindo sem aporte mensal: {investindo:.2f}")
print(f"Incidindo a inflação: {Calcular_Investimento.incidir_inflacao(investindo ,INFLACAOANUAL):.2f}")
print(f"Renda passiva mensal gerada: {rendaPassivaInvestindo:.2f}")
print(f"Incidindo a inflação: {Calcular_Investimento.incidir_inflacao(rendaPassivaInvestindo ,INFLACAOANUAL):.2f}")
Calcular_Investimento.decaimento_em_50_anos(rendaPassivaInvestindo, INFLACAOANUAL)

print("\n")

print(f"Tempo para alcançar o objetivo investindo e reinvestindo: {objetivoAnosIR} Anos e {objetivoMesesIR} Meses")
print(f"Tempo para alcançar o objetivo investindo: {objetivoAnosI} Anos e {objetivoMesesI} Meses")