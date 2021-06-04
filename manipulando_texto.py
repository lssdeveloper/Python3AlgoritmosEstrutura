frase = 'Curso em Video Python'
# fatiamento
print(frase[:5])      # Curso
print(frase[9:14])    # Video
print(frase[9:21:2])  # VdoPto
print(frase[9::3])    # VePh
print(frase.count('o', 0, 14))  # 2
print(frase.find('deo')) # começa na posição 11
print('Curso' in frase) # True
print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
print(frase.capitalize())  # Curso em video android
print(frase.title()) # Curso Em Video Android
frase = '  Aprenda Python   '  # 19 caracters
print(len(frase))
print(len(frase.strip()))   # remove os espaços no ínicio e no fim  # 14 caracters
print(len(frase))           # 19 caracters
print(len(frase.rstrip()))  # remove os espaços da direita  # 16 caracters  r de right
print(len(frase.lstrip()))  # remove os espaços da esquerda  # 17 caracters  l de left
frase = 'Curso em Video Python'
print(frase.split())   # ['Curso', 'em', 'Video', 'Python']
print('-'.join(frase)) #C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n
print('-'.join(frase.split()))  # Curso-em-Video-Python