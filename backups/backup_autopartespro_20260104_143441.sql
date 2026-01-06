-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: autopartespro
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Categoría',6,'add_categoria'),(22,'Can change Categoría',6,'change_categoria'),(23,'Can delete Categoría',6,'delete_categoria'),(24,'Can view Categoría',6,'view_categoria'),(25,'Can add Marca',7,'add_marca'),(26,'Can change Marca',7,'change_marca'),(27,'Can delete Marca',7,'delete_marca'),(28,'Can view Marca',7,'view_marca'),(29,'Can add Producto',8,'add_producto'),(30,'Can change Producto',8,'change_producto'),(31,'Can delete Producto',8,'delete_producto'),(32,'Can view Producto',8,'view_producto'),(33,'Can add Imagen de producto',9,'add_productoimagen'),(34,'Can change Imagen de producto',9,'change_productoimagen'),(35,'Can delete Imagen de producto',9,'delete_productoimagen'),(36,'Can view Imagen de producto',9,'view_productoimagen'),(37,'Can add Carrito',10,'add_carrito'),(38,'Can change Carrito',10,'change_carrito'),(39,'Can delete Carrito',10,'delete_carrito'),(40,'Can view Carrito',10,'view_carrito'),(41,'Can add Detalle de orden',11,'add_detalleorden'),(42,'Can change Detalle de orden',11,'change_detalleorden'),(43,'Can delete Detalle de orden',11,'delete_detalleorden'),(44,'Can view Detalle de orden',11,'view_detalleorden'),(45,'Can add Historial de orden',12,'add_historialorden'),(46,'Can change Historial de orden',12,'change_historialorden'),(47,'Can delete Historial de orden',12,'delete_historialorden'),(48,'Can view Historial de orden',12,'view_historialorden'),(49,'Can add Ítem del carrito',13,'add_itemcarrito'),(50,'Can change Ítem del carrito',13,'change_itemcarrito'),(51,'Can delete Ítem del carrito',13,'delete_itemcarrito'),(52,'Can view Ítem del carrito',13,'view_itemcarrito'),(53,'Can add Orden',14,'add_orden'),(54,'Can change Orden',14,'change_orden'),(55,'Can delete Orden',14,'delete_orden'),(56,'Can view Orden',14,'view_orden'),(57,'Can add Usuario',16,'add_usuario'),(58,'Can change Usuario',16,'change_usuario'),(59,'Can delete Usuario',16,'delete_usuario'),(60,'Can view Usuario',16,'view_usuario'),(61,'Can add Dirección de envío',15,'add_direccionenvio'),(62,'Can change Dirección de envío',15,'change_direccionenvio'),(63,'Can delete Dirección de envío',15,'delete_direccionenvio'),(64,'Can view Dirección de envío',15,'view_direccionenvio');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_usuarios_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuarios_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuarios_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-12-26 19:32:55.000000','7','Aceite',2,'[]',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'contenttypes','contenttype'),(10,'pedidos','carrito'),(11,'pedidos','detalleorden'),(12,'pedidos','historialorden'),(13,'pedidos','itemcarrito'),(14,'pedidos','orden'),(6,'productos','categoria'),(7,'productos','marca'),(8,'productos','producto'),(9,'productos','productoimagen'),(5,'sessions','session'),(15,'usuarios','direccionenvio'),(16,'usuarios','usuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-12-24 20:31:11.000000'),(2,'contenttypes','0002_remove_content_type_name','2025-12-24 20:31:11.000000'),(3,'auth','0001_initial','2025-12-24 20:31:11.000000'),(4,'auth','0002_alter_permission_name_max_length','2025-12-24 20:31:12.000000'),(5,'auth','0003_alter_user_email_max_length','2025-12-24 20:31:12.000000'),(6,'auth','0004_alter_user_username_opts','2025-12-24 20:31:12.000000'),(7,'auth','0005_alter_user_last_login_null','2025-12-24 20:31:12.000000'),(8,'auth','0006_require_contenttypes_0002','2025-12-24 20:31:12.000000'),(9,'auth','0007_alter_validators_add_error_messages','2025-12-24 20:31:12.000000'),(10,'auth','0008_alter_user_username_max_length','2025-12-24 20:31:12.000000'),(11,'auth','0009_alter_user_last_name_max_length','2025-12-24 20:31:12.000000'),(12,'auth','0010_alter_group_name_max_length','2025-12-24 20:31:12.000000'),(13,'auth','0011_update_proxy_permissions','2025-12-24 20:31:12.000000'),(14,'auth','0012_alter_user_first_name_max_length','2025-12-24 20:31:12.000000'),(15,'usuarios','0001_initial','2025-12-24 20:31:12.000000'),(16,'admin','0001_initial','2025-12-24 20:31:12.000000'),(17,'admin','0002_logentry_remove_auto_add','2025-12-24 20:31:12.000000'),(18,'admin','0003_logentry_add_action_flag_choices','2025-12-24 20:31:12.000000'),(19,'productos','0001_initial','2025-12-24 20:31:13.000000'),(20,'pedidos','0001_initial','2025-12-24 20:31:13.000000'),(21,'pedidos','0002_initial','2025-12-24 20:31:14.000000'),(22,'sessions','0001_initial','2025-12-24 20:31:14.000000'),(23,'usuarios','0002_alter_direccionenvio_options_alter_usuario_options_and_more','2025-12-24 22:40:32.000000'),(24,'pedidos','0003_alter_orden_usuario','2025-12-24 22:54:37.000000'),(25,'usuarios','0003_alter_direccionenvio_options_alter_usuario_options_and_more','2026-01-04 17:29:29.000000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('nmge9vuyv956qsq3l8hoiglmpb23rgw4','.eJxVjMsKwjAQAP9lzxLyTujRu98QNpuNqUoKTXsS_10KPeh1Zpg3JNy3lvbBa5oLTKDg8ssy0pP7IcoD-30RtPRtnbM4EnHaIW5L4df1bP8GDUeDCRxVbWSg6Ezl4D07dhGplCyNxmjRBJQ1E1ppJSJWYqVsjcVXZ8hq-HwB-hY4qg:1vYXd1:9d5b7qoPp2b1uEncJRKT-M2ZTI7ibZEAk3FGViXG0mc','2026-01-07 22:46:47.000000'),('zfownnh2s378t1mr8lfl0t03dunl1as2','.eJxVjDsKwzAQBe-ydTCy9bFwmSsE3Jrn1QqLBBv0KULI3YMhRdLODPOiBa1uSyuSlxRoop4uv2wF32U_RSsNOR2lO6XsNTFqOvbuJtxyqs8Zjybl-u3_JhvKRhNZjoNWI3uro4zOiRXrwSGsSg_wBnqEiivDKKMARJa-N9EHF61mM9D7A2zUOy8:1vYXnh:cRvH5sUkXFdbE-CXKL4yMoV7RIMr_7-wz6JPM9XzWzA','2026-01-07 22:57:49.000000');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos_carrito`
--

DROP TABLE IF EXISTS `pedidos_carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedidos_carrito` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `session_key` varchar(40) DEFAULT NULL,
  `creado` datetime(6) NOT NULL,
  `actualizado` datetime(6) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pedidos_carrito_usuario_id_e9336b4d_fk_usuarios_usuario_id` (`usuario_id`),
  CONSTRAINT `pedidos_carrito_usuario_id_e9336b4d_fk_usuarios_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos_carrito`
--

LOCK TABLES `pedidos_carrito` WRITE;
/*!40000 ALTER TABLE `pedidos_carrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedidos_carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos_detalleorden`
--

DROP TABLE IF EXISTS `pedidos_detalleorden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedidos_detalleorden` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cantidad` int(10) unsigned NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  `orden_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pedidos_detalleorden_producto_id_280265a8_fk_productos` (`producto_id`),
  KEY `pedidos_detalleorden_orden_id_05da307b_fk_pedidos_orden_id` (`orden_id`),
  CONSTRAINT `pedidos_detalleorden_orden_id_05da307b_fk_pedidos_orden_id` FOREIGN KEY (`orden_id`) REFERENCES `pedidos_orden` (`id`),
  CONSTRAINT `pedidos_detalleorden_producto_id_280265a8_fk_productos` FOREIGN KEY (`producto_id`) REFERENCES `productos_producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos_detalleorden`
--

LOCK TABLES `pedidos_detalleorden` WRITE;
/*!40000 ALTER TABLE `pedidos_detalleorden` DISABLE KEYS */;
INSERT INTO `pedidos_detalleorden` VALUES (1,1,45000.00,45000.00,18,1),(2,1,45000.00,45000.00,18,2),(3,1,900.00,900.00,3,3),(4,1,45000.00,45000.00,18,4),(5,1,45000.00,45000.00,18,5),(6,1,45000.00,45000.00,18,6),(7,1,45000.00,45000.00,18,7),(8,1,45000.00,45000.00,18,8),(9,1,45000.00,45000.00,18,9),(10,1,900.00,900.00,3,10),(11,1,45000.00,45000.00,18,11),(12,1,900.00,900.00,3,12),(13,1,900.00,900.00,3,13),(14,1,900.00,900.00,3,14),(15,1,900.00,900.00,3,15),(16,1,45000.00,45000.00,18,16),(17,1,900.00,900.00,3,17),(18,1,900.00,900.00,3,18),(19,1,900.00,900.00,3,19),(20,1,900.00,900.00,3,20),(21,1,45000.00,45000.00,18,21),(22,1,900.00,900.00,3,22),(23,1,900.00,900.00,3,23),(24,1,900.00,900.00,3,24),(25,1,900.00,900.00,3,25),(26,1,900.00,900.00,3,26),(27,1,900.00,900.00,3,27),(28,1,900.00,900.00,3,28),(29,1,900.00,900.00,3,29),(30,1,900.00,900.00,3,30);
/*!40000 ALTER TABLE `pedidos_detalleorden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos_historialorden`
--

DROP TABLE IF EXISTS `pedidos_historialorden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedidos_historialorden` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `estado_anterior` varchar(20) NOT NULL,
  `estado_nuevo` varchar(20) NOT NULL,
  `observaciones` longtext NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `usuario_id` bigint(20) DEFAULT NULL,
  `orden_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pedidos_historialord_usuario_id_7f22edac_fk_usuarios_` (`usuario_id`),
  KEY `pedidos_historialorden_orden_id_0e8be20a_fk_pedidos_orden_id` (`orden_id`),
  CONSTRAINT `pedidos_historialord_usuario_id_7f22edac_fk_usuarios_` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`),
  CONSTRAINT `pedidos_historialorden_orden_id_0e8be20a_fk_pedidos_orden_id` FOREIGN KEY (`orden_id`) REFERENCES `pedidos_orden` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos_historialorden`
--

LOCK TABLES `pedidos_historialorden` WRITE;
/*!40000 ALTER TABLE `pedidos_historialorden` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedidos_historialorden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos_itemcarrito`
--

DROP TABLE IF EXISTS `pedidos_itemcarrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedidos_itemcarrito` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cantidad` int(10) unsigned NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `agregado` datetime(6) NOT NULL,
  `carrito_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pedidos_itemcarrito_carrito_id_producto_id_eaa16ded_uniq` (`carrito_id`,`producto_id`),
  KEY `pedidos_itemcarrito_producto_id_ae5829f9_fk_productos` (`producto_id`),
  CONSTRAINT `pedidos_itemcarrito_carrito_id_16ecb48e_fk_pedidos_carrito_id` FOREIGN KEY (`carrito_id`) REFERENCES `pedidos_carrito` (`id`),
  CONSTRAINT `pedidos_itemcarrito_producto_id_ae5829f9_fk_productos` FOREIGN KEY (`producto_id`) REFERENCES `productos_producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos_itemcarrito`
--

LOCK TABLES `pedidos_itemcarrito` WRITE;
/*!40000 ALTER TABLE `pedidos_itemcarrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedidos_itemcarrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos_orden`
--

DROP TABLE IF EXISTS `pedidos_orden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedidos_orden` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `numero_orden` varchar(20) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_confirmacion` datetime(6) DEFAULT NULL,
  `fecha_pago` datetime(6) DEFAULT NULL,
  `fecha_envio` datetime(6) DEFAULT NULL,
  `fecha_entrega` datetime(6) DEFAULT NULL,
  `cliente_nombre` varchar(100) NOT NULL,
  `cliente_apellido` varchar(100) NOT NULL,
  `cliente_email` varchar(254) NOT NULL,
  `cliente_telefono` varchar(20) NOT NULL,
  `cliente_rut` varchar(12) NOT NULL,
  `direccion_calle` varchar(200) NOT NULL,
  `direccion_numero` varchar(20) NOT NULL,
  `direccion_dpto` varchar(20) NOT NULL,
  `direccion_comuna` varchar(100) NOT NULL,
  `direccion_region` varchar(100) NOT NULL,
  `direccion_codigo_postal` varchar(10) NOT NULL,
  `direccion_indicaciones` longtext NOT NULL,
  `metodo_pago` varchar(20) NOT NULL,
  `metodo_envio` varchar(20) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `costo_envio` decimal(10,2) NOT NULL,
  `descuento` decimal(10,2) NOT NULL,
  `iva` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `referencia_pago` varchar(100) NOT NULL,
  `comprobante_pago` varchar(100) DEFAULT NULL,
  `notas` longtext NOT NULL,
  `codigo_seguimiento` varchar(100) NOT NULL,
  `url_seguimiento` varchar(200) NOT NULL,
  `usuario_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_orden` (`numero_orden`),
  KEY `pedidos_ord_numero__911dc4_idx` (`numero_orden`),
  KEY `pedidos_ord_usuario_80513a_idx` (`usuario_id`),
  KEY `pedidos_ord_estado_9236f3_idx` (`estado`),
  KEY `pedidos_ord_fecha_c_ddd3fd_idx` (`fecha_creacion`),
  CONSTRAINT `pedidos_orden_usuario_id_75ad4775_fk_usuarios_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos_orden`
--

LOCK TABLES `pedidos_orden` WRITE;
/*!40000 ALTER TABLE `pedidos_orden` DISABLE KEYS */;
INSERT INTO `pedidos_orden` VALUES (1,'ORD-870A50E8','pendiente','2025-12-24 22:56:00.000000',NULL,NULL,NULL,NULL,'Test Guest','User','guest@test.com','+56912345678','','Test St','123','','Santiago','RM','','','transferencia','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(2,'ORD-368BF9A3','pendiente','2025-12-24 22:56:36.000000',NULL,NULL,NULL,NULL,'Test Guest','User','guest@test.com','+56912345678','','Test St','123','','Santiago','RM','','','transferencia','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(3,'ORD-2234E07B','pendiente','2025-12-24 23:06:22.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenidad General San martin 181 Vallegrande Lampa ','181','','Lampa','Región Metropolitana','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(4,'ORD-48A5837A','pendiente','2025-12-24 23:07:42.000000',NULL,NULL,NULL,NULL,'Debug User','Debug Lastname','debug@test.com','+56912345678','','Debug St','123','','Santiago','RM','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(5,'ORD-2E153A8F','pendiente','2025-12-24 23:08:49.000000',NULL,NULL,NULL,NULL,'Debug User','Debug Lastname','debug@test.com','+56912345678','','Debug St','123','','Santiago','RM','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(6,'ORD-798A828B','pendiente','2025-12-24 23:09:18.000000',NULL,NULL,NULL,NULL,'Debug User','Debug Lastname','debug@test.com','+56912345678','','Debug St','123','','Santiago','RM','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(7,'ORD-BCC0137E','pendiente','2025-12-24 23:10:08.000000',NULL,NULL,NULL,NULL,'Debug User','Debug Lastname','debug@test.com','+56912345678','','Debug St','123','','Santiago','RM','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(8,'ORD-4900C1EC','pendiente','2025-12-24 23:10:52.000000',NULL,NULL,NULL,NULL,'Debug User','Debug Lastname','debug@test.com','+56912345678','','Debug St','123','','Santiago','RM','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(9,'ORD-4A42486F','pendiente','2025-12-24 23:11:24.000000',NULL,NULL,NULL,NULL,'Debug User','Debug Lastname','debug@test.com','+56912345678','','Debug St','123','','Santiago','RM','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'343776998-9bb2edb3-c9b8-4d5c-a2e0-231b7a573ce0','','','','',NULL),(10,'ORD-25E9D4EA','pendiente','2025-12-24 23:13:36.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martín 181 Vallegrande Lampa ','181','','Lampa','Región Metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(11,'ORD-E5163F29','pendiente','2025-12-24 23:15:04.000000',NULL,NULL,NULL,NULL,'Debug User','Debug Lastname','debug@test.com','+56912345678','','Debug St','123','','Santiago','RM','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(12,'ORD-95E3D8F7','pendiente','2025-12-24 23:17:44.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martin 181 Vallegrande Lampa','181','','Lampa','Región Metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(13,'ORD-5F896E64','pendiente','2025-12-24 23:20:48.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martin 181 Vallegrande Lampa','181','','Lampa','Región Metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(14,'ORD-155C2B4F','pendiente','2025-12-24 23:22:02.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martin 181 Vallegrande Lampa ','181','','Lampa','Región Metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(15,'ORD-6E4A8334','pendiente','2025-12-24 23:22:14.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martin 181 Vallegrande Lampa ','181','','Lampa','Región Metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(16,'ORD-580FDF28','pendiente','2025-12-26 02:29:51.000000',NULL,NULL,NULL,NULL,'Test','User','test@user.com','123456789','','Test St','123','','TestComuna','TestRegion','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(17,'ORD-474E6EFE','pendiente','2025-12-26 02:32:38.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martín 181 Vallegrande Lampa','181','','Lampa ','Región Metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(18,'ORD-8FA31628','pendiente','2025-12-26 02:37:48.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martín 181 vallegrande Lampa ','181','','Lampa','Region metropolitana','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(19,'ORD-F82772AA','pendiente','2025-12-26 02:46:44.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San martin 181 Vallegrande Lampa','casa ','','Lampa','Region Metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(20,'ORD-0C577036','pendiente','2025-12-26 02:48:00.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','cristobal2025.suarez.montenegro@gmail.com','985993861','','Avenida General San Martin 181 Vallegrande Lampa','181','','Lampa','Region metropolitana','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',NULL),(21,'ORD-E1836030','pendiente','2025-12-26 02:50:43.000000',NULL,NULL,NULL,NULL,'Test','User','test@user.com','123456789','','Test St','123','','TestComuna','TestRegion','','','mercadopago','domicilio',45000.00,0.00,0.00,8550.00,45000.00,'','','','','',NULL),(22,'ORD-EEF7C5BD','pendiente','2025-12-26 16:31:01.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenidas General san martin 181','181','','Lampa','Region metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'2914738060-5df2179d-fd47-4ac5-9353-b5fa8f3af57a','','','','',1),(23,'ORD-35A62667','pendiente','2025-12-26 16:32:02.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenidas General san martin 181','181','','Lampa','Region metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'2914738060-5045e2bd-cf1d-4dd2-856c-c4b27dec63fa','','','','',1),(24,'ORD-E462ABC5','pendiente','2025-12-26 16:34:15.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenidas General san martin 181','181','','Lampa','Region metropolitana ','','','transferencia','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(25,'ORD-2AD8B94B','pendiente','2025-12-26 17:01:58.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenida General San martin 181 Vallegrande Lampa ','181','','Lampa','Region metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'2914738060-eae61329-a5bb-4849-839c-4b3a51b4ebc1','','','','',1),(26,'ORD-CBF5F4A0','pendiente','2025-12-26 17:02:22.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenida General San martin 181 Vallegrande Lampa ','181','','Lampa','Region metropolitana ','','','transferencia','domicilio',900.00,0.00,0.00,171.00,900.00,'','','','','',1),(27,'ORD-11398CB1','pendiente','2025-12-27 01:33:05.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenida General San martin 181 Vallegrande lampa ','181','','Lampa ','Region metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'343776998-68b1af54-5611-4596-b74d-a8aa39f2d35f','','','','',1),(28,'ORD-077AA888','pendiente','2025-12-27 02:19:59.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenida General San martin 181 Vallegrande lampa ','181','','Lampa ','Region metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'343776998-8855eaeb-e103-412e-a26e-9fec3f81a6fd','','','','',1),(29,'ORD-CE270481','pendiente','2025-12-27 02:21:44.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenida General San martin 181 Vallegrande lampa ','181','','Lampa ','Region metropolitana ','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'343776998-37b55223-7f33-4409-971c-39b7e0f7b60f','','','','',1),(30,'ORD-EED7C67A','pendiente','2025-12-27 02:23:15.000000',NULL,NULL,NULL,NULL,'Cristóbal Javier','Montenegro','testuser7@gmail.com','985993861','','Avenida General San martin 181 Vallegrande Lampa ','181','','Lampa ','Region metropolitana','','','mercadopago','domicilio',900.00,0.00,0.00,171.00,900.00,'343776998-9a23f513-94dc-4dbe-ac11-0648b021aea1','','','','',1);
/*!40000 ALTER TABLE `pedidos_orden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_categoria`
--

DROP TABLE IF EXISTS `productos_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos_categoria` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `orden` int(11) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_categoria`
--

LOCK TABLES `productos_categoria` WRITE;
/*!40000 ALTER TABLE `productos_categoria` DISABLE KEYS */;
INSERT INTO `productos_categoria` VALUES (1,'Filtros','filtros','','',0,1),(2,'Tuercas','tuercas','','',0,1),(3,'Originales','originales','','',0,1),(4,'Espejos','espejos','','',0,1),(5,'Mascara','mascara','','',0,1),(6,'Bomba de Agua','bomba-de-agua','','',0,1),(7,'Aceite','aceite','','',0,1),(8,'Mensula','mensula','','',0,1),(9,'Tapa deposito agua radiador','tapa-deposito-agua-radiador','','',0,1),(10,'Refrigerante','refrigerante','','',0,1),(11,'Kit Mantención','kit-mantención','','',0,1),(12,'Originales ford','originales-ford','','',0,1),(13,'Baterías','baterías','','',0,1),(14,'Frenos','frenos','','',0,1),(15,'Suspensión','suspensión','','',0,1),(16,'Correas','correas','','',0,1),(17,'Radiadores','radiadores','','',0,1),(18,'Bujías','bujías','','',0,1);
/*!40000 ALTER TABLE `productos_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_marca`
--

DROP TABLE IF EXISTS `productos_marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos_marca` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `descripcion` longtext NOT NULL,
  `activa` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_marca`
--

LOCK TABLES `productos_marca` WRITE;
/*!40000 ALTER TABLE `productos_marca` DISABLE KEYS */;
INSERT INTO `productos_marca` VALUES (1,'Honda','','',1),(2,'MG','','',1),(3,'Mitsubishi','','',1),(4,'Ford y Mazda','','',1),(5,'Ford','','',1),(6,'Varta','','',1),(7,'Toyota','','',1),(8,'Kia','','',1),(9,'Chevrolet','','',1),(10,'NGK','','',1);
/*!40000 ALTER TABLE `productos_marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_producto`
--

DROP TABLE IF EXISTS `productos_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos_producto` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `SKU` varchar(50) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `descripcion` longtext NOT NULL,
  `descripcion_corta` varchar(300) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `precio_antes` decimal(10,2) DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `stock_minimo` int(11) NOT NULL,
  `modelo_compatible` varchar(200) NOT NULL,
  `año_compatible` varchar(100) NOT NULL,
  `garantia` varchar(100) NOT NULL,
  `peso` decimal(6,2) DEFAULT NULL,
  `dimensiones` varchar(100) NOT NULL,
  `imagen_principal` varchar(100) NOT NULL,
  `imagen_2` varchar(100) DEFAULT NULL,
  `imagen_3` varchar(100) DEFAULT NULL,
  `imagen_4` varchar(100) DEFAULT NULL,
  `destacado` tinyint(1) NOT NULL,
  `nuevo` tinyint(1) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `categoria_id` bigint(20) NOT NULL,
  `marca_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `SKU` (`SKU`),
  UNIQUE KEY `slug` (`slug`),
  KEY `productos_p_SKU_7b58f2_idx` (`SKU`),
  KEY `productos_p_nombre_456643_idx` (`nombre`),
  KEY `productos_p_categor_17b5fc_idx` (`categoria_id`),
  KEY `productos_p_precio_d043df_idx` (`precio`),
  KEY `productos_p_destaca_a20b31_idx` (`destacado`),
  KEY `productos_producto_marca_id_fc6a9dea_fk_productos_marca_id` (`marca_id`),
  CONSTRAINT `productos_producto_categoria_id_1fef506a_fk_productos` FOREIGN KEY (`categoria_id`) REFERENCES `productos_categoria` (`id`),
  CONSTRAINT `productos_producto_marca_id_fc6a9dea_fk_productos_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `productos_marca` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_producto`
--

LOCK TABLES `productos_producto` WRITE;
/*!40000 ALTER TABLE `productos_producto` DISABLE KEYS */;
INSERT INTO `productos_producto` VALUES (1,'HON-FIL-001','Filtro Caja Cambio Honda','filtro-caja-cambio-honda-hon-fil-001','Repuesto original Honda - Filtro Caja Cambio Honda','',35000.00,NULL,NULL,10,5,'','','',NULL,'','productos/filtro-caja-cambio-honda.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',1,1),(2,'MG-TUE-002','Tuercas de seguridad MG ONE,MG ZS,MG ZX','tuercas-de-seguridad-mg-onemg-zsmg-zx-mg-tue-002','Repuesto original MG - Tuercas de seguridad MG ONE,MG ZS,MG ZX','',70000.00,NULL,NULL,10,5,'','','',NULL,'','productos/tuercas-de-seguridad-mg.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',2,2),(3,'MG-REP-003','Venta de repuestos Originales MG','venta-de-repuestos-originales-mg-mg-rep-003','Repuesto original MG - Venta de repuestos Originales MG','',900.00,NULL,NULL,10,5,'','','',NULL,'','productos/venta-de-respuestos-originales-mg.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',3,2),(4,'HON-ESP-004','Espejo Honda City 2014 al 2021','espejo-honda-city-2014-al-2021-hon-esp-004','Repuesto original Honda - Espejo Honda City 2014 al 2021','',230000.00,NULL,NULL,10,5,'','','',NULL,'','productos/espejo-honda-city-2014-al-2021.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',4,1),(5,'HON-MAS-005','Mascara Honda Pilot y Ridgeline','mascara-honda-pilot-y-ridgeline-hon-mas-005','Repuesto original Honda - Mascara Honda Pilot y Ridgeline','',230000.00,NULL,NULL,10,5,'','','',NULL,'','productos/mascara-honda-pilot-y-ridgeline.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',5,1),(6,'HON-BOM-006','Bomba de agua Honda Pilot o Ridgeline','bomba-de-agua-honda-pilot-o-ridgeline-hon-bom-006','Repuesto original Honda - Bomba de agua Honda Pilot o Ridgeline','',230000.00,NULL,NULL,10,5,'','','',NULL,'','productos/bomba-de-agua-honda-pilot-o-ridgeline.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',6,1),(7,'MIT-ACE-007','Aceite motor Mitsubishi','aceite-motor-mitsubishi-mit-ace-007','Repuesto original Mitsubishi - Aceite motor Mitsubishi','',69000.00,NULL,NULL,10,5,'','','',NULL,'','productos/aceite-motor-mitsubishi.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',7,3),(8,'HON-ACE-008','Aceite caja Honda cada uno','aceite-caja-honda-cada-uno-hon-ace-008','Repuesto original Honda - Aceite caja Honda cada uno','',13000.00,NULL,NULL,10,5,'','','',NULL,'','productos/aceite-caja-honda.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',7,1),(9,'HON-MEN-009','Mensula parachoque delantero Honda CRV 2002 al 2006','mensula-parachoque-delantero-honda-crv-2002-al-2006-hon-men-009','Repuesto original Honda - Mensula parachoque delantero Honda CRV 2002 al 2006','',40000.00,NULL,NULL,10,5,'','','',NULL,'','productos/mensula-parach-delantero-honda.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',8,1),(10,'FOR-TAP-010','Tapa deposito agua radiador Ford y Mazda. Original Ford','tapa-deposito-agua-radiador-ford-y-mazda-original-ford-for-tap-010','Repuesto original Ford y Mazda - Tapa deposito agua radiador Ford y Mazda. Original Ford','',25000.00,NULL,NULL,10,5,'','','',NULL,'','productos/tapa-deposito-agua-radiador-for-mazda.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',9,4),(11,'HON-ACE-011','Aceite motor 5W30 Honda','aceite-motor-5w30-honda-hon-ace-011','Repuesto original Honda - Aceite motor 5W30 Honda','',17000.00,NULL,NULL,10,5,'','','',NULL,'','productos/aceite-motor-honda.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',7,1),(12,'HON-ACE-012','Aceite caja CVT modelos hasta 2014','aceite-caja-cvt-modelos-hasta-2014-hon-ace-012','Repuesto original Honda - Aceite caja CVT modelos hasta 2014','',17000.00,NULL,NULL,10,5,'','','',NULL,'','productos/aceite-caja-honda2.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',7,1),(13,'HON-COO-013','Coolant Original Honda','coolant-original-honda-hon-coo-013','Repuesto original Honda - Coolant Original Honda','',35000.00,NULL,NULL,10,5,'','','',NULL,'','productos/colan-original-honda.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',10,1),(14,'HON-ACE-014','Aceite Diferencial Honda VTM-4 / 3.8 lts.','aceite-diferencial-honda-vtm-4-38-lts-hon-ace-014','Repuesto original Honda - Aceite Diferencial Honda VTM-4 / 3.8 lts.','',60000.00,NULL,NULL,10,5,'','','',NULL,'','productos/aceite-diferencial-honda.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',7,1),(15,'HON-ACE-015','Aceite caja ATF-TYPE 3.1','aceite-caja-atf-type-31-hon-ace-015','Repuesto original Honda - Aceite caja ATF-TYPE 3.1','',69000.00,NULL,NULL,10,5,'','','',NULL,'','productos/aceite-caja-typer-r.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',7,1),(16,'MG-KIT-016','Kit Mantención MG ZX/ZC','kit-mantencion-mg-zxzc-mg-kit-016','Repuesto original MG - Kit Mantención MG ZX/ZC','',105000.00,NULL,NULL,10,5,'','','',NULL,'','productos/kit-mantencion.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',11,2),(17,'MG-FIL-017','Filtro Combustible MG','filtro-combustible-mg-mg-fil-017','Repuesto original MG - Filtro Combustible MG','',15000.00,NULL,NULL,10,5,'','','',NULL,'','productos/filtro-mg.jpg','','','',0,1,1,'2025-12-24 21:59:05.000000','2025-12-24 21:59:05.000000',1,2),(18,'FOR-REP-018','Venta de repuestos Originales Ford','venta-de-repuestos-originales-ford-for-rep-018','Repuesto original Ford - Venta de repuestos Originales Ford','',45000.00,NULL,NULL,10,5,'','','',NULL,'','productos/for.jpg','','','',0,1,1,'2025-12-24 21:59:06.000000','2025-12-24 21:59:06.000000',12,5),(19,'VAR-BAT-019','Batería de auto 12V','bateria-de-auto-12v-var-bat-019','Repuesto original Varta - Batería de auto 12V','',120000.00,NULL,NULL,10,5,'','','',NULL,'','productos/disponible-variedad.jpg','','','',0,1,1,'2025-12-24 21:59:06.000000','2025-12-24 21:59:06.000000',13,6),(20,'HON-FRE-020','Pastillas de freno Honda Civic','pastillas-de-freno-honda-civic-hon-fre-020','Repuesto original Honda - Pastillas de freno Honda Civic','',80000.00,NULL,NULL,10,5,'','','',NULL,'','productos/410201-PD391H-802.jpg','','','',0,1,1,'2025-12-24 21:59:06.000000','2025-12-24 21:59:06.000000',14,1),(21,'TOY-AMO-021','Amortiguadores delanteros Toyota Corolla','amortiguadores-delanteros-toyota-corolla-toy-amo-021','Repuesto original Toyota - Amortiguadores delanteros Toyota Corolla','',150000.00,NULL,NULL,10,5,'','','',NULL,'','productos/disponible-variedad.jpg','','','',0,1,1,'2025-12-24 21:59:06.000000','2025-12-24 21:59:06.000000',15,7),(22,'KIA-COR-022','Correa de distribución Kia Rio','correa-de-distribucion-kia-rio-kia-cor-022','Repuesto original Kia - Correa de distribución Kia Rio','',50000.00,NULL,NULL,10,5,'','','',NULL,'','productos/disponible-variedad.jpg','','','',0,1,1,'2025-12-24 21:59:06.000000','2025-12-24 21:59:06.000000',16,8),(23,'CHE-RAD-023','Radiador Chevrolet Spark','radiador-chevrolet-spark-che-rad-023','Repuesto original Chevrolet - Radiador Chevrolet Spark','',90000.00,NULL,NULL,10,5,'','','',NULL,'','productos/disponible-variedad.jpg','','','',0,1,1,'2025-12-24 21:59:06.000000','2025-12-24 21:59:06.000000',17,9),(24,'NGK-BUJ-024','Bujías NGK para motor 1.6L','bujias-ngk-para-motor-16l-ngk-buj-024','Repuesto original NGK - Bujías NGK para motor 1.6L','',25000.00,NULL,NULL,10,5,'','','',NULL,'','productos/disponible-variedad.jpg','','','',0,1,1,'2025-12-24 21:59:06.000000','2025-12-24 21:59:06.000000',18,10);
/*!40000 ALTER TABLE `productos_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_productoimagen`
--

DROP TABLE IF EXISTS `productos_productoimagen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos_productoimagen` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `imagen` varchar(100) NOT NULL,
  `orden` int(11) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `productos_productoim_producto_id_2a13319c_fk_productos` (`producto_id`),
  CONSTRAINT `productos_productoim_producto_id_2a13319c_fk_productos` FOREIGN KEY (`producto_id`) REFERENCES `productos_producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_productoimagen`
--

LOCK TABLES `productos_productoimagen` WRITE;
/*!40000 ALTER TABLE `productos_productoimagen` DISABLE KEYS */;
/*!40000 ALTER TABLE `productos_productoimagen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_direccionenvio`
--

DROP TABLE IF EXISTS `usuarios_direccionenvio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios_direccionenvio` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `alias` varchar(50) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `calle` varchar(100) NOT NULL,
  `numero` varchar(20) NOT NULL,
  `dpto` varchar(20) NOT NULL,
  `comuna` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `codigo_postal` varchar(20) NOT NULL,
  `indicaciones` longtext NOT NULL,
  `por_defecto` tinyint(1) NOT NULL,
  `creado` datetime(6) NOT NULL,
  `actualizado` datetime(6) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarios_direccionen_usuario_id_b3d33e1d_fk_usuarios_` (`usuario_id`),
  CONSTRAINT `usuarios_direccionen_usuario_id_b3d33e1d_fk_usuarios_` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_direccionenvio`
--

LOCK TABLES `usuarios_direccionenvio` WRITE;
/*!40000 ALTER TABLE `usuarios_direccionenvio` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_direccionenvio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario`
--

DROP TABLE IF EXISTS `usuarios_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios_usuario` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `rut` varchar(12) DEFAULT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `comuna` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `es_cliente` tinyint(1) NOT NULL,
  `es_vendedor` tinyint(1) NOT NULL,
  `es_admin` tinyint(1) NOT NULL,
  `newsletter` tinyint(1) NOT NULL,
  `terminos_aceptados` tinyint(1) NOT NULL,
  `codigo_cliente` varchar(50) DEFAULT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  `ultimo_acceso` datetime(6) DEFAULT '2025-12-24 22:38:02.000000',
  `bloqueado_hasta` datetime(6) DEFAULT NULL,
  `intentos_fallidos` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `codigo_cliente` (`codigo_cliente`),
  UNIQUE KEY `usuarios_usuario_rut_d29aa436_uniq` (`rut`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario`
--

LOCK TABLES `usuarios_usuario` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario` DISABLE KEYS */;
INSERT INTO `usuarios_usuario` VALUES (1,'pbkdf2_sha256$1200000$2sZGVy9hc0FQF3N2tdh4mk$t3RXMyo34g5txbSyrezak1qauIMnNBQQCPtVC6IZ1h0=','2025-12-24 22:57:49.000000',1,'admin','','','admin@autopartespro.cl',1,1,'2025-12-24 20:35:54.000000','','','','','',1,0,1,1,0,'CLI-36794BB3','2025-12-24 20:35:55.000000','2025-12-24 22:57:49.000000',NULL,0);
/*!40000 ALTER TABLE `usuarios_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario_groups`
--

DROP TABLE IF EXISTS `usuarios_usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios_usuario_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_usuario_groups_usuario_id_group_id_4ed5b09e_uniq` (`usuario_id`,`group_id`),
  KEY `usuarios_usuario_groups_group_id_e77f6dcf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `usuarios_usuario_gro_usuario_id_7a34077f_fk_usuarios_` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`),
  CONSTRAINT `usuarios_usuario_groups_group_id_e77f6dcf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario_groups`
--

LOCK TABLES `usuarios_usuario_groups` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario_user_permissions`
--

DROP TABLE IF EXISTS `usuarios_usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios_usuario_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_usuario_user_pe_usuario_id_permission_id_217cadcd_uniq` (`usuario_id`,`permission_id`),
  KEY `usuarios_usuario_use_permission_id_4e5c0f2f_fk_auth_perm` (`permission_id`),
  CONSTRAINT `usuarios_usuario_use_permission_id_4e5c0f2f_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `usuarios_usuario_use_usuario_id_60aeea80_fk_usuarios_` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario_user_permissions`
--

LOCK TABLES `usuarios_usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-04 14:34:42
