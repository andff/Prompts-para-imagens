import os
from PIL import Image, ImageOps

# Tamanho final
TAMANHO = (300, 300)

# Pasta atual
pasta = os.path.dirname(os.path.abspath(__file__))

# Extensões válidas
extensoes = ('.png', '.jpg', '.jpeg')

for arquivo in os.listdir(pasta):
    if arquivo.lower().endswith(extensoes):
        caminho = os.path.join(pasta, arquivo)

        try:
            with Image.open(caminho) as img:
                # Converte para RGB (evita erro com JPG)
                img = img.convert("RGB")

                # Faz resize + crop central automaticamente
                img_final = ImageOps.fit(
                    img,
                    TAMANHO,
                    Image.Resampling.LANCZOS,  # alta qualidade
                    centering=(0.5, 0.5)      # crop central
                )

                # Salva sobrescrevendo
                img_final.save(caminho, quality=95)

                print(f"OK: {arquivo}")

        except Exception as e:
            print(f"Erro em {arquivo}: {e}")

print("Finalizado!")