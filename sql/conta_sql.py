CREATE_TABLE_CONTA = """
CREATE TABLE IF NOT EXISTS Conta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL UNIQUE,
    tipo TEXT NOT NULL,
    saldo REAL NOT NULL,
    descricao TEXT NOT NULL,
    ativa BOOLEAN NOT NULL
);
"""

INSERT_CONTA = """
INSERT INTO Conta (codigo, nome, tipo, saldo, descricao, ativa)
VALUES (?, ?, ?, ?, ?, ?)
"""

UPDATE_CONTA = """
UPDATE Conta 
SET id = ?,
    codigo = ?, 
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

CHECAGEM_CONTA = """
SELECT * FROM Conta 
WHERE codigo = ? OR nome = ?
"""