class Cifra_de_Cesar(
    private var frase_primaria: String = "Voce ja procurou hotel na internet hoje",
    private var frase_secundaria: String = "SOX"
) {
    public fun get_FrasePrimaria() = this.frase_primaria
    public fun get_FraseSecundaria() = this.frase_secundaria

    public fun set_FrasePrimaria(frase: String){
        this.frase_primaria = frase
    }
    public fun set_FraseSecundaria(frase: String){
        this.frase_secundaria = frase
    }

    public fun criarMarcacao(){

    }

    // Colocar uma restrição por fora dessa função para garantir a chegada de um char.
    public fun cifrar_ou_descifrar(choice: Char){

    }
}