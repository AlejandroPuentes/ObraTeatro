/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     13/02/2022 5:47:50 p. m.                     */
/*==============================================================*/


alter table "Convocatoria"
   drop constraint FK_CONVOCAT_CONV_OBRA_OBRATEAT;

alter table "Emp_Obra"
   drop constraint FK_EMP_OBRA_EMP_OBRA_EMPLEADO;

alter table "Emp_Obra"
   drop constraint FK_EMP_OBRA_RELATIONS_PRESENTA;

alter table "Emp_Obra"
   drop constraint FK_EMP_OBRA_RELATIONS_ROL;

alter table "Escritor"
   drop constraint FK_ESCRITOR_PAI_ESCRI_PAIS;

alter table "Est_Conv"
   drop constraint FK_EST_CONV_EST_CONV_CONVOCAT;

alter table "Est_Conv"
   drop constraint FK_EST_CONV_EST_CONV2_ESTUDIAN;

alter table "Estudiante"
   drop constraint FK_ESTUDIAN_ESTU_CARR_CARRERA;

alter table "Estudiante"
   drop constraint FK_ESTUDIAN_TIPOIDEN__TIPOIDEN;

alter table GP
   drop constraint FK_GP_GP_GASTOS;

alter table GP
   drop constraint FK_GP_GP2_PRESENTA;

alter table "Hora"
   drop constraint FK_HORA_PRESE_HOR_PRESENTA;

alter table "ObraTeatro"
   drop constraint FK_OBRATEAT_COOR_OBRA_EMPLEADO;

alter table "ObraTeatro"
   drop constraint FK_OBRATEAT_DIRE_OBRA_EMPLEADO;

alter table "ObraTeatro"
   drop constraint FK_OBRATEAT_ESCR_OBRA_ESCRITOR;

alter table "ObraTeatro"
   drop constraint FK_OBRATEAT_OBRATE_PA_PAIS;

alter table "Personaje"
   drop constraint FK_PERSONAJ_RELATIONS_OBRATEAT;

alter table "Personaje"
   drop constraint FK_PERSONAJ_RELATIONS_ESTUDIAN;

alter table "Presen_Dia"
   drop constraint FK_PRESEN_D_PRESEN_DI_DIA;

alter table "Presen_Dia"
   drop constraint FK_PRESEN_D_PRESEN_DI_PRESENTA;

alter table "PresentacionObra"
   drop constraint FK_PRESENTA_OBRA_PRES_OBRATEAT;

alter table "PresentacionObra"
   drop constraint FK_PRESENTA_PRES_TEA_TEATRO;

alter table "PresentacionObra"
   drop constraint FK_PRESENTA_PRESE_TIP_TIPOPRES;

alter table "TipoO_ObraTea"
   drop constraint FK_TIPOO_OB_TIPOO_OBR_OBRATEAT;

alter table "TipoO_ObraTea"
   drop constraint FK_TIPOO_OB_TIPOO_OBR_TIPOOBRA;

drop table "Carrera" cascade constraints;

drop index "Conv_Obra_FK";

drop table "Convocatoria" cascade constraints;

drop table "Dia" cascade constraints;

drop index "Relationship_25_FK";

drop index "Relationship_24_FK";

drop index "Emp_Obra_FK";

drop table "Emp_Obra" cascade constraints;

drop table "Empleado" cascade constraints;

drop index "Pai_Escri_FK";

drop table "Escritor" cascade constraints;

drop index "Est_Conv_FK";

drop index "Est_Conv2_FK";

drop table "Est_Conv" cascade constraints;

drop index "Tipoiden_estu2_FK";

drop index "Estu_Carr_FK";

drop table "Estudiante" cascade constraints;

drop index GP2_FK;

drop table GP cascade constraints;

drop table "Gastos" cascade constraints;

drop index "Prese_hora_FK";

drop table "Hora" cascade constraints;

drop index "ObraTe_Pais_FK";

