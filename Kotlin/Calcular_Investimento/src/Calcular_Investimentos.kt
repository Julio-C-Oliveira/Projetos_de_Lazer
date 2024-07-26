import kotlin.math.pow

class Calcular_Investimentos(
    private var tempoEmAnos: Byte = 3,
    private var tempoEmMeses: Byte = 11,
    private var rentabilidadeMensal: Float = (0.12F/12) + 1,
    private var montanteInicial: Double = 10.0,
    private var aporteMensal: Float = 3000.0F,
    private var objetivo: Double = 300000.0,
    private var inflacaoMensal: Float = 0.65F/10/12
) {
    // Get Functions:
    public fun get_TempoEmAnos() = this.tempoEmAnos
    public fun get_TempoEmMeses() = this.tempoEmMeses
    public fun get_TempoTotalEmMeses() = this.tempoTotalEmMeses
    public fun get_RentabilidadeMensal() = this.rentabilidadeMensal
    public fun get_MontanteInicial() = this.montanteInicial
    public fun get_AporteMensal() = this.aporteMensal
    public fun get_Objetivo() = this.objetivo
    public fun get_InflacaoMensal() = this.inflacaoMensal

    // Set Functions:
    public fun set_TempoEmAnos(anos: Byte){
        this.tempoEmAnos = anos
    }
    public fun set_TempoEmMeses(meses: Byte){
        this.tempoEmMeses = meses
    }
    public fun set_TempoTotalEmMeses(meses: Int){
        this.tempoTotalEmMeses = meses
    }
    public fun set_RentabilidadeMensal(rentabilidadeAnual: Float){
        this.rentabilidadeMensal = rentabilidadeAnual/12
    }
    public fun set_MontanteInicial(montante: Double){
        this.montanteInicial = montante
    }
    public fun set_AporteMensal(aporte: Float){
        this.aporteMensal = aporte
    }
    public fun set_Objetivo(montanteAlvo: Double){
        this.objetivo = montanteAlvo
    }
    public fun set_InflacaoMensal(inflacaoDecenal: Float){
        this.inflacaoMensal = inflacaoDecenal/10/12
    }

    // Váriaveis:
    var tempoTotalEmMeses: Int = ((get_TempoEmAnos() * 12) + get_TempoEmMeses())

    // Utils Functions
    public fun investindoComAporteERentabilidade(): Double{
        var montante:Double = get_MontanteInicial()
        var tempoTotalEmMeses = get_TempoTotalEmMeses()

        while (tempoTotalEmMeses > 0) {
            montante = montante * get_RentabilidadeMensal() + get_AporteMensal()
            tempoTotalEmMeses--
        }
        return montante
    }
    public fun investindoComAporte() = get_MontanteInicial() + get_AporteMensal() * get_TempoTotalEmMeses()
    public fun poupancaComRentabilidade() = get_MontanteInicial() * get_RentabilidadeMensal().pow(get_TempoTotalEmMeses())

    public  fun rentabilidadeMensalGerada(montante: Double) = montante * (get_RentabilidadeMensal()-1)

    public fun decaimentoPelaInflacao(montante: Double) = montante*((1-get_InflacaoMensal()).pow(get_TempoTotalEmMeses()))

    data class Investimentos(val resultadoInvestindoComAporteERentabilidade: Double,
        val resultadoInvestindoComAporte: Double,
        val resultadoPoupancaComRentabilidade: Double,
        val rentabilidadeIcAR: Double,
        val rentabilidadeIcA: Double,
        val rentabilidadePcR: Double,
        val decaimentoIcAR: Double,
        val decaimentoIcA: Double,
        val decaimentoPcR: Double
        )

    public fun calcular_investimento(): Investimentos{
        val montanteIcAR: Double = investindoComAporteERentabilidade()
        val montanteIcA: Double = investindoComAporte()
        val montantePcR: Double = poupancaComRentabilidade()
        val rentabilidadeIcAR: Double = rentabilidadeMensalGerada(montanteIcAR)
        val rentabilidadeIcA: Double =  rentabilidadeMensalGerada(montanteIcA)
        val rentabilidadePcR: Double = rentabilidadeMensalGerada(montantePcR)
        val decaimentoIcAR: Double = decaimentoPelaInflacao(montanteIcAR)
        val decaimentoIcA: Double = decaimentoPelaInflacao(montanteIcA)
        val decaimentoPcR: Double = decaimentoPelaInflacao(montantePcR)

        return Investimentos(
            montanteIcAR,
            montanteIcA,
            montantePcR,
            rentabilidadeIcAR,
            rentabilidadeIcA,
            rentabilidadePcR,
            decaimentoIcAR,
            decaimentoIcA,
            decaimentoPcR
        )
    }

    data class Tempo(val anos: Int, val meses: Int)
    data class TempoParaObjetivo(val estrategiaIcAR: Tempo, val estrategiaIcA: Tempo)
    public fun objetivoIcAR(): Tempo{
        var tempo: Int = 0
        var montante: Double = 0.0
        while (montante < get_Objetivo()){
            montante = montante * get_RentabilidadeMensal() + get_AporteMensal()
            tempo++
        }
        return Tempo(tempo/12, tempo%12)
    }
    public fun objetivoIcA(): Tempo{
        var tempo: Int = 0
        var montante: Double = 0.0
        while (montante < get_Objetivo()){
            montante += get_AporteMensal()
            tempo++
        }
        return Tempo(tempo/12, tempo%12)
    }
    public fun tempoParaObjetivo(): TempoParaObjetivo{
        val tempoParaObjetivoIcAR = objetivoIcAR()
        val tempoParaObjetivoIcA = objetivoIcA()

        return TempoParaObjetivo(tempoParaObjetivoIcAR, tempoParaObjetivoIcA)
    }
}