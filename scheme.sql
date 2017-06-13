
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `j_issues_list`
-- ----------------------------
DROP TABLE IF EXISTS `j_issues_list`;
CREATE TABLE `j_issues_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` varchar(50) NOT NULL,
  `issuetype` varchar(50) NOT NULL,
  `summary` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `versiontype` varchar(50) NOT NULL,
  `field` varchar(50) NOT NULL,
  `module` varchar(50) NOT NULL,
  `assignee` varchar(50) NOT NULL,
  `versions` varchar(50) NOT NULL,
  `severity` varchar(50) NOT NULL,
  `reproduce` varchar(50) NOT NULL,
  `f_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `delete_flag` tinyint(2) DEFAULT '0',
  `raw_add_time` timestamp NULL DEFAULT NULL,
  `raw_update_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
