
import sqlite3
import os

# ==========================================
# MODULO 1. CREACION DE LA BASE DE DATOS
# ==========================================

def crear_bd():
    os.makedirs("database", exist_ok=True)

    conexion = sqlite3.connect("database/EMPLEADOS.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            CURP TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            calle TEXT,
            colonia TEXT,
            telefono TEXT
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos EMPLEADOS creada correctamente.")


# ==========================================
# MODULO 2. ALTA DE EMPLEADOS
# ==========================================

def alta_empleado():
    conexion = sqlite3.connect("database/EMPLEADOS.db")
    cursor = conexion.cursor()

    print("\n===== ALTA DE EMPLEADO =====")

    curp = input("CURP: ").strip().upper()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    calle = input("Calle: ").strip()
    colonia = input("Colonia: ").strip()
    telefono = input("Telefono: ").strip()

    if not curp or not nombre or not apellido:
        print("Error: CURP, nombre y apellido son obligatorios.")
        conexion.close()
        return

    try:
        cursor.execute("""
            INSERT INTO empleados (
                CURP, nombre, apellido, calle, colonia, telefono
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            curp, nombre, apellido, calle, colonia, telefono
        ))

        conexion.commit()
        print("\nEmpleado registrado correctamente.")

    except sqlite3.IntegrityError:
        print("Error: ya existe un empleado con esa CURP.")

    except sqlite3.Error as error:
        print(f"Error al registrar al empleado: {error}")

    finally:
        conexion.close()


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":
    crear_bd()
    alta_empleado()