drop index "Escr_Obra_FK";

drop index "Coor_obra_FK";

drop index "Dire_Obra_FK";

drop table "ObraTeatro" cascade constraints;

drop table "Pais" cascade constraints;

drop index "Relationship_20_FK";

drop index "Relationship_18_FK";

drop table "Personaje" cascade constraints;

drop index "Presen_Dia_FK";

drop index "Presen_Dia2_FK";

drop table "Presen_Dia" cascade constraints;

drop index "Prese_TipP_FK";

drop index "Obra_Pres_FK";

drop index "Pres_Tea_FK";

drop table "PresentacionObra" cascade constraints;

drop table "Rol" cascade constraints;

drop table "Teatro" cascade constraints;

drop table "TipoIdentificacion" cascade constraints;

drop index "TipoO_ObraTea_FK";

drop index "TipoO_ObraTea2_FK";

drop table "TipoO_ObraTea" cascade constraints;

drop table "TipoPresentacion" cascade constraints;

drop table "tipoObra" cascade constraints;

/*==============================================================*/
/* Table: "Carrera"                                             */
/*==============================================================*/
create table "Carrera" 
(
   "idCarrera"          NUMBER(3,0)          not null,
   "nombreCarr"         VARCHAR2(30)         not null,
   constraint PK_CARRERA primary key ("idCarrera")
);

/*==============================================================*/
/* Table: "Convocatoria"                                        */
/*==============================================================*/
create table "Convocatoria" 
(
   "idconvocatoria"     VARCHAR2(3)          not null,
   "idObra"             VARCHAR2(4)          not null,
   "personaje"          VARCHAR2(20)         not null,
   constraint PK_CONVOCATORIA primary key ("idconvocatoria")
);

/*==============================================================*/
/* Index: "Conv_Obra_FK"                                        */
/*==============================================================*/
create index "Conv_Obra_FK" on "Convocatoria" (
   "idObra" ASC
);

/*==============================================================*/
/* Table: "Dia"                                                 */
/*==============================================================*/
create table "Dia" 
(
   "idDia"              NUMBER(2,0)          not null,
   "dia"                DATE                 not null,
   constraint PK_DIA primary key ("idDia")
);

/*==============================================================*/
/* Table: "Emp_Obra"                                            */
/*==============================================================*/
create table "Emp_Obra" 
(
   "idlistaEM"          VARCHAR2(3)          not null,
   "idEmpleado"         VARCHAR2(4)          not null,
   "idpresentacion"     VARCHAR2(4)          not null,
   "idRol"              VARCHAR2(4)          not null,
   "idObra"             VARCHAR2(4)          not null,
   constraint PK_EMP_OBRA primary key ("idlistaEM"),
   constraint AK_IDENTIFIER_1_EMP_OBRA unique ("idEmpleado", "idObra")
);

/*==============================================================*/
/* Index: "Emp_Obra_FK"                                         */
/*==============================================================*/
create index "Emp_Obra_FK" on "Emp_Obra" (
   "idEmpleado" ASC
);

/*==============================================================*/
/* Index: "Relationship_24_FK"                                  */
/*==============================================================*/
create index "Relationship_24_FK" on "Emp_Obra" (
   "idpresentacion" ASC
);

/*==============================================================*/
/* Index: "Relationship_25_FK"                                  */
/*==============================================================*/
create index "Relationship_25_FK" on "Emp_Obra" (
   "idRol" ASC
);

/*==============================================================*/
/* Table: "Empleado"                                            */
/*==============================================================*/
create table "Empleado" 
(
   "idEmpleado"         VARCHAR2(4)          not null,
   "nombreEm"           VARCHAR2(30)         not null,
   "Attribute_33"       NUMBER(11,0)         not null,
   constraint PK_EMPLEADO primary key ("idEmpleado")
);

