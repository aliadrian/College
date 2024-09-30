CREATE TABLE bilägare(
pnr VARCHAR2(13) PRIMARY KEY,
fnamn VARCHAR2(20),
enamn VARCHAR2(20),
bor_i VARCHAR2(20),
jobbar_i VARCHAR2(20));

CREATE TABLE fordon(
regnr VARCHAR2(6) PRIMARY KEY,
pnr REFERENCES bilägare(pnr),
tillverkare VARCHAR2(20),
modell VARCHAR2(20),
årsmodell NUMBER(4),
hk NUMBER(4),
datum DATE);

INSERT INTO bilägare VALUES('19490321-7899','hans','rosenboll','borlänge','falun');
INSERT INTO bilägare VALUES('19540201-4428','tomas','kvist','gagnef','borlänge');
INSERT INTO bilägare VALUES('19650823-7999','roger','nyberg','borlänge','falun');
INSERT INTO bilägare VALUES('19710601-7799','lena','malm','borlänge','falun');
INSERT INTO bilägare VALUES('19690321-7898','ollas','bullas','falun','borlänge');
INSERT INTO bilägare VALUES('19590421-7199','tåmmy','dåmert','borlänge','falun');
INSERT INTO bilägare VALUES('19610321-4299','rollf','ekengren','borlänge','falun');
INSERT INTO bilägare VALUES('19810321-7199','maria','stjärnkvist','borlänge','falun');
INSERT INTO bilägare VALUES('19720721-7899','leyla','errstraid','borlänge','falun');
INSERT INTO bilägare VALUES('19380321-7799','arne','möller','borlänge','falun');
INSERT INTO fordon VALUES('ase456','19490321-7899','volvo','945',1998,160,to_date('2003-08-11','YYYY-MM-DD'));
INSERT INTO fordon VALUES('ptg889','19490321-7899','fiat','excel',1991,287,to_date('1998-05-19','YYYY-MM-DD'));
INSERT INTO fordon VALUES('bon666','19540201-4428','john deere','gris',1967,48,to_date('1989-06-28','YYYY-MM-DD'));
INSERT INTO fordon VALUES('rog589','19650823-7999','saab','900 talladega',1997,205,to_date('2003-05-11','YYYY-MM-DD'));
INSERT INTO fordon VALUES('ert456','19710601-7799','volvo','850',1997,150,to_date('2001-07-11','YYYY-MM-DD'));
INSERT INTO fordon VALUES('ola774','19690321-7898','mb','e420',1998,285,to_date('2000-08-11','YYYY-MM-DD'));
INSERT INTO fordon VALUES('thf345','19590421-7199','opel','kapitän',1968,105,to_date('1991-06-11','YYYY-MM-DD'));
INSERT INTO fordon VALUES('dde411','19610321-4299','saab','9000 aero',1998,225,to_date('2000-07-28','YYYY-MM-DD'));
INSERT INTO fordon VALUES('ser478','19810321-7199','audi','tt',2003,247,to_date('2004-07-05','YYYY-MM-DD'));
INSERT INTO fordon VALUES('fgt147','19720721-7899','volvo','66',1981,62,to_date('2003-05-11','YYYY-MM-DD'));
INSERT INTO fordon VALUES('tau444','19380321-7799','ford','taunus',1973,95,to_date('1975-08-23','YYYY-MM-DD'));
INSERT INTO fordon VALUES('pot333','19540201-4428','volvo','745',1989,93,to_date('1996-01-11','YYYY-MM-DD'));
COMMIT;

----------- UPPGIFT 1 ---------------------

declare
v_regnr fordon.regnr%type; 
v_tillverkare fordon.tillverkare%type;
v_modell fordon.modell%type;
begin
	select upper(regnr), initcap(tillverkare), initcap(modell) into v_regnr, v_tillverkare, v_modell from fordon
	where pnr = '19650823-7999';
	dbms_output.put_line('Regnr: '|| v_regnr);
	dbms_output.put_line('Tillverkare: '|| v_tillverkare);
	dbms_output.put_line('Modell: '|| v_modell);
end;

----------- UPPGIFT 2 ---------------------

