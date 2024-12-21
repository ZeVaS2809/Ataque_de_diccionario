# Diccionario de contraseñas
passwords = [
    "MariaPaula1999", "MPaula1999", "Soto1999", "Jimenez1999", "MariaPaula25Junio",
    "Doky1999", "SanAntonio99", "25Junio1999", "MPaula25/06", "DokySan99",
    "SotoJimenez25", "MariaDoky99", "June25Doky", "SanBelén1999", "25Jun1999",
    "MariaPaula_1999", "M!Paula1999", "D0ky_25Jun", "25_Jun!1999", "San!Antonio99",
    "D@kyBelén99", "Paula$25Jun", "MariaPaulaSoto1999", "M.P.Soto99!", 
    "25Junio_SanAntonio99", "Doky_SotoJimenez1999", "M@r1aP@ula_25Jun!Doky1999_SotoJ1menez"
]

# Contraseña objetivo
target_password = "M@r1aP@ula_25Jun!Doky1999_SotoJ1menez"

# Función para probar el diccionario
def test_passwords(dictionary, target):
    print("Probando contraseñas del diccionario...")
    for password in dictionary:
        print(f"Probando: {password}")
        if password == target:
            print(f"¡Contraseña encontrada! La contraseña es: {password}")
            return True
    print("No se encontró la contraseña en el diccionario.")
    return False

# Llamada a la función
if __name__ == "__main__":
    found = test_passwords(passwords, target_password)
    if not found:
        print("Considera actualizar o expandir el diccionario.")
