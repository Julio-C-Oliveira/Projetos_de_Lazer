// fun utilizado para criar uma função
public fun primeiraInteracao() {
    println("Com quebra de linha") // imprime na tela com quebra de linha
    print("Hello World") // imprime na tela sem quebra de linha
}

public fun segundaInteracao() {
    val nascimento: String = "14/05/2003" // váriaveis criadas com val são imutaveis.
    var idade: Int = 21 // váriaveis criadas com var são mutáveis.
    var teste: String
    teste = "12K"
    println()
    println(nascimento + "\n" + idade)
    println(teste)
}

// Tipos de váriaveis
public fun terceiraInteracao() {
    val myNum: Int = 5                // Int
    val myDoubleNum: Double = 5.99    // Double
    val myLetter: Char = 'D'          // Char
    val myBoolean: Boolean = true     // Boolean
    val myText: String = "Hello"      // String

    /*
    Existem mais tipos de Int e de Floats:
    Ints:
    - Byte: -128 até 127
    - Short: -32768 até 32767
    - Int: -2147483648 até 2147483647
    - Long: -9223372036854775807 até 9223372036854775807

    Floats:
    - Float: até 6 dígitos após o ponto flutuante.
    - Double: até 15 dígitos após o ponto flutuante.

    Conversores:
    - toByte()
    - toShort()
    - toInt()
    - toLong()
    - toFloat()
    - toDouble()
    - toChar()
    */
    println(myNum)
}

fun quartaInteracao() {
    /*
    Operadores Aritimeticos:
        + somar
        - subtrair
        * multiplicar
        / dividir
        % resto
        ++ incrementar
        -- decrementar

    Operadores de Assimilação:
        = recebe/assimilar
        += somar algum valor com o valor da váriavel
        -= subtrair algum valor com o valor da váriavel
        *= multiplicar algum valor com o valor da váriavel
        /= dividir algum valor com o valor da váriavel
        %= tirar o resto de um valor com o valor da váriavel

    Operadores de Comparação:
        == igualdade
        != diferente
        > maior que
        < menor que
        >= maior ou igual
        <= menor ou igual

    Operadores Lógicos:
        && operador and/e
        || operador or/ou
        ! operador not/não
    */
}

fun quintaInteracao() {
    var algo = "Byakugan"
    var nanika: String = "Setsugen no Ao"

    println(algo[0])
    println(nanika[1])
    println(nanika)
    println("O tamamho dessa string é de " + nanika.length + " caracteres.")
    println(nanika.uppercase())
    println(nanika.lowercase())
    println(algo.compareTo(nanika)) // comparando duas strings se retornar 0 elas são iguais
    println(nanika.indexOf("Ao"))
    println(nanika.plus(algo))
    println("Watashi no namae is $nanika now you conhecerá a dor $algo")
}

fun sextaInteracao() {
    var valor = 2
    if (2 > valor) {
        println("$valor é menor a 2")
    } else if (2 == valor) {
        println("$valor é igual a 2")
    } else {
        println("$valor não é menor ou igual a 2")
    }

    val zaWarudo = if (valor > 2) {
        "Star Platinum"
    } else {
        "Za Warudo"
    }

    val starPlatinum = if (valor < 2) "BANKAI" else "HINOKAMI KAGURA"
}

fun setimaInteracao() {
    val dia = 0

    val result = when (dia) {
        1 -> "Domingo"
        2 -> "Segunda"
        3 -> "Terça"
        4 -> "Quarta"
        5 -> "Quinta"
        6 -> "Sexta"
        7 -> "Sábado"
        else -> "Inválido meu nobre"
    }

    println(result)

    var c:Int = 8
    while (c > 5) {
        println(c)
        c--
        if (c%2 == 0) {
            println("C: $c o resto de 2 é igual ${c%2}")
            break
        }
    }
    do {
        if (c%2 == 0) {
            c--
            continue
        }
        println(c)
        c--
    }
    while (c > 2)
}

fun oitavaInteracao () {
    val animes = arrayOf("Shimoneta", "Konosuba", "Grand Blue", "Chainsaw Man")
    println("A divindade ${animes[0]} deve ser apreciada")
    animes[2] = "Bleach"
    println(animes[2])
    println(animes.size)

    if ("Shimoneta" in animes) {
        println("Você é um ser iluminado")
    } else {
        println("Blasfêmia mero mortal")
    }

    for (anime in animes) {
        println(anime)
    }
}

fun nonaInteracao() {
    for (num in 1..15) {
        println(num)
    }
    for (letra:Char in 'a'..'z') {
        println(letra)
    }
}

fun decimaInteracao() {
    fun funcao01(x: Int): Int{
        return (x+3)
    }
    println(funcao01(3))

    fun funcao02(x: Int, y: Int) = x + y
    println(funcao02(3,3))
}

class Autobot{
    var brand = ""
    var model = ""
    var year = 0
}

class Autobot2(var brand: String, var model: String, var year: Int)

fun createAutobot(brand: String, model: String, year: Int): Autobot{
    val autobot = Autobot()
    autobot.brand = brand
    autobot.model = model
    autobot.year = year

    return autobot
}

fun createAutobot2(brand: String, model: String, year: Int): Autobot2{
    return (Autobot2(brand, model, year))
}

fun main() {
    //primeiraInteracao()
    //segundaInteracao()
    //terceiraInteracao()
    //quartaInteracao()
    //quintaInteracao()
    //sextaInteracao()
    //setimaInteracao()
    //oitavaInteracao()
    //nonaInteracao()
    //decimaInteracao()
}