# Databricks notebook source
# DBTITLE 1,Create External location
# MAGIC %sql
# MAGIC CREATE EXTERNAL LOCATION uc_bronze_dl
# MAGIC  URL 'abfss://bronze@databricksucexternalloca.dfs.core.windows.net/'
# MAGIC  WITH (STORAGE CREDENTIAL uc_external_location_demo);

# COMMAND ----------

# MAGIC %sql
# MAGIC desc external location uc_bronze_dl;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE EXTERNAL LOCATION uc_silver_dl
# MAGIC  URL 'abfss://silver@databricksucexternalloca.dfs.core.windows.net/'
# MAGIC  WITH (STORAGE CREDENTIAL uc_external_location_demo);

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE EXTERNAL LOCATION uc_gold_dl
# MAGIC  URL 'abfss://gold@databricksucexternalloca.dfs.core.windows.net/'
# MAGIC  WITH (STORAGE CREDENTIAL uc_external_location_demo);

# COMMAND ----------


