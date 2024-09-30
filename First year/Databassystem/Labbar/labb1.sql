REM   Script: LABB_1
REM   LABB_1

create sequence seq_ägarbyte 
start with 1 
increment by 1;

select myseq.nextval 
from dual;

create sequence myseq 
start with 1 
increment by 1;

select myseq.nextval 
from dual;

create table KUND ( 
	persnr varchar2(13) NOT NULL PRIMARY KEY, 
	username varchar2(50) NOT NULL, 	 
    passwd varchar2(50) NOT NULL, 
	fnamn varchar2(60) NOT NULL, 
    enamn varchar2(60) NOT NULL, 
 	kredittyp varchar2(20) NOT NULL, 
	telnr varchar2(12), 
) 
;

create table KUND ( 
	persnr varchar2(13) NOT NULL PRIMARY KEY, 
	username varchar2(50) NOT NULL, 	 
    passwd varchar2(50) NOT NULL, 
	fnamn varchar2(60) NOT NULL, 
    enamn varchar2(60) NOT NULL, 
 	kredittyp varchar2(20) NOT NULL, 
	telnr varchar2(12) 
    ) 
;

select *  
from KUND;

select *  
from KUND;

insert into KUND(persnr,username,passwd,fnamn,enamn,kredittyp,telnr) 
values('19900617-5678','calel','12345','Calle','Andersson','Debit','0705551122');

select * 
from KUND;

create table KUNDORDER ( 
    ordnr varchar2(20) NOT NULL PRIMARY KEY, 
	persnr varchar(13) NOT NULL, 
    datum varchar(10) NOT NULL, 
    FOREIGN KEY (persnr) REFERENCES KUND(persnr) 
) 
 
;

INSERT INTO KUND(ordnr,persnr,datum) 
VALUES('56723','19900617-5678','04-11-2024') 
 
;

INSERT INTO KUND(ordnr,persnr,datum) 
VALUES('56723','19900617-5678','04-11-2024');

INSERT INTO KUNDORDER(ordnr,persnr,datum) 
VALUES('56723','19900617-5678','04-11-2024');

SELECT * FROM KUNDORDER 
;

INSERT INTO KUNDORDER(ordnr,persnr,datum) 
VALUES('67888','19990222-1234','04-12-2024');

CREATE TABLE VARUGRUPP( 
    vgnr varchar2(20) NOT NULL PRIMARY KEY, 
    vgnamn varchar2(200) NOT NULL 
);

CREATE TABLE ARTIKEL( 
    artnr varchar2(20) PRIMARY KEY, 
    vgnr varchar2(20) NOT NULL, 
    artnamn varchar2(200) NOT NULL, 
    pris float NOT NULL, 
    FOREIGN KEY (vgnr) REFERENCES VARUGRUPP(vgnr) 
);

CREATE TABLE KUNDVAGN( 
    radnr number NOT NULL PRIMARY KEY, 
    ordnr varchar2(20) NOT NULL, 
    artnr varchar2(20) NOT NULL, 
    antal number NOT NULL, 
    FOREIGN KEY (ordnr) REFERENCES KUNDORDER(ordnr) 
    FOREIGN KEY (artnr) REFERENCES ARTIKEL(artnr) 
);

CREATE TABLE KUNDVAGN( 
    radnr number NOT NULL PRIMARY KEY, 
    ordnr varchar2(20) NOT NULL, 
    artnr varchar2(20) NOT NULL, 
    antal number NOT NULL, 
    FOREIGN KEY (ordnr) REFERENCES KUNDORDER(ordnr), 
    FOREIGN KEY (artnr) REFERENCES ARTIKEL(artnr) 
);

CREATE TABLE ARTIKELBILD( 
    bildnr varchar2(20) PRIMARY KEY, 
    artnr varchar2(20) NOT NULL, 
    filtyp varchar2(30) NOT NULL, 
    width float NOT NULL, 
    height float NOT NULL, 
    path varchar2(300) NOT NULL, 
    FOREIGN KEY (artnr) REFERENCES ARTIKEL(artnr) 
);

