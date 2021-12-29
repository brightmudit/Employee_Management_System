-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: employee_database
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `eId` int NOT NULL,
  `eName` varchar(50) NOT NULL DEFAULT 'NULL',
  `eGender` varchar(8) NOT NULL,
  `eAge` int NOT NULL,
  `eSalary` int NOT NULL,
  `eBonus` int NOT NULL,
  `eDepartment` varchar(25) NOT NULL,
  PRIMARY KEY (`eId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (501,'Aman Singh','Male',23,15000,2000,'Cusomer Care'),(502,'Rajeev Jain','Male',45,60000,0,'Production'),(503,'Gautam Motwani','Male',26,15000,2000,'Cusomer Care'),(504,'Kripesh Agarwa','Male',30,15000,2000,'Cusomer Care'),(505,'Shanti Sharma','Female',35,25000,3500,'HR'),(506,'Neha Rathore','Female',21,15000,2000,'Cusomer Care'),(507,'Gaurav Jain','Male',25,15000,2000,'Cusomer Care'),(508,'Amit Berwa','Male',30,25000,3500,'HR'),(509,'Ayushi Dass','Female',29,15000,2000,'Cusomer Care'),(510,'Sumit Devnath','Male',38,35000,5000,'Sales'),(511,'Diya Gupta','Female',22,15000,2000,'Cusomer Care'),(512,'Nidhi Jangid','Female',45,60000,0,'Production'),(513,'Krishna Kumawat','Female',35,35000,5000,'Sales'),(514,'Aryan Khan','Male',27,15000,2000,'Cusomer Care'),(515,'Riya Shekhawat','Female',22,15000,2000,'Cusomer Care'),(516,'Mudit Choudhary','Male',18,400000,0,'SDE2'),(517,'Aditya Bajaj','Male',23,15000,2000,'Cusomer Care'),(518,'Nitin Kumar','Male',28,15000,2000,'Cusomer Care'),(519,'Naman Mathur','Male',30,35000,5000,'Sales'),(521,'Mukul Roy','Male',39,35000,5000,'Sales'),(522,'Mishti Gupta','Female',21,15000,2000,'Cusomer Care'),(523,'Alak Das','Male',38,1000000,10000,'PGT Commerce'),(524,'Akshay Kumar','Male',55,200000,10000,'General Manager'),(530,'Tanmay Singh','Male',35,35000,5000,'Sales');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_attendance`
--

DROP TABLE IF EXISTS `employee_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_attendance` (
  `eid` int NOT NULL,
  `eName` varchar(50) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_attendance`
--

LOCK TABLES `employee_attendance` WRITE;
/*!40000 ALTER TABLE `employee_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_attendance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-29 11:42:34
