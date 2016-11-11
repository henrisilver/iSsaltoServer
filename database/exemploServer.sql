-- Script de testes da base de dados a ser utilizada pelo sistema iSsalto.
-- Utilizacao:
-- $ heroku
-- $ heroku pg:psql --app issalto DATABASE
-- \i <PATH_PARA_ESTE_SCRIPT>
DELETE FROM Ocorrencia;
DELETE from Usuario;
INSERT INTO Usuario VALUES ('Cassio', 'fd3409cbae982', 100000000.0, -22.0060879521827, -47.8954013809562);
INSERT INTO Usuario VALUES ('Fagner', 'abcdef1234567', 20.0, 30.0, 30.0);
INSERT INTO Usuario VALUES ('Walter', '7654321fedbca', 5.5, 87.0, 42.0);
INSERT INTO Usuario VALUES ('Guilherme', 'a1b2c3d4e5f67', 1.0, 40.0, 5.0);
INSERT INTO Ocorrencia (Username, Tipo, OcorrenciaTimestamp, LocalizacaoX, LocalizacaoY, Descricao) VALUES ('Fagner', 0, '2016-12-29 07:20:14', 15.0, 25.0, 'Malandgragem meu... Roubaram meu celular');
INSERT INTO Ocorrencia (Username, Tipo, OcorrenciaTimestamp, LocalizacaoX, LocalizacaoY, Descricao) VALUES('Walter', 1, '2016-12-29 07:20:14', 98.1, 23.4, 'Furtaram meu PokemonGO :('); -- ERRO: PK repetida em Ocorrencia
INSERT INTO Ocorrencia (Username, Tipo, OcorrenciaTimestamp, LocalizacaoX, LocalizacaoY, Descricao) VALUES('Guilherme', 2, '2016-01-17 16:47:33', 20.0, 20.0, 'Invadiu a area, eu defendo!'); -- Erro: FK Username nao existe