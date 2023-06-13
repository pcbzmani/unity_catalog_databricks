# Databricks notebook source
dbutils.fs.ls('abfss://demo@databricksucexternalloca.dfs.core.windows.net/')

# COMMAND ----------

df = spark.read.format('csv').\
    option('header',True).\
    load('abfss://demo@databricksucexternalloca.dfs.core.windows.net/circuits.csv')

# COMMAND ----------

display(df)

# COMMAND ----------


