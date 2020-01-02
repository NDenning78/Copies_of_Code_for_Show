-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema belt_exam
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `belt_exam` ;

-- -----------------------------------------------------
-- Schema belt_exam
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `belt_exam` DEFAULT CHARACTER SET utf8 ;
USE `belt_exam` ;

-- -----------------------------------------------------
-- Table `belt_exam`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `belt_exam`.`users` ;

CREATE TABLE IF NOT EXISTS `belt_exam`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt_exam`.`quotes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `belt_exam`.`quotes` ;

CREATE TABLE IF NOT EXISTS `belt_exam`.`quotes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `author` VARCHAR(255) NOT NULL,
  `content` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_quotes_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_quotes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `belt_exam`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `belt_exam`.`likes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `belt_exam`.`likes` ;

CREATE TABLE IF NOT EXISTS `belt_exam`.`likes` (
  `user_id` INT(11) NOT NULL,
  `quote_id` INT(11) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  INDEX `fk_users_has_quotes_quotes1_idx` (`quote_id` ASC) VISIBLE,
  INDEX `fk_users_has_quotes_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_quotes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `belt_exam`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_quotes_quotes1`
    FOREIGN KEY (`quote_id`)
    REFERENCES `belt_exam`.`quotes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
