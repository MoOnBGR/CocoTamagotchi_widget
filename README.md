# Tamagotchi de escritorio

Un tamagotchi flotante en Linux, hecho con Python + Tkinter.
Arte 100%  ilustraciones ASCII,es muy basico solo tiene las funciones de  hambre, animo y energia que bajan solas
con el tiempo.

## Requisitos

- Python 3
- Tkinter (en Fedora no siempre viene instalado por defecto):

```bash
sudo dnf install python3-tkinter
```

## Instalación y primer uso

1. Clona o copia el proyecto a tu carpeta personal:

```bash
mkdir -p ~/tamagotchi
cd ~/tamagotchi
```

2. Prueba que corre bien:

```bash
python3 tamagotchi_widget.py
```

Debería aparecer una ventana rosa sin bordes, abajo a la derecha de tu pantalla,
siempre encima de las demas ventanas.
## Guardado de progreso

El estado se guarda automaticamente en:

```
~/.local/share/tamagotchi-widget/state.json
```

Cada vez que abres el programa, calcula cuanto tiempo paso desde la ultima vez
y ajusta hambre/animo/energia — igual que un tamagotchi real que sigue "viviendo"
aunque no lo tengas abierto.

## Para hacerlo ejecutable

1. Asegurate de que la primera linea del archivo sea exactamente:

```python
#!/usr/bin/env python3
```

2. Dale permiso de ejecucion:

```bash
chmod +x ~/tamagotchi/tamagotchi_widget.py
```

3. Pruébalo:

```bash
~/tamagotchi/tamagotchi_widget.py
```

## Icono en el menu de aplicaciones y en la barra

1. Copia tu imagen a la carpeta de iconos del usuario:

```bash
mkdir -p ~/.local/share/icons
cp ~/tamagotchi/iconCat.png ~/.local/share/icons/tamagotchi.png
```

2. Crea el lanzador:

```bash
nano ~/.local/share/applications/tamagotchi.desktop
```

   Contenido (reemplaza `TU_USUARIO` por el resultado de `whoami`):

```ini
[Desktop Entry]
Type=Application
Name=Tamagotchi
Comment=Mi tamagotchi de escritorio
Exec=/home/TU_USUARIO/tamagotchi/tamagotchi_widget.py
Icon=/home/TU_USUARIO/.local/share/icons/tamagotchi.png
Terminal=false
Categories=Utility;Game;
```

```bash
chmod +x ~/.local/share/applications/tamagotchi.desktop
```

3. Busca "Tamagotchi" en el menu de aplicaciones (tecla Super/Windows). Deberia
   aparecer con tu icono.

##Referencias
![Icono del tamagotchi](imagenes/) 
