import os
from PIL import Image, ImageOps

# Tamanho final
TAMANHO = (400, 400)

# Pasta atual
pasta = os.path.dirname(os.path.abspath(__file__))

# Extensões válidas
extensoes = ('.png', '.jpg', '.jpeg')

for arquivo in os.listdir(pasta):
    if arquivo.lower().endswith(extensoes):
        caminho = os.path.join(pasta, arquivo)

        try:
            with Image.open(caminho) as img:
                # Converte para RGB (necessário para JPG)
                img = img.convert("RGB")

                # Resize + crop central (sem deformar)
                img_final = ImageOps.fit(
                    img,
                    TAMANHO,
                    Image.Resampling.LANCZOS,
                    centering=(0.5, 0.5)
                )

                # Novo nome sempre em JPG
                nome_base = os.path.splitext(arquivo)[0]
                novo_caminho = os.path.join(pasta, f"{nome_base}.jpg")

                # Salva com compressão
                img_final.save(
                    novo_caminho,
                    format="JPEG",
                    quality=80,
                    optimize=True
                )

                # Remove original se não for JPG ou se quiser substituir
                if caminho != novo_caminho:
                    os.remove(caminho)

                print(f"Convertido: {arquivo} -> {nome_base}.jpg")

        except Exception as e:
            print(f"Erro em {arquivo}: {e}")

print("Finalizado!")