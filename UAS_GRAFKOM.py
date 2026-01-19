from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# ================= GLOBAL =================
rot_x = 0.0
rot_y = 0.0
rot_z = 0.0
current_object = 0
show_grid = True
wireframe = False

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 650

objects = [
    ("Kubus", "Merah", (1, 0, 0)),
    ("Piramida", "Hijau", (0, 1, 0)),
    ("Prisma Segitiga", "Biru", (0, 0, 1)),
    ("Bola", "Kuning", (1, 1, 0)),
    ("Tabung", "Cyan", (0, 1, 1)),
    ("Kerucut", "Magenta", (1, 0, 1)),
]

# ================= INIT =================
def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)

    glLightfv(GL_LIGHT0, GL_POSITION, [5, 8, 10, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])

    glClearColor(0.08, 0.08, 0.1, 1)

# ================= GRID =================
def draw_grid(size=10, step=1):
    glDisable(GL_LIGHTING)
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_LINES)
    for i in range(-size, size + 1, step):
        glVertex3f(i, 0, -size)
        glVertex3f(i, 0, size)
        glVertex3f(-size, 0, i)
        glVertex3f(size, 0, i)
    glEnd()
    glEnable(GL_LIGHTING)

# ================= JUDUL (HUD 2D) =================
def draw_title(text):
    glDisable(GL_LIGHTING)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glRasterPos2f(300, WINDOW_HEIGHT - 100)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(ch))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_LIGHTING)

# ================= OBJEK =================
def draw_cube(color):
    glColor3f(*color)
    glutSolidCube(2)

def draw_pyramid(color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 1.5, 0); glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1)
    glVertex3f(0, 1.5, 0); glVertex3f(1, -1, 1); glVertex3f(1, -1, -1)
    glVertex3f(0, 1.5, 0); glVertex3f(1, -1, -1); glVertex3f(-1, -1, -1)
    glVertex3f(0, 1.5, 0); glVertex3f(-1, -1, -1); glVertex3f(-1, -1, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1); glVertex3f(-1, -1, -1)
    glEnd()

def draw_prism(color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 1, 1); glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1)
    glVertex3f(0, 1, -1); glVertex3f(-1, -1, -1); glVertex3f(1, -1, -1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(0, 1, 1); glVertex3f(0, 1, -1)
    glVertex3f(-1, -1, -1); glVertex3f(-1, -1, 1)

    glVertex3f(0, 1, 1); glVertex3f(0, 1, -1)
    glVertex3f(1, -1, -1); glVertex3f(1, -1, 1)

    glVertex3f(-1, -1, 1); glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1); glVertex3f(1, -1, 1)
    glEnd()

def draw_sphere(color):
    glColor3f(*color)
    glutSolidSphere(1.2, 40, 40)

def draw_cylinder(color):
    glColor3f(*color)
    quad = gluNewQuadric()
    gluCylinder(quad, 1, 1, 2.5, 30, 30)

def draw_cone(color):
    glColor3f(*color)
    glutSolidCone(1.2, 2.5, 30, 30)

# ================= DISPLAY =================
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_title(
        "BANGUN RUANG 3D INTERAKTIF DENGAN TRANFORMASI GEOMETRIS BERBASIS PYTHON"
    )

    gluLookAt(6, 6, 10, 0, 1, 0, 0, 1, 0)

    if show_grid:
        draw_grid()

    nama_objek, nama_warna, color = objects[current_object]

    glPushMatrix()
    glTranslatef(0, 1.5, 0)
    glRotatef(rot_x, 1, 0, 0)
    glRotatef(rot_y, 0, 1, 0)
    glRotatef(rot_z, 0, 0, 1)

    if wireframe:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    if current_object == 0:
        draw_cube(color)
    elif current_object == 1:
        draw_pyramid(color)
    elif current_object == 2:
        draw_prism(color)
    elif current_object == 3:
        draw_sphere(color)
    elif current_object == 4:
        draw_cylinder(color)
    elif current_object == 5:
        draw_cone(color)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glPopMatrix()

    # ===== NAME TAG (BAWAH TENGAH) =====
    glDisable(GL_LIGHTING)
    glColor3f(1, 1, 1)
    glRasterPos3f(-1.5, -5, 0)
    for ch in f"{nama_objek} - {nama_warna}":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glEnable(GL_LIGHTING)

    glutSwapBuffers()

# ================= INPUT =================
def keyboard(key, x, y):
    global rot_x, rot_y, rot_z, current_object, show_grid, wireframe

    if key == b'w': rot_x -= 5
    elif key == b's': rot_x += 5
    elif key == b'a': rot_y -= 5
    elif key == b'd': rot_y += 5
    elif key == b'q': rot_z -= 5
    elif key == b'e': rot_z += 5
    elif key == b'r': rot_x = rot_y = rot_z = 0
    elif key == b'g': show_grid = not show_grid
    elif key == b'f': wireframe = not wireframe
    elif key == b'\r':
        current_object = (current_object + 1) % len(objects)

    glutPostRedisplay()

def reshape(w, h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH = w
    WINDOW_HEIGHT = h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50)
    glMatrixMode(GL_MODELVIEW)

# ================= MAIN =================
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Grafika Komputer 3D")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
