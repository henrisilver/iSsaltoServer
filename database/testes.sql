-- Script de testes da base de dados a ser utilizada pelo sistema iSsalto.
-- Utilizacao:
-- $ heroku
-- $ heroku pg:psql --app issalto DATABASE
-- \i <PATH_PARA_ESTE_SCRIPT>
INSERT INTO Usuario VALUES ('Joaozinho', 'fd3409cbae982', 10.2, 1.0, 1.1);
SELECT * FROM Usuario;
INSERT INTO Ocorrencia VALUES(1, 'Joaozinho', 0, '2016-12-29 07:20:14', 98.1, 23.4, 'Malandgragem meu');
SELECT * FROM Ocorrencia;
INSERT INTO Ocorrencia VALUES(1, 'Joaozinho', 0, '2016-12-29 07:20:14', 98.1, 23.4, 'Malandgragem meu'); -- ERRO: PK repetida em Ocorrencia
INSERT INTO Ocorrencia VALUES(2, 'Jonas', 3, '2016-01-17 16:47:33', -34.1, 40.4, 'Coitado do Jonas'); -- Erro: FK Username nao existe
DELETE FROM Ocorrencia WHERE id = 1;
DELETE from Usuario where Username = 'Joaozinho';