/*==============================================================*/
/* Table: "Escritor"                                            */
/*==============================================================*/
create table "Escritor" 
(
   "idEscritor"         NUMBER(3,0)          not null,
   "idPais"             NUMBER(3,0)          not null,
   "nombreEs"           VARCHAR2(30)         not null,
   constraint PK_ESCRITOR primary key ("idEscritor")
);

/*==============================================================*/
/* Index: "Pai_Escri_FK"                                        */
/*==============================================================*/
create index "Pai_Escri_FK" on "Escritor" (
   "idPais" ASC
);

/*==============================================================*/
/* Table: "Est_Conv"                                            */
/*==============================================================*/
create table "Est_Conv" 
(
   "idEstCon"           VARCHAR2(3)          not null,
   "idconvocatoria"     VARCHAR2(3)          not null,
   "identificacion"     NUMBER(10,0)         not null,
   constraint PK_EST_CONV primary key ("idEstCon"),
   constraint AK_IDENTIFIER_1_EST_CONV unique ("idconvocatoria", "identificacion")
);

/*==============================================================*/
/* Index: "Est_Conv2_FK"                                        */
/*==============================================================*/
create index "Est_Conv2_FK" on "Est_Conv" (
   "identificacion" ASC
);

/*==============================================================*/
/* Index: "Est_Conv_FK"                                         */
/*==============================================================*/
create index "Est_Conv_FK" on "Est_Conv" (
   "idconvocatoria" ASC
);

/*==============================================================*/
/* Table: "Estudiante"                                          */
/*==============================================================*/
create table "Estudiante" 
(
   "identificacion"     NUMBER(10,0)         not null,
   "idCarrera"          NUMBER(3,0)          not null,
   "idTipoIdent"        NUMBER(2,0)          not null,
   "nombre"             VARCHAR2(30)         not null,
   "apellido"           VARCHAR2(30)         not null,
   "fecha_nacimiento"   DATE                 not null,
   "codigo"             NUMBER(11,0)         not null,
   "correo"             VARCHAR2(45)         not null,
   constraint PK_ESTUDIANTE primary key ("identificacion")
);

/*==============================================================*/
/* Index: "Estu_Carr_FK"                                        */
/*==============================================================*/
create index "Estu_Carr_FK" on "Estudiante" (
   "idCarrera" ASC
);

/*==============================================================*/
/* Index: "Tipoiden_estu2_FK"                                   */
/*==============================================================*/
create index "Tipoiden_estu2_FK" on "Estudiante" (
   "idTipoIdent" ASC
);

/*==============================================================*/
/* Table: GP                                                    */
/*==============================================================*/
create table GP 
(
   "idGastos"           NUMBER(2)            not null,
   "idpresentacion"     VARCHAR2(4)          not null,
   "total"              NUMBER(15,0),
   constraint PK_GP primary key ("idGastos", "idpresentacion"),
   constraint AK_GASTOSPK_GP unique ("idGastos")
);

/*==============================================================*/
/* Index: GP2_FK                                                */
/*==============================================================*/
create index GP2_FK on GP (
   "idpresentacion" ASC
);

/*==============================================================*/
/* Table: "Gastos"                                              */
/*==============================================================*/
create table "Gastos" 
(
   "idGastos"           NUMBER(2)            not null,
   "descG"              VARCHAR2(45)         not null,
   "valor"              NUMBER(6)            not null,
   constraint PK_GASTOS primary key ("idGastos")
);

/*==============================================================*/
/* Table: "Hora"                                                */
/*==============================================================*/
create table "Hora" 
(
   "idHora"             NUMBER(3)            not null,
   "idpresentacion"     VARCHAR2(4)          not null,
   "hora"               DATE                 not null,
   constraint PK_HORA primary key ("idHora")
);

/*==============================================================*/
/* Index: "Prese_hora_FK"                                       */
/*==============================================================*/
create index "Prese_hora_FK" on "Hora" (
   "idpresentacion" ASC
);

