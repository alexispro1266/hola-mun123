import webbrowser
import os

# Contenido HTML con CSS y JavaScript
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Hola Mundo Interactivo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            text-align: center;
            margin-top: 100px;
        }
        h1 {
            color: #333;
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        p {
            font-size: 20px;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>¡Bienvenido!</h1>
    <p>Haz clic en el botón para ver un mensaje</p>
    <button onclick="mostrarMensaje()">Mostrar mensaje</button>
    <p id="mensaje"></p>

    <script>
        function mostrarMensaje() {
            document.getElementById("mensaje").innerText = "¡Hola mundo desde HTML, CSS y JavaScript!";
        }
    </script>
</body>
</html>
"""

# Guardar el archivo HTML
file_path = "pagina_interactiva.html"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Abrir en navegador predeterminado
webbrowser.open(f"file://{os.path.abspath(file_path)}")
