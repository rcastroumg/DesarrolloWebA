from models.EmpresaModel import EmpresaModel
import utils.Cipher as Cipher

class UsuarioUtil:
    def validarPassword(pwd:str, idusuario:str):
        password = Cipher.vigenere_cipher(pwd,"analisisdesistemas","decrypt")
        empresa = EmpresaModel.ObtenerEmpresaUsuario(idusuario)[0]

        indice=0
        mayusculas=0
        minusculas=0
        numeros=0
        especiales=0
        longitud=0

        longitud = len(password)
        while indice < len(password):
            letra = password[indice]
            if letra.isupper() == True:
                mayusculas +=1
            elif letra.islower() == True:
                minusculas +=1
            elif letra.isnumeric() == True:
                numeros += 1
            else:
                especiales += 1
            
            indice += 1

        if (longitud >= empresa["PasswordLargo"] and 
            mayusculas >= empresa["PasswordCantidadMayusculas"] and
            minusculas >= empresa["PasswordCantidadMinusculas"] and
            numeros >= empresa["PasswordCantidadNumeros"] and
            especiales >= empresa["PasswordCantidadCaracteresEspeciales"]):
            return True
        else:
            return False