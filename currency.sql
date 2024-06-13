-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           8.4.0 - MySQL Community Server - GPL
-- OS do Servidor:               Linux
-- HeidiSQL Versão:              12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para FpiConversion
CREATE DATABASE IF NOT EXISTS `FpiConversion` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `FpiConversion`;

-- Copiando estrutura para tabela FpiConversion.conversions
CREATE TABLE IF NOT EXISTS `conversions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `conversion_id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `base_currency` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `amount` double NOT NULL DEFAULT (0),
  `conversions` json NOT NULL,
  `request_ip` varchar(20) NOT NULL DEFAULT '0',
  `request_date` datetime NOT NULL,
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela FpiConversion.conversions: ~14 rows (aproximadamente)
REPLACE INTO `conversions` (`id`, `conversion_id`, `base_currency`, `amount`, `conversions`, `request_ip`, `request_date`, `username`) VALUES
	(1, '9f2bc46e8c98', 'USD', 100, '{"BRL": {"amount": 513.45, "unit_value": 5.13}, "EUR": {"amount": 91.82, "unit_value": 0.92}}', '127.0.0.1', '2024-05-16 02:39:13', 'caiords'),
	(2, 'ba31ed721f12', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 17.88, "unit_value": 0.18}, "USD": {"amount": 19.48, "unit_value": 0.19}}', '127.0.0.1', '2024-05-16 02:39:13', 'caiords'),
	(3, '3d1659ccb1c6', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.6, "unit_value": 0.2}}', '127.0.0.1', '2024-05-20 05:21:06', 'anonymous'),
	(4, 'a1b3ea43484a', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.6, "unit_value": 0.2}}', '127.0.0.1', '2024-05-20 05:21:06', 'anonymous'),
	(5, 'e5489fa18726', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.6, "unit_value": 0.2}}', '127.0.0.1', '2024-05-20 05:21:06', 'anonymous'),
	(6, '1649a3244886', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}}', '127.0.0.1', '2024-05-21 02:14:55', 'anonymous'),
	(7, '0501997844ed', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}}', '127.0.0.1', '2024-05-21 02:14:55', 'anonymous'),
	(8, '85e962e74eb6', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}}', '127.0.0.1', '2024-05-21 02:14:55', 'anonymous'),
	(9, '18c81c34ab61', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}}', '127.0.0.1', '2024-05-21 02:14:55', 'anonymous'),
	(10, '2bcf171d423d', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}}', '127.0.0.1', '2024-05-21 02:14:55', 'anonymous'),
	(11, '325773e5ecd9e1420b62', 'BRL', 100, '{"EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}, "errors": [{"error": "Currency not found.", "suggest": ["USD", "JPY", "CZK", "DKK", "HUF", "SEK", "CHF", "ISK", "NOK", "AUD", "CAD", "CNY", "HKD", "MXN", "NZD", "PHP", "SGD"], "currency": "BRLL"}]}', '127.0.0.1', '2024-05-21 02:31:23', 'anonymous'),
	(12, '6fae8057c5a3', 'BRL', 100, '{"EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}, "errors": [{"error": "Currency not found.", "suggest": ["EUR", "USD", "JPY", "BGN", "GBP", "HUF", "PLN", "RON", "RUB", "TRY", "AUD", "BRL", "IDR", "ILS", "INR", "MXN", "MYR", "PHP", "SGD", "THB"], "currency": "CZKK"}]}', '127.0.0.1', '2024-05-21 02:31:23', 'anonymous'),
	(13, '5861cbeb4e36', 'BRL', 100, '{"EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}, "errors": [{"error": "Currency not found.", "suggest": "CZK", "currency": "CZKK"}]}', '127.0.0.1', '2024-05-21 02:33:40', 'anonymous'),
	(14, '1a22086c4afd', 'BRL', 100, '{"EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}, "errors": [{"error": "Currency not found.", "suggest": "BRL", "currency": "BRLL"}]}', '127.0.0.1', '2024-05-21 02:33:40', 'anonymous'),
	(15, 'be2601bc9658', 'BRL', 100, '{"EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}, "errors": [{"error": "Currency not found.", "suggest": "BRL", "currency": "BRRELL"}]}', '127.0.0.1', '2024-05-21 02:33:40', 'anonymous'),
	(16, '2db980af3bca', 'BRL', 100, '{"BRL": {"amount": 100.0, "unit_value": 1.0}, "EUR": {"amount": 18.02, "unit_value": 0.18}, "USD": {"amount": 19.57, "unit_value": 0.2}, "errors": []}', '127.0.0.1', '2024-05-21 02:33:40', 'anonymous');

