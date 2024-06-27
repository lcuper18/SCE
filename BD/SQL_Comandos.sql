-- Crear la base de datos
CREATE DATABASE SCE_Database;

-- Usar la base de datos
USE SCE_Database;

-- Crear la tabla Estudiantes
CREATE TABLE Estudiantes (
    id_estudiante INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido1 VARCHAR(50),
    apellido2 VARCHAR(50),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_nacimiento DATE,
    direccion VARCHAR(255)
);

-- Crear la tabla Proyectos
CREATE TABLE Proyectos (
    id_proyecto INT PRIMARY KEY,
    nombre_proyecto VARCHAR(255),
    tutor VARCHAR(100),
    ubicacion_geografica VARCHAR(255),
    descripcion_proyecto TEXT,
    fecha_aprobacion DATE
);

-- Crear la tabla Detalles_SCE
CREATE TABLE Detalles_SCE (
    id_detalle_sce INT PRIMARY KEY,
    id_proyecto INT,
    poblacion_meta TEXT,
    breve_descripcion TEXT,
    justificacion TEXT,
    objetivo_general TEXT,
    metas TEXT,
    cronograma_actividades TEXT,
    actividades_evaluacion TEXT,
    recursos TEXT,
    bitacora TEXT,
    registro_horas_estudiantes TEXT,
    registro_horas_personal TEXT,
    anexos TEXT,
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto)
);

-- Crear la tabla Objetivos_Especificos
CREATE TABLE Objetivos_Especificos (
    id_objetivo INT PRIMARY KEY,
    id_detalle_sce INT,
    objetivo TEXT,
    FOREIGN KEY (id_detalle_sce) REFERENCES Detalles_SCE(id_detalle_sce)
);

-- Crear la tabla Periodos
CREATE TABLE Periodos (
    id_periodo INT PRIMARY KEY,
    nombre_periodo VARCHAR(50),
    fecha_inicio DATE,
    fecha_fin DATE
);

-- Crear la tabla de relación Estudiante-Proyecto
CREATE TABLE Estudiante_Proyecto (
    id_estudiante INT,
    id_proyecto INT,
    PRIMARY KEY (id_estudiante, id_proyecto),
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto)
);

-- Crear la tabla de relación Proyecto-Período
CREATE TABLE Proyecto_Periodo (
    id_proyecto INT,
    id_periodo INT,
    PRIMARY KEY (id_proyecto, id_periodo),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto),
    FOREIGN KEY (id_periodo) REFERENCES Periodos(id_periodo)
);

CREATE TABLE Docentes (
    id_docente INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido1 VARCHAR(50),
    apellido2 VARCHAR(50),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_nacimiento DATE,
    direccion VARCHAR(255)
);

-- Modificar la tabla Proyectos para agregar la columna id_tutor
ALTER TABLE Proyectos
ADD COLUMN id_tutor INT;

-- Agregar la clave foránea para vincular Proyectos con Docentes
ALTER TABLE Proyectos
ADD CONSTRAINT fk_tutor
FOREIGN KEY (id_tutor) REFERENCES Docentes(id_docente);

-- Crear la tabla Estados_Proyecto
CREATE TABLE Estados_Proyecto (
    id_estado INT PRIMARY KEY AUTO_INCREMENT,
    nombre_estado VARCHAR(50),
    descripcion_estado TEXT,
    fecha_creacion DATETIME DEFAULT NOW(),
    fecha_modificacion DATETIME DEFAULT NOW()
);

-- Usar la base de datos
USE SCE_Database;

-- Insertar los datos en la tabla Estados_Proyecto
INSERT INTO Estados_Proyecto (nombre_estado, descripcion_estado) VALUES
('Borrador', 'El proyecto está en fase de redacción y aún no se ha presentado oficialmente.'),
('Presentado', 'El proyecto ha sido entregado a la institución para su revisión.'),
('En Revisión', 'Las autoridades están evaluando la propuesta del proyecto.'),
('Aprobado', 'El proyecto cumple con los requisitos y ha sido aceptado.'),
('Aprobado con Condiciones', 'El proyecto se acepta, pero requiere modificaciones antes de iniciar.'),
('Rechazado', 'El proyecto no cumple con los criterios y no es aceptado.'),
('En Ejecución', 'El proyecto está actualmente en marcha.'),
('Suspendido', 'El proyecto se ha detenido temporalmente debido a algún problema.'),
('Cancelado', 'El proyecto se ha detenido permanentemente antes de completarse.'),
('Completado', 'Todas las actividades del proyecto se han realizado con éxito.'),
('En Evaluación', 'Se está analizando el impacto y resultados del proyecto terminado.'),
('Certificado', 'El proyecto ha sido oficialmente reconocido y se ha emitido constancia.');

-- Modificar la tabla Proyectos para agregar la columna id_estado
ALTER TABLE Proyectos
ADD COLUMN id_estado INT,
ADD CONSTRAINT fk_estado_proyecto
FOREIGN KEY (id_estado)
REFERENCES Estados_Proyecto(id_estado);

-- Eliminar - Relacion entre tablas.
ALTER TABLE Proyectos
DROP FOREIGN KEY fk_tutor;

ALTER TABLE Docentes
MODIFY COLUMN id_docente VARCHAR(50);

ALTER TABLE Proyectos
MODIFY COLUMN id_tutor VARCHAR(50);

-- Restablecer - Relacion entre tablas.
ALTER TABLE Proyectos
ADD CONSTRAINT fk_tutor
FOREIGN KEY (id_tutor)
REFERENCES Docentes(id_docente);

SELECT * from Docentes;
