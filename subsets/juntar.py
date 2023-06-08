def juntar_archivos(archivo1, archivo2, archivo_salida):
    with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2, open(archivo_salida, 'w') as salida:
        contenido1 = f1.read()
        contenido2 = f2.read()
        
        # Escribir contenido del archivo 1 en el archivo de salida
        salida.write(contenido1)
        
        # Escribir contenido del archivo 2 en el archivo de salida
        salida.write(contenido2)

# Ejemplo de uso
archivo1 = 'subsets\\Tokyo_JP_train.txt'
archivo2 = 'subsets\\Tokyo_JP_validation.txt'
archivo_salida = 'subsets\\Tokyo_JP_train_completo.txt'

juntar_archivos(archivo1, archivo2, archivo_salida)