-- Copiando estrutura para tabela FpiConversion.currencies
CREATE TABLE IF NOT EXISTS `currencies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '0',
  `name_plural` varchar(50) NOT NULL DEFAULT '0',
  `code` varchar(6) NOT NULL DEFAULT '0',
  `c_value` float DEFAULT NULL,
  `base_currency` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela FpiConversion.currencies: ~33 rows (aproximadamente)
REPLACE INTO `currencies` (`id`, `name`, `name_plural`, `code`, `c_value`, `base_currency`, `updated_at`) VALUES
	(1, 'Euro', 'Euros', 'EUR', 1, 'EUR', '2024-05-23 20:58:13'),
	(2, 'US Dollar', 'US dollars', 'USD', 1.08268, 'EUR', '2024-05-23 20:58:13'),
	(3, 'Japanese Yen', 'Japanese yen', 'JPY', 169.666, 'EUR', '2024-05-23 20:58:13'),
	(4, 'Bulgarian Lev', 'Bulgarian leva', 'BGN', 1.95242, 'EUR', '2024-05-23 20:58:13'),
	(5, 'Czech Republic Koruna', 'Czech Republic korunas', 'CZK', 24.7023, 'EUR', '2024-05-23 20:58:13'),
	(6, 'Danish Krone', 'Danish kroner', 'DKK', 7.4618, 'EUR', '2024-05-23 20:58:13'),
	(7, 'British Pound Sterling', 'British pounds sterling', 'GBP', 0.851066, 'EUR', '2024-05-23 20:58:13'),
	(8, 'Hungarian Forint', 'Hungarian forints', 'HUF', 386.806, 'EUR', '2024-05-23 20:58:13'),
	(9, 'Polish Zloty', 'Polish zlotys', 'PLN', 4.26631, 'EUR', '2024-05-23 20:58:13'),
	(10, 'Romanian Leu', 'Romanian lei', 'RON', 4.97395, 'EUR', '2024-05-23 20:58:13'),
	(11, 'Swedish Krona', 'Swedish kronor', 'SEK', 11.6191, 'EUR', '2024-05-23 20:58:13'),
	(12, 'Swiss Franc', 'Swiss francs', 'CHF', 0.990689, 'EUR', '2024-05-23 20:58:13'),
	(13, 'Icelandic Króna', 'Icelandic krónur', 'ISK', 150.048, 'EUR', '2024-05-23 20:58:13'),
	(14, 'Norwegian Krone', 'Norwegian kroner', 'NOK', 11.5869, 'EUR', '2024-05-23 20:58:13'),
	(15, 'Croatian Kuna', 'Croatian kunas', 'HRK', 7.20469, 'EUR', '2024-05-23 20:58:13'),
	(16, 'Russian Ruble', 'Russian rubles', 'RUB', 97.6199, 'EUR', '2024-05-23 20:58:13'),
	(17, 'Turkish Lira', 'Turkish Lira', 'TRY', 34.8057, 'EUR', '2024-05-23 20:58:13'),
	(18, 'Australian Dollar', 'Australian dollars', 'AUD', 1.63576, 'EUR', '2024-05-23 20:58:13'),
	(19, 'Brazilian Real', 'Brazilian reals', 'BRL', 5.57862, 'EUR', '2024-05-23 20:58:13'),
	(20, 'Canadian Dollar', 'Canadian dollars', 'CAD', 1.4821, 'EUR', '2024-05-23 20:58:13'),
	(21, 'Chinese Yuan', 'Chinese yuan', 'CNY', 7.83446, 'EUR', '2024-05-23 20:58:13'),
	(22, 'Hong Kong Dollar', 'Hong Kong dollars', 'HKD', 8.4465, 'EUR', '2024-05-23 20:58:13'),
	(23, 'Indonesian Rupiah', 'Indonesian rupiahs', 'IDR', 17288.5, 'EUR', '2024-05-23 20:58:13'),
	(24, 'Israeli New Sheqel', 'Israeli new sheqels', 'ILS', 3.98087, 'EUR', '2024-05-23 20:58:13'),
	(25, 'Indian Rupee', 'Indian rupees', 'INR', 90.1084, 'EUR', '2024-05-23 20:58:13'),
	(26, 'South Korean Won', 'South Korean won', 'KRW', 1474.71, 'EUR', '2024-05-23 20:58:13'),
	(27, 'Mexican Peso', 'Mexican pesos', 'MXN', 18.0309, 'EUR', '2024-05-23 20:58:13'),
	(28, 'Malaysian Ringgit', 'Malaysian ringgits', 'MYR', 5.07783, 'EUR', '2024-05-23 20:58:13'),
	(29, 'New Zealand Dollar', 'New Zealand dollars', 'NZD', 1.77466, 'EUR', '2024-05-23 20:58:13'),
	(30, 'Philippine Peso', 'Philippine pesos', 'PHP', 62.7914, 'EUR', '2024-05-23 20:58:13'),
	(31, 'Singapore Dollar', 'Singapore dollars', 'SGD', 1.46168, 'EUR', '2024-05-23 20:58:13'),
	(32, 'Thai Baht', 'Thai baht', 'THB', 39.5191, 'EUR', '2024-05-23 20:58:13'),
	(33, 'South African Rand', 'South African rand', 'ZAR', 19.7998, 'EUR', '2024-05-23 20:58:13');

-- Copiando estrutura para tabela FpiConversion.logins
CREATE TABLE IF NOT EXISTS `logins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `logged_at` datetime NOT NULL,
  `login_ip` varchar(20) NOT NULL DEFAULT '0',
  `user_agent` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela FpiConversion.logins: ~5 rows (aproximadamente)
