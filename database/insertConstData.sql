-- Script para inserção das colunas de dados constantes na base de dados
-- a ser utilizada pelo sistema iSsalto.
-- Utilizacao:
-- $ heroku
-- $ heroku pg:psql --app issalto DATABASE
-- \i <PATH_PARA_ESTE_SCRIPT>
INSERT INTO TipoOcorrencia (Id, Nome) VALUES (0, 'Assalto');
INSERT INTO TipoOcorrencia (Id, Nome) VALUES (1, 'Furto');
INSERT INTO TipoOcorrencia (Id, Nome) VALUES (2, 'Invasao de Propriedade');
INSERT INTO TipoOcorrencia (Id, Nome) VALUES (3, 'Assedio');
INSERT INTO TipoOcorrencia (Id, Nome) VALUES (4, 'Sequestro');
INSERT INTO TipoOcorrencia (Id, Nome) VALUES (5, 'Assassinato');
INSERT INTO TipoOcorrencia (Id, Nome) VALUES (6, 'Roubo de Automóvel');