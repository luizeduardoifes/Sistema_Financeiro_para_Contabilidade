CREATE_TABLE_CONTA = """
CREATE TABLE IF NOT EXISTS Conta (
    codigo TEXT NOT NULL,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    saldo REAL NOT NULL,
    descricao TEXT NOT NULL,
    ativa BOOLEAN DEFAULT NULL
);
"""

INSERT_CONTA = """
INSERT INTO Conta (codigo, nome, tipo, saldo, descricao, ativa)
VALUES (?, ?, ?, ?, ?, ?)
"""

UPDATE_CONTA = """
UPDATE Conta 
SET codigo = ?, 
    nome = ?,
    tipo = ?,
    saldo = ?,
    descricao = ?,
    ativa = ?
WHERE codigo = ?;
"""

DELETE_CONTA = """
DELETE FROM Conta 
WHERE codigo = ?;
"""

