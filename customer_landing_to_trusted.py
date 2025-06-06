import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

CustomerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options ={"multiline":False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-supraja/customer/landing/"],
        "recurse":True,
    },
    transformation_ctx = "CustomerLanding_node1",
)

PrivacyFilter_node1696826394878 = Filter.apply(
    frame=CustomerLanding_node1,
    f = lambda row:(not (row["shareWithResearchAsOfDate"] == 0)),
    transformation_ctx = "PrivacyFilter_node1696826394878",
)

TrustedCustomerZone_node2 = glueContext.write_dynamic_frame.from_options(
    frame=PrivacyFilter_node1696826394878,
    connection_type="s3",
    format="json",
    connection_options={
        "path":"s3://stedi-supraja/customer/trusted/",
        "partitionKeys":[],
        },
    transformation_ctx = "TrustedCustomerZone_node2"
)    
job.commit()