-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.4.3 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for db_flask_api
DROP DATABASE IF EXISTS `db_flask_api`;
CREATE DATABASE IF NOT EXISTS `db_flask_api` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_flask_api`;

-- Dumping structure for table db_flask_api.book
DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `year` int NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table db_flask_api.book: ~2 rows (approximately)
DELETE FROM `book`;
INSERT INTO `book` (`id`, `title`, `author`, `year`, `description`, `category_id`) VALUES
	(1, 'Negeri 5 Menara', 'Ahmad Fuadi', 2009, 'Negeri 5 Menara merupakan novel yang menceritakan tentang kehidupan 6 santri dari 6 daerah yang berbeda menuntut ilmu di Pondok Madani (PM) Ponorogo Jawa Timur yang jauh dari rumah dan berhasil mewujudkan mimpi menggapai jendela dunia.', 2),
	(2, 'The Pragmatic Programmer: From Journeyman to Master', ' Andrew Hunt', 1999, ' buku tentang pemrograman komputer dan rekayasa perangkat lunak', 3),
	(4, 'The Pragmatic Programmer: From Journeyman to Master', ' Andrew Hunt', 1999, ' buku tentang pemrograman komputer dan rekayasa perangkat lunak', 5),
	(5, 'Pengantar Algoritma', 'Thomas H. Cormen', 1989, 'buku tentang pemrograman komputer', 3);

-- Dumping structure for table db_flask_api.category
DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table db_flask_api.category: ~5 rows (approximately)
DELETE FROM `category`;
INSERT INTO `category` (`id`, `name`) VALUES
	(5, 'Agama'),
	(4, 'Non Fiksi'),
	(2, 'Novel'),
	(3, 'Pemrograman');

-- Dumping structure for table db_flask_api.level
DROP TABLE IF EXISTS `level`;
CREATE TABLE IF NOT EXISTS `level` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table db_flask_api.level: ~2 rows (approximately)
DELETE FROM `level`;
INSERT INTO `level` (`id`, `name`) VALUES
	(1, 'Administrator'),
	(2, 'User');

-- Dumping structure for table db_flask_api.user
DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `status` enum('ACTIVE','INACTIVE') NOT NULL,
  `level_id` int NOT NULL,
  `api_key` text NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  KEY `level_id` (`level_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`level_id`) REFERENCES `level` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping structure for table db_flask_api.borrow
DROP TABLE IF EXISTS `borrow`;
CREATE TABLE IF NOT EXISTS `borrow` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `user_id` int NOT NULL,
  `borrow_date` datetime NOT NULL,
  `return_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `borrow_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table db_flask_api.user: ~4 rows (approximately)
DELETE FROM `user`;
INSERT INTO `user` (`user_id`, `username`, `password`, `full_name`, `status`, `level_id`, `api_key`) VALUES
	(1, 'koprawi', '$2b$12$KVj9jVnCVP0otKCzU5D4bOPeA5RmdbefzmzYz6RY/dQYJO1tvGb1K', 'Muhammad koprawi', 'ACTIVE', 1, ''),
	(2, 'budi', '$2b$12$NThQ7YXR/9kMsYmZ3qRQ8uYtgnhuWrhCOMtctnDS8nBH750vsFaDC', 'Budi Budi', 'ACTIVE', 2, ''),
	(3, 'awang', '$2b$12$Eb9ETazGXgdxLvJ/Y19hd.bUSQDJZ2zaAkcolbmlVOT3TYCQVf1U2', 'Awang', 'ACTIVE', 1, ''),
	(4, 'bima', '$2b$12$86yijYgJKg6ak2nAdolGfuXA5lEwDbJCyBV0O5wsbR3JZy2CEY0TO', 'Bima', 'ACTIVE', 1, 'tuPGv88RQovKwJXst4zZIMwgYxk4P2Ln');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
