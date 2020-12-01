CREATE TABLE `category` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(30) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`),
    UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `nutriment` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(45) NOT NULL,
    `url` varchar(200) NOT NULL,
    `nutriscore` varchar(1) NOT NULL,
    `category` int NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`),
    UNIQUE KEY `url_UNIQUE` (`url`),
    KEY `fk_nutriment_category_idx` (`category`),
    CONSTRAINT `fk_nutriment_category` FOREIGN KEY (`category`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci