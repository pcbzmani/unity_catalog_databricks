# Databricks notebook source
# MAGIC %sql
# MAGIC create catalog if not exists formula1_dev;

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog formula1_dev;

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists bronze
# MAGIC managed location 'abfss://bronze@databricksucexternalloca.dfs.core.windows.net/bronze/'

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists silver
# MAGIC managed location 'abfss://silver@databricksucexternalloca.dfs.core.windows.net/silver/'

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists gold
# MAGIC managed location 'abfss://gold@databricksucexternalloca.dfs.core.windows.net/gold/'

# COMMAND ----------


