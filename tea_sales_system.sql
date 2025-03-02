-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: tea_sales_system
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add order',8,'add_order'),(30,'Can change order',8,'change_order'),(31,'Can delete order',8,'delete_order'),(32,'Can view order',8,'view_order'),(33,'Can add order item',9,'add_orderitem'),(34,'Can change order item',9,'change_orderitem'),(35,'Can delete order item',9,'delete_orderitem'),(36,'Can view order item',9,'view_orderitem'),(37,'Can add evaluation',10,'add_evaluation'),(38,'Can change evaluation',10,'change_evaluation'),(39,'Can delete evaluation',10,'delete_evaluation'),(40,'Can view evaluation',10,'view_evaluation'),(41,'Can add address',11,'add_address'),(42,'Can change address',11,'change_address'),(43,'Can delete address',11,'delete_address'),(44,'Can view address',11,'view_address'),(45,'Can add category',12,'add_category'),(46,'Can change category',12,'change_category'),(47,'Can delete category',12,'delete_category'),(48,'Can view category',12,'view_category'),(49,'Can add product',13,'add_product'),(50,'Can change product',13,'change_product'),(51,'Can delete product',13,'delete_product'),(52,'Can view product',13,'view_product'),(53,'Can add 茶叶产地',14,'add_origin'),(54,'Can change 茶叶产地',14,'change_origin'),(55,'Can delete 茶叶产地',14,'delete_origin'),(56,'Can view 茶叶产地',14,'view_origin'),(57,'Can add promotion',15,'add_promotion'),(58,'Can change promotion',15,'change_promotion'),(59,'Can delete promotion',15,'delete_promotion'),(60,'Can view promotion',15,'view_promotion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_management_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_management_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_management_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-11-05 13:38:44.260681','1','绿茶',1,'[{\"added\": {}}]',12,2),(2,'2024-11-05 13:39:02.339346','2','龙井',1,'[{\"added\": {}}]',12,2),(3,'2024-11-05 13:39:48.102053','3','碧螺春',1,'[{\"added\": {}}]',12,2),(4,'2024-11-05 13:40:06.585814','4','白茶',1,'[{\"added\": {}}]',12,2),(5,'2024-11-05 13:40:17.975887','5','白毫银针',1,'[{\"added\": {}}]',12,2),(6,'2024-11-05 13:40:29.305894','6','白牡丹',1,'[{\"added\": {}}]',12,2),(7,'2024-11-05 13:40:55.708093','7','黄茶',1,'[{\"added\": {}}]',12,2),(8,'2024-11-05 13:41:05.009603','8','君山银针',1,'[{\"added\": {}}]',12,2),(9,'2024-11-05 13:41:13.506310','9','蒙顶黄芽',1,'[{\"added\": {}}]',12,2),(10,'2024-11-05 13:41:30.458177','10','乌龙茶',1,'[{\"added\": {}}]',12,2),(11,'2024-11-05 13:42:25.106910','11','铁观音',1,'[{\"added\": {}}]',12,2),(12,'2024-11-05 13:42:34.672858','12','大红袍',1,'[{\"added\": {}}]',12,2),(13,'2024-11-05 13:42:58.875102','13','红茶',1,'[{\"added\": {}}]',12,2),(14,'2024-11-05 13:43:15.927405','14','正山小种',1,'[{\"added\": {}}]',12,2),(15,'2024-11-05 13:43:22.449076','15','金骏眉',1,'[{\"added\": {}}]',12,2),(16,'2024-11-05 13:43:32.981771','16','祁门红茶',1,'[{\"added\": {}}]',12,2),(17,'2024-11-05 13:44:14.313425','17','黑茶',1,'[{\"added\": {}}]',12,2),(18,'2024-11-05 13:44:22.782327','18','普洱茶',1,'[{\"added\": {}}]',12,2),(19,'2024-11-05 13:44:30.238706','19','六堡茶',1,'[{\"added\": {}}]',12,2),(20,'2024-11-05 13:47:06.442942','20','花茶',1,'[{\"added\": {}}]',12,2),(21,'2024-11-05 13:47:25.833169','21','茉莉花茶',1,'[{\"added\": {}}]',12,2),(22,'2024-11-05 13:47:37.198775','22','菊花茶',1,'[{\"added\": {}}]',12,2),(23,'2024-11-05 13:57:48.303740','1','浙江 (中国)',1,'[{\"added\": {}}]',14,2),(24,'2024-11-05 13:57:58.701675','2','安徽 (中国)',1,'[{\"added\": {}}]',14,2),(25,'2024-11-05 13:58:07.597600','3','江西 (中国)',1,'[{\"added\": {}}]',14,2),(26,'2024-11-05 13:58:14.186621','4','湖南 (中国)',1,'[{\"added\": {}}]',14,2),(27,'2024-11-05 13:58:21.654332','5','广西 (中国)',1,'[{\"added\": {}}]',14,2),(28,'2024-11-05 13:58:27.568324','6','陕西 (中国)',1,'[{\"added\": {}}]',14,2),(29,'2024-11-05 13:58:33.834818','7','江苏 (中国)',1,'[{\"added\": {}}]',14,2),(30,'2024-11-05 13:58:42.934849','8','福建 (中国)',1,'[{\"added\": {}}]',14,2),(31,'2024-11-05 13:58:48.886387','9','湖北 (中国)',1,'[{\"added\": {}}]',14,2),(32,'2024-11-05 13:58:54.705841','10','贵州 (中国)',1,'[{\"added\": {}}]',14,2),(33,'2024-11-05 13:59:01.544905','11','山东 (中国)',1,'[{\"added\": {}}]',14,2),(34,'2024-11-05 13:59:09.397205','12','河南 (中国)',1,'[{\"added\": {}}]',14,2),(35,'2024-11-05 13:59:17.402589','13','云南 (中国)',1,'[{\"added\": {}}]',14,2),(36,'2024-11-05 13:59:23.398824','14','四川 (中国)',1,'[{\"added\": {}}]',14,2),(37,'2024-11-05 13:59:45.297164','15','重庆 (中国)',1,'[{\"added\": {}}]',14,2),(38,'2024-11-05 13:59:56.913702','16','广东 (中国)',1,'[{\"added\": {}}]',14,2),(39,'2024-11-05 14:00:03.837812','17','台湾 (中国)',1,'[{\"added\": {}}]',14,2),(40,'2024-11-16 14:20:17.658463','1','8折',1,'[{\"added\": {}}]',15,2),(41,'2024-11-16 14:21:01.840376','2','满300减50',1,'[{\"added\": {}}]',15,2),(42,'2024-11-16 14:21:45.057683','3','满10赠1',1,'[{\"added\": {}}]',15,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'order_management','evaluation'),(8,'order_management','order'),(9,'order_management','orderitem'),(12,'product_management','category'),(14,'product_management','origin'),(13,'product_management','product'),(15,'product_management','promotion'),(6,'sessions','session'),(11,'user_management','address'),(7,'user_management','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-27 14:40:21.338110'),(2,'auth','0001_initial','2024-10-27 14:40:22.742595'),(6,'contenttypes','0002_remove_content_type_name','2024-10-27 14:40:23.332438'),(7,'auth','0002_alter_permission_name_max_length','2024-10-27 14:40:23.503277'),(8,'auth','0003_alter_user_email_max_length','2024-10-27 14:40:23.540508'),(9,'auth','0004_alter_user_username_opts','2024-10-27 14:40:23.555673'),(10,'auth','0005_alter_user_last_login_null','2024-10-27 14:40:23.672430'),(11,'auth','0006_require_contenttypes_0002','2024-10-27 14:40:23.681742'),(12,'auth','0007_alter_validators_add_error_messages','2024-10-27 14:40:23.700403'),(13,'auth','0008_alter_user_username_max_length','2024-10-27 14:40:23.851874'),(14,'auth','0009_alter_user_last_name_max_length','2024-10-27 14:40:23.990865'),(15,'auth','0010_alter_group_name_max_length','2024-10-27 14:40:24.026773'),(16,'auth','0011_update_proxy_permissions','2024-10-27 14:40:24.043068'),(17,'auth','0012_alter_user_first_name_max_length','2024-10-27 14:40:24.187878'),(18,'sessions','0001_initial','2024-10-27 14:40:24.276239'),(21,'product_management','0001_initial','2024-10-30 01:01:45.914021'),(24,'user_management','0001_initial','2024-11-03 08:58:26.076620'),(25,'admin','0001_initial','2024-11-03 08:58:26.392147'),(26,'admin','0002_logentry_remove_auto_add','2024-11-03 08:58:26.405185'),(27,'admin','0003_logentry_add_action_flag_choices','2024-11-03 08:58:26.422843'),(28,'user_management','0002_auto_20241030_0901','2024-11-03 08:58:26.711031'),(29,'order_management','0001_initial','2024-11-03 08:58:28.035723'),(30,'user_management','0003_auto_20241030_2105','2024-11-03 08:58:28.158308'),(31,'user_management','0004_auto_20241103_1658','2024-11-03 08:58:28.388964'),(32,'product_management','0002_auto_20241105_2108','2024-11-05 13:08:38.120216'),(33,'user_management','0005_remove_user_status','2024-11-05 13:08:38.202288'),(34,'user_management','0006_auto_20241105_2115','2024-11-05 13:16:05.014932'),(35,'user_management','0007_auto_20241105_2133','2024-11-05 13:36:22.014599'),(36,'product_management','0003_origin','2024-11-05 13:56:03.254825'),(37,'product_management','0004_product_origin','2024-11-05 14:04:13.052016'),(38,'order_management','0002_auto_20241112_2222','2024-11-12 14:23:01.941286'),(39,'product_management','0005_alter_product_stock','2024-11-12 14:23:01.958749'),(40,'order_management','0003_alter_order_status','2024-11-12 14:26:23.312357'),(41,'order_management','0004_alter_order_status','2024-11-13 13:12:24.932866'),(42,'product_management','0006_auto_20241116_2212','2024-11-16 14:12:48.067807'),(43,'order_management','0005_remove_order_total_price','2024-11-16 15:44:08.866412'),(44,'product_management','0007_auto_20241116_2344','2024-11-16 15:44:10.031088'),(45,'order_management','0006_auto_20241117_1727','2024-11-17 09:27:27.141949'),(46,'order_management','0007_order_total_price','2024-11-17 09:36:06.577645'),(47,'order_management','0008_alter_evaluation_unique_together','2024-11-18 13:12:50.669150'),(48,'order_management','0009_auto_20241121_2132','2024-11-21 13:32:53.756011');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('672bdj17ubzi8hppja5cbzkv0zlz1l98','e30:1t7W0I:zolGFT4Zi5JbAsRs1IPYbGajGyLG3wdpI0iGl56Th-0','2024-11-17 08:30:34.116731'),('7vqyw09xh7qli91swoa8j5k8bladgj56','.eJxVjskOwiAURf-FtWmYZOjO-iHkAQ8xhpoUWDX9d1vThS7vcG7uShz0ll2vuLhnJCNh5PLreQgvnI_gKwvM8MCCcxvOpA73Xtu73HZkOst_Cxlq3nHtgwjGwzVJBjGaqI0FRE8tGi4S5UogAmVWWakURZ60TlxRxQVIEY5bAZZGxnXbPr9IPAU:1tFYrp:jepELrYNV5z7BM0dSMJigmBztXzdm_obehCTI55LMzs','2024-12-09 13:11:05.456849'),('dfu8bvh3rtbsp74tbp8a08nxmodcj1m2','.eJxVjEsOAiEQRO_C2kz42YA79SCkgUaMAROBlfHujmYWuqx69erJPM5R_Oz08NfEDkyw3W8XMN6ofcA3Vmx4oUptLBvpy3n2ca_HVTlt47-Hgr2suglRRRtwn7XAlGwy1iFR4I6sVJlLUETIhQOnATjJbEyWwEEq1CoK9noDeUQ4uQ:1tSuQf:9IgH5F-S3nr1qz0oJyQZ0ONx09CkE24TDHPxUOyn_C0','2025-01-15 08:50:13.112038'),('ew5y1e5jszlyihczd92fa4jg7c2ymi2f','e30:1t7XBa:OA9VH5CNHSGmWn970tHvTp1sczWK2pYGhzVPN4LKYiQ','2024-11-17 09:46:18.531457'),('hs3lg4t1z1j2frrpuyo8kaznghzgrvtt','e30:1t7W0M:bkJK7s0XgH1jZnLBXTJsiaFz0k3VZ6AQfhTl8v0Xras','2024-11-17 08:30:38.326312');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_management_evaluation`
--

DROP TABLE IF EXISTS `order_management_evaluation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_management_evaluation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `score` double NOT NULL,
  `comments` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `evaluate_time` datetime(6) DEFAULT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_management_eva_order_id_7827f631_fk_order_man` (`order_id`),
  KEY `order_management_eva_product_id_a7ed33b4_fk_product_m` (`product_id`),
  KEY `order_management_evaluation_user_id_34c87f21` (`user_id`),
  CONSTRAINT `order_management_eva_order_id_7827f631_fk_order_man` FOREIGN KEY (`order_id`) REFERENCES `order_management_order` (`id`),
  CONSTRAINT `order_management_eva_product_id_a7ed33b4_fk_product_m` FOREIGN KEY (`product_id`) REFERENCES `product_management_product` (`id`),
  CONSTRAINT `order_management_eva_user_id_34c87f21_fk_user_mana` FOREIGN KEY (`user_id`) REFERENCES `user_management_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_management_evaluation`
--

LOCK TABLES `order_management_evaluation` WRITE;
/*!40000 ALTER TABLE `order_management_evaluation` DISABLE KEYS */;
INSERT INTO `order_management_evaluation` VALUES (1,4,'还可以吧','2024-11-18 13:10:45.577492',18,2,1),(3,3,'一般般','2024-11-18 13:12:58.063304',16,2,1),(4,5,'好','2024-11-25 08:40:52.640937',9,2,1);
/*!40000 ALTER TABLE `order_management_evaluation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_management_order`
--

DROP TABLE IF EXISTS `order_management_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_management_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address_id` bigint DEFAULT NULL,
  `user_id` bigint NOT NULL,
  `after_sale_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `discount` decimal(10,2) NOT NULL,
  `final_price` decimal(10,2) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `payment_method` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `payment_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_management_ord_address_id_a60d5925_fk_user_mana` (`address_id`),
  KEY `order_management_ord_user_id_6631c928_fk_user_mana` (`user_id`),
  CONSTRAINT `order_management_ord_address_id_a60d5925_fk_user_mana` FOREIGN KEY (`address_id`) REFERENCES `user_management_address` (`id`),
  CONSTRAINT `order_management_ord_user_id_6631c928_fk_user_mana` FOREIGN KEY (`user_id`) REFERENCES `user_management_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_management_order`
--

LOCK TABLES `order_management_order` WRITE;
/*!40000 ALTER TABLE `order_management_order` DISABLE KEYS */;
INSERT INTO `order_management_order` VALUES (1,'2024-11-10 13:44:30.754703','2024-11-13 12:52:05.126729','completed',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(2,'2024-11-10 13:45:33.641741','2024-11-18 12:46:54.350509','completed',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(3,'2024-11-10 13:46:22.861471','2024-11-13 13:12:53.332398','cancelled',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(4,'2024-11-10 13:48:50.313127','2024-11-17 13:23:01.861592','cancelled',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(5,'2024-11-10 13:52:51.221466','2024-11-17 13:23:04.003454','cancelled',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(6,'2024-11-10 13:53:36.177926','2024-11-17 13:23:05.908158','cancelled',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(7,'2024-11-10 13:53:44.724678','2024-11-18 12:57:55.551322','pending_review',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(8,'2024-11-10 13:58:03.925725','2024-11-18 12:57:56.031295','pending_review',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(9,'2024-11-11 01:52:04.853567','2024-11-25 08:40:52.664220','completed',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(10,'2024-11-12 13:31:14.378978','2024-11-18 12:57:56.870110','pending_review',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(11,'2024-11-12 14:24:19.362327','2024-11-18 12:57:57.194045','pending_review',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(12,'2024-11-12 14:26:50.145386','2024-11-18 12:57:57.527181','pending_review',2,1,'none',0.00,0.00,0.00,NULL,'pending'),(13,'2024-11-17 09:36:17.937473','2024-11-18 12:57:57.880492','pending_review',NULL,1,'none',50.00,250.00,300.00,NULL,'pending'),(14,'2024-11-17 09:40:29.562588','2024-11-18 12:57:43.666636','pending_receipt',2,1,'none',50.00,250.00,300.00,NULL,'pending'),(15,'2024-11-17 09:41:37.203704','2024-11-18 13:14:06.961159','pending_review',2,1,'none',50.00,250.00,300.00,NULL,'pending'),(16,'2024-11-17 09:43:00.383007','2024-11-18 12:59:12.685448','pending_review',2,1,'none',50.00,250.00,300.00,NULL,'pending'),(17,'2024-11-17 09:43:33.445234','2024-11-18 13:14:18.466536','pending_review',2,1,'none',0.00,0.00,300.00,NULL,'pending'),(18,'2024-11-17 10:00:14.365856','2024-11-18 12:59:11.505078','pending_review',2,1,'none',240.00,60.00,300.00,NULL,'pending'),(19,'2024-11-17 10:02:13.277706','2024-11-18 12:57:28.809950','pending_shipment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(20,'2024-11-17 13:22:07.626660','2024-11-18 10:31:49.715924','pending_shipment',2,1,'none',1010.00,2290.00,3300.00,NULL,'pending'),(21,'2024-11-18 10:32:40.268325','2024-11-18 12:57:29.159305','pending_shipment',2,1,'none',1010.00,2290.00,3300.00,NULL,'pending'),(22,'2024-11-18 10:34:48.562586','2024-11-18 12:57:29.556115','pending_shipment',2,1,'none',1010.00,2290.00,3300.00,NULL,'pending'),(23,'2024-11-18 10:35:59.871051','2024-11-21 14:41:28.991637','pending_shipment',2,1,'none',1010.00,2290.00,3300.00,NULL,'pending'),(24,'2024-11-18 10:36:46.159710','2025-01-01 08:25:41.762752','pending_shipment',2,1,'none',230.00,670.00,900.00,NULL,'pending'),(25,'2024-11-18 10:37:45.403146','2025-01-01 08:42:44.564501','pending_shipment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(26,'2024-11-18 10:51:39.103222','2024-11-18 10:51:39.103222','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(27,'2024-11-18 10:52:39.139375','2024-11-18 10:52:39.139375','pending_payment',2,1,'none',180.00,720.00,900.00,NULL,'pending'),(28,'2024-11-25 13:24:40.695123','2024-11-25 13:24:40.695123','pending_payment',2,1,'none',0.00,300.00,300.00,NULL,'pending'),(29,'2025-01-01 08:22:00.937653','2025-01-01 08:22:00.937653','pending_payment',2,1,'none',0.00,300.00,300.00,NULL,'pending'),(30,'2025-01-01 08:40:07.630171','2025-01-01 08:40:07.630171','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(31,'2025-01-01 08:40:49.893516','2025-01-01 08:40:49.898511','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(32,'2025-01-01 08:40:56.815383','2025-01-01 08:40:56.821100','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(33,'2025-01-01 08:41:02.317658','2025-01-01 08:41:02.323695','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(34,'2025-01-01 08:44:01.151231','2025-01-01 08:44:01.156200','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(35,'2025-01-01 08:45:43.797440','2025-01-01 08:45:43.802398','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(36,'2025-01-01 08:46:50.660620','2025-01-01 08:46:50.666622','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(37,'2025-01-01 08:47:04.636224','2025-01-01 08:47:04.643328','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending'),(38,'2025-01-01 08:50:13.084258','2025-01-01 08:50:13.090872','pending_payment',2,1,'none',60.00,240.00,300.00,NULL,'pending');
/*!40000 ALTER TABLE `order_management_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_management_orderitem`
--

DROP TABLE IF EXISTS `order_management_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_management_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_management_ord_order_id_14fc180e_fk_order_man` (`order_id`),
  KEY `order_management_ord_product_id_08c590a0_fk_product_m` (`product_id`),
  CONSTRAINT `order_management_ord_order_id_14fc180e_fk_order_man` FOREIGN KEY (`order_id`) REFERENCES `order_management_order` (`id`),
  CONSTRAINT `order_management_ord_product_id_08c590a0_fk_product_m` FOREIGN KEY (`product_id`) REFERENCES `product_management_product` (`id`),
  CONSTRAINT `order_management_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_management_orderitem`
--

LOCK TABLES `order_management_orderitem` WRITE;
/*!40000 ALTER TABLE `order_management_orderitem` DISABLE KEYS */;
INSERT INTO `order_management_orderitem` VALUES (1,1,300.00,8,2),(2,2,300.00,9,2),(3,1,300.00,10,2),(4,1,300.00,11,2),(5,2,300.00,12,2),(6,1,300.00,16,2),(7,1,300.00,17,2),(8,1,300.00,18,2),(9,1,300.00,19,2),(10,11,300.00,20,2),(11,3,300.00,24,2),(12,1,300.00,25,2),(13,1,300.00,26,2),(14,3,300.00,27,2),(15,1,300.00,28,3),(16,1,300.00,29,3),(17,1,300.00,30,2),(18,1,300.00,38,3);
/*!40000 ALTER TABLE `order_management_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_management_category`
--

DROP TABLE IF EXISTS `product_management_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_management_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci,
  `parent_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `product_management_c_parent_id_d440f2ac_fk_product_m` (`parent_id`),
  CONSTRAINT `product_management_c_parent_id_d440f2ac_fk_product_m` FOREIGN KEY (`parent_id`) REFERENCES `product_management_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_management_category`
--

LOCK TABLES `product_management_category` WRITE;
/*!40000 ALTER TABLE `product_management_category` DISABLE KEYS */;
INSERT INTO `product_management_category` VALUES (1,'绿茶','不发酵茶，保留了茶叶的天然绿色，口感清新',NULL),(2,'龙井','',1),(3,'碧螺春','',1),(4,'白茶','轻微发酵茶，工艺简单，茶叶呈现自然白色',NULL),(5,'白毫银针','',4),(6,'白牡丹','',4),(7,'黄茶','轻度发酵茶，特点是“闷黄”工艺，使茶汤带有黄亮的色泽',NULL),(8,'君山银针','',7),(9,'蒙顶黄芽','',7),(10,'乌龙茶','半发酵茶，介于绿茶和红茶之间，具有独特的花香',NULL),(11,'铁观音','',10),(12,'大红袍','',10),(13,'红茶','全发酵茶，茶汤颜色较深，香气浓郁',NULL),(14,'正山小种','',13),(15,'金骏眉','',13),(16,'祁门红茶','',13),(17,'黑茶','后发酵茶，经过微生物发酵，适合长期储藏',NULL),(18,'普洱茶','',17),(19,'六堡茶','',17),(20,'花茶','',NULL),(21,'茉莉花茶','',20),(22,'菊花茶','',20);
/*!40000 ALTER TABLE `product_management_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_management_origin`
--

DROP TABLE IF EXISTS `product_management_origin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_management_origin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_management_origin`
--

LOCK TABLES `product_management_origin` WRITE;
/*!40000 ALTER TABLE `product_management_origin` DISABLE KEYS */;
INSERT INTO `product_management_origin` VALUES (1,'浙江','中国',''),(2,'安徽','中国',''),(3,'江西','中国',''),(4,'湖南','中国',''),(5,'广西','中国',''),(6,'陕西','中国',''),(7,'江苏','中国',''),(8,'福建','中国',''),(9,'湖北','中国',''),(10,'贵州','中国',''),(11,'山东','中国',''),(12,'河南','中国',''),(13,'云南','中国',''),(14,'四川','中国',''),(15,'重庆','中国',''),(16,'广东','中国',''),(17,'台湾','中国','');
/*!40000 ALTER TABLE `product_management_origin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_management_product`
--

DROP TABLE IF EXISTS `product_management_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_management_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cover` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cost_price` decimal(18,3) NOT NULL,
  `sales_price` decimal(18,3) NOT NULL,
  `stock` decimal(18,3) NOT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `category_id` bigint DEFAULT NULL,
  `origin_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_management_p_category_id_c8549eca_fk_product_m` (`category_id`),
  KEY `product_management_p_origin_id_85c06615_fk_product_m` (`origin_id`),
  CONSTRAINT `product_management_p_category_id_c8549eca_fk_product_m` FOREIGN KEY (`category_id`) REFERENCES `product_management_category` (`id`),
  CONSTRAINT `product_management_p_origin_id_85c06615_fk_product_m` FOREIGN KEY (`origin_id`) REFERENCES `product_management_origin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_management_product`
--

LOCK TABLES `product_management_product` WRITE;
/*!40000 ALTER TABLE `product_management_product` DISABLE KEYS */;
INSERT INTO `product_management_product` VALUES (2,'P1','西湖龙井','西湖龙井','cover/longjin_pAkmyLY.jpg','0',190.000,300.000,3.000,'2024-11-06 13:38:28.194769',2,1),(3,'P2','碧螺春','碧螺春','cover/biluochun_G7msYBZ.jpg','0',100.000,300.000,6.000,'2024-11-23 14:37:28.514979',3,15);
/*!40000 ALTER TABLE `product_management_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_management_product_promotion`
--

DROP TABLE IF EXISTS `product_management_product_promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_management_product_promotion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` bigint NOT NULL,
  `promotion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_management_produ_product_id_promotion_id_a0f0ff4c_uniq` (`product_id`,`promotion_id`),
  KEY `product_management_p_promotion_id_ca918c83_fk_product_m` (`promotion_id`),
  CONSTRAINT `product_management_p_product_id_c470f1a0_fk_product_m` FOREIGN KEY (`product_id`) REFERENCES `product_management_product` (`id`),
  CONSTRAINT `product_management_p_promotion_id_ca918c83_fk_product_m` FOREIGN KEY (`promotion_id`) REFERENCES `product_management_promotion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_management_product_promotion`
--

LOCK TABLES `product_management_product_promotion` WRITE;
/*!40000 ALTER TABLE `product_management_product_promotion` DISABLE KEYS */;
INSERT INTO `product_management_product_promotion` VALUES (6,2,1),(5,2,2),(7,3,1),(8,3,2),(9,3,3);
/*!40000 ALTER TABLE `product_management_product_promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_management_promotion`
--

DROP TABLE IF EXISTS `product_management_promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_management_promotion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `promotion_type` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `discount` decimal(5,2) DEFAULT NULL,
  `full_price` decimal(10,2) DEFAULT NULL,
  `reduction_price` decimal(10,2) DEFAULT NULL,
  `buy_quantity` int DEFAULT NULL,
  `gift_quantity` int DEFAULT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `priority` int NOT NULL,
  `allow_stack` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_management_promotion`
--

LOCK TABLES `product_management_promotion` WRITE;
/*!40000 ALTER TABLE `product_management_promotion` DISABLE KEYS */;
INSERT INTO `product_management_promotion` VALUES (1,'8折','discount',0.80,NULL,NULL,NULL,NULL,'2024-11-01 14:19:54.000000','2025-11-01 14:20:14.000000',1,100,0),(2,'满300减50','full_reduction',NULL,300.00,50.00,NULL,NULL,'2024-11-01 14:20:46.000000','2025-11-11 14:20:55.000000',1,80,0),(3,'满10赠1','buy_gift',NULL,NULL,NULL,10,1,'2024-11-01 14:21:28.000000','2025-12-30 14:21:39.000000',1,200,0);
/*!40000 ALTER TABLE `product_management_promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_management_promotion_applicable_products`
--

DROP TABLE IF EXISTS `product_management_promotion_applicable_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_management_promotion_applicable_products` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `promotion_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_management_promo_promotion_id_product_id_35d27ed9_uniq` (`promotion_id`,`product_id`),
  KEY `product_management_p_product_id_8ed7bcc8_fk_product_m` (`product_id`),
  CONSTRAINT `product_management_p_product_id_8ed7bcc8_fk_product_m` FOREIGN KEY (`product_id`) REFERENCES `product_management_product` (`id`),
  CONSTRAINT `product_management_p_promotion_id_9f2a5987_fk_product_m` FOREIGN KEY (`promotion_id`) REFERENCES `product_management_promotion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_management_promotion_applicable_products`
--

LOCK TABLES `product_management_promotion_applicable_products` WRITE;
/*!40000 ALTER TABLE `product_management_promotion_applicable_products` DISABLE KEYS */;
INSERT INTO `product_management_promotion_applicable_products` VALUES (1,1,2),(3,2,2);
/*!40000 ALTER TABLE `product_management_promotion_applicable_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_management_address`
--

DROP TABLE IF EXISTS `user_management_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_management_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_number` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `postal_code` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `province` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `district` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address_line` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_management_addr_user_id_6a5f5af1_fk_user_mana` (`user_id`),
  CONSTRAINT `user_management_addr_user_id_6a5f5af1_fk_user_mana` FOREIGN KEY (`user_id`) REFERENCES `user_management_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_management_address`
--

LOCK TABLES `user_management_address` WRITE;
/*!40000 ALTER TABLE `user_management_address` DISABLE KEYS */;
INSERT INTO `user_management_address` VALUES (2,'A1','13111111111','230601','天津','天津市','宁河县','111号',1,1);
/*!40000 ALTER TABLE `user_management_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_management_user`
--

DROP TABLE IF EXISTS `user_management_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_management_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `birthday` datetime(6) NOT NULL,
  `c_time` datetime(6) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `gender` varchar(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_management_user`
--

LOCK TABLES `user_management_user` WRITE;
/*!40000 ALTER TABLE `user_management_user` DISABLE KEYS */;
INSERT INTO `user_management_user` VALUES (1,'A1','qawsedrf1','11@qq.com','13111111111','2024-10-31 00:00:00.000000','2024-11-03 08:59:33.937794',0,'M',1,'2025-01-01 08:21:47.757802',1),(2,'admin','pbkdf2_sha256$260000$oJyhXB7ESmr1ETgkaYbciq$JQyYTtbAlaJ/bXHH70yQ6XotMxygvG01nHfeO+H0dj4=','497898@qq.com','15230378721','2024-10-31 00:00:00.000000','2024-11-05 13:36:22.004356',1,'M',1,'2024-11-17 12:52:43.048529',1);
/*!40000 ALTER TABLE `user_management_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_management_user_groups`
--

DROP TABLE IF EXISTS `user_management_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_management_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_management_user_groups_user_id_group_id_bed1779a_uniq` (`user_id`,`group_id`),
  KEY `user_management_user_groups_group_id_6f577055_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_management_user_groups_group_id_6f577055_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_management_user_user_id_092e6f6b_fk_user_mana` FOREIGN KEY (`user_id`) REFERENCES `user_management_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_management_user_groups`
--

LOCK TABLES `user_management_user_groups` WRITE;
/*!40000 ALTER TABLE `user_management_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_management_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_management_user_user_permissions`
--

DROP TABLE IF EXISTS `user_management_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_management_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_management_user_use_user_id_permission_id_c71a3268_uniq` (`user_id`,`permission_id`),
  KEY `user_management_user_permission_id_d8c2b1e9_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_management_user_permission_id_d8c2b1e9_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_management_user_user_id_4b8c2c7b_fk_user_mana` FOREIGN KEY (`user_id`) REFERENCES `user_management_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_management_user_user_permissions`
--

LOCK TABLES `user_management_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_management_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_management_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-11 17:00:07
