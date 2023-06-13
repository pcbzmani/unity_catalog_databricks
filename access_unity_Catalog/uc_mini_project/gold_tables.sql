-- Databricks notebook source
drop table if exists  formula1_dev.gold.f1_winner;

create table if not exists formula1_dev.gold.f1_winner as
select dr.name, count(*) as winning_cnt from formula1_dev.silver.drivers dr
inner join formula1_dev.silver.results re   
on dr.driver_id = re.driver_id
where re.position = 1
group by dr.name;

-- COMMAND ----------

select * from formula1_dev.gold.f1_winner 
order by winning_cnt desc

-- COMMAND ----------


