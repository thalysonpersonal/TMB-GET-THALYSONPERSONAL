function calcular() {
    var peso = parseFloat(document.getElementById('peso').value);
    var altura = parseFloat(document.getElementById('altura').value) / 100; // Convertendo altura para metros
    var idade = parseInt(document.getElementById('idade').value);
    var sexo = document.getElementById('sexo').value;
    var atividade = document.getElementById('atividade').value;
    var metabolismo_basal;

    if (sexo === 'masculino') {
        metabolismo_basal = 66 + (13.75 * peso) + (5 * altura * 100) - (6.75 * idade);
    } else {
        metabolismo_basal = 655 + (9.56 * peso) + (1.85 * altura * 100) - (4.68 * idade);
    }

    var gasto_energetico_total;

    switch (atividade) {
        case 'sedentario':
            gasto_energetico_total = metabolismo_basal * 1.2;
            break;
        case 'leve':
            gasto_energetico_total = metabolismo_basal * 1.375;
            break;
        case 'moderado':
            gasto_energetico_total = metabolismo_basal * 1.55;
            break;
        case 'ativo':
            gasto_energetico_total = metabolismo_basal * 1.725;
            break;
        case 'muito ativo':
            gasto_energetico_total = metabolismo_basal * 1.9;
            break;
        default:
            gasto_energetico_total = "Nível de atividade inválido";
    }

    document.getElementById('resultado').innerHTML = "Metabolismo Basal: " + metabolismo_basal.toFixed(2) + " kcal/dia<br>Gasto Energético Total: " + gasto_energetico_total.toFixed(2) + " kcal/dia";
}