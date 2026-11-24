-- Base de datos para los tickets de SUPERMERCADOS EL AHORRO
DROP DATABASE IF EXISTS tickets_db;
CREATE DATABASE tickets_db CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE tickets_db;

CREATE TABLE sucursal (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    nombre    VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    cif       VARCHAR(9)   NOT NULL UNIQUE,
    telefono  VARCHAR(15)
);

-- id = codigo del cajero que sale en el ticket (015, 033...)
CREATE TABLE empleado (
    id          INT PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL
);

CREATE TABLE producto (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL UNIQUE,
    precio      DECIMAL(8,2) NOT NULL
);

-- EFECTIVO, TARJETA...
CREATE TABLE forma_pago (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE
);

-- numero = el que sale en "Ticket: 20010001"
CREATE TABLE ticket (
    numero        INT PRIMARY KEY,
    fecha_hora    DATETIME NOT NULL,
    sucursal_id   INT NOT NULL,
    empleado_id   INT NOT NULL,
    subtotal      DECIMAL(8,2) NOT NULL,
    iva           DECIMAL(8,2) NOT NULL,
    total         DECIMAL(8,2) NOT NULL,
    forma_pago_id INT NOT NULL,
    autorizacion  VARCHAR(10) NULL,
    FOREIGN KEY (sucursal_id)   REFERENCES sucursal(id),
    FOREIGN KEY (empleado_id)   REFERENCES empleado(id),
    FOREIGN KEY (forma_pago_id) REFERENCES forma_pago(id)
);

-- cantidad con 3 decimales porque hay productos por kg (2.500)
CREATE TABLE ticket_linea (
    ticket_numero INT NOT NULL,
    producto_id   INT NOT NULL,
    cantidad      DECIMAL(8,3) NOT NULL,
    importe       DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (ticket_numero, producto_id),
    FOREIGN KEY (ticket_numero) REFERENCES ticket(numero),
    FOREIGN KEY (producto_id)   REFERENCES producto(id)
);
