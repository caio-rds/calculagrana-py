CREATE TABLE currencies (
    id INT AUTO INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(3) NOT NULL,
    symbol VARCHAR(5) NOT NULL,
    c_value FLOAT,
    base_currency VARCHAR(6),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);