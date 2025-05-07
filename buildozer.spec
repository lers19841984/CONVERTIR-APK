[app]

# Nombre de tu aplicación
title = MiAppKivy

# Nombre del paquete (debe ser único)
package.name = miappkivy

# Nombre del dominio (usar tu dominio inverso)
package.domain = com.tudominio

# Archivo principal
source.dir = .

# Archivo de entrada principal
source.include_exts = py,png,jpg,kv,atlas
main.py = main.py

# Versión (formato: major.minor.revision)
version = 0.1

# Requerimientos
requirements = python3,kivy

# Permisos Android
android.permissions = INTERNET

# Icono
icon.filename = icon.png

# Orientación
orientation = portrait

android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0  # Versión actualizada
android.accept_sdk_license = True     # Aceptar licencias automáticamente
