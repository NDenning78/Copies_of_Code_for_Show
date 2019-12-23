-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: dojo_tweets_2
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
-- Table structure for table `followed_users`
--

DROP TABLE IF EXISTS `followed_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `followed_users` (
  `user_following` int(11) NOT NULL,
  `user_being_followed` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY `fk_users_has_users_users2_idx` (`user_being_followed`),
  KEY `fk_users_has_users_users1_idx` (`user_following`),
  CONSTRAINT `fk_users_has_users_users1` FOREIGN KEY (`user_following`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_users_has_users_users2` FOREIGN KEY (`user_being_followed`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `followed_users`
--

LOCK TABLES `followed_users` WRITE;
/*!40000 ALTER TABLE `followed_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `followed_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `liked_tweets`
--

DROP TABLE IF EXISTS `liked_tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `liked_tweets` (
  `user_id` int(11) NOT NULL,
  `tweet_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY `fk_users_has_tweets_tweets1_idx` (`tweet_id`),
  KEY `fk_users_has_tweets_users1_idx` (`user_id`),
  CONSTRAINT `fk_users_has_tweets_tweets1` FOREIGN KEY (`tweet_id`) REFERENCES `tweets` (`id`),
  CONSTRAINT `fk_users_has_tweets_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `liked_tweets`
--

LOCK TABLES `liked_tweets` WRITE;
/*!40000 ALTER TABLE `liked_tweets` DISABLE KEYS */;
INSERT INTO `liked_tweets` VALUES (10,12,'2019-07-17 23:34:25','2019-07-17 23:34:25'),(10,13,'2019-07-17 23:36:18','2019-07-17 23:36:18'),(10,11,'2019-07-17 23:36:51','2019-07-17 23:36:51'),(10,10,'2019-07-17 23:36:57','2019-07-17 23:36:57'),(10,9,'2019-07-17 23:37:05','2019-07-17 23:37:05'),(10,8,'2019-07-17 23:37:15','2019-07-17 23:37:15'),(10,14,'2019-07-18 13:15:23','2019-07-18 13:15:23'),(10,16,'2019-07-18 14:04:08','2019-07-18 14:04:08'),(10,17,'2019-07-18 14:22:59','2019-07-18 14:22:59'),(11,18,'2019-07-18 15:46:55','2019-07-18 15:46:55'),(11,19,'2019-07-18 15:56:58','2019-07-18 15:56:58'),(12,20,'2019-07-19 18:40:00','2019-07-19 18:40:00'),(12,19,'2019-07-19 18:40:02','2019-07-19 18:40:02'),(11,21,'2019-07-19 18:43:25','2019-07-19 18:43:25');
/*!40000 ALTER TABLE `liked_tweets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweets`
--

DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tweets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `content` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_tweets_users_idx` (`user_id`),
  CONSTRAINT `fk_tweets_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets`
--

LOCK TABLES `tweets` WRITE;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
INSERT INTO `tweets` VALUES (7,10,'let\'s begin','2019-07-17 23:12:15','2019-07-17 23:12:15'),(8,10,'Understanding flask and mysql is taking some time..more than expected.','2019-07-17 23:13:14','2019-07-17 23:13:14'),(9,10,'go team !','2019-07-17 23:13:22','2019-07-17 23:13:22'),(10,10,'styling helps me understand each element better.','2019-07-17 23:27:45','2019-07-17 23:27:45'),(11,10,'still going-you can get it!','2019-07-17 23:30:46','2019-07-17 23:30:46'),(12,10,'testing123','2019-07-17 23:34:22','2019-07-17 23:34:22'),(13,10,'let\'s begin','2019-07-17 23:35:04','2019-07-17 23:35:04'),(14,10,'let\'s begin','2019-07-17 23:36:13','2019-07-17 23:36:13'),(15,10,'day two still working..fingers crossed.','2019-07-18 13:14:08','2019-07-18 13:14:08'),(16,10,'what up Devon!','2019-07-18 14:04:05','2019-07-18 14:04:05'),(17,10,'dojo tweets is almost fully functional..create, read, edit, update, and delete all work now..just need to get the followers and follow link up.','2019-07-18 14:17:46','2019-07-18 14:17:46'),(18,10,'let\'s begin','2019-07-18 14:55:27','2019-07-18 14:55:27'),(19,11,'Understanding flask and mysql is taking some time..more than expected.','2019-07-18 15:56:50','2019-07-18 15:56:50'),(20,12,'go coding dojo!','2019-07-19 18:39:58','2019-07-19 18:39:58'),(21,11,'finally! edit, delete, like, unlike all work!! followers are next! don\'t break it!! thanks ;)','2019-07-19 18:43:18','2019-07-19 18:43:18');
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (5,'Daisy','Johnson','skye@gmail.com','$2b$12$ljacUEvGq2KZ5HRlACLbeuJ3PjV8iXDWety537TVBbOfb18VCfGN2','2019-07-17 22:51:28','2019-07-17 22:51:28'),(10,'Neil','Denning','nrdprod8@gmail.com','$2b$12$UbpghC78EAL9Lj3dgBFyiOceAkaH6nTbcrAAMlnPIFgUrINAeXy8K','2019-07-17 23:08:41','2019-07-17 23:08:41'),(11,'Leslie ','Knope','parks@gmail.com','$2b$12$qgeiHDfBQnk4IhAvD6FSte32Xi6crbq8jIHOwajJIR5KJcZslhd1u','2019-07-18 15:45:53','2019-07-18 15:45:53'),(12,'Tom ','Brady','pats@gmail.com','$2b$12$iX7xv/nTaJhjYTVVij050.cGkiV6Fa5TU5E0mB.jquaeENkb1xu2G','2019-07-19 18:36:29','2019-07-19 18:36:29');
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

-- Dump completed on 2019-07-19 18:46:20
