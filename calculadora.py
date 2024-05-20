<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora TMB e GET</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="header">
        <h1>@thalysonpersonal</h1>
        <h2>CALCULADORA TMB E GET</h2>
    </div>
    
    <div class="calculator">
        <div class="form-group">
            <label for="peso">Peso (kg):</label>
            <input type="number" id="peso" name="peso" required>
        </div>
        <div class="form-group">
            <label for="altura">Altura (cm):</label>
            <input type="number" id="altura" name="altura" required>
        </div>
        <div class="form-group">
            <label for="idade">Idade:</label>
            <input type="number" id="idade" name="idade" required>
        </div>
        <div class="form-group">
            <label for="sexo">Sexo:</label>
            <select id="sexo" name="sexo" required>
                <option value="masculino">Masculino</option>
                <option value="feminino">Feminino</option>
            </select>
        </div>
        <div class="form-group">
            <label for="atividade">Nível de atividade:</label>
            <select id="atividade" name="atividade" required>
                <option value="sedentario">Sedentário</option>
                <option value="leve">Leve</option>
                <option value="moderado">Moderado</option>
                <option value="ativo">Ativo</option>
                <option value="muito ativo">Muito Ativo</option>
            </select>
        </div>
        <button onclick="calcular()">Calcular</button>
        <div id="resultado"></div>
    </div>

    <div class="footer">
        <p>@thalysonpersonal</p>
    </div>

    <script>
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
    </script>
</body>
</html>