CHECK CONSTRAINT KUND.kredittyp 


desc user_constraints


desc KUND.kredittyp


desc kund.kredittyp


select * from KUND 
;

CHECK KUND.kredittyp('hög','medel','låg')


CHECK (KUND.kredittyp('hög','medel','låg'))


CHECK (KUND.kredittyp 'hög','medel','låg')


ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(kredittyp);

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK('hög','medel','låg');

ALTER TABLE kund 
ADD CONSTRAINT kund_kredittyp_ck CHECK('hög','medel','låg');

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(kredittyp =('hög','medel','låg'));

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(kredittyp ='hög','medel','låg');

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(kredittyp in ('hög','medel','låg'));

alter table KUND drop constraint kredittyp;

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(KUND.kredittyp in ('hög','medel','låg'));

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(kredittyp in ('hög','medel','låg'));

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE 
FROM USER_CONSTRAINTS 
WHERE TABLE_NAME = KUND AND COLUMN_NAME = kredittyp;

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE 
FROM USER_CONSTRAINTS 
WHERE TABLE_NAME = KUND AND COLUMN_NAME = 'kredittyp';

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE 
FROM USER_CONSTRAINTS 
WHERE TABLE_NAME = 'KUND' AND COLUMN_NAME = 'kredittyp';

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE 
FROM USER_CONSTRAINTS 
WHERE TABLE_NAME = KUND AND COLUMN_NAME = KREDITTYP;

SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE 
FROM USER_CONSTRAINTS 
WHERE TABLE_NAME = KUND AND COLUMN_NAME = kredittyp;

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(KREDITTYP in ('hög','medel','låg'));

SELECT COUNT(*) FROM USER_CONSTRAINTS WHERE TABLE_NAME = KUND;

SELECT COUNT(*) FROM USER_CONSTRAINTS WHERE KUND;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUND';

WHERE TABLE_NAME = KUND AND COLUMN_NAME = KREDITTYP; 


alter table KUND 
rename constraint SYS_C00153343788 to KUND_persnr_pk;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUND';

alter table KUND 
drop constraint SYS_C00153343782, 
drop constraint SYS_C00153343783, 
drop constraint SYS_C00153343784, 
drop constraint SYS_C00153343785, 
drop constraint SYS_C00153343786, 
drop constraint SYS_C00153343787, 
 
 
;

alter table KUND 
drop constraint SYS_C00153343782, 
drop constraint SYS_C00153343783, 
drop constraint SYS_C00153343784, 
drop constraint SYS_C00153343785, 
drop constraint SYS_C00153343786, 
drop constraint SYS_C00153343787 
 
 
;

alter table KUND 
drop constraint SYS_C00153343782, 
drop constraint SYS_C00153343783, 
drop constraint SYS_C00153343784, 
drop constraint SYS_C00153343785, 
drop constraint SYS_C00153343786, 
drop constraint SYS_C00153343787;

alter table KUND 
drop constraint SYS_C00153343782;

drop constraint SYS_C00153343783;

drop constraint SYS_C00153343784;

drop constraint SYS_C00153343785;

drop constraint SYS_C00153343786;

drop constraint SYS_C00153343787;

alter table KUND 
drop constraint SYS_C00153343782;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUND';

alter table KUND 
drop constraint SYS_C00153343783;

alter table KUND 
drop constraint SYS_C00153343784;

alter table KUND 
drop constraint SYS_C00153343785;

alter table KUND 
drop constraint SYS_C00153343786;

alter table KUND 
drop constraint SYS_C00153343787;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUND';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUND';

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(KREDITTYP in ('hög','medel','låg'));

UPDATE KUND SET kredittyp = 'medel' WHERE kredittyp NOT IN ('hög', 'medel', 'låg');

ALTER TABLE KUND 
ADD CONSTRAINT KUND_kredittyp_ck CHECK(KREDITTYP in ('hög','medel','låg'));

