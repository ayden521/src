CREATE TABLE `activities` (
`activity` varchar(100) DEFAULT NULL,
`type` varchar(100) DEFAULT NULL,
`participants` INTEGER,
`price` INTEGER,
`link` varchar(100) DEFAULT NULL,
`key` varchar(100) DEFAULT NULL,
`accessibility` INTEGER,
`create_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);