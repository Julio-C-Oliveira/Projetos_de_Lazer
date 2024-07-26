class Utilitarios {
    data class DoisInts(val primeiroValor: Byte, val segundoValor: Byte)
    public fun dividirStringEConverterParaInt(stringAlvo:String, divisorDeString: Char): DoisInts{
        val stringDividida = stringAlvo.split("$divisorDeString")
        val primeiraPosicao = stringDividida[0].toByteOrNull()
        val segundaPosicao = stringDividida[1].toByteOrNull()

        if (primeiraPosicao == null || segundaPosicao == null) {
            return DoisInts(-1, -1)
        } else {
            return DoisInts(primeiraPosicao, segundaPosicao)
        }
    }
}