select * from KUND 
 
 
 
;

check(kund.kredittyp) 


select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUND';

ALTER TABLE KUND 
ADD CONSTRAINT KUND_username_uq UNIQUE(username);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUND';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'ARTIKELBILD';

alter table ARTIKEL 
DROP CONSTRAINT SYS_C00153348342 
DROP CONSTRAINT SYS_C00153348343 
DROP CONSTRAINT SYS_C00153348344 
DROP CONSTRAINT SYS_C00153348345 
DROP CONSTRAINT SYS_C00153348346 
DROP CONSTRAINT SYS_C00153348347 
DROP CONSTRAINT SYS_C00153348348;

alter table ARTIKELBILD 
DROP CONSTRAINT SYS_C00153348342 
DROP CONSTRAINT SYS_C00153348343 
DROP CONSTRAINT SYS_C00153348344 
DROP CONSTRAINT SYS_C00153348345 
DROP CONSTRAINT SYS_C00153348346 
DROP CONSTRAINT SYS_C00153348347 
DROP CONSTRAINT SYS_C00153348348;

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_uq UNIQUE(username);

ADD CONSTRAINT ARTIKELBILD_bildnr_uq UNIQUE(username); 


ADD CONSTRAINT ARTIKELBILD_bildnr_uq UNIQUE(username); 


ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_pk PRIMARY KEY(bildnr) 
ADD CONSTRAINT ARTIKELBILD_artnr_fk FOREIGN KEY(artnr) 
ADD CONSTRAINT ARTIKELBILD_filtyp_ck CHECK(filtyp in ('gif','jpg')) 
ADD CONSTRAINT ARTIKELBILD_width_ck CHECK(width) 
ADD CONSTRAINT ARTIKELBILD_height_ck CHECK(height) 
ADD CONSTRAINT ARTIKELBILD_path_ck CHECK(path);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_pk PRIMARY KEY(bildnr) 
ADD CONSTRAINT ARTIKELBILD_artnr_fk FOREIGN KEY(artnr) 
ADD CONSTRAINT ARTIKELBILD_filtyp_ck CHECK(filtyp in ('gif','jpg')) 
ADD CONSTRAINT ARTIKELBILD_width_ck CHECK(width) 
ADD CONSTRAINT ARTIKELBILD_height_ck CHECK(height);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_pk PRIMARY KEY(bildnr) 
ADD CONSTRAINT ARTIKELBILD_artnr_fk FOREIGN KEY(artnr) 
ADD CONSTRAINT ARTIKELBILD_filtyp_ck CHECK(filtyp in ('gif','jpg')) 
ADD CONSTRAINT ARTIKELBILD_width_ck CHECK(width) 
ADD CONSTRAINT ARTIKELBILD_height_ck CHECK(height) 
ADD CONSTRAINT ARTIKELBILD_path_ck CHECK(path);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_pk PRIMARY KEY(bildnr), 
ADD CONSTRAINT ARTIKELBILD_artnr_fk FOREIGN KEY(artnr), 
ADD CONSTRAINT ARTIKELBILD_filtyp_ck CHECK(filtyp in ('gif','jpg')), 
ADD CONSTRAINT ARTIKELBILD_width_ck CHECK(width), 
ADD CONSTRAINT ARTIKELBILD_height_ck CHECK(height), 
ADD CONSTRAINT ARTIKELBILD_path_ck CHECK(path);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_pk PRIMARY KEY(bildnr), 
ADD CONSTRAINT ARTIKELBILD_artnr_fk FOREIGN KEY(artnr) REFERENCES ARTIKEL(artnr), 
ADD CONSTRAINT ARTIKELBILD_filtyp_ck CHECK(filtyp in ('gif','jpg')), 
ADD CONSTRAINT ARTIKELBILD_width_ck CHECK(width), 
ADD CONSTRAINT ARTIKELBILD_height_ck CHECK(height), 
ADD CONSTRAINT ARTIKELBILD_path_ck CHECK(path);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_pk PRIMARY KEY(bildnr) 
ADD CONSTRAINT ARTIKELBILD_artnr_fk FOREIGN KEY(artnr) REFERENCES ARTIKEL(artnr) 
ADD CONSTRAINT ARTIKELBILD_filtyp_ck CHECK(filtyp in ('gif','jpg')) 
ADD CONSTRAINT ARTIKELBILD_width_ck CHECK(width) 
ADD CONSTRAINT ARTIKELBILD_height_ck CHECK(height) 
ADD CONSTRAINT ARTIKELBILD_path_ck CHECK(path);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_bildnr_pk PRIMARY KEY(bildnr);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_artnr_fk FOREIGN KEY(artnr) REFERENCES ARTIKEL(artnr);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_filtyp_ck CHECK(filtyp IN ('gif','jpg'));

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_width_ck CHECK(width IS NOT NULL);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_height_ck CHECK(height IS NOT NULL);

