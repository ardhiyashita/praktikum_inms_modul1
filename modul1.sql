/*
SQLyog Ultimate - MySQL GUI v8.21 
MySQL - 5.5.5-10.4.11-MariaDB-log : Database - 12_mb_2005551007
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`12_mb_2005551007` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `12_mb_2005551007`;

/*Table structure for table `tb_pertandingan` */

DROP TABLE IF EXISTS `tb_pertandingan`;

CREATE TABLE `tb_pertandingan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_peserta_a` int(11) DEFAULT NULL,
  `id_peserta_b` int(11) DEFAULT NULL,
  `hasil` varchar(50) DEFAULT NULL,
  `mulai` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `selesai` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  KEY `FK_peserta_a` (`id_peserta_a`),
  KEY `FK_peserta_b` (`id_peserta_b`),
  CONSTRAINT `FK_peserta_a` FOREIGN KEY (`id_peserta_a`) REFERENCES `tb_peserta` (`id`),
  CONSTRAINT `FK_peserta_b` FOREIGN KEY (`id_peserta_b`) REFERENCES `tb_peserta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_pertandingan` */

insert  into `tb_pertandingan`(`id`,`id_peserta_a`,`id_peserta_b`,`hasil`,`mulai`,`selesai`) values (3,1,3,'pemenang didapatkan','2022-03-05 16:40:15','2022-03-05 16:40:15'),(5,2,3,NULL,'2022-03-05 12:37:39','0000-00-00 00:00:00'),(6,2,1,NULL,'2022-03-05 13:42:32','2022-03-05 13:42:32'),(8,1,2,'NULL','2022-03-05 14:09:38','0000-00-00 00:00:00'),(9,1,2,'pemenang didapatkan','2022-03-05 16:04:44','2022-03-05 16:04:44'),(12,5,6,'terdapat pemenang','2022-03-05 19:43:22','2022-03-05 19:43:22');

/*Table structure for table `tb_peserta` */

DROP TABLE IF EXISTS `tb_peserta`;

CREATE TABLE `tb_peserta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_depan` varchar(255) DEFAULT NULL,
  `nama_belakang` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `no_telp` varchar(13) DEFAULT NULL,
  `id_rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_tb_peserta` (`id_rank`),
  CONSTRAINT `FK_tb_peserta` FOREIGN KEY (`id_rank`) REFERENCES `tb_rank` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_peserta` */

insert  into `tb_peserta`(`id`,`nama_depan`,`nama_belakang`,`alamat`,`no_telp`,`id_rank`) values (1,'ardhiya','shita','sesetan','000',1),(2,'deva','vedanty','sesetan','111',3),(3,'putu','vedanty','pakusari','222',6),(5,'tata','nofera','kuta','333',2),(6,'rani','sania','gang banteng','555',1);

/*Table structure for table `tb_rank` */

DROP TABLE IF EXISTS `tb_rank`;

CREATE TABLE `tb_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank` varchar(50) DEFAULT NULL,
  `deskripsi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_rank` */

insert  into `tb_rank`(`id`,`rank`,`deskripsi`) values (1,'Penyisihan','Perserta Babak penyisihan pertandingan catur'),(2,'16 besar','Masuk ke dalam peringkat 16 Besar pada pertandingan'),(3,'8 besar','Masuk ke dalam peringkat 8 Besar pada pertandingan'),(4,'4 besar','Masuk ke dalam peringkat 4 Besar (Semifinal) pada pertandingan'),(5,'2 besar','Masuk ke dalam peringkat 2 Besar (Final) pada pertandingan'),(6,'Juara 2','Juara Kedua Pertandingan Catur'),(7,'Juara 1','Juara Pertama Pertandingan Catur');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
