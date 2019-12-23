-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: belt_exam
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `likes` (
  `user_id` int(11) NOT NULL,
  `quote_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY `fk_users_has_quotes_quotes1_idx` (`quote_id`),
  KEY `fk_users_has_quotes_users_idx` (`user_id`),
  CONSTRAINT `fk_users_has_quotes_quotes1` FOREIGN KEY (`quote_id`) REFERENCES `quotes` (`id`),
  CONSTRAINT `fk_users_has_quotes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (5,7,'2019-07-26 19:37:19','2019-07-26 19:37:19');
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotes`
--

DROP TABLE IF EXISTS `quotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `author` varchar(255) NOT NULL,
  `content` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_quotes_users1_idx` (`user_id`),
  CONSTRAINT `fk_quotes_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotes`
--

LOCK TABLES `quotes` WRITE;
/*!40000 ALTER TABLE `quotes` DISABLE KEYS */;
INSERT INTO `quotes` VALUES (3,1,'ZooLoo','Plenty sits still, Hunger is a wnderer.','2019-07-26 13:53:14','2019-07-26 13:53:14'),(4,2,'Joseph Conrad','The beliefs in a supernatural source of evil, men alone are quite capable of every wickedness.','2019-07-26 14:03:10','2019-07-26 14:03:10'),(6,5,'Albert Einstein','imagination is more important than knowledge.','2019-07-26 15:17:49','2019-07-26 15:17:49'),(7,5,'Albert Einstein','if you can\'t explain it simply, you don\'t understand it enough.','2019-07-26 15:32:44','2019-07-26 15:32:44');
/*!40000 ALTER TABLE `quotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Daisy','Johnson','skye@gmail.com','$2b$12$pXjerbU1CoSfDv85mbyo1upGPjfpV81aeaMlkU8hgvqkjsm1a0E/m','2019-07-26 19:30:40','2019-07-26 19:30:40'),(2,'Daisy','','','$2b$12$ldMo77l6.2mhPEvGCSfiKubwlDvpgzscJ1TOwosbqXRzXS.QtYfGq','2019-07-26 14:37:47','2019-07-26 14:37:47'),(3,'Leslie ','Knope','parks@gmail.com','$2b$12$7c9vEguSxanv.8m9CHeJQecLpOw5mYe0BvljYvYzibef5q910i5Ge','2019-07-26 14:58:50','2019-07-26 14:58:50'),(4,'sponge','bob','underthesea@gmail.com','$2b$12$VOFxlMn2dlxSuFcetyS5eO0bBsQEvAenDVDFceWkFlnICHn.SM1qa','2019-07-26 12:11:24','2019-07-26 12:11:24'),(5,'Jimmy ','Hoffa','topofbrick@gmail.com','$2b$12$3Jt9WRX3AekHkBgQDSpzUugbQzB1.aLfmBnY127FuXz6cQS6wgTcu','2019-07-26 12:11:52','2019-07-26 12:11:52'),(7,'Neil','Denning','nrdprod8@gmail.com','$2b$12$YoG5NKSZvIZHZZoggjGgqe2iyKvr1C59ikilzC6s7DGV6ZxPEip82','2019-07-26 15:02:36','2019-07-26 15:02:36'),(8,'Devon ','Almarinez','da@gmail.com','$2b$12$b4FqY0/O8m2lgGGh8BRgReuB4uzNjx5kSYE37X1DjtnvlxZs5ImTS','2019-07-26 18:49:47','2019-07-26 18:49:47');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-26 19:48:10
