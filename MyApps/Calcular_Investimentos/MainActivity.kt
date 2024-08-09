package com.example.calcular_investimento

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import com.example.calcular_investimento.ui.theme.Calcular_InvestimentoTheme
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.GridItemSpan
import androidx.compose.material3.TextField
import androidx.compose.ui.Alignment
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import java.util.Locale
import androidx.compose.ui.unit.dp


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        val investimento = Calcular_Investimentos(
            0,
            0,
            (0.12F/12) + 1,
            0.0,
            0.0F,
            0.0,
            0.65F/10/12
        )

        setContent {
            Calcular_InvestimentoTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    App(
                        investimento = investimento,
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

@Composable
//fun App(modifier: Modifier){
fun App(investimento: Calcular_Investimentos, modifier: Modifier){
    // Entrada
    var tempoEmAnos by remember {
        mutableStateOf("0")
    }
    var tempoEmMeses by remember {
        mutableStateOf("0")
    }
    var rentabilidadeMensal by remember {
        mutableStateOf("0.12")
    }
    var montanteInicial by remember {
        mutableStateOf("0.0")
    }
    var aporteMensal by remember {
        mutableStateOf("0.0")
    }
    var objetivoFinal by remember {
        mutableStateOf("0.0")
    }
    var inflacaoDecenal by remember {
        mutableStateOf("0.65")
    }

    Column(modifier = Modifier
        .fillMaxSize()
        .padding(16.dp), horizontalAlignment = Alignment.CenterHorizontally) {
        LazyVerticalGrid(columns = GridCells.Fixed(2)) {
            item{
                TextField(
                    value = tempoEmAnos,
                    onValueChange = {tempoEmAnos = it},
                    label = {
                        Text(text = "Tempo em Anos")
                    })
            }
            item {
                TextField(
                    value = tempoEmMeses,
                    onValueChange = {tempoEmMeses = it},
                    label = {
                        Text(text = "Tempo em Meses")
                    })
            }
            item {
                TextField(
                    value = montanteInicial,
                    onValueChange = {montanteInicial = it},
                    label = {
                        Text(text = "Montante Inicial")
                    })
            }
            item {
                TextField(
                    value = aporteMensal,
                    onValueChange = {aporteMensal = it},
                    label = {
                        Text(text = "Aporte Mensal")
                    })
            }
            item {
                TextField(
                    value = rentabilidadeMensal,
                    onValueChange = {rentabilidadeMensal = it},
                    label = {
                        Text(text = "Rentabilidade Anual")
                    })
            }
            item {
                TextField(
                    value = inflacaoDecenal,
                    onValueChange = {inflacaoDecenal = it},
                    label = {
                        Text(text = "Inflação Decenal")
                    })
            }
            item(span = { GridItemSpan(2) }) {
                TextField(
                    value = objetivoFinal,
                    onValueChange = {objetivoFinal = it},
                    label = {
                        Text(text = "Objetivo")
                    })
            }
        }

        // Lógica
        investimento.set_TempoEmAnos(if (tempoEmAnos.toByteOrNull() != null) tempoEmAnos.toByte() else 0)
        investimento.set_TempoEmMeses(if (tempoEmMeses.toByteOrNull() != null) tempoEmMeses.toByte() else 0)
        investimento.set_RentabilidadeMensal(if (rentabilidadeMensal.toFloatOrNull() != null) rentabilidadeMensal.toFloat() else 0.12F)
        investimento.set_MontanteInicial(if (montanteInicial.toDoubleOrNull() != null) montanteInicial.toDouble() else 0.0)
        investimento.set_AporteMensal(if (aporteMensal.toFloatOrNull() != null) aporteMensal.toFloat() else 0.0F)
        investimento.set_Objetivo(if (objetivoFinal.toDoubleOrNull() != null) objetivoFinal.toDouble() else 0.0)
        investimento.set_InflacaoMensal(if (inflacaoDecenal.toFloatOrNull() != null) inflacaoDecenal.toFloat() else 0.65F)

        println("### Iniciando Cálculos de Rentabilidade")
        val resultadoInvestimentos: Calcular_Investimentos.Investimentos = investimento.calcular_investimento()
        println("### Cálculos de Rentabilidade Finalizados ###")
        println("### Iniciando Cálculos de Tempo para o Objetivo")
        val tempoParaObjetivo: Calcular_Investimentos.TempoParaObjetivo = investimento.tempoParaObjetivo()
        println("### Cálculos de Tempo para o Objetivo finalizados ###")

        // Saída
        Spacer(modifier = Modifier.height(32.dp))
        Text(text = "Estrátegia de Aporte + Rentabilidade:")
        Text(text = "Montante Final: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.resultadoInvestindoComAporteERentabilidade)}R$")
        Text(text = "Decaimento pela Inflacao: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.decaimentoIcAR)}R$")
        Text(text = "Rentabilidade Mensal Gerada: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.rentabilidadeIcAR)}R$")
        Spacer(modifier = Modifier.height(32.dp))
        Text(text = "Estrátegia de somente Aporte:")
        Text(text = "Montante Final: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.resultadoInvestindoComAporte)}R$")
        Text(text = "Decaimento pela Inflacao: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.decaimentoIcA)}R$")
        Text(text = "Rentabilidade Mensal Gerada: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.rentabilidadeIcA)}R\$")
        Spacer(modifier = Modifier.height(32.dp))
        Text(text = "Estrátegia de somente Rentabilidade:")
        Text(text = "Montante Final: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.resultadoPoupancaComRentabilidade)}R$")
        Text(text = "Decaimento pela Inflacao: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.decaimentoPcR)}R$")
        Text(text = "Rentabilidade Mensal Gerada: ${String.format(Locale.getDefault(), "%.2f", resultadoInvestimentos.rentabilidadePcR)}R$")
        Spacer(modifier = Modifier.height(32.dp))
        Text(text = "Estrátegia de Aporte + Rentabilidade:")
        Text(text = "${tempoParaObjetivo.estrategiaIcAR.anos} anos e ${tempoParaObjetivo.estrategiaIcAR.meses} meses.")
        Text(text = "Estrátegia de somente Aporte:")
        Text(text = "${tempoParaObjetivo.estrategiaIcA.anos} anos e ${tempoParaObjetivo.estrategiaIcA.meses} meses.")
        Spacer(modifier = Modifier.height(32.dp))
    }
}