REPLACE INTO `logins` (`id`, `username`, `logged_at`, `login_ip`, `user_agent`) VALUES
	(7, 'caiords', '2024-05-15 04:57:56', '127.0.0.1', 'insomnia/9.1.0'),
	(8, 'caiords', '2024-05-15 17:54:06', '127.0.0.1', 'insomnia/9.1.0'),
	(9, 'caiords', '2024-05-15 18:09:02', '127.0.0.1', 'insomnia/9.1.0'),
	(10, 'caiords', '2024-05-16 02:25:33', '127.0.0.1', 'insomnia/9.1.0'),
	(11, 'caiords', '2024-05-16 02:28:41', '127.0.0.1', 'insomnia/9.1.0'),
	(12, 'caiords', '2024-05-16 02:46:02', '127.0.0.1', 'insomnia/9.1.0');

-- Copiando estrutura para tabela FpiConversion.recovery
CREATE TABLE IF NOT EXISTS `recovery` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0',
  `code` varchar(6) NOT NULL,
  `way` varchar(5) NOT NULL,
  `send_to` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `request_ip` varchar(20) NOT NULL,
  `request_date` datetime NOT NULL,
  `used` tinyint(1) NOT NULL,
  `used_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `code` (`code`),
  KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela FpiConversion.recovery: ~1 rows (aproximadamente)
REPLACE INTO `recovery` (`id`, `username`, `code`, `way`, `send_to`, `request_ip`, `request_date`, `used`, `used_date`) VALUES
	(11, 'caiords', '079767', 'email', 'billiechannel1@gmail.com', '127.0.0.1', '2024-05-21 04:25:15', 0, NULL);

-- Copiando estrutura para tabela FpiConversion.users
CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(30) NOT NULL DEFAULT '',
  `password` tinytext NOT NULL,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `full_name` varchar(70) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `phone_number` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `token` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela FpiConversion.users: ~1 rows (aproximadamente)
REPLACE INTO `users` (`username`, `password`, `email`, `full_name`, `phone_number`, `created_at`, `updated_at`, `token`) VALUES
	('caiords', '$2b$12$b0MJ4FZ5MXVOV9f5XKCQ6OySfrGdYBGxhk9FA2R4OEzX9JsPsjwT.', 'billiechannel1@gmail.com', 'Caio Reis dos Santos de Cresci', '(21) 99660-6109', '2024-05-19 22:44:23', '2024-05-19 22:44:23', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