ALTER TABLE ARTIKELBILD 
ADD CONSTRAINT ARTIKELBILD_path_ck CHECK(path IS NOT NULL);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'ARTIKELBILD';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

alter table KUNDORDER 
modify ordnr number;

alter table KUNDORDER 
modify COLUMN ordnr number;

alter table KUNDORDER 
modify ordnr number;

alter table KUNDVAGN 
modify ordnr number;

alter table KUNDVAGN 
modify ordnr to number;

alter table KUNDVAGN 
modify ordnr to NUMBER;

DELETE FROM KUNDORDER WHERE ordnr = '56723' 
 
 
 
 
;

alter table KUNDVAGN 
modify ordnr NUMBER;

ALTER TABLE KUNDORDER 
  MODIFY(ordnr NUMBER) 
 
 
 
 
 
;

alter table KUNDORDER 
DROP CONSTRAINT SYS_C00153345145 
DROP CONSTRAINT SYS_C00153345146 
DROP CONSTRAINT SYS_C00153345147 
DROP CONSTRAINT SYS_C00153345148 
DROP CONSTRAINT SYS_C00153348349;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

alter table KUNDORDER 
DROP CONSTRAINT SYS_C00153345145 
DROP CONSTRAINT SYS_C00153345146 
DROP CONSTRAINT SYS_C00153345147 
DROP CONSTRAINT SYS_C00153345148 
DROP CONSTRAINT SYS_C00153348349;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

alter table KUNDORDER 
DROP CONSTRAINT SYS_C00153345145 
DROP CONSTRAINT SYS_C00153345146 
DROP CONSTRAINT SYS_C00153345147 
DROP CONSTRAINT SYS_C00153345148 
DROP CONSTRAINT SYS_C00153345149;

alter table KUNDVAGN 
-- DROP CONSTRAINT SYS_C00153345145 
-- DROP CONSTRAINT SYS_C00153345146 
-- DROP CONSTRAINT SYS_C00153345147 
-- DROP CONSTRAINT SYS_C00153345148 
-- DROP CONSTRAINT SYS_C00153345149;

alter table KUNDVAGN 
-- DROP CONSTRAINT SYS_C00153345145 
-- DROP CONSTRAINT SYS_C00153345146 
-- DROP CONSTRAINT SYS_C00153345147 
-- DROP CONSTRAINT SYS_C00153345148 
-- DROP CONSTRAINT SYS_C00153345149;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDVAGN';

select constraint_name,constraint_type 
-- from user_constraints 
-- where table_name = 'KUNDVAGN';

alter table KUNDVAGN 
DROP CONSTRAINT SYS_C00153348102 
DROP CONSTRAINT SYS_C00153348103 
DROP CONSTRAINT SYS_C00153348104 
DROP CONSTRAINT SYS_C00153348105 
DROP CONSTRAINT SYS_C00153348106 
DROP CONSTRAINT SYS_C00153348107 
DROP CONSTRAINT SYS_C00153348108 
 
