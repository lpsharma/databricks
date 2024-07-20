# Databricks notebook source
# Python Version

import sys

print(sys.version)

# COMMAND ----------

catalog = "lalitcatalog"
schema = "customschema"
volume = "Azurevol"
download_url = "https://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv"
file_name = "baby_names.csv"
table_name = "baby_names"
path_volume = "/Volumes/" + catalog + "/" + schema + "/" + volume
path_table = catalog + "." + schema
print(path_table) # Show the complete path
print(path_volume) # Show the complete path

dbutils.fs.cp(f"{download_url}", f"{path_volume}" + "/" + f"{file_name}")


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM read_files('/Volumes/lalitcatalog/customschema/Azurevol/Accounts.csv')
