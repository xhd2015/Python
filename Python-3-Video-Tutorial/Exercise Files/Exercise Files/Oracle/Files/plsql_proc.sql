set echo on

create or replace procedure myproc(v1_p in number, v2_p out number) as
begin
   v2_p := v1_p * 2;
end;
/

show errors

exit
