<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Jogo de Bingo Profissional</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #f0f0f0; }
        .globo { display: inline-block; margin: 20px; }
        .globo canvas { background-color: #fff; border: 2px solid #000; border-radius: 50%; }
        .button { padding: 10px 20px; background-color: #28a745; color: #fff; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        .button:hover { background-color: #218838; }
    </style>
</head>
<body>
    <h1>Jogo de Bingo Profissional</h1>
    <div class="globos">
        <div id="globo1" class="globo">
            <canvas id="canvas1" width="200" height="200"></canvas>
            <button class="button" onclick="sortear(1)">Sortear Globo 1</button>
        </div>
        <div id="globo2" class="globo">
            <canvas id="canvas2" width="200" height="200"></canvas>
            <button class="button" onclick="sortear(2)">Sortear Globo 2</button>
        </div>
        <div id="globo3" class="globo">
            <canvas id="canvas3" width="200" height="200"></canvas>
            <button class="button" onclick="sortear(3)">Sortear Globo 3</button>
        </div>
        <div id="globo4" class="globo">
            <canvas id="canvas4" width="200" height="200"></canvas>
            <button class="button" onclick="sortear(4)">Sortear Globo 4</button>
        </div>
    </div>
    <script src="bingo.js"></script>
</body>
</html>
