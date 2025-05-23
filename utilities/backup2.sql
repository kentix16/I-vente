-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: gestion
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id_cli` varchar(10) NOT NULL,
  `login` varchar(25) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(15) NOT NULL,
  PRIMARY KEY (`id_cli`),
  UNIQUE KEY `id_cli` (`id_cli`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES ('CLI001','martin_dupont','martin.dupont@email.com','mdp123'),('CLI002','sophie_martin','sophie.martin@gmail.com','pass456'),('CLI003','julien_bernard','julien.bernard@yahoo.fr','secret789'),('CLI004','marie_durand','marie.durand@hotmail.com','motdepasse1'),('CLI005','pierre_lefebvre','pierre.lefebvre@outlook.com','password2');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `depense`
--

DROP TABLE IF EXISTS `depense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `depense` (
  `id_dep` varchar(10) NOT NULL,
  `nom_dep` varchar(30) DEFAULT NULL,
  `date_dep` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `somme_dep` int DEFAULT NULL,
  PRIMARY KEY (`id_dep`),
  UNIQUE KEY `id_dep` (`id_dep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `depense`
--

LOCK TABLES `depense` WRITE;
/*!40000 ALTER TABLE `depense` DISABLE KEYS */;
INSERT INTO `depense` VALUES ('DEP001','Achat stock smartphones','2024-12-10 10:30:00',25600),('DEP002','Frais de livraison','2024-12-12 14:15:00',451),('DEP003','Publicité Facebook','2024-12-20 09:45:00',891),('DEP004','Loyer magasin janvier','2025-01-01 08:00:00',3200),('DEP005','Électricité janvier','2025-01-05 16:30:00',285),('DEP006','Achat stock tablettes','2025-01-10 11:20:00',18750),('DEP007','Salaires janvier','2025-01-31 17:00:00',8500),('DEP008','Assurance magasin','2025-02-01 09:15:00',676),('DEP009','Réparation vitrine','2025-02-08 13:45:00',320),('DEP010','Achat stock ordinateurs','2025-02-15 10:10:00',32400),('DEP011','Loyer magasin février','2025-02-01 08:00:00',3200),('DEP012','Électricité février','2025-02-05 15:20:00',301),('DEP013','Publicité Google Ads','2025-02-18 12:30:00',1250),('DEP014','Salaires février','2025-02-28 17:00:00',8500),('DEP015','Loyer magasin mars','2025-03-01 08:00:00',3200),('DEP016','Achat stock écrans','2025-03-05 09:45:00',15680),('DEP017','Formation personnel','2025-03-08 14:00:00',890),('DEP018','Électricité mars','2025-03-05 16:15:00',276),('DEP019','Maintenance équipements','2025-03-12 11:30:00',451),('DEP020','Achat stock claviers','2025-03-15 13:20:00',8960),('DEP021','Publicité Instagram','2025-03-18 10:45:00',676),('DEP022','Fournitures bureau','2025-03-22 15:10:00',190),('DEP023','Nettoyage magasin','2025-03-25 09:30:00',225),('DEP024','Salaires mars','2025-03-31 17:00:00',8500),('DEP025','Loyer magasin avril','2025-04-01 08:00:00',3200),('DEP026','Achat emballages','2025-04-03 12:15:00',346),('DEP027','Transport marchandises','2025-04-06 14:30:00',567),('DEP028','Électricité avril','2025-04-05 16:45:00',299),('DEP029','Rénovation espace vente','2025-04-10 10:20:00',2850),('DEP030','Achat nouvelles étagères','2025-04-12 13:50:00',1240),('DEP031','Publicité radio locale','2025-04-15 11:35:00',950),('DEP032','Système de sécurité upgrade','2025-04-18 16:00:00',1681),('DEP033','Formation vente','2025-04-20 09:45:00',760),('DEP034','Frais bancaires avril','2025-04-22 14:20:00',126),('DEP035','Achat caisse enregistreuse','2025-04-25 12:10:00',890),('DEP036','Salaires avril','2025-04-30 17:00:00',8500),('DEP037','Loyer magasin mai','2025-05-01 08:00:00',3200),('DEP038','Achat stock accessoires','2025-05-03 10:40:00',12450),('DEP039','Campagne email marketing','2025-05-06 15:25:00',421),('DEP040','Électricité mai','2025-05-05 16:30:00',313),('DEP041','Réparation climatisation','2025-05-08 11:15:00',680),('DEP042','Achat nouveaux présentoirs','2025-05-10 13:45:00',1561),('DEP043','Formation service client','2025-05-12 09:20:00',691),('DEP044','Assurance produits','2025-05-15 14:35:00',845),('DEP045','Frais de port clients','2025-05-18 12:50:00',235),('DEP046','Publicité YouTube','2025-05-20 16:10:00',780),('DEP047','Salaires mai','2025-05-31 17:00:00',8500),('DEP048','Achat matériel','2025-03-07 11:45:00',2340),('DEP049','Abonnement logiciel gestion','2025-03-10 14:20:00',157),('DEP050','Frais comptable Q1','2025-03-31 15:30:00',950),('DEP051','Achat véhicule livraison','2025-04-02 09:00:00',18500),('DEP052','Carburant avril','2025-04-05 16:20:00',890),('DEP053','Entretien véhicule','2025-04-08 10:30:00',246),('DEP054','Taxe professionnelle','2025-04-15 13:15:00',2150),('DEP055','Abonnement téléphone','2025-04-18 11:50:00',90),('DEP056','Internet entreprise','2025-04-20 15:40:00',126),('DEP057','Conseil juridique','2025-04-25 14:00:00',680),('DEP058','Carburant mai','2025-05-03 17:10:00',921),('DEP059','Prime performance équipe','2025-05-07 12:30:00',1500),('DEP060','Matériel nettoyage','2025-05-09 09:45:00',79),('DEP061','Réparation lumière','2025-05-12 16:25:00',340),('DEP062','Audit sécurité','2025-05-16 13:40:00',751),('DEP063','Frais bancaires mai','2025-05-22 10:15:00',142),('DEP064','Achat stock périphériques','2025-03-04 12:00:00',9876),('DEP065','Campagne affichage urbain','2025-03-14 15:45:00',1450),('DEP066','Frais participation salon','2025-03-20 09:30:00',2890),('DEP067','Stand salon professionnel','2025-03-21 11:20:00',1251),('DEP068','Hébergement salon','2025-03-22 18:00:00',457),('DEP069','Repas d\'affaires','2025-03-23 12:45:00',190),('DEP070','Transport salon','2025-03-24 08:30:00',287),('DEP071','Goodies promotionnels','2025-04-01 14:15:00',679),('DEP072','Mise à jour site web','2025-04-05 16:50:00',890),('DEP073','Photos produits pro','2025-04-08 13:25:00',451),('DEP074','Rédaction fiches produits','2025-04-11 10:40:00',321),('DEP075','Optimisation SEO','2025-04-14 15:10:00',750),('DEP076','Achat serveur sauvegarde','2025-04-17 11:30:00',1890),('DEP077','Licence antivirus entreprise','2025-04-19 14:45:00',246),('DEP078','Formation cybersécurité','2025-04-22 09:15:00',560),('DEP079','Mise en conformité RGPD','2025-04-26 16:30:00',1251),('DEP080','Audit énergétique','2025-05-02 10:20:00',681),('DEP081','Installation LED','2025-05-05 13:35:00',2340),('DEP082','Isolation thermique','2025-05-08 15:50:00',3451),('DEP083','Nouveau système chauffage','2025-05-11 09:40:00',4890),('DEP084','Peinture façade','2025-05-14 12:25:00',1681),('DEP085','Signalétique extérieure','2025-05-17 16:15:00',890),('DEP086','Aménagement parking','2025-05-19 11:05:00',2151),('DEP087','Achat mobilier accueil','2025-03-06 14:50:00',1340),('DEP088','Machine à café bureau','2025-03-09 10:35:00',457),('DEP089','Fontaine à eau','2025-03-12 15:20:00',190),('DEP090','Plantes décoratives','2025-03-16 12:10:00',79),('DEP091','Tableau d\'affichage','2025-03-19 16:40:00',126),('DEP092','Casiers personnels','2025-03-23 09:25:00',680),('DEP093','Vestiaire équipe','2025-03-26 13:55:00',890),('DEP094','Cuisine d\'appoint','2025-03-29 11:15:00',1251),('DEP095','Frais mission commerciale','2025-04-03 17:20:00',1891),('DEP096','Prospection nouveaux clients','2025-04-07 14:30:00',568),('DEP097','Échantillons gratuits','2025-04-10 10:45:00',346),('DEP098','Catalogue produits','2025-04-13 15:05:00',780),('DEP099','Cartes de visite','2025-04-16 12:50:00',90),('DEP100','Tampon entreprise','2025-04-18 09:30:00',46),('DEP101','Papier en-tête','2025-04-21 16:10:00',123),('DEP102','Enveloppes personnalisées','2025-04-23 13:25:00',68),('DEP103','Étiquettes produits','2025-04-26 11:40:00',157),('DEP104','Code-barres','2025-04-28 14:55:00',235),('DEP105','Scanner codes-barres','2025-05-01 10:20:00',457),('DEP106','Imprimante étiquettes','2025-05-04 15:35:00',678),('DEP107','Consommables imprimante','2025-05-06 12:45:00',190),('DEP108','Papier thermique','2025-05-09 09:15:00',146),('DEP109','Cartouches d\'encre','2025-05-12 16:30:00',235),('DEP110','Maintenance imprimantes','2025-05-15 11:50:00',320),('DEP111','Contrat maintenance','2025-05-18 14:10:00',890),('DEP112','Extension garantie','2025-05-21 10:25:00',567),('DEP113','Achat stock housses protection','2025-03-08 13:40:00',2341),('DEP114','Accessoires téléphones','2025-03-11 16:55:00',1890),('DEP115','Chargeurs universels','2025-03-15 12:20:00',1457),('DEP116','Câbles données','2025-03-18 09:35:00',790),('DEP117','Adaptateurs secteur','2025-03-21 15:50:00',678),('DEP118','Batteries externes','2025-03-24 11:05:00',2346),('DEP119','Supports véhicule','2025-03-27 14:40:00',568),('DEP120','Kits piéton Bluetooth','2025-03-30 10:15:00',890),('DEP121','Enceintes portables','2025-04-02 16:25:00',1235),('DEP122','Casques audio gaming','2025-04-06 13:50:00',1567),('DEP123','Microphones streaming','2025-04-09 11:30:00',790),('DEP124','Webcams HD','2025-04-12 15:15:00',1346),('DEP125','Éclairage LED streaming','2025-04-15 12:40:00',457),('DEP126','Fond vert chroma','2025-04-18 09:55:00',190),('DEP127','Trépieds ajustables','2025-04-21 16:20:00',235),('DEP128','Stabilisateurs smartphone','2025-04-24 13:35:00',346),('DEP129','Objectifs macro','2025-04-27 10:50:00',567),('DEP130','Filtres photo','2025-04-29 15:05:00',123),('DEP131','Sacs transport','2025-05-02 12:30:00',290),('DEP132','Mousses protection','2025-05-05 09:45:00',68),('DEP133','Sangles sécurité','2025-05-08 16:00:00',46),('DEP134','Produits nettoyage écrans','2025-05-11 13:25:00',90),('DEP135','Chiffons microfibre','2025-05-14 11:40:00',35),('DEP136','Solutions désinfectantes','2025-05-17 15:55:00',79),('DEP137','Gants manipulation','2025-05-20 12:10:00',23),('DEP138','Blouses protection','2025-05-22 09:20:00',157),('DEP139','Formation premiers secours','2025-03-13 14:35:00',450),('DEP140','Trousse premiers secours','2025-03-17 11:50:00',90),('DEP141','Extincteur portable','2025-03-20 16:05:00',126),('DEP142','Détecteur fumée','2025-03-23 13:20:00',78),('DEP143','Éclairage secours','2025-03-26 10:35:00',235),('DEP144','Plan évacuation','2025-03-29 15:50:00',46),('DEP145','Signalisation sécurité','2025-04-01 12:15:00',168),('DEP146','Caméras surveillance sup','2025-04-04 09:30:00',1891),('DEP147','Disque dur stockage vidéo','2025-04-07 16:45:00',457),('DEP148','Moniteur surveillance','2025-04-10 14:00:00',678),('DEP149','Câblage réseau','2025-04-13 11:15:00',346),('DEP150','Switch réseau 24 ports','2025-04-16 15:30:00',568),('DEP151','Points d\'accès WiFi','2025-04-19 12:45:00',789),('DEP152','Routeur professionnel','2025-04-22 10:00:00',890),('DEP153','Firewall entreprise','2025-04-25 16:15:00',1235),('DEP154','Onduleur serveur','2025-04-28 13:30:00',679),('DEP155','Batteries onduleur','2025-05-01 11:45:00',235),('DEP156','Climatisation serveur','2025-05-04 15:00:00',2891),('DEP157','Baie de brassage','2025-05-07 12:20:00',1456),('DEP158','Panneaux de brassage','2025-05-10 09:35:00',346),('DEP159','Cordons RJ45','2025-05-13 16:50:00',123),('DEP160','Étiquettes réseau','2025-05-16 14:05:00',68),('DEP161','Documentation technique','2025-05-19 11:20:00',190),('DEP162','Formation réseau','2025-05-21 15:35:00',890),('DEP163','Certification technique','2025-03-05 10:50:00',1251),('DEP164','Abonnement magazines pro','2025-03-12 14:25:00',157),('DEP165','Conférence technologique','2025-03-19 16:40:00',568),('DEP166','Webinaire spécialisé','2025-03-25 13:15:00',90),('DEP167','Cours en ligne','2025-04-01 10:30:00',235),('DEP168','Certification qualité','2025-04-08 15:45:00',678),('DEP169','Audit qualité','2025-04-15 12:00:00',890),('DEP170','Manuel procédures','2025-04-22 09:15:00',146),('DEP171','Classeurs documentation','2025-04-29 16:30:00',79),('DEP172','Archivage documents','2025-05-06 13:45:00',235),('DEP173','Destruction documents','2025-05-13 11:00:00',157),('DEP174','Coffre-fort','2025-05-20 15:15:00',567),('DEP175','Assurance documents','2025-03-07 12:30:00',346),('DEP176','Frais notaire','2025-03-14 09:45:00',891),('DEP177','Enregistrement marque','2025-03-21 16:00:00',1235),('DEP178','Dépôt modèle','2025-03-28 13:20:00',457),('DEP179','Brevets innovations','2025-04-04 10:35:00',2890),('DEP180','Recherche antériorité','2025-04-11 15:50:00',678),('DEP181','Conseil propriété intellect','2025-04-18 12:05:00',1568),('DEP182','Contrat licence','2025-04-25 09:20:00',890),('DEP183','Redevances licence','2025-05-02 16:35:00',2346),('DEP184','Droits d\'auteur','2025-05-09 13:50:00',457),('DEP185','Photos stock','2025-05-16 11:05:00',190),('DEP186','Vidéos promo','2025-05-22 15:20:00',1235),('DEP187','Montage vidéo','2025-03-03 12:35:00',568),('DEP188','Effets sonores','2025-03-10 09:50:00',123),('DEP189','Musique libre droits','2025-03-17 16:05:00',235),('DEP190','Voice-over','2025-03-24 13:25:00',346),('DEP191','Traduction contenus','2025-03-31 10:40:00',678),('DEP192','Sous-titrage vidéos','2025-04-07 15:55:00',190),('DEP193','Localisation app','2025-04-14 12:10:00',891),('DEP194','Tests utilisateurs','2025-04-21 09:25:00',457),('DEP195','Développement app mobile','2025-04-28 16:40:00',3451),('DEP196','Publication stores','2025-05-05 13:55:00',235),('DEP197','Maintenance app','2025-05-12 11:10:00',568),('DEP198','Mises à jour','2025-05-19 15:25:00',346),('DEP199','Support technique','2025-05-21 12:40:00',679),('DEP200','Hébergement cloud','2025-05-22 09:55:00',190);
/*!40000 ALTER TABLE `depense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `historique`
--

DROP TABLE IF EXISTS `historique`;
/*!50001 DROP VIEW IF EXISTS `historique`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `historique` AS SELECT 
 1 AS `date`,
 1 AS `somme`,
 1 AS `mouvement`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `produit_vendu_group`
--

DROP TABLE IF EXISTS `produit_vendu_group`;
/*!50001 DROP VIEW IF EXISTS `produit_vendu_group`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `produit_vendu_group` AS SELECT 
 1 AS `SUM(qte)`,
 1 AS `id_produit`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `produit_vendu_group2`
--

DROP TABLE IF EXISTS `produit_vendu_group2`;
/*!50001 DROP VIEW IF EXISTS `produit_vendu_group2`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `produit_vendu_group2` AS SELECT 
 1 AS `somme`,
 1 AS `id_produit`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `produits_vendu`
--

DROP TABLE IF EXISTS `produits_vendu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produits_vendu` (
  `id_pv` varchar(10) NOT NULL,
  `date_de_vente` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `qte` int DEFAULT NULL,
  `id_produit` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_pv`),
  KEY `fq_id_produit` (`id_produit`),
  CONSTRAINT `fq_id_produit` FOREIGN KEY (`id_produit`) REFERENCES `stock` (`id_produit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produits_vendu`
--

LOCK TABLES `produits_vendu` WRITE;
/*!40000 ALTER TABLE `produits_vendu` DISABLE KEYS */;
INSERT INTO `produits_vendu` VALUES ('PROV001','2024-12-15 14:30:00',2,'PRO001'),('PROV002','2024-12-18 09:15:00',1,'PRO005'),('PROV003','2024-12-22 16:45:00',3,'PRO012'),('PROV004','2025-01-08 11:20:00',1,'PRO023'),('PROV005','2025-01-12 13:50:00',2,'PRO034'),('PROV006','2025-01-15 10:30:00',1,'PRO045'),('PROV007','2025-01-22 15:25:00',4,'PRO056'),('PROV008','2025-02-03 12:10:00',2,'PRO067'),('PROV009','2025-02-07 14:40:00',1,'PRO078'),('PROV010','2025-02-14 09:55:00',3,'PRO089'),('PROV011','2025-02-18 16:20:00',2,'PRO100'),('PROV012','2025-02-25 11:35:00',1,'PRO111'),('PROV013','2025-03-02 13:15:00',5,'PRO001'),('PROV014','2025-03-05 10:45:00',2,'PRO002'),('PROV015','2025-03-08 14:20:00',3,'PRO003'),('PROV016','2025-03-12 09:30:00',1,'PRO004'),('PROV017','2025-03-15 16:10:00',4,'PRO006'),('PROV018','2025-03-18 12:50:00',2,'PRO007'),('PROV019','2025-03-22 15:35:00',6,'PRO008'),('PROV020','2025-03-25 11:25:00',1,'PRO009'),('PROV021','2025-03-28 13:40:00',3,'PRO010'),('PROV022','2025-04-01 09:15:00',2,'PRO011'),('PROV023','2025-04-04 14:55:00',4,'PRO013'),('PROV024','2025-04-07 10:20:00',1,'PRO014'),('PROV025','2025-04-10 16:30:00',5,'PRO015'),('PROV026','2025-04-13 12:45:00',2,'PRO016'),('PROV027','2025-04-16 15:10:00',3,'PRO017'),('PROV028','2025-04-19 11:35:00',1,'PRO018'),('PROV029','2025-04-22 13:20:00',7,'PRO019'),('PROV030','2025-04-25 09:50:00',2,'PRO020'),('PROV031','2025-04-28 14:15:00',4,'PRO021'),('PROV032','2025-05-01 10:40:00',3,'PRO022'),('PROV033','2025-05-04 16:25:00',1,'PRO024'),('PROV034','2025-05-07 12:30:00',5,'PRO025'),('PROV035','2025-05-10 15:45:00',2,'PRO026'),('PROV036','2025-05-13 11:10:00',6,'PRO027'),('PROV037','2025-05-16 13:55:00',1,'PRO028'),('PROV038','2025-05-19 09:25:00',3,'PRO029'),('PROV039','2025-05-22 14:40:00',2,'PRO030'),('PROV040','2025-03-03 16:15:00',4,'PRO031'),('PROV041','2025-03-06 10:50:00',1,'PRO032'),('PROV042','2025-03-09 13:25:00',3,'PRO033'),('PROV043','2025-03-13 15:40:00',2,'PRO035'),('PROV044','2025-03-16 11:20:00',5,'PRO036'),('PROV045','2025-03-19 14:05:00',1,'PRO037'),('PROV046','2025-03-23 09:45:00',4,'PRO038'),('PROV047','2025-03-26 16:30:00',2,'PRO039'),('PROV048','2025-03-29 12:15:00',3,'PRO040'),('PROV049','2025-04-02 15:50:00',6,'PRO041'),('PROV050','2025-04-05 10:35:00',1,'PRO042'),('PROV051','2025-04-08 13:20:00',2,'PRO043'),('PROV052','2025-04-11 16:45:00',4,'PRO044'),('PROV053','2025-04-14 11:30:00',1,'PRO046'),('PROV054','2025-04-17 14:15:00',3,'PRO047'),('PROV055','2025-04-20 10:55:00',5,'PRO048'),('PROV056','2025-04-23 15:25:00',2,'PRO049'),('PROV057','2025-04-26 12:40:00',1,'PRO050'),('PROV058','2025-04-29 09:10:00',4,'PRO051'),('PROV059','2025-05-02 16:35:00',3,'PRO052'),('PROV060','2025-05-05 11:50:00',2,'PRO053'),('PROV061','2025-05-08 14:25:00',6,'PRO054'),('PROV062','2025-05-11 10:15:00',1,'PRO055'),('PROV063','2025-05-14 13:45:00',3,'PRO057'),('PROV064','2025-05-17 15:20:00',2,'PRO058'),('PROV065','2025-05-20 12:05:00',4,'PRO059'),('PROV066','2025-03-04 09:30:00',1,'PRO060'),('PROV067','2025-03-07 16:55:00',5,'PRO061'),('PROV068','2025-03-10 11:40:00',2,'PRO062'),('PROV069','2025-03-14 14:10:00',3,'PRO063'),('PROV070','2025-03-17 10:25:00',1,'PRO064'),('PROV071','2025-03-20 15:50:00',4,'PRO065'),('PROV072','2025-03-24 12:35:00',2,'PRO066'),('PROV073','2025-03-27 13:15:00',6,'PRO068'),('PROV074','2025-03-30 09:45:00',1,'PRO069'),('PROV075','2025-04-03 16:20:00',3,'PRO070'),('PROV076','2025-04-06 11:05:00',2,'PRO071'),('PROV077','2025-04-09 14:40:00',5,'PRO072'),('PROV078','2025-04-12 10:30:00',1,'PRO073'),('PROV079','2025-04-15 15:15:00',4,'PRO074'),('PROV080','2025-04-18 12:50:00',3,'PRO075'),('PROV081','2025-04-21 09:25:00',2,'PRO076'),('PROV082','2025-04-24 16:10:00',1,'PRO077'),('PROV083','2025-04-27 11:45:00',6,'PRO079'),('PROV084','2025-04-30 14:30:00',2,'PRO080'),('PROV085','2025-05-03 10:20:00',4,'PRO081'),('PROV086','2025-05-06 15:55:00',1,'PRO082'),('PROV087','2025-05-09 12:40:00',3,'PRO083'),('PROV088','2025-05-12 13:25:00',5,'PRO084'),('PROV089','2025-05-15 09:15:00',2,'PRO085'),('PROV090','2025-05-18 16:00:00',1,'PRO087'),('PROV091','2025-05-21 11:35:00',4,'PRO088'),('PROV092','2025-03-01 14:20:00',3,'PRO090'),('PROV093','2025-03-11 10:45:00',2,'PRO091'),('PROV094','2025-03-21 15:30:00',1,'PRO092'),('PROV095','2025-03-31 12:10:00',5,'PRO093'),('PROV096','2025-04-08 09:50:00',2,'PRO094'),('PROV097','2025-04-18 16:25:00',3,'PRO096'),('PROV098','2025-04-28 11:15:00',1,'PRO097'),('PROV099','2025-05-08 14:55:00',4,'PRO098'),('PROV100','2025-05-18 10:40:00',2,'PRO099'),('PROV101','2025-03-05 15:25:00',6,'PRO101'),('PROV102','2025-03-15 12:50:00',1,'PRO102'),('PROV103','2025-03-25 09:35:00',3,'PRO103'),('PROV104','2025-04-04 16:15:00',2,'PRO104'),('PROV105','2025-04-14 13:40:00',5,'PRO105'),('PROV106','2025-04-24 10:25:00',1,'PRO106'),('PROV107','2025-05-04 15:10:00',4,'PRO107'),('PROV108','2025-05-14 11:55:00',2,'PRO108'),('PROV109','2025-03-02 14:35:00',3,'PRO109'),('PROV110','2025-03-12 09:20:00',1,'PRO110'),('PROV111','2025-03-22 16:45:00',6,'PRO112'),('PROV112','2025-04-01 12:30:00',2,'PRO113'),('PROV113','2025-04-11 15:15:00',4,'PRO114'),('PROV114','2025-04-21 10:05:00',1,'PRO115'),('PROV115','2025-05-01 13:50:00',3,'PRO116'),('PROV116','2025-05-11 11:25:00',5,'PRO117'),('PROV117','2025-05-21 16:10:00',2,'PRO118'),('PROV118','2025-03-08 14:45:00',1,'PRO119'),('PROV119','2025-03-18 10:30:00',4,'PRO120'),('PROV120','2025-03-28 15:20:00',3,'PRO121'),('PROV121','2025-04-07 12:15:00',2,'PRO122'),('PROV122','2025-04-17 09:40:00',6,'PRO123'),('PROV123','2025-04-27 16:35:00',1,'PRO124'),('PROV124','2025-05-07 13:25:00',5,'PRO126'),('PROV125','2025-05-17 10:50:00',2,'PRO127'),('PROV126','2025-03-06 15:45:00',4,'PRO128'),('PROV127','2025-03-16 11:30:00',1,'PRO129'),('PROV128','2025-03-26 14:20:00',3,'PRO130'),('PROV129','2025-04-05 09:55:00',2,'PRO131'),('PROV130','2025-04-15 16:40:00',5,'PRO132'),('PROV131','2025-04-25 12:25:00',1,'PRO133'),('PROV132','2025-05-05 15:10:00',4,'PRO134'),('PROV133','2025-05-15 10:35:00',3,'PRO135'),('PROV134','2025-03-09 13:50:00',2,'PRO137'),('PROV135','2025-03-19 11:15:00',6,'PRO138'),('PROV136','2025-03-29 16:05:00',1,'PRO139'),('PROV137','2025-04-08 14:40:00',4,'PRO140'),('PROV138','2025-04-18 10:25:00',2,'PRO141'),('PROV139','2025-04-28 15:55:00',3,'PRO142'),('PROV140','2025-05-08 12:45:00',5,'PRO143'),('PROV141','2025-05-18 09:30:00',1,'PRO144'),('PROV142','2025-03-03 16:20:00',4,'PRO145'),('PROV143','2025-03-13 13:35:00',2,'PRO146'),('PROV144','2025-03-23 10:10:00',3,'PRO147'),('PROV145','2025-04-02 15:45:00',1,'PRO148'),('PROV146','2025-04-12 12:30:00',6,'PRO149'),('PROV147','2025-04-22 09:15:00',2,'PRO150'),('PROV148','2025-05-02 16:50:00',4,'PRO151'),('PROV149','2025-05-12 11:40:00',3,'PRO152'),('PROV150','2025-05-22 14:25:00',5,'PRO153'),('PROV151','2025-03-07 10:55:00',1,'PRO154'),('PROV152','2025-03-17 15:30:00',2,'PRO155'),('PROV153','2025-03-27 12:20:00',4,'PRO156'),('PROV154','2025-04-06 09:45:00',3,'PRO157'),('PROV155','2025-04-16 16:15:00',6,'PRO158'),('PROV156','2025-04-26 13:05:00',1,'PRO159'),('PROV157','2025-05-06 10:40:00',5,'PRO160'),('PROV158','2025-05-16 15:25:00',2,'PRO161'),('PROV159','2025-03-04 12:50:00',4,'PRO162'),('PROV160','2025-03-14 09:35:00',1,'PRO163'),('PROV161','2025-03-24 16:10:00',3,'PRO164'),('PROV162','2025-04-03 13:45:00',2,'PRO165'),('PROV163','2025-04-13 11:20:00',5,'PRO166'),('PROV164','2025-04-23 14:55:00',1,'PRO167'),('PROV165','2025-05-03 10:30:00',4,'PRO168'),('PROV166','2025-05-13 15:15:00',3,'PRO169'),('PROV167','2025-03-10 12:40:00',6,'PRO170'),('PROV168','2025-03-20 09:25:00',2,'PRO171'),('PROV169','2025-03-30 16:00:00',1,'PRO172'),('PROV170','2025-04-09 13:35:00',4,'PRO173'),('PROV171','2025-04-19 11:10:00',3,'PRO174'),('PROV172','2025-04-29 14:45:00',5,'PRO175'),('PROV173','2025-05-09 10:20:00',2,'PRO176'),('PROV174','2025-05-19 15:55:00',1,'PRO177'),('PROV175','2025-03-11 12:15:00',4,'PRO178'),('PROV176','2025-03-21 09:50:00',3,'PRO179'),('PROV177','2025-03-31 16:25:00',2,'PRO180'),('PROV178','2025-04-10 13:10:00',6,'PRO181'),('PROV179','2025-04-20 10:45:00',1,'PRO182'),('PROV180','2025-04-30 15:20:00',5,'PRO183'),('PROV181','2025-05-10 12:35:00',2,'PRO184'),('PROV182','2025-05-20 09:10:00',4,'PRO185'),('PROV183','2025-03-01 16:45:00',3,'PRO186'),('PROV184','2025-03-11 11:30:00',1,'PRO187'),('PROV185','2025-03-21 14:05:00',2,'PRO188'),('PROV186','2025-03-31 10:40:00',5,'PRO189'),('PROV187','2025-04-10 15:15:00',4,'PRO190'),('PROV188','2025-04-20 12:50:00',1,'PRO191'),('PROV189','2025-04-30 09:25:00',3,'PRO192'),('PROV190','2025-05-10 16:00:00',2,'PRO193'),('PROV191','2025-05-20 13:35:00',6,'PRO194'),('PROV192','2025-03-05 11:20:00',1,'PRO195'),('PROV193','2025-03-15 14:55:00',4,'PRO196'),('PROV194','2025-03-25 10:30:00',2,'PRO197'),('PROV195','2025-04-04 15:05:00',3,'PRO198'),('PROV196','2025-04-14 12:40:00',5,'PRO199'),('PROV197','2025-04-24 09:15:00',1,'PRO200'),('PROV198','2025-05-04 16:50:00',4,'PRO001'),('PROV199','2025-05-14 11:25:00',2,'PRO005'),('PROV200','2025-05-22 14:10:00',3,'PRO010');
/*!40000 ALTER TABLE `produits_vendu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `id_produit` varchar(20) NOT NULL,
  `nom` varchar(40) DEFAULT NULL,
  `pu` int DEFAULT NULL,
  `id_type` varchar(10) DEFAULT NULL,
  `qt` int NOT NULL,
  PRIMARY KEY (`id_produit`),
  UNIQUE KEY `uq_id_produit` (`id_produit`),
  KEY `FK_id_type` (`id_type`),
  CONSTRAINT `FK_id_type` FOREIGN KEY (`id_type`) REFERENCES `type_produit` (`id_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES ('PRO001','iPhone 15 Pro',1300,'TYP001',45),('PRO002','Samsung Galaxy S24',900,'TYP001',32),('PRO003','Google Pixel 8',700,'TYP001',28),('PRO004','OnePlus 12',800,'TYP001',15),('PRO005','Xiaomi 14',650,'TYP001',22),('PRO006','iPad Pro 12.9',1300,'TYP002',18),('PRO007','Samsung Galaxy Tab S9',850,'TYP002',25),('PRO008','iPad Air 5',700,'TYP002',33),('PRO009','Microsoft Surface Pro 9',1200,'TYP002',12),('PRO010','Lenovo Tab P12',500,'TYP002',19),('PRO011','MacBook Pro 16',2900,'TYP003',8),('PRO012','Dell XPS 15',2000,'TYP003',14),('PRO013','HP Spectre x360',1600,'TYP003',11),('PRO014','Lenovo ThinkPad X1',2200,'TYP003',9),('PRO015','ASUS ZenBook Pro',1800,'TYP003',16),('PRO016','LG UltraGear 27GL850',400,'TYP004',42),('PRO017','Samsung Odyssey G7',600,'TYP004',28),('PRO018','ASUS ROG Swift PG279Q',700,'TYP004',21),('PRO019','Dell S2721DGF',330,'TYP004',35),('PRO020','BenQ EX2780Q',450,'TYP004',17),('PRO021','Logitech MX Master 3S',110,'TYP005',67),('PRO022','Corsair K95 RGB Platinum',200,'TYP005',23),('PRO023','Razer DeathStalker V2 Pro',250,'TYP005',31),('PRO024','SteelSeries Apex Pro',180,'TYP005',29),('PRO025','HyperX Alloy Elite RGB',130,'TYP005',44),('PRO026','iPhone 14',1000,'TYP001',58),('PRO027','Samsung Galaxy A54',450,'TYP001',73),('PRO028','Redmi Note 12 Pro',330,'TYP001',86),('PRO029','Nothing Phone 2',600,'TYP001',19),('PRO030','Sony Xperia 1 V',1400,'TYP001',7),('PRO031','iPad 10',450,'TYP002',51),('PRO032','Galaxy Tab A8',230,'TYP002',64),('PRO033','Huawei MatePad Pro',600,'TYP002',16),('PRO034','Amazon Fire HD 10',150,'TYP002',92),('PRO035','Lenovo Tab M10',180,'TYP002',47),('PRO036','MacBook Air M2',1500,'TYP003',21),('PRO037','ASUS VivoBook S15',900,'TYP003',33),('PRO038','Acer Swift 3',700,'TYP003',41),('PRO039','HP Pavilion 15',800,'TYP003',38),('PRO040','MSI Modern 14',650,'TYP003',26),('PRO041','AOC 24G2U',180,'TYP004',89),('PRO042','Philips 276E8VJSB',200,'TYP004',54),('PRO043','MSI Optix MAG274QRF',330,'TYP004',31),('PRO044','ViewSonic VP2458',150,'TYP004',76),('PRO045','Gigabyte M27Q',280,'TYP004',43),('PRO046','Apple Magic Keyboard',180,'TYP005',39),('PRO047','Microsoft Surface Keyboard',100,'TYP005',52),('PRO048','Keychron K2',90,'TYP005',71),('PRO049','Das Keyboard 4 Professional',170,'TYP005',18),('PRO050','Ducky One 2 Mini',110,'TYP005',34),('PRO051','iPhone SE 3',530,'TYP001',41),('PRO052','Motorola Edge 40',600,'TYP001',27),('PRO053','Realme GT 3',700,'TYP001',23),('PRO054','Vivo X90 Pro',1000,'TYP001',14),('PRO055','Oppo Find X6',850,'TYP001',18),('PRO056','Surface Go 3',400,'TYP002',29),('PRO057','Xiaomi Pad 6',350,'TYP002',45),('PRO058','TCL Tab 10s',200,'TYP002',62),('PRO059','Honor Pad 8',250,'TYP002',37),('PRO060','Nokia T20',180,'TYP002',56),('PRO061','Framework Laptop',1400,'TYP003',5),('PRO062','System76 Lemur Pro',1250,'TYP003',8),('PRO063','Razer Blade 15',2500,'TYP003',3),('PRO064','Alienware m15 R7',2200,'TYP003',6),('PRO065','Origin Millennium',3500,'TYP003',2),('PRO066','ASUS ProArt PA278QV',350,'TYP004',28),('PRO067','Acer Predator X27',2000,'TYP004',4),('PRO068','HP Z27',300,'TYP004',36),('PRO069','Dell UltraSharp U2720Q',550,'TYP004',19),('PRO070','LG 27UN850-W',400,'TYP004',25),('PRO071','Corsair K70 RGB MK.2',160,'TYP005',47),('PRO072','Razer Huntsman Elite',200,'TYP005',32),('PRO073','SteelSeries Apex 7',150,'TYP005',41),('PRO074','HyperX Alloy Origins',100,'TYP005',58),('PRO075','ROCCAT Vulcan 122',180,'TYP005',24),('PRO076','Honor Magic 5 Pro',900,'TYP001',16),('PRO077','Fairphone 5',700,'TYP001',21),('PRO078','Asus ROG Phone 7',1200,'TYP001',9),('PRO079','Red Magic 8 Pro',800,'TYP001',13),('PRO080','Black Shark 5 Pro',700,'TYP001',11),('PRO081','Boox Tab Ultra',600,'TYP002',15),('PRO082','reMarkable 2',400,'TYP002',22),('PRO083','Kindle Scribe',340,'TYP002',38),('PRO084','Supernote A5 X',460,'TYP002',17),('PRO085','Kobo Elipsa 2E',400,'TYP002',26),('PRO086','GPD Win 4',1000,'TYP003',7),('PRO087','Steam Deck',650,'TYP003',12),('PRO088','ASUS ROG Flow X13',1800,'TYP003',9),('PRO089','MSI GS66 Stealth',2300,'TYP003',4),('PRO090','Gigabyte Aero 17',2800,'TYP003',3),('PRO091','Samsung M8',700,'TYP004',23),('PRO092','Apple Studio Display',1600,'TYP004',8),('PRO093','Dell C3422WE',1000,'TYP004',12),('PRO094','Ultrawide LG 38WN95C',1300,'TYP004',7),('PRO095','Samsung Odyssey Neo G9',2500,'TYP004',2),('PRO096','Logitech G915 TKL',230,'TYP005',35),('PRO097','Anne Pro 2',80,'TYP005',67),('PRO098','Drop CTRL',200,'TYP005',19),('PRO099','Varmilo VA87M',140,'TYP005',28),('PRO100','Leopold FC750R',150,'TYP005',31),('PRO101','Poco X5 Pro',350,'TYP001',54),('PRO102','CMF Phone 1',200,'TYP001',83),('PRO103','Tecno Phantom V',600,'TYP001',19),('PRO104','Infinix Zero 30',300,'TYP001',47),('PRO105','Doogee S100',250,'TYP001',32),('PRO106','Teclast T50',190,'TYP002',41),('PRO107','Chuwi HiPad X',230,'TYP002',35),('PRO108','Alldocube iPlay 50',160,'TYP002',58),('PRO109','UNISOC Tiger T610',140,'TYP002',67),('PRO110','Blackview Tab 13',200,'TYP002',44),('PRO111','Clevo NH58RCQ',1200,'TYP003',11),('PRO112','Tongfang GK5NR0O',900,'TYP003',16),('PRO113','Metabox Alpha-X',1700,'TYP003',7),('PRO114','Eluktronics MECH-15',1500,'TYP003',9),('PRO115','XMG Core 15',1300,'TYP003',12),('PRO116','Cooler Master GM27-CF',200,'TYP004',52),('PRO117','Nixeus EDG 27',300,'TYP004',33),('PRO118','Pixio PX277 Prime',250,'TYP004',41),('PRO119','Monoprice 27in CrystalPro',180,'TYP004',59),('PRO120','Sceptre C305B-200UN',230,'TYP004',46),('PRO121','Akko 3108 World Tour',90,'TYP005',73),('PRO122','KBDfans Tofu65',160,'TYP005',22),('PRO123','GMMK Pro',170,'TYP005',27),('PRO124','Mode SixtyFive',400,'TYP005',8),('PRO125','Iron165 R2',550,'TYP005',4),('PRO126','Cubot KingKong 9',180,'TYP001',38),('PRO127','Ulefone Armor 22',220,'TYP001',29),('PRO128','Oukitel WP30',160,'TYP001',51),('PRO129','AGM G2 Guardian',300,'TYP001',24),('PRO130','Conquest S20',400,'TYP001',16),('PRO131','Toscido X109',150,'TYP002',63),('PRO132','Pritom K7',100,'TYP002',87),('PRO133','Vankyo S30',120,'TYP002',74),('PRO134','Dragon Touch K10',130,'TYP002',68),('PRO135','Yestel X2',90,'TYP002',91),('PRO136','One-Netbook 4',1900,'TYP003',5),('PRO137','GPD Pocket 3',1300,'TYP003',8),('PRO138','Chuwi MiniBook X',500,'TYP003',18),('PRO139','TopJoy Falcon',800,'TYP003',13),('PRO140','Planet Computers Astro',900,'TYP003',10),('PRO141','KOORUI 24E3',90,'TYP004',94),('PRO142','ASUS VP249HE',110,'TYP004',82),('PRO143','MSI Pro MP161',200,'TYP004',47),('PRO144','Portable ASUS ZenScreen',250,'TYP004',36),('PRO145','InnoView 15.6',180,'TYP004',58),('PRO146','Nuphy Air60',110,'TYP005',45),('PRO147','Keydous NJ80',90,'TYP005',62),('PRO148','Womier K87',80,'TYP005',76),('PRO149','Epomaker SK61',70,'TYP005',89),('PRO150','RK Royal Kludge RK61',60,'TYP005',95),('PRO151','Redmi 13C',130,'TYP001',71),('PRO152','Samsung Galaxy A15',200,'TYP001',56),('PRO153','Realme C67',160,'TYP001',64),('PRO154','Tecno Spark 20',120,'TYP001',78),('PRO155','Infinix Hot 40',140,'TYP001',69),('PRO156','Lenovo Tab M8',100,'TYP002',84),('PRO157','Amazon Fire 7',60,'TYP002',127),('PRO158','Walmart Onn 8',80,'TYP002',103),('PRO159','Hoozo 10',90,'TYP002',96),('PRO160','Acer Iconia One 7',70,'TYP002',112),('PRO161','Laptop BMAX Y11',300,'TYP003',31),('PRO162','Jumper EZbook X3',250,'TYP003',38),('PRO163','TECLAST F7 Plus 3',330,'TYP003',25),('PRO164','Yepo 737A6',200,'TYP003',47),('PRO165','KUU A8S',280,'TYP003',34),('PRO166','Acer SB220Q',80,'TYP004',108),('PRO167','HP 22f',90,'TYP004',97),('PRO168','LG 22MK430H',100,'TYP004',87),('PRO169','Samsung F22T350',110,'TYP004',79),('PRO170','BenQ GW2283',120,'TYP004',73),('PRO171','Redragon K552',40,'TYP005',134),('PRO172','Havit KB395L',30,'TYP005',156),('PRO173','Omoton K8',35,'TYP005',142),('PRO174','AmazonBasics KU-0833',20,'TYP005',189),('PRO175','Logitech K120',25,'TYP005',167),('PRO176','Nokia C32',90,'TYP001',93),('PRO177','Wiko Y82',80,'TYP001',104),('PRO178','Alcatel 1S',100,'TYP001',86),('PRO179','ZTE Blade A72',110,'TYP001',77),('PRO180','TCL 305i',70,'TYP001',118),('PRO181','Huawei MatePad SE',150,'TYP002',59),('PRO182','Oscal Pad 15',130,'TYP002',71),('PRO183','DOOGEE T30 Ultra',190,'TYP002',48),('PRO184','UMIDIGI A15 Tab',140,'TYP002',65),('PRO185','Blackview Tab 16',170,'TYP002',54),('PRO186','CHUWI GemiBook XPro',380,'TYP003',23),('PRO187','Teclast F15 Plus 2',320,'TYP003',29),('PRO188','Jumper EZbook S5',360,'TYP003',26),('PRO189','BMAX B4 Plus',290,'TYP003',33),('PRO190','KUU K2s',270,'TYP003',37),('PRO191','Kogan 24\" Curved',150,'TYP004',61),('PRO192','Westinghouse WM24FX9019',140,'TYP004',67),('PRO193','Philips 243V5LHAB',130,'TYP004',74),('PRO194','Hannspree HC240HXB',120,'TYP004',81),('PRO195','Sceptre E248W-19203R',110,'TYP004',88),('PRO196','KLIM Chroma',50,'TYP005',119),('PRO197','VicTsing PC257',45,'TYP005',128),('PRO198','Jelly Comb KS-G08',40,'TYP005',137),('PRO199','Arteck HB030B',35,'TYP005',146),('PRO200','Anker Ultra Compact',30,'TYP005',158);
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_produit`
--

DROP TABLE IF EXISTS `type_produit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_produit` (
  `id_type` varchar(10) NOT NULL,
  `nom_type` varchar(20) DEFAULT NULL,
  `id_cli` varchar(10) NOT NULL,
  UNIQUE KEY `id_type` (`id_type`),
  KEY `FK_id_client` (`id_cli`),
  CONSTRAINT `FK_id_client` FOREIGN KEY (`id_cli`) REFERENCES `client` (`id_cli`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_produit`
--

LOCK TABLES `type_produit` WRITE;
/*!40000 ALTER TABLE `type_produit` DISABLE KEYS */;
INSERT INTO `type_produit` VALUES ('TYP001','Smartphones','CLI001'),('TYP002','Tablettes','CLI001'),('TYP003','Ordinateurs p','CLI001'),('TYP004','Écrans','CLI001'),('TYP005','Claviers','CLI001');
/*!40000 ALTER TABLE `type_produit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `historique`
--

/*!50001 DROP VIEW IF EXISTS `historique`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `historique` AS select `pv`.`date_de_vente` AS `date`,(`s`.`pu` * `pv`.`qte`) AS `somme`,'gain' AS `mouvement` from (`produits_vendu` `pv` join `stock` `s` on((`s`.`id_produit` = `pv`.`id_produit`))) union all select `depense`.`date_dep` AS `date`,`depense`.`somme_dep` AS `somme`,'d�pense' AS `mouvement` from `depense` order by `date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `produit_vendu_group`
--

/*!50001 DROP VIEW IF EXISTS `produit_vendu_group`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `produit_vendu_group` AS select sum(`produits_vendu`.`qte`) AS `SUM(qte)`,`produits_vendu`.`id_produit` AS `id_produit` from `produits_vendu` group by `produits_vendu`.`id_produit` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `produit_vendu_group2`
--

/*!50001 DROP VIEW IF EXISTS `produit_vendu_group2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `produit_vendu_group2` AS select sum(`produits_vendu`.`qte`) AS `somme`,`produits_vendu`.`id_produit` AS `id_produit` from `produits_vendu` group by `produits_vendu`.`id_produit` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-22 13:23:03
