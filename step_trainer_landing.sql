CREATE EXTERNAL TABLE `landing_855424f8fc42f87e9ab204b412c7ce2b`(
  `sensorreadingtime` bigint COMMENT 'from deserializer', 
  `serialnumber` string COMMENT 'from deserializer', 
  `distancefromobject` int COMMENT 'from deserializer')
PARTITIONED BY ( 
  `partition_0` string, 
  `partition_1` string)
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'paths'='distanceFromObject,sensorReadingTime,serialNumber') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stedi-supraja/step_trainer/landing/'
TBLPROPERTIES (
  'CRAWL_RUN_ID'='c1075f13-fb72-4581-b98a-653315259038', 
  'CrawlerSchemaDeserializerVersion'='1.0', 
  'CrawlerSchemaSerializerVersion'='1.0', 
  'UPDATED_BY_CRAWLER'='step_trainer-landing3', 
  'averageRecordSize'='1032', 
  'classification'='json', 
  'compressionType'='none', 
  'objectCount'='3', 
  'partition_filtering.enabled'='true', 
  'recordCount'='3194', 
  'sizeKey'='3298200', 
  'typeOfData'='file')
