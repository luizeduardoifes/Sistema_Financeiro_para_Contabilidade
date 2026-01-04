CREATE_TABLE_CONTA = """
CREATE TABLE IF NOT EXISTS Conta (
    codigo TEXT NOT NULL,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    saldo REAL NOT NULL
);
"""

INSERT_CONTA = """
INSERT INTO Conta (codigo, nome, tipo, saldo)
VALUES (?, ?, ?, ?)
"""

UPDATE_CONTA = """
UPDATE Conta 
SET codigo = ?, 
    nome = ?,
    tipo = ?,
    saldo = ?
WHERE codigo = ?;
"""

DELETE_CONTA = """
DELETE FROM Conta 
WHERE codigo = ?;
"""

