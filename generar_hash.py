from werkzeug.security import generate_password_hash, check_password_hash

contrasena = input("Escribe la contraseña que quieres proteger: ")
hash_generado = generate_password_hash(contrasena)

print("\ncopia este hash completo (sin espacios):")
print(hash_generado)

prueba_buena = check_password_hash(hash_generado, contrasena)
prueba_mala = check_password_hash(hash_generado, "otral123")
print("\n¿La contraseña correcta coincide?", prueba_buena)
print("¿Una contraseña falsa coincide?  ", prueba_mala)