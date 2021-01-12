
CREATE TABLE `category` (
  `idcategory` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcategory`),
  UNIQUE KEY `idcategory_UNIQUE` (`idcategory` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE `product` (
  `idproduct` INT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `url` VARCHAR(200) NOT NULL,
  `nutriscore` VARCHAR(1) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idproduct`),
  UNIQUE KEY `idproduct_UNIQUE` (`idproduct` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  UNIQUE INDEX `url_UNIQUE` (`url` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE `open_food_fact`.`category_product` (
  `category` INT NOT NULL,
  `product` INT NOT NULL,
  PRIMARY KEY (`category`, `product`),
  INDEX `product_idx` (`product` ASC) VISIBLE,
  CONSTRAINT `category`
    FOREIGN KEY (`category`)
    REFERENCES `open_food_fact`.`category` (`idcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product`
    FOREIGN KEY (`product`)
    REFERENCES `open_food_fact`.`product` (`idproduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `open_food_fact`.`favorite` (
  `idfavorite` INT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idfavorite`),
  UNIQUE INDEX `idfavorite_UNIQUE` (`idfavorite` ASC) VISIBLE);
