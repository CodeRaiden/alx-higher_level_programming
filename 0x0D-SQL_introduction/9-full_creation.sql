-- create second_table if it doesn't already exist
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT, `name` VARCHAR(256), `score` INT
);
-- insert records into second_table
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES
(1, 'John', 10),
(2, 'Mike', 3),
(3, 'Tom', 14),
(4, 'Sam', 8);