/*==============================================================*/
/* Table: "ObraTeatro"                                          */
/*==============================================================*/
create table "ObraTeatro" 
(
   "idObra"             VARCHAR2(4)          not null,
   "idDirector"         VARCHAR2(4)          not null,
   "idCoordinador"      VARCHAR2(4)          not null,
   "idEscritor"         NUMBER(3,0)          not null,
   "idPais"             NUMBER(3,0)          not null,
   "titulo"             VARCHAR2(30)         not null,
   "año_Crea"           NUMBER(4,0)          not null,
   constraint PK_OBRATEATRO primary key ("idObra")
);

/*==============================================================*/
/* Index: "Dire_Obra_FK"                                        */
/*==============================================================*/
create index "Dire_Obra_FK" on "ObraTeatro" (
   "idDirector" ASC
);

/*==============================================================*/
/* Index: "Coor_obra_FK"                                        */
/*==============================================================*/
create index "Coor_obra_FK" on "ObraTeatro" (
   "idCoordinador" ASC
);

/*==============================================================*/
/* Index: "Escr_Obra_FK"                                        */
/*==============================================================*/
create index "Escr_Obra_FK" on "ObraTeatro" (
   "idEscritor" ASC
);

/*==============================================================*/
/* Index: "ObraTe_Pais_FK"                                      */
/*==============================================================*/
create index "ObraTe_Pais_FK" on "ObraTeatro" (
   "idPais" ASC
);

/*==============================================================*/
/* Table: "Pais"                                                */
/*==============================================================*/
create table "Pais" 
(
   "idPais"             NUMBER(3,0)          not null,
   "nombre"             VARCHAR2(30)         not null,
   constraint PK_PAIS primary key ("idPais")
);

/*==============================================================*/
/* Table: "Personaje"                                           */
/*==============================================================*/
create table "Personaje" 
(
   "idPersonaje"        NUMBER(2,0)          not null,
   "idObra"             VARCHAR2(4)          not null,
   "estudiantico"       NUMBER(10,0)         not null,
   "namePersonaje"      VARCHAR2(30)         not null,
   constraint PK_PERSONAJE primary key ("idPersonaje")
);

/*==============================================================*/
/* Index: "Relationship_18_FK"                                  */
/*==============================================================*/
create index "Relationship_18_FK" on "Personaje" (
   "idObra" ASC
);

/*==============================================================*/
/* Index: "Relationship_20_FK"                                  */
/*==============================================================*/
create index "Relationship_20_FK" on "Personaje" (
   "estudiantico" ASC
);

/*==============================================================*/
/* Table: "Presen_Dia"                                          */
/*==============================================================*/
create table "Presen_Dia" 
(
   "idpreXDia"          VARCHAR2(3)          not null,
   "idDia"              NUMBER(2,0)          not null,
   "idpresentacion"     VARCHAR2(4)          not null,
   constraint PK_PRESEN_DIA primary key ("idpreXDia"),
   constraint AK_IDENTIFIER_1_PRESEN_D unique ("idDia", "idpresentacion")
);

/*==============================================================*/
/* Index: "Presen_Dia2_FK"                                      */
/*==============================================================*/
create index "Presen_Dia2_FK" on "Presen_Dia" (
   "idpresentacion" ASC
);

/*==============================================================*/
/* Index: "Presen_Dia_FK"                                       */
/*==============================================================*/
create index "Presen_Dia_FK" on "Presen_Dia" (
   "idDia" ASC
);

/*==============================================================*/
/* Table: "PresentacionObra"                                    */
/*==============================================================*/
create table "PresentacionObra" 
(
   "idpresentacion"     VARCHAR2(4)          not null,
   "idTeatro"           VARCHAR2(4)          not null,
   "idObra"             VARCHAR2(4)          not null,
   "idTipP"             NUMBER(1)            not null,
   "tipoPresentacion"   VARCHAR2(25)         not null,
   "dias"               DATE                 not null,
   "nFunciones"         NUMBER(1,0)          not null,
   constraint PK_PRESENTACIONOBRA primary key ("idpresentacion")
);

