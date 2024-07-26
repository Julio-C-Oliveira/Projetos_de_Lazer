/*
val utils = Utilitarios()

val divisorDeString: Char = ','

print("Por quanto tempo você planeja investir?\nInsira o tempo no formato ANOS${divisorDeString}MESES: ")
//val tempoInvestindo = readLine()
val tempoInvestindo = readlnOrNull()
if (tempoInvestindo != null) {
    val tempoInvestidoDividido = utils.dividirStringEConverterParaInt(tempoInvestindo, divisorDeString)
    val tempoEmAnos: Byte = tempoInvestidoDividido.primeiroValor
    val tempoEmMeses: Byte = tempoInvestidoDividido.segundoValor
    if (tempoEmAnos >= 0) {
        println("Tempo inserido, $tempoEmAnos anos e $tempoEmMeses meses.")

    } else {
        println("O valor inserido é  inválido, verifique se você inseriu um número maior ou igual a zero e se não adicionou um espaço antes ou depois da vírgula.")
    }

} else {
    println("O valor inserido é inválido.")
}
*/

fun main(){
    val investimento = Calcular_Investimentos(
        5,
        0,
        (0.12F/12) + 1,
        3000.0,
        1000.0F,
        100000.0,
        0.65F/10/12
    )

    val resultado_investimetos: Calcular_Investimentos.Investimentos = investimento.calcular_investimento()

    println("\nMontante Inicial: ${String.format("%.2f", investimento.get_MontanteInicial())}R$\n")
    println("Estrátegia de Aporte + Rentabilidade:")
    println("   Montante Final: ${String.format("%.2f", resultado_investimetos.resultadoInvestindoComAporteERentabilidade)}R$")
    println("   Decaimento pela Inflacao: ${String.format("%.2f", resultado_investimetos.decaimentoIcAR)}R$")
    println("   Rentabilidade Mensal Gerada: ${String.format("%.2f", resultado_investimetos.rentabilidadeIcAR)}R$\n")

    println("Estrátegia de somente Aporte:")
    println("   Montante Final, Aporte: ${String.format("%.2f", resultado_investimetos.resultadoInvestindoComAporte)}R$")
    println("   Decaimento pela Inflacao: ${String.format("%.2f", resultado_investimetos.decaimentoIcA)}R$")
    println("   Rentabilidade Mensal Gerada: ${String.format("%.2f", resultado_investimetos.rentabilidadeIcA)}R$\n")

    println("Estrátegia de somente Rentabilidade:")
    println("   Montante Final, Rentabilidade: ${String.format("%.2f", resultado_investimetos.resultadoPoupancaComRentabilidade)}R$")
    println("   Decaimento pela Inflacao: ${String.format("%.2f", resultado_investimetos.decaimentoPcR)}R$")
    println("   Rentabilidade Mensal Gerada: ${String.format("%.2f", resultado_investimetos.rentabilidadePcR)}R$\n")

    val tempo_para_objetivo: Calcular_Investimentos.TempoParaObjetivo = investimento.tempoParaObjetivo()

    println("Estrátegia de Aporte + Rentabilidade: ${tempo_para_objetivo.estrategiaIcAR}")
    println("Estrátegia de somente Aporte: ${tempo_para_objetivo.estrategiaIcA}")
}