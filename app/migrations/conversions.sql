CREATE IF NOT EXISTS TABLE conversions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    conversion_id VARCHAR(30),
    base_currency VARCHAR(3),
    amount DOUBLE,
    conversions JSON,
    request_ip VARCHAR(20),
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    username varchar(50)
);