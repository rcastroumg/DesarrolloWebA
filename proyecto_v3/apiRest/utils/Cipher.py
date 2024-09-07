def vigenere_cipher(texto, key, mode='encrypt'):
    # Definir el alfabeto
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba0123456789$@!#%'

    # Asegurarse de que el mensaje y la clave estén en mayúsculas
    #texto = texto.upper()
    #key = key.upper()

    # Crear una cadena para almacenar el resultado
    result = ''

    # Inicializar un índice para recorrer la clave
    key_index = 0

    for letra in texto:
        if letra in alfabeto:
            if mode == 'encrypt':
                # Cifrar: suma el índice del carácter del mensaje con el índice del carácter de la clave
                encrypted_letra = alfabeto[(alfabeto.index(letra) + alfabeto.index(key[key_index])) % len(alfabeto)]
            else:
                # Descifrar: resta el índice del carácter de la clave del índice del carácter del mensaje
                decrypted_letra = alfabeto[(alfabeto.index(letra) - alfabeto.index(key[key_index])) % len(alfabeto)]

            # Agregar el carácter cifrado o descifrado al resultado
            if mode == 'encrypt':
                result += encrypted_letra
            else:
                result += decrypted_letra

            # Avanzar al siguiente carácter de la clave (cíclicamente)
            key_index = (key_index + 1) % len(key)
        else:
            # Si el carácter no está en el alfabeto, simplemente agrégalo al resultado sin cifrarlo/descifrarlo
            result += letra

    return result