/*==============================================================*/
/* Index: "Pres_Tea_FK"                                         */
/*==============================================================*/
create index "Pres_Tea_FK" on "PresentacionObra" (
   "idTeatro" ASC
);

/*==============================================================*/
/* Index: "Obra_Pres_FK"                                        */
/*==============================================================*/
create index "Obra_Pres_FK" on "PresentacionObra" (
   "idObra" ASC
);

/*==============================================================*/
/* Index: "Prese_TipP_FK"                                       */
/*==============================================================*/
create index "Prese_TipP_FK" on "PresentacionObra" (
   "idTipP" ASC
);

/*==============================================================*/
/* Table: "Rol"                                                 */
/*==============================================================*/
create table "Rol" 
(
   "idRol"              VARCHAR2(4)          not null,
   "nombreRol"          VARCHAR2(30)         not null,
   constraint PK_ROL primary key ("idRol")
);

/*==============================================================*/
/* Table: "Teatro"                                              */
/*==============================================================*/
create table "Teatro" 
(
   "idTeatro"           VARCHAR2(4)          not null,
   "nombreT"            VARCHAR2(30)         not null,
   "horasDisp"          NUMBER(2,0)          not null,
   constraint PK_TEATRO primary key ("idTeatro")
);

/*==============================================================*/
/* Table: "TipoIdentificacion"                                  */
/*==============================================================*/
create table "TipoIdentificacion" 
(
   "idTipoIdent"        NUMBER(2,0)          not null,
   "descTipo"           VARCHAR2(30)         not null,
   constraint PK_TIPOIDENTIFICACION primary key ("idTipoIdent")
);

/*==============================================================*/
/* Table: "TipoO_ObraTea"                                       */
/*==============================================================*/
create table "TipoO_ObraTea" 
(
   "idtipoOOTea"        VARCHAR2(3)          not null,
   "idObra"             VARCHAR2(4)          not null,
   "idTipoObra"         VARCHAR2(4)          not null,
   constraint PK_TIPOO_OBRATEA primary key ("idtipoOOTea"),
   constraint AK_IDENTIFIER_1_TIPOO_OB unique ("idObra", "idTipoObra")
);

/*==============================================================*/
/* Index: "TipoO_ObraTea2_FK"                                   */
/*==============================================================*/
create index "TipoO_ObraTea2_FK" on "TipoO_ObraTea" (
   "idTipoObra" ASC
);

/*==============================================================*/
/* Index: "TipoO_ObraTea_FK"                                    */
/*==============================================================*/
create index "TipoO_ObraTea_FK" on "TipoO_ObraTea" (
   "idObra" ASC
);

/*==============================================================*/
/* Table: "TipoPresentacion"                                    */
/*==============================================================*/
create table "TipoPresentacion" 
(
   "idTipP"             NUMBER(1)            not null,
   "descTipP"           VARCHAR2(20)         not null,
   constraint PK_TIPOPRESENTACION primary key ("idTipP")
);

/*==============================================================*/
/* Table: "tipoObra"                                            */
/*==============================================================*/
create table "tipoObra" 
(
   "idTipoObra"         VARCHAR2(4)          not null,
   "descTipo"           VARCHAR2(30)         not null,
   constraint PK_TIPOOBRA primary key ("idTipoObra")
);

alter table "Convocatoria"
   add constraint FK_CONVOCAT_CONV_OBRA_OBRATEAT foreign key ("idObra")
      references "ObraTeatro" ("idObra");

alter table "Emp_Obra"
   add constraint FK_EMP_OBRA_EMP_OBRA_EMPLEADO foreign key ("idEmpleado")
      references "Empleado" ("idEmpleado");

alter table "Emp_Obra"
   add constraint FK_EMP_OBRA_RELATIONS_PRESENTA foreign key ("idpresentacion")
      references "PresentacionObra" ("idpresentacion");

