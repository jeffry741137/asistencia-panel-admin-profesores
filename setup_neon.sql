-- ================================================================
-- SCRIPT SQL PARA NEON POSTGRESQL
-- Ejecutar en el SQL Editor de Neon (console.neon.tech)
-- ================================================================

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    nombre_completo TEXT DEFAULT '',
    institucion TEXT DEFAULT '',
    salon TEXT DEFAULT '',
    activo BOOLEAN DEFAULT TRUE,
    creado_en TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS codigos_invitacion (
    id SERIAL PRIMARY KEY,
    codigo TEXT UNIQUE NOT NULL,
    usado BOOLEAN DEFAULT FALSE,
    creado_en TIMESTAMPTZ DEFAULT NOW(),
    expira_en TIMESTAMPTZ NOT NULL,
    usado_por TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS alumnos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    nombre TEXT NOT NULL,
    genero TEXT CHECK(genero IN ('nino','nina')) DEFAULT 'nino',
    orden INTEGER DEFAULT 0,
    UNIQUE(usuario_id, nombre)
);

CREATE TABLE IF NOT EXISTS asistencia (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE,
    clave TEXT NOT NULL,
    alumno TEXT NOT NULL,
    dia TEXT NOT NULL,
    marca TEXT NOT NULL,
    hora TEXT NOT NULL,
    motivo TEXT DEFAULT '',
    UNIQUE(usuario_id, clave, alumno, dia)
);

-- Índices para mejor rendimiento
CREATE INDEX IF NOT EXISTS idx_asistencia_usuario ON asistencia(usuario_id);
CREATE INDEX IF NOT EXISTS idx_asistencia_clave ON asistencia(clave);
CREATE INDEX IF NOT EXISTS idx_asistencia_dia ON asistencia(dia);
CREATE INDEX IF NOT EXISTS idx_alumnos_usuario ON alumnos(usuario_id);
CREATE INDEX IF NOT EXISTS idx_codigos_codigo ON codigos_invitacion(codigo);

-- ✅ Listo! Las tablas se crearán automáticamente.
