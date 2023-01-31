-- MySQL Script generated by MySQL Workbench
-- Tue Jan 24 15:46:56 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema database_opendeurdag
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema database_opendeurdag
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `database_opendeurdag` DEFAULT CHARACTER SET utf8 ;
USE `database_opendeurdag` ;

-- -----------------------------------------------------
-- Table `database_opendeurdag`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_opendeurdag`.`users` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `name` TEXT(18) NOT NULL,
  `last_name` TEXT(18) NOT NULL,
  `email_address` TEXT(38) NOT NULL,
  `email_child` TEXT(38) NOT NULL,
  `age_child` INT NOT NULL,
  `direction` TEXT(50) NOT NULL,
  `contact` TINYINT NOT NULL,
  `phone_number` INT NOT NULL,
  `code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_opendeurdag`.`questions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_opendeurdag`.`questions` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `question` TEXT(45) NOT NULL,
  `multy` INT(45) NOT NULL,
   `clas` TEXT(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_opendeurdag`.`results`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_opendeurdag`.`results` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `questions_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  `result` TINYINT NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database_opendeurdag`.`answers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database_opendeurdag`.`answers` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `answer` TEXT(50) NOT NULL,
  `questions_id` INT NOT NULL,
  `correct` TEXT(50) NOT NULL,
  `possible` TEXT(50) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;