-- Databricks notebook source
show catalogs;

-- COMMAND ----------

use catalog uc_demo_catalog;

-- COMMAND ----------

show schemas;

-- COMMAND ----------

use schema uc_demo_f1schema;

-- COMMAND ----------

show tables

-- COMMAND ----------

use catalog uc_demo_catalog;
use schema uc_demo_f1schema;
select * from circuits;

-- COMMAND ----------


