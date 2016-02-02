set echo on
drop table ptab;

create table ptab (mydata varchar(20), myid number);

commit;

create or replace function myfunc(d_p in varchar2, i_p in number) return number as
begin
  insert into ptab (mydata, myid) values (d_p, i_p);
  return (i_p * 2);
end;
/

show errors

exit