alter table "Emp_Obra"
   add constraint FK_EMP_OBRA_RELATIONS_ROL foreign key ("idRol")
      references "Rol" ("idRol");

alter table "Escritor"
   add constraint FK_ESCRITOR_PAI_ESCRI_PAIS foreign key ("idPais")
      references "Pais" ("idPais");

alter table "Est_Conv"
   add constraint FK_EST_CONV_EST_CONV_CONVOCAT foreign key ("idconvocatoria")
      references "Convocatoria" ("idconvocatoria");

alter table "Est_Conv"
   add constraint FK_EST_CONV_EST_CONV2_ESTUDIAN foreign key ("identificacion")
      references "Estudiante" ("identificacion");

alter table "Estudiante"
   add constraint FK_ESTUDIAN_ESTU_CARR_CARRERA foreign key ("idCarrera")
      references "Carrera" ("idCarrera");

alter table "Estudiante"
   add constraint FK_ESTUDIAN_TIPOIDEN__TIPOIDEN foreign key ("idTipoIdent")
      references "TipoIdentificacion" ("idTipoIdent");

alter table GP
   add constraint FK_GP_GP_GASTOS foreign key ("idGastos")
      references "Gastos" ("idGastos");

alter table GP
   add constraint FK_GP_GP2_PRESENTA foreign key ("idpresentacion")
      references "PresentacionObra" ("idpresentacion");

alter table "Hora"
   add constraint FK_HORA_PRESE_HOR_PRESENTA foreign key ("idpresentacion")
      references "PresentacionObra" ("idpresentacion");

alter table "ObraTeatro"
   add constraint FK_OBRATEAT_COOR_OBRA_EMPLEADO foreign key ("idCoordinador")
      references "Empleado" ("idEmpleado");

alter table "ObraTeatro"
   add constraint FK_OBRATEAT_DIRE_OBRA_EMPLEADO foreign key ("idDirector")
      references "Empleado" ("idEmpleado");

alter table "ObraTeatro"
   add constraint FK_OBRATEAT_ESCR_OBRA_ESCRITOR foreign key ("idEscritor")
      references "Escritor" ("idEscritor");

alter table "ObraTeatro"
   add constraint FK_OBRATEAT_OBRATE_PA_PAIS foreign key ("idPais")
      references "Pais" ("idPais");

alter table "Personaje"
   add constraint FK_PERSONAJ_RELATIONS_OBRATEAT foreign key ("idObra")
      references "ObraTeatro" ("idObra");

alter table "Personaje"
   add constraint FK_PERSONAJ_RELATIONS_ESTUDIAN foreign key ("estudiantico")
      references "Estudiante" ("identificacion");

alter table "Presen_Dia"
   add constraint FK_PRESEN_D_PRESEN_DI_DIA foreign key ("idDia")
      references "Dia" ("idDia");

alter table "Presen_Dia"
   add constraint FK_PRESEN_D_PRESEN_DI_PRESENTA foreign key ("idpresentacion")
      references "PresentacionObra" ("idpresentacion");

alter table "PresentacionObra"
   add constraint FK_PRESENTA_OBRA_PRES_OBRATEAT foreign key ("idObra")
      references "ObraTeatro" ("idObra");

alter table "PresentacionObra"
   add constraint FK_PRESENTA_PRES_TEA_TEATRO foreign key ("idTeatro")
      references "Teatro" ("idTeatro");

alter table "PresentacionObra"
   add constraint FK_PRESENTA_PRESE_TIP_TIPOPRES foreign key ("idTipP")
      references "TipoPresentacion" ("idTipP");

alter table "TipoO_ObraTea"
   add constraint FK_TIPOO_OB_TIPOO_OBR_OBRATEAT foreign key ("idObra")
      references "ObraTeatro" ("idObra");

alter table "TipoO_ObraTea"
   add constraint FK_TIPOO_OB_TIPOO_OBR_TIPOOBRA foreign key ("idTipoObra")
      references "tipoObra" ("idTipoObra");

