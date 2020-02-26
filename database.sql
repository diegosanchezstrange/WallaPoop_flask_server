CREATE OR REPLACE DATABASE wallapoop;
use wallapoop;


CREATE OR REPLACE TABLE User
(
    ID INT NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(30) NOT NULL,
    PASSWD VARCHAR(128) NOT NULL,
    PRIMARY KEY (ID)
);

INSERT INTO User (NAME, PASSWD) VALUES ("Diego", "33d20866f39ac545df5959282dc1aa62315365808ce750371c6d9c511caf577d6b98c85baeacca2d307223fa26aab0f5253dda18cdb873cc73169bd1d02a82d6");

CREATE OR REPLACE TABLE Product
(
    ID INT NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(128) NOT NULL,
    DESCRIPTION VARCHAR(256) NOT NULL,
    PRICE INT NOT NULL,
    PRODUCT_OWNER INT NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY(PRODUCT_OWNER) REFERENCES User(ID)
);

INSERT INTO Product (NAME, DESCRIPTION, PRICE, PRODUCT_OWNER) VALUES ("PS4", "Consola de videojuegos", 120, 1);
