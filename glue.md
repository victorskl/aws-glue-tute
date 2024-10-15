# AWS Glue

Managed data integration service.

3 components:

- Crawler
- Job (ETL)
- Catalog

## Catalog

- contain metadata store (Hive metastore) --- _Glue Metastore is a serverless Apache Hive compatible metastore_ 
- contain database 
- a database contain tables
- database and table can be provisioned by
  - AWS Console
  - AWS CLI
  - Terraform, CDK or CloudFormation

## Compute

3 engines:

- Python Shell (single node)
- Spark (multi-nodes)
- Ray (multi-nodes)

## Use Case

Typically, Glue Crawler crawls the data and Catalog them.

Glue Job can be Spark ETL job written in Python.
  - S3 in / S3 out
  - RDS/JDBC/RDBMS in / S3 out
  - RDS/JDBC/RDBMS in / Another RDBMS out
  - Lake in / Lake out (Parquet, ORC, Iceberg, Delta, ...)
  - ... so on so forth

A complex workflow consisting of multiple Glue Jobs can be orchestrated by AWS SteFunction.

Support both ETL and ELT data integration pattern.