-- ALTER TABLE KUNDORDER 
--   MODIFY(ordnr NUMBER) 
 
 
 
 
 
;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDVAGN';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

alter table KUNDVAGN 
DROP CONSTRAINT SYS_C00153345145 
DROP CONSTRAINT SYS_C00153345146 
DROP CONSTRAINT SYS_C00153345147 
DROP CONSTRAINT SYS_C00153345148 
DROP CONSTRAINT SYS_C00153345149;

alter table KUNDORDER 
DROP CONSTRAINT SYS_C00153345145 
DROP CONSTRAINT SYS_C00153345146 
DROP CONSTRAINT SYS_C00153345147 
DROP CONSTRAINT SYS_C00153345148 
DROP CONSTRAINT SYS_C00153345149;

ALTER TABLE KUNDORDER 
  MODIFY(ordnr NUMBER);

ALTER TABLE KUNDVAGN 
  MODIFY(ordnr NUMBER) 
 
 
 
 
 
;

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_ordnr_pk PRIMARY KEY(ordnr);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_persnr_fk FOREIGN KEY(persnr) REFERENCES KUND(persnr);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck PRIMARY KEY(datum);

ALTER TABLE KUNDORDER 
  MODIFY(datum DATE) 
 
 
 
 
 
;

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_ordnr_pk PRIMARY KEY(ordnr);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_persnr_fk FOREIGN KEY(persnr) REFERENCES KUND(persnr);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(datum);

ALTER TABLE KUNDORDER 
  MODIFY(datum DATE) 
 
 
 
 
 
;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(datum);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(datum = DATE);

select * from KUNDORDER 
 
 
 
 
;

select datum from KUNDORDER 
 
 
 
 
;

SELECT column_name  
FROM all_tab_columns  
WHERE table_name = 'KUNDORDER' 
 
 
 
;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(DATUM);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(DATUM);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(DATUM);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(datum is not null);

ALTER TABLE KUNDORDER 
ADD CONSTRAINT KUNDORDER_datum_ck CHECK(datum is not null);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDORDER 
  MODIFY(radnr number) 
 
-- select * from KUNDORDER 
 
 
 
;

ALTER TABLE KUNDVAGN 
  MODIFY(radnr number) 
 
-- select * from KUNDORDER 
 
 
 
;

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_radnr_pk PRIMARY KEY(radnr);

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_ordnr_fk FOREIGN KEY(ordnr) REFERENCES KUNDORDER(ordnr);

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_artnr_fk FOREIGN KEY(artnr) REFERENCES ARTIKEL(artnr);

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_antal_ck CHECK(antal is not null);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDVAGN';

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_ordnr_fk FOREIGN KEY(ordnr IS NOT NULL) REFERENCES KUNDORDER(ordnr);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_ordnr_fk FOREIGN KEY(ordnr) REFERENCES KUNDORDER(ordnr);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_ordnr_fk FOREIGN KEY(ordnr) REFERENCES KUNDORDER(ordnr) IS NOT NULL;

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_ordnr_fk FOREIGN KEY(ordnr) REFERENCES KUNDORDER(ordnr);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

SELECT * 
FROM KUND 
WHERE * IS NOT NULL;

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_ordnr_fk FOREIGN KEY(ordnr) REFERENCES KUNDORDER(ordnr);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

SELECT * 
FROM KUNDVAGN 
WHERE * IS NOT NULL;

ALTER TABLE KUNDVAGN 
ADD CONSTRAINT KUNDVAGN_ordnr_fk FOREIGN KEY(ordnr) REFERENCES KUNDORDER(ordnr);

select constraint_name,constraint_type 
from user_constraints 
where table_name = 'KUNDORDER';

SELECT * 
FROM KUNDVAGN 
WHERE ordnr IS NOT NULL;

SELECT * 
FROM KUNDVAGN 
WHERE ordnr IS NOT NULL;

INSERT INTO KUNDORDER(ordnr,persnr,datum) 
VALUES('','19900617-5678','');

