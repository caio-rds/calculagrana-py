CREATE TABLE logins (
    id INT AUTO INCREMENT PRIMARY KEY,
    username VARCHAR(20),
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    login_ip VARCHAR(20)
    user_agent VARCHAR(20)
);