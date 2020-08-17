
# SQL
- CREATE DATABASE sims_db CHARACTER SET utf8;

```SQL
studentstudentstudentCREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `English` int NOT NULL,
  `Python` int NOT NULL,
  `C` int NOT NULL,
  `Total_score` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
SELECT * FROM agent.user;
```



````SQL
INSERT INTO `sims_db`.`student` (`id`, `name`, `English`, `Python`, `C`, `Total_score`) VALUES ('1', 'zhangsan', '100', '100', '100', '300');
INSERT INTO `sims_db`.`student` (`id`, `name`, `English`, `Python`, `C`, `Total_score`) VALUES ('2', 'xiaoming', '99', '99', '99', '297');
INSERT INTO `sims_db`.`student` (`id`, `name`, `English`, `Python`, `C`, `Total_score`) VALUES ('3', 'xiaoliang', '60', '60', '60', '180');
INSERT INTO `sims_db`.`student` (`id`, `name`, `English`, `Python`, `C`, `Total_score`) VALUES ('4', 'lisi', '100', '100', '100', '300');
INSERT INTO `sims_db`.`student` (`id`, `name`, `English`, `Python`, `C`, `Total_score`) VALUES ('5', 'wangwu', '60', '60', '60', '180');
INSERT INTO `sims_db`.`student` (`id`, `name`, `English`, `Python`, `C`, `Total_score`) VALUES ('6', 'xiaoliu', '50', '50', '50', '50');
INSERT INTO `sims_db`.`student` (`id`, `name`, `English`, `Python`, `C`, `Total_score`) VALUES ('7', 'zhouqi', '70', '70', '70', '210');
````


