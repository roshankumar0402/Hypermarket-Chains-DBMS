SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


-- Database: `cs582_hypermarket`

-- Table structure for table `admin`

CREATE TABLE `admin` (
  `ANAME` varchar(20) NOT NULL,
  `APASS` varchar(20) NOT NULL,
  PRIMARY KEY(ANAME)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- Dumping data for table `admin`

INSERT INTO `admin` (`ANAME`, `APASS`) VALUES
('555', 'admin'),('533', 'admin'),('544', 'admin')
,('511', 'admin'),('522', 'admin'),('588', 'admin')
,('500', 'admin'),('577', 'admin'),('566', 'admin');


-- Table structure for table `Dist`

CREATE TABLE `Dist` (
  `DID` int(11) NOT NULL,
  `DNAME` varchar(20) NOT NULL,
  `DPASS` varchar(20) NOT NULL DEFAULT 'admin',
  `DTYPE` varchar(20) NOT NULL,
  `DLOC` varchar(30) NOT NULL, PRIMARY KEY(DID)
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table `Dist`

INSERT INTO `Dist` (`DID`, `DNAME`, `DPASS`, `DTYPE`, `DLOC`) VALUES
(1000, 'Fritolay', 'admin', 'Electrical', 'Delhi'),
(1001, 'Pepsico', 'admin', 'CoolDrinks', 'Hyderabad'),
(1002, 'YogaBar', 'admin', 'Snacks', 'Bengaluru'),
(1003, 'Cello', 'admin', 'Stationery', 'Kolkata'),
(1004, 'Boat', 'admin', 'Earphones', 'Chennai'),
(1005, 'HP', 'admin', 'Computers', 'Jaipur'),
(1006, 'John Jacob', 'admin', 'Eyewear', 'Hyderabad'),
(1007, 'Unilever', 'admin', 'FMCG', 'Bengaluru'),
(1008, 'ITC', 'admin', 'FMCG', 'Chennai');


-- Table structure for table `store`

CREATE TABLE `store` (
  `SID` int(11) NOT NULL,
  `SPASS` varchar(20) NOT NULL DEFAULT 'admin',
  `SBRANCHNAME` varchar(20) NOT NULL,
  `SCITY` varchar(20) NOT NULL,
  `SREGION` varchar(20) NOT NULL,
  `SSTATE` varchar(20) NOT NULL,
  `SPCODE` int(11) NOT NULL,PRIMARY KEY(SID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table `store`

INSERT INTO `store` (`SID`, `SPASS`, `SBRANCHNAME`, `SCITY`, `SREGION`, `SSTATE`, `SPCODE`) VALUES
(100, 'admin', 'Ajmal Nagar', 'Delhi', 'North Delhi', 'Delhi', 131222),
(101, 'admin', 'Silk Point', 'Bidar', 'North Karnataka', 'Karnataka', 585401),
(102, 'admin', 'Banashankari', 'Bengaluru', 'South Karnataka', 'Karnataka', 585403),
(103, 'admin', 'Yeshawantpur', 'Bengaluru', 'South Karnataka', 'Karnataka', 585333),
(104, 'admin', 'VV nagar', 'Mysore', 'Central Karnataka', 'Karnataka', 585233),
(105, 'admin', 'Batra Nagar', 'Allahabad', 'North UP', 'UP', 485401),
(106, 'admin', 'Shanti Layout', 'Jaipur', 'South Rajasthan', 'Rajasthan', 385401),
(107, 'admin', 'Amar Colony', 'Kozhikode', 'North Kerala', 'Kerala', 457401),
(108, 'admin', 'Nippani', 'Gulbarga', 'North Karnataka', 'Karnataka', 595401),
(109, 'admin', 'Bhuvana Colony', 'Bengaluru', 'South Karnataka', 'Karnataka', 585567),
(110, 'admin', 'Ganesh Nagar', 'Shimla', 'North Kashmir', 'Kashmir', 591401),
(111, 'admin', 'Tulasi Layout', 'Shillong', 'North Meghalaya', 'Meghalaya', 185234);

-- Table structure for table `sales`

CREATE TABLE `sales` (
  `SALESID` int(11) NOT NULL,
  `SDATE` date NOT NULL,
  `SCOST` int(11) NOT NULL,
  `SID` int(11) NOT NULL,PRIMARY KEY(SALESID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

alter table sales  add constraint sales_fk foreign key(SID) references store(SID) on delete CASCADE on update CASCADE;


INSERT INTO `sales` (`SALESID`, `SDATE`, `SCOST`, `SID`) VALUES
(222, '2022-11-22', 40079, 100),
(223, '2022-11-22', 70000, 100),
(227, '2022-11-28', 59879, 102),
(228, '2022-11-25', 60000, 103),
(229, '2022-11-17', 70000, 104),
(230, '2022-11-27', 70000, 111),
(235, '2022-11-25', 70000, 110),
(240, '2022-11-23', 70000, 111),
(242, '2022-11-20', 70000, 105),
(244, '2022-11-24', 70000, 106),
(250, '2022-11-28', 70000, 108);


-- Table structure for table `stock`

CREATE TABLE `stock` (
  `CRY` varchar(20) NOT NULL,
  `SCRY` varchar(20) NOT NULL,
  `QUANT` int(11) NOT NULL,
  `SID` int(11) NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

alter table stock  add constraint stock_fk foreign key(SID) references store(SID) on delete CASCADE on update CASCADE;

-- Dumping data for table `stock`

INSERT INTO `stock` (`CRY`, `SCRY`, `QUANT`, `SID`) VALUES
('Electrical', 'Mobiles', 30, 101),
('Snacks', 'Cereal', 300, 100),
('Electrical', 'Wires', 500, 100),
('Computers', 'Laptops', 10, 111),
('FMCG', 'Shampoo', 1000, 111),
('CoolDrinks', 'Pepsi', 2000, 107),
('Stationery', 'Pen', 5000, 106),
('Earphones', 'Bluetooth', 150, 108),
('Eyewear', 'Contact Lens', 170, 109),
('Earphones', 'Neck Band', 400, 104),
('Eyewear', 'Spectacles', 120, 103),
('FMCG', 'Cigarette', 1500, 102),
('FMCG', 'Soap', 3000, 105);


-- Table structure for table `st_orders`

CREATE TABLE `st_orders` (
  `SID` int(11) NOT NULL,
  `ORDID` int(11) NOT NULL,
  `DID` int(11) NOT NULL,
  `ORDDATE` date NOT NULL,
  `PMYSTAT` varchar(20) NOT NULL DEFAULT 'PENDING',
  `SHPMODE` varchar(20) NOT NULL DEFAULT 'Normal',
  `SHPSTAT` varchar(20) NOT NULL DEFAULT 'PENDING',
  PRIMARY KEY(ORDID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

alter table st_orders  add constraint strodr1_fk foreign key(SID) references store(SID) on delete CASCADE on update CASCADE;
alter table st_orders  add constraint strodr2_fk foreign key(DID) references Dist(DID) on delete CASCADE on update CASCADE;

-- Dumping data for table `st_orders`

INSERT INTO `st_orders` (`SID`, `ORDID`, `DID`, `ORDDATE`, `PMYSTAT`, `SHPMODE`, `SHPSTAT`) VALUES
(100, 500, 1000, '2022-11-15', '', 'Premium', 'Delivered'),
(100, 501, 1001, '2022-11-28'  , 'PAID', 'Normal', 'PENDING'),
(101, 502, 1001,'2022-11-27' , 'PAID', 'Premium', 'Delivered'),
(102, 503, 1002,'2022-11-18' , 'PAID', 'Normal', 'PENDING'),
(103, 504, 1003, '2022-11-25', '', 'Normal', 'PENDING'),
(105, 505, 1004, '2022-11-22' , '', 'Normal', 'PENDING'),
(106, 506, 1005, '2022-11-26', '', 'Normal', 'PENDING'),
(105, 507, 1006, '2022-11-28', '', 'Normal', 'PENDING'),
(111, 508, 1008, '2022-11-28', '', 'Normal', 'PENDING');


-- Table structure for table `t`

CREATE TABLE `t` (
  `temp` varchar(20) NOT NULL,
  `tee` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table `t`

INSERT INTO `t` (`temp`, `tee`) VALUES
('', '2018-11-30 19:21:11'),
('', '2018-11-30 19:21:32'),
('501', '2018-11-30 19:22:00'),
('503', '2018-11-30 19:25:07'),
('501', '2018-11-30 19:25:20'),
('502', '2018-11-30 19:25:47'),
('501', '2018-11-30 19:31:55'),
('501', '2018-11-30 19:34:22'),
('501', '2018-11-30 19:34:27'),
('505', '2018-11-30 19:34:30'),
('502', '2018-11-30 19:35:50'),
('506', '2018-11-30 19:35:54'),
('503', '2018-11-30 19:36:36'),
('501', '2018-11-30 19:37:40'),
('501', '2018-11-30 19:38:26'),
('501', '2018-11-30 19:38:41'),
('501', '2018-11-30 19:39:42'),
('502', '2018-11-30 19:47:54'),
('503', '2018-11-30 19:47:56'),
('503', '2018-11-30 19:49:10'),
('505', '2018-11-30 19:49:13'),
('505', '2018-11-30 19:49:15'),
('501', '2018-11-30 19:49:17'),
('503', '2018-11-30 19:50:47'),
('501', '2018-11-30 19:50:53'),
('502', '2018-11-30 19:52:55'),
('502', '2018-11-30 19:53:10'),
('502', '2018-11-30 19:53:32'),
('SCITY', '2018-11-30 19:56:55'),
('SREGION', '2018-11-30 19:58:50'),
('SBRANCHNAME', '2018-11-30 19:59:08'),
('SBRANCHNAME', '2018-12-01 04:09:12'),
('501', '2018-12-01 04:15:09');



-- JOIN:
-- 1. Natural join:
SELECT str.SBRANCHNAME,str.SCITY,stk.SCRY,stk.QUANT FROM store as str NATURAL JOIN stock as stk;
-- 2 Left join::
SELECT * from dist LEFT JOIN st_orders ON dist.DID=st_orders.DID;
-- 3 Right join::
SELECT sales.SALESID, store.SBRANCHNAME,sales.SDATE,sales.SCOST 
FROM store RIGHT JOIN sales ON sales.SID=store.SID ORDER BY sales.SDATE;
-- 4 Inner join::
SELECT dist.DNAME,dist.DTYPE,dist.DLOC,st_orders.ORDDATE,st_orders.SHPSTAT 
from dist INNER JOIN st_orders ON dist.DID=st_orders.DID ORDER BY dist.DNAME;

DELIMITER $$
CREATE TRIGGER trigger_earphone BEFORE INSERT
ON stock FOR EACH ROW
BEGIN
DECLARE msg VARCHAR(50);
	DECLARE val int;
	SET msg = "No of items in category more than 3";
	SET val = (SELECT COUNT(*) FROM stock WHERE cry = new.cry GROUP BY cry);
	IF val>3 THEN
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT= msg;
	END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE Dist_in_Hyd()

BEGIN
	DECLARE DistID int;
	DECLARE DistName varchar(255);
    DECLARE DistPass varchar(255);
	DECLARE DistType varchar(255);
    DECLARE DistLoc varchar(255);
	DECLARE exit_loop BOOLEAN DEFAULT FALSE;
	DECLARE d_cursor CURSOR FOR SELECT DID, DNAME, DPASS, DTYPE, DLOC FROM dist;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET exit_loop = TRUE;
	OPEN d_cursor;
	d_loop:LOOP
	
		FETCH FROM d_cursor INTO DistID,DistName,DistPass,DistType,DistLoc;
		IF exit_loop THEN
			LEAVE d_loop;
		END IF;
		IF DistLoc = "Hyderabad" THEN 
			SELECT  DistID,DistName,DistPass,DistType,DistLoc;
		END IF;
	END LOOP d_loop;
	CLOSE d_cursor;
END $$

DELIMITER $$
CREATE FUNCTION connectivity(distLoc varchar(255))
RETURNS varchar(100)
DETERMINISTIC 
BEGIN
DECLARE n int default 0; 
DECLARE msg varchar(100);
select count(DLOC) into n
from dist
where DLOC =distLoc ;
if n>1 then
set msg:= "Good Connectivity";
else
set msg:= "Bad Connectivity";
end if;
RETURN msg;
END; $$
DELIMITER ;
select DID,DLOC, connectivity(DLOC) from dist;

-- Indexes for dumped tables
--

--
-- Indexes for table `Dist`
--


--
-- Indexes for table `sales`
--
-- ALTER TABLE `sales`
--   ADD PRIMARY KEY (`SALESID`);

-- --
-- -- Indexes for table `stock`
-- --
-- ALTER TABLE `stock`
--   ADD KEY `SID` (`SID`);

-- --
-- -- Indexes for table `store`
-- --
-- ALTER TABLE `store`
--   ADD PRIMARY KEY (`SID`);

-- --
-- -- Indexes for table `st_orders`
-- --
-- ALTER TABLE `st_orders`
--   ADD PRIMARY KEY (`ORDID`),
--   ADD KEY `DID` (`DID`);

-- --
-- -- AUTO_INCREMENT for dumped tables
-- --

--
-- AUTO_INCREMENT for table `Dist`
--
-- ALTER TABLE `Dist`
--   MODIFY `DID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1002;

-- --
-- -- AUTO_INCREMENT for table `sales`
-- --
-- ALTER TABLE `sales`
--   MODIFY `SALESID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=230;

-- --
-- -- AUTO_INCREMENT for table `store`
-- --
-- ALTER TABLE `store`
--   MODIFY `SID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

-- --
-- -- AUTO_INCREMENT for table `st_orders`
-- --
-- ALTER TABLE `st_orders`
--   MODIFY `ORDID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=509;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `stock`
--
-- ALTER TABLE `stock`
--   ADD CONSTRAINT `stock_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `store` (`SID`) ON DELETE CASCADE;

-- --
-- -- Constraints for table `st_orders`
-- --
-- ALTER TABLE `st_orders`
--   ADD CONSTRAINT `st_orders_ibfk_1` FOREIGN KEY (`DID`) REFERENCES `Dist` (`DID`) ON DELETE CASCADE;
-- COMMIT;

-- -*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT *-;
-- -*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS *-;
-- -*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION *-;
