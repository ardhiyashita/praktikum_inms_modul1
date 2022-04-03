/*
SQLyog Ultimate - MySQL GUI v8.21 
MySQL - 5.5.5-10.4.11-MariaDB-log : Database - db_modul1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_modul1` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `db_modul1`;

/*Table structure for table `tb_sync` */

DROP TABLE IF EXISTS `tb_sync`;

CREATE TABLE `tb_sync` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_tabel` int(11) DEFAULT NULL,
  `aksi` varchar(255) DEFAULT NULL,
  `sinkronisasi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_sync` */

insert  into `tb_sync`(`id`,`id_tabel`,`aksi`,`sinkronisasi`) values (1,1,'insert','telah sinkron'),(2,2,'insert','telah sinkron'),(5,1,'update','telah sinkron'),(6,2,'update','telah sinkron'),(7,1,'delete','telah sinkron'),(9,6,'insert',NULL);

/*Table structure for table `tb_transaksi` */

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pegawai` varchar(255) NOT NULL,
  `customer` varchar(255) NOT NULL,
  `barang` varchar(255) NOT NULL,
  `harga` varchar(255) NOT NULL,
  `status_transaksi` varchar(255) NOT NULL,
  `tgl_transaksi` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_transaksi` */

insert  into `tb_transaksi`(`id`,`pegawai`,`customer`,`barang`,`harga`,`status_transaksi`,`tgl_transaksi`,`updated_at`,`deleted_at`) values (6,'rangga','rina','roti','12000','pending','2022-03-19 23:40:06','0000-00-00 00:00:00',NULL);

/* Trigger structure for table `tb_transaksi` */

DELIMITER $$

/*!50003 DROP TRIGGER*//*!50032 IF EXISTS */ /*!50003 `sync_insert` */$$

/*!50003 CREATE */ /*!50017 DEFINER = 'root'@'localhost' */ /*!50003 TRIGGER `sync_insert` AFTER INSERT ON `tb_transaksi` FOR EACH ROW BEGIN
	
	DECLARE id_sync int;
	SET id_sync = (SELECT MAX(id) FROM tb_transaksi);
	INSERT INTO tb_sync (id_tabel, aksi) VALUES (id_sync, 'insert');
    END */$$


DELIMITER ;

/* Trigger structure for table `tb_transaksi` */

DELIMITER $$

/*!50003 DROP TRIGGER*//*!50032 IF EXISTS */ /*!50003 `sync_update` */$$

/*!50003 CREATE */ /*!50017 DEFINER = 'root'@'localhost' */ /*!50003 TRIGGER `sync_update` AFTER UPDATE ON `tb_transaksi` FOR EACH ROW BEGIN
    
	DECLARE id_sync INT;
	SET id_sync = (SELECT id FROM tb_transaksi WHERE updated_at = now());
	INSERT INTO tb_sync (id_tabel, aksi) VALUES (id_sync, 'update');
    END */$$


DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
