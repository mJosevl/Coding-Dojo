
/* 1) Consulta: crea 3 dojos nuevos */
/* 3) Consulta: crea 3 dojos nuevos */
INSERT INTO dojos( nombre )
VALUES ( 'Chile' ),
	   ( 'USA' ),
       ( 'Mexico ');
       
SELECT *
FROM dojos;

/* 2) Consulta: elimina los 3 dojos que acabas de crear */
DELETE FROM dojos
WHERE id = 1;

DELETE FROM dojos
WHERE id = 2;

DELETE FROM dojos
WHERE id = 3;

/* 4) Consulta: crea 3 ninjas que pertenezcan al primer dojo */
INSERT INTO ninjas( nombre, apellido, edad, id_dojo )
VALUES( 'Alex', 'Miller', 25, 4 ),
	  ( 'Martha', 'Gonzalez', 23, 4 ),
      ( 'Roger', 'Infante', 18, 4 );
      
SELECT *
FROM ninjas;

/* 5) Consulta: crea 3 ninjas que pertenezcan al segundo dojo */
INSERT INTO ninjas( nombre, apellido, edad, id_dojo )
VALUES( 'Miguel', 'Gonzalez', 27, 5 ),
	  ( 'Ana', 'Morales', 23, 5 ),
      ( 'Alan', 'Infante', 19, 5 );
      
SELECT *
FROM ninjas;

/* 6) Consulta: crea 3 ninjas que pertenezcan al tercer dojo */
INSERT INTO ninjas( nombre, apellido, edad, id_dojo )
VALUES( 'Brianna', 'Winston', 24, 6 ),
	  ( 'Julieta', 'Rodriguez', 19, 6 ),
      ( 'Marcela', 'Torres', 29, 6 );
      
SELECT *
FROM ninjas;

/* 7) Consulta: recupera todos los ninjas del primer dojo */
SELECT *
FROM ninjas
WHERE id_dojo = 4;

/* 8) Consulta: recupera todos los ninjas del último dojo */
SELECT *
FROM ninjas
WHERE id_dojo = 6;

/* 9) Consulta: recupera el dojo del último ninja */
SELECT d.nombre AS 'Dojo', n.nombre, n.apellido
FROM ninjas n JOIN dojos d
	ON n.id_dojo = d.id
WHERE n.id = 9;


