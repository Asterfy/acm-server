/*
  Warnings:

  - You are about to drop the `User` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropTable
DROP TABLE "User";

-- CreateTable
CREATE TABLE "alumnos" (
    "id" SERIAL NOT NULL,
    "codigo" VARCHAR(255) NOT NULL,
    "nombres" VARCHAR(255) NOT NULL,
    "apellido_paterno" VARCHAR(255) NOT NULL,
    "apellido_materno" VARCHAR(255) NOT NULL,
    "numero_telefono" VARCHAR(255) NOT NULL,
    "correo" VARCHAR(255) NOT NULL,

    CONSTRAINT "alumnos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "alumnos_competidores" (
    "id" SERIAL NOT NULL,
    "lenguaje_dominio" VARCHAR(255),
    "area_especialidad" VARCHAR(255),
    "id_alumno" INTEGER,

    CONSTRAINT "alumnos_competidores_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "contests" (
    "id" BIGSERIAL NOT NULL,
    "edicion" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "fecha" TIMESTAMPTZ(6) NOT NULL,
    "anio" INTEGER NOT NULL,
    "id_semestre" BIGINT,

    CONSTRAINT "contests_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "equipos" (
    "id" SERIAL NOT NULL,
    "nombre_equipo" VARCHAR(255) NOT NULL,
    "categoria" VARCHAR(255) NOT NULL,
    "puesto" INTEGER,
    "id_contest" BIGINT,

    CONSTRAINT "equipos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "miembros" (
    "id" BIGSERIAL NOT NULL,
    "github_username" VARCHAR(255) NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "id_alumno" INTEGER,
    "id_rol" BIGINT,

    CONSTRAINT "miembros_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "miembros_team" (
    "id" BIGSERIAL NOT NULL,
    "fecha_inclusion" TIMESTAMPTZ(6),
    "es_lider" BOOLEAN DEFAULT false,
    "estado_miembro" BOOLEAN DEFAULT true,
    "id_miembro" BIGINT,
    "id_team" BIGINT,

    CONSTRAINT "miembros_team_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "participantes_contest" (
    "id" SERIAL NOT NULL,
    "universidad" VARCHAR(255) NOT NULL,
    "semestre" VARCHAR(255) NOT NULL,
    "creditos" INTEGER NOT NULL,
    "id_equipo" INTEGER,
    "id_alumno_competidor" INTEGER,

    CONSTRAINT "participantes_contest_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "preguntas" (
    "id" BIGSERIAL NOT NULL,
    "letra_pregunta" VARCHAR(255) NOT NULL,
    "info_pregunta" VARCHAR(255) NOT NULL,
    "id_contest" BIGINT,

    CONSTRAINT "preguntas_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "roles" (
    "id" BIGSERIAL NOT NULL,
    "nombre_rol" VARCHAR(255) NOT NULL,
    "permiso" VARCHAR(255) NOT NULL,

    CONSTRAINT "roles_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "scientific_articles" (
    "id" BIGSERIAL NOT NULL,
    "titulo_articulo" VARCHAR(255) NOT NULL,
    "doi" VARCHAR(255) NOT NULL,
    "pdf_link" VARCHAR(255) NOT NULL,
    "fecha_publicacion" TIMESTAMPTZ(6),
    "id_miembro" BIGINT,

    CONSTRAINT "scientific_articles_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "semestre" (
    "id" BIGSERIAL NOT NULL,
    "nombre_semestre" VARCHAR(255) NOT NULL,

    CONSTRAINT "semestre_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "teams" (
    "id" BIGSERIAL NOT NULL,
    "nombre_team" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,

    CONSTRAINT "teams_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "alumnos_competidores" ADD CONSTRAINT "alumnos_competidores_id_alumno_fkey" FOREIGN KEY ("id_alumno") REFERENCES "alumnos"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "contests" ADD CONSTRAINT "contests_id_semestre_fkey" FOREIGN KEY ("id_semestre") REFERENCES "semestre"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "equipos" ADD CONSTRAINT "equipos_id_contest_fkey" FOREIGN KEY ("id_contest") REFERENCES "contests"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "miembros" ADD CONSTRAINT "miembros_id_alumno_fkey" FOREIGN KEY ("id_alumno") REFERENCES "alumnos"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "miembros" ADD CONSTRAINT "miembros_id_rol_fkey" FOREIGN KEY ("id_rol") REFERENCES "roles"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "miembros_team" ADD CONSTRAINT "miembros_team_id_miembro_fkey" FOREIGN KEY ("id_miembro") REFERENCES "miembros"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "miembros_team" ADD CONSTRAINT "miembros_team_id_team_fkey" FOREIGN KEY ("id_team") REFERENCES "teams"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "participantes_contest" ADD CONSTRAINT "participantes_contest_id_alumno_competidor_fkey" FOREIGN KEY ("id_alumno_competidor") REFERENCES "alumnos_competidores"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "participantes_contest" ADD CONSTRAINT "participantes_contest_id_equipo_fkey" FOREIGN KEY ("id_equipo") REFERENCES "equipos"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "preguntas" ADD CONSTRAINT "preguntas_id_contest_fkey" FOREIGN KEY ("id_contest") REFERENCES "contests"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "scientific_articles" ADD CONSTRAINT "scientific_articles_id_miembro_fkey" FOREIGN KEY ("id_miembro") REFERENCES "miembros"("id") ON DELETE SET NULL ON UPDATE CASCADE;
