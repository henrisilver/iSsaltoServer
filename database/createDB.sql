-- Script para criação da base de dados a ser utilizada pelo sistema iSsalto.
-- Utilizacao:
-- $ heroku
-- $ heroku pg:psql --app issalto DATABASE
-- \i <PATH_PARA_ESTE_SCRIPT>
DROP TABLE IF EXISTS TipoOcorrencia, Usuario, Ocorrencia CASCADE;

CREATE TABLE TipoOcorrencia( -- Tabela que modela um tipo de ocorrencia
	Id integer NOT NULL PRIMARY KEY, -- Identificador do tipo de ocorrencia
	Nome varchar(45) NOT NULL -- Descricao textual (nome) do tipo de ocorrencia
);

CREATE TABLE Usuario( -- Tabela que modela um usuario do sistema
	Username varchar(45) NOT NULL PRIMARY KEY, -- Username do usuario
	Hash varchar(45) NOT NULL, -- hash criada pela API do facebook para autenticacao
	RaioDeBusca double precision NOT NULL, -- raio a partir do ponto de interesse do usurario para busca de ocorrencias
	PosX double precision NOT NULL, -- longitude do ponto de interesse do usuario
	PosY double precision NOT NULL -- latitude do ponto de interesse do usuario
);

CREATE TABLE Ocorrencia( -- Tabela que modela uma ocorrencia registrada
	Id serial NOT NULL PRIMARY KEY, -- Identificador da Ocorrencia
	Username varchar(45) NOT NULL REFERENCES Usuario(Username), -- Username que registrou a ocorrencia
	Tipo integer NOT NULL REFERENCES TipoOcorrencia(Id), -- Tipo da ocorrencia em questao
	OcorrenciaTimestamp timestamp NOT NULL, -- Timestamp da ocorrencia
	LocalizacaoX double precision NOT NULL, -- Longitude da ocorrencia
	LocalizacaoY double precision NOT NULL, -- Latitude da ocorrencia
	Descricao varchar(450) -- Descricao opcional da ocorrencia
);