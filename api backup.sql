-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_details`
--

DROP TABLE IF EXISTS `account_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_details` (
  `account_id` int NOT NULL,
  `service_type` varchar(45) NOT NULL,
  `customer_id_fk` int NOT NULL,
  PRIMARY KEY (`account_id`),
  KEY `fk_ACCOUNT_DETAILS_CUSTOMER1_idx` (`customer_id_fk`),
  CONSTRAINT `fk_ACCOUNT_DETAILS_CUSTOMER1` FOREIGN KEY (`customer_id_fk`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_details`
--

LOCK TABLES `account_details` WRITE;
/*!40000 ALTER TABLE `account_details` DISABLE KEYS */;
INSERT INTO `account_details` VALUES (101,'Electricity',30),(102,'Internet',31),(103,'Internet',32),(104,'Electricity',33),(105,'Electricity',34),(106,'Electricity',35),(107,'Electricity',36),(108,'Electricity',37),(109,'Internet',38),(110,'Internet',39),(111,'Electricity',40),(112,'Electricity',41),(113,'Electricity',42),(114,'Electricity',42),(115,'Internet',43),(116,'Internet',44),(117,'Electricity',45),(118,'Electricity',46),(119,'Electricity',47),(120,'Electricity',48),(121,'Internet',49),(122,'Internet',50),(123,'Electricity',51),(124,'Electricity',52),(125,'Electricity',53),(126,'Electricity',54),(127,'Internet',55),(128,'Internet',56),(129,'Electricity',57);
/*!40000 ALTER TABLE `account_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `contact_number` bigint NOT NULL,
  `customer_address` varchar(100) NOT NULL,
  `network_id_fk` int NOT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `fk_CUSTOMER_NETWORK_INFRASTRUCTURE_idx` (`network_id_fk`),
  CONSTRAINT `fk_CUSTOMER_NETWORK_INFRASTRUCTURE` FOREIGN KEY (`network_id_fk`) REFERENCES `network_infrastructure` (`network_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (30,'John','Doe',9171234567,'Milagrosa',18),(31,'Jane','Smith',9181234567,'Manalo Extension',18),(32,'Robert','Johnson',9191234567,'San Rafael',1),(33,'Michael','Williams',9201234567,'Tanabag',1),(34,'William','Brown',9211234567,'Santa Cruz',2),(35,'David','Jones',9221234567,'Santa Lourdez',2),(36,'Caesar','Ven',917756658,'Manalo Extension',18),(37,'Charles','Miller',9241234567,'Marufinas',4),(38,'Joseph','Davis',9251234567,'Maoyon',5),(39,'Thomas','Martinez',9261234567,'Tanabag',6),(40,'Christopher','Hernandez',9271234567,'Langogan Subdivision',7),(41,'Daniel','Lopez',9281234567,'Inagawan Town',8),(42,'Matthew','Gonzalez',9291234567,'Irawan Village',9),(43,'Anthony','Wilson',9301234567,'Kalipay Bay',10),(44,'Mark','Anderson',9311234567,'Kamuning Extension',11),(45,'Donald','Thomas',9321234567,'Langogan Town',12),(46,'Steven','Taylor',9331234567,'Lucbuan Avenue',13),(47,'Paul','Moore',9341234567,'Luzviminda Village',14),(48,'Andrew','Jackson',9351234567,'Macarascas Island',15),(49,'Joshua','Martin',9361234567,'Magkakaibigan City',16),(50,'Kenneth','Lee',9371234567,'Maligaya Court',17),(51,'Kevin','Perez',9381234567,'Manggahan Forest',19),(52,'Brian','Thompson',9391234567,'Sicsican Ville',20),(53,'George','White',9401234567,'Tagburos Street',21),(54,'Edward','Harris',9411234567,'Tiniguiban Heights',22),(55,'Ronald','Sanchez',9421234567,'Salvacion Inn',23),(56,'Timothy','Clark',9431234567,'Milagrosa Villas',18),(57,'Jason','Ramirez',9441234567,'Guni Guni',18);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_infrastructure`
--

DROP TABLE IF EXISTS `network_infrastructure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_infrastructure` (
  `network_id` int NOT NULL,
  `grid_location` varchar(75) NOT NULL,
  `grid_name` varchar(75) NOT NULL,
  PRIMARY KEY (`network_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_infrastructure`
--

LOCK TABLES `network_infrastructure` WRITE;
/*!40000 ALTER TABLE `network_infrastructure` DISABLE KEYS */;
INSERT INTO `network_infrastructure` VALUES (1,'Babuyan','Babuyan Recloser'),(2,'Bacungan','Bacungan Recloser'),(3,'Bahile','Bahile Recloser'),(4,'Binduyan','Binduyan Recloser'),(5,'Buenavista','Buenavista Recloser'),(6,'Cabayugan','Cabayugan Recloser'),(7,'Concepcion','Concepcion Recloser'),(8,'Inagawan','Inagawan Recloser'),(9,'Irawan','Irawan Recloser'),(10,'Kalipay','Kalipay Recloser'),(11,'Kamuning','Kamuning Recloser'),(12,'Langogan','Langogan Recloser'),(13,'Lucbuan','Lucbuan Recloser'),(14,'Luzviminda','Luzviminda Recloser'),(15,'Macarascas','Macarascas Recloser'),(16,'Magkakaibigan','Magkakaibigan Recloser'),(17,'Maligaya','Maligaya Recloser'),(18,'Manalo','Manalo Recloser'),(19,'Manggahan','Manggahan Recloser'),(20,'Sicsican','Sicsican Recloser'),(21,'Tagburos','Tagburos Recloser'),(22,'Tiniguiban','Tiniguiban Recloser'),(23,'Salvacion','Salvacion Recloser');
/*!40000 ALTER TABLE `network_infrastructure` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-26 19:17:58