declare
v_regnr fordon.regnr%type; 
v_tillverkare fordon.tillverkare%type;
v_modell fordon.modell%type;
begin
	select regnr, tillverkare, modell into v_regnr, v_tillverkare, v_modell from fordon
	where pnr = '19540201-4428';
	dbms_output.put_line('Regnr: '|| upper(v_regnr));
	dbms_output.put_line('Tillverkare: '|| initcap(v_tillverkare));
	dbms_output.put_line('Modell: '|| initcap(v_modell));
exception
    when others then
    	dbms_output.put_line('Något blev fel!');
end;

----------- UPPGIFT 3 ---------------------

declare
v_regnr fordon.regnr%type; 
v_tillverkare fordon.tillverkare%type;
v_modell fordon.modell%type;

begin
	select regnr, tillverkare, modell into v_regnr, v_tillverkare, v_modell from fordon
	where pnr  = '19540201-4428';
	dbms_output.put_line('Regnr: '||upper(v_regnr));
	dbms_output.put_line('Tillverkare: '|| initcap(v_tillverkare));
	dbms_output.put_line('Modell: '|| initcap(v_modell));
exception
    when others then
    	dbms_output.put_line('Följande blev fel: ');
		dbms_output.put_line('Felkod: '|| sqlcode);
		dbms_output.put_line('Felmeddelande: '|| sqlerrm);
end;

----------- UPPGIFT 4 ---------------------

declare
cursor c_kundinfo is select fnamn,enamn, pnr, round((sysdate - to_date(substr(pnr, 1, 8), 'YYYYMMDD')) / 365, 1) ålder
from bilägare;
-- select round((sysdate - to_date(substr(pnr, 1, 8), 'YYYYMMDD')) / 365, 1) || ' år.' as ålder from bilägare;
begin
	for rec in c_kundinfo loop
		dbms_output.put_line(initcap(rec.fnamn)||', '||initcap(rec.enamn)||', '|| rec.ålder || ' år.'); 
	end loop;
end;

----------- UPPGIFT 5 ---------------------

declare
cursor c_kundinfo is select fnamn,enamn,pnr
from bilägare
order by
pnr asc;
v_pnr bilägare.pnr%type;
v_fnamn bilägare.fnamn%type;
v_enamn bilägare.enamn%type;
v_antal_bilar number;
v_text_för_bilar varchar2(10);
begin
	for rec in c_kundinfo loop
    	v_antal_bilar := 0;

		select count(*)
    	into v_antal_bilar
        from fordon
        where pnr = rec.pnr;

		if v_antal_bilar > 1 then
            v_text_för_bilar := ' bilar';
        else
            v_text_för_bilar := ' bil';
        end if;

		dbms_output.put_line(rec.pnr||', '||rec.fnamn||', '||rec.enamn||', äger: '|| v_antal_bilar || v_text_för_bilar); 
	end loop;
end;

----------- UPPGIFT 6 ---------------------

CREATE TABLE fartdåre(
pnr VARCHAR2(13),
fnamn VARCHAR2(20),
enamn VARCHAR2(20),
regnr VARCHAR2(6),
tillverkare VARCHAR2(20),
modell VARCHAR2(20));

select b.pnr, b.fnamn, b.enamn, f.regnr, f.tillverkare, f.modell 
from bilägare b, fordon f 
where b.pnr = f.pnr 
and f.hk > 200;

declare
cursor c_fartdåre is select b.pnr, b.fnamn, b.enamn, f.regnr, f.tillverkare, f.modell 
from bilägare b, fordon f 
where b.pnr = f.pnr 
and f.hk > 200;

v_rec c_fartdåre%rowtype; 

begin    
	if not c_fartdåre%isopen then 
    	open c_fartdåre;
	end if;

	loop
		fetch c_fartdåre 
        into v_rec;
		exit when c_fartdåre%notfound;
			insert into fartdåre(pnr, fnamn, enamn, regnr, tillverkare, modell) 
            values(v_rec.pnr, v_rec.fnamn, v_rec.enamn, v_rec.regnr, v_rec.tillverkare, v_rec.modell);
	end loop;
	commit;
	dbms_output.put_line('Kopieringen är klar!');
close c_fartdåre;
end;

select * from fartdåre