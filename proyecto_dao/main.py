from usuario import Usuario
from usuario_dao import UsuarioDAO

dao = UsuarioDAO()

# Agregar 3 usuarios iniciales
usuario1 = Usuario(None, "Ricardo Puc", "pava@gmail.com")
usuario2 = Usuario(None, "Yael Ake", "RataAke@gmail.com")
usuario3 = Usuario(None, "BetoArt", "BetoArt@gmail.com")

dao.agregar_usuario(usuario1)
dao.agregar_usuario(usuario2)
dao.agregar_usuario(usuario3)
print("Tres usuarios agregados.")

# Mostrar la lista de usuarios antes de modificaciones
print("\n🔍 Lista de usuarios antes de modificaciones:")
usuarios = dao.obtener_usuarios()
for usuario in usuarios:
    print(usuario)

# Buscar el usuario "BetoArt" y actualizarlo
usuario_beto = next((u for u in usuarios if u.nombre == "BetoArt"), None)
if usuario_beto:
    usuario_actualizado = Usuario(usuario_beto.id, "Carballo Carvajal", "UnyPolloGames@gmail.com")
    dao.actualizar_usuario(usuario_actualizado)
    print(f"\n Usuario 'BetoArt' actualizado a: {usuario_actualizado}")
else:
    print("\n No se encontró un usuario llamado 'BetoArt'.")

# Buscar y eliminar a Yael Ake si existe
usuario_yael = next((u for u in usuarios if u.nombre == "Yael Ake"), None)
if usuario_yael:
    dao.eliminar_usuario(usuario_yael.id)
    print(f"\n❌ Usuario eliminado: {usuario_yael.nombre}")
else:
    print("\n⚠️ No se encontró un usuario llamado 'Yael Ake'.")

# Mostrar la lista de usuarios después de las modificaciones
print("\n Lista final de usuarios:")
usuarios = dao.obtener_usuarios()
for usuario in usuarios:
    print(usuario)
