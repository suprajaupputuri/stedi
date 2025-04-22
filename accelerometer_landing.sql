CREATE EXTERNAL TABLE `landing_6b3cb3b3e420d6357a73bb3830f52087`(
  `user` string COMMENT 'from deserializer', 
  `timestamp` bigint COMMENT 'from deserializer', 
  `x` double COMMENT 'from deserializer', 
  `y` double COMMENT 'from deserializer', 
  `z` double COMMENT 'from deserializer')
PARTITIONED BY ( 
  `partition_0` string, 
  `partition_1` string)
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'paths'='timestamp,user,x,y,z') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stedi-supraja/accelerometer/landing/'
TBLPROPERTIES (
  'CRAWL_RUN_ID'='51d005de-c123-46e2-ae13-e559c7c5d1a9', 
  'CrawlerSchemaDeserializerVersion'='1.0', 
  'CrawlerSchemaSerializerVersion'='1.0', 
  'UPDATED_BY_CRAWLER'='Accelerator-landing2', 
  'averageRecordSize'='761', 
  'classification'='json', 
  'compressionType'='none', 
  'objectCount'='9', 
  'partition_filtering.enabled'='true', 
  'recordCount'='9007', 
  'sizeKey'='6871328', 
  'typeOfData'='file')
