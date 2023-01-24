-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 07 jun 2022 om 11:33
-- Serverversie: 10.4.21-MariaDB
-- PHP-versie: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `first_test`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `answer`
--

CREATE TABLE `answer` (
  `ID` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `answertext` text NOT NULL,
  `juist_ant` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `answer`
--

INSERT INTO `answer` (`ID`, `question_id`, `answertext`, `juist_ant`) VALUES
(1, 1, '-5', 1),
(2, 2, '5', 0),
(3, 2, '10', 1),
(4, 2, '3', 0),
(5, 3, '10', 1),
(6, 3, '15', 0),
(7, 3, '20', 0),
(8, 4, '2', 1),
(9, 4, '- 2', 1),
(10, 4, '8', 0),
(11, 5, '6', 0),
(12, 5, '8', 0),
(13, 6, '10', 1),
(14, 18, '13', 1),
(15, 14, 'de', 1),
(16, 15, 'j', 1),
(17, 15, 'f', 0),
(18, 15, 'f', 0),
(19, 16, 'f', 0),
(20, 16, 'j', 1),
(21, 16, 'f', 0),
(22, 17, 'f', 0),
(23, 17, 'f', 0),
(24, 17, 'j', 1),
(25, 18, '8', 0),
(26, 19, 'f', 0),
(27, 19, 'j', 1),
(28, 19, 'f', 0),
(29, 20, 'test juist', 1),
(30, 20, 'test fout ', 0),
(31, 20, 'test fout', 0),
(32, 7, 'juist', 1),
(33, 8, 'juist', 1),
(34, 9, 'juist', 1),
(35, 10, 'juist', 1),
(36, 11, 'juist', 1),
(37, 12, 'juist', 1),
(38, 13, 'juist', 1);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `questions`
--

CREATE TABLE `questions` (
  `ID` int(11) NOT NULL,
  `vraag` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Gegevens worden geëxporteerd voor tabel `questions`
--

INSERT INTO `questions` (`ID`, `vraag`) VALUES
(1, 'wat is 3 - 8'),
(2, '9 + 1?'),
(3, 'Wat is 5 * 2'),
(4, '2 tot de 2de'),
(5, '7-1'),
(6, '5*2'),
(7, 'vraag 7'),
(8, 'vraag 8'),
(9, 'vraag 9'),
(10, 'vraag 10'),
(11, 'vraag 11'),
(12, 'vraag 12'),
(13, 'vraag 13'),
(14, 'het of de gip'),
(15, 'vraag 15'),
(16, 'vraag 16'),
(17, 'vraag 17'),
(18, '7+6'),
(19, 'vraag 19'),
(20, 'vraag 20');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `results`
--

CREATE TABLE `results` (
  `ID` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `result` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `naam` text NOT NULL,
  `email` text NOT NULL,
  `contact` smallint(6) NOT NULL,
  `achternaam` text NOT NULL,
  `leeftijd` int(11) NOT NULL,
  `richting` text NOT NULL,
  `naam_ouder` text NOT NULL,
  `email_ouder` text NOT NULL,
  `telefoonnummer` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `answer`
--
ALTER TABLE `answer`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `question_id` (`question_id`);

--
-- Indexen voor tabel `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`ID`);

--
-- Indexen voor tabel `results`
--
ALTER TABLE `results`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `question_id` (`question_id`);

--
-- Indexen voor tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `answer`
--
ALTER TABLE `answer`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT voor een tabel `questions`
--
ALTER TABLE `questions`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT voor een tabel `results`
--
ALTER TABLE `results`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=329;

--
-- AUTO_INCREMENT voor een tabel `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- Beperkingen voor geëxporteerde tabellen
--

--
-- Beperkingen voor tabel `answer`
--
ALTER TABLE `answer`
  ADD CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`ID`);

--
-- Beperkingen voor tabel `results`
--
ALTER TABLE `results`
  ADD CONSTRAINT `results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`ID`),
  ADD CONSTRAINT `results_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `questions` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
