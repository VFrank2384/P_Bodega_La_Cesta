-- ==========================================
-- BASE DE DATOS: BODEGA LA CESTA
-- ==========================================
DROP DATABASE IF EXISTS bodega_la_cesta;
CREATE DATABASE bodega_la_cesta;
USE bodega_la_cesta;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    stock INT NOT NULL,
    stock_minimo INT NOT NULL DEFAULT 5
);

-- Insertamos productos de prueba (incluyendo algunos críticos)
INSERT INTO productos (nombre, stock, stock_minimo) VALUES 
('Leche Gloria', 12, 5),
('Arroz Costeño', 4, 5),     
('Fideos Don Vittorio', 8, 5),
('Aceite Primor', 2, 5),    
('Azúcar Rubia', 15, 5),
('Atún Florida', 3, 5);