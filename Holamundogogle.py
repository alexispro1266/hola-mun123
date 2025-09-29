import webbrowser
import os

# Crea el archivo HTML con "Hola mundo"
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Hola Mundo</title>
</head>
<body>
    <h1>Hola tia jannet</h1>
</body>
</html>
"""

# Guarda el archivo
file_path = "hola_mundo.html"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Abre el archivo en el navegador
webbrowser.open(f"file://{os.path.abspath(file_path)}")
