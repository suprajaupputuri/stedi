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

CustomerTrusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options = {"multiline":True},
    connection_type = "s3",
    format = "json",
    connection_options = {
        "paths":["s3://stedi-supraja/customer/trusted"],
        "recurse":True,
    },
    transformation_ctx="CustomerTrusted_node1"
)
    
AccelerometerLanding_node1  = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline":True},
    connection_type="s3",
    format="json",
    connection_options = {
        "paths":["s3://stedi-supraja/accelerometer/landing/"],
        "recurse":True,
        
    },
    transformation_ctx = "AccelerometerLanding_node1"
)
    
JoinCustomer_node = Join.apply(
    frame1=CustomerTrusted_node1,
    frame2=AccelerometerLanding_node1,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="JoinCustomer_node"
)
    
DropFields_node=DropFields.apply(
    frame=JoinCustomer_node,
    paths=["serialNumber",
           "shareWithPublicAsOfDate",
           "birthday",
           "registrationDate",
           "shareWithResearchAsOfDate",
           "customerName",
           "email",
           "lastUpdateDate",
           "phone",
           "shareWithFriendsAsOfDate"
           ],
   transformation_ctx="DropFields_node",
)

AccelerometerTrusted_node2 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node,
    connection_type="s3",
    format="json",
    connection_options={
        "path":"s3://stedi-supraja/accelerometer/trusted/",
        "partitionKeys":[],
        },
    transformation_ctx="AccelerometerTrusted_node2")
job.commit()