# respond.io-DevOpsAssessment

################# Prequisites ################

Install Python3,
Install and Configure AWS CLI,
Install AWS SAM CLI,
######################################################################################

############################ TASK 1 #######################

Step 1
create Lambda Function using SAM

Step 2
create trigger for Lambda when new object added in S3 bucket, you can verify trigger by going to S3Bucke/Properties/EventNotfications

Step 3
lambda function that 1: Check if file is zip or not, 2: if not, download file in temp, 3: will convert it to zip, 4: Upload file to s3
and 5: Delete older file from S3 bucket

Step 4
Create Custom Role and Permission for Lambda function to get,put and delete obj from S3 bucket

############################ TASK 2 #######################

Create S3 Bucket that will have Json Video Files and Connect with LAMBDA in Template File

##############################################################################################

########### To run this project run: #####################

sam deploy --capabilities CAPABILITY_NAMED_IAM (in terminal)

##############################################################################################

############################ TASK 4 ########################

######################## Cost Analysis ##################### 

######################### LAMBDA COST ######################

Unit conversions
Number of requests: 1000000 per hour * (730 hours in a month) = 730000000 per month
Amount of memory allocated: 128 MB x 0.0009765625 GB in a MB = 0.125 GB
Amount of ephemeral storage allocated: 512 MB x 0.0009765625 GB in a MB = 0.5 GB
Pricing calculations
730,000,000 requests x 4 ms x 0.001 ms to sec conversion factor = 2,920,000.00 total compute (seconds)
0.125 GB x 2,920,000.00 seconds = 365,000.00 total compute (GB-s)
365,000.00 GB-s - 400000 free tier GB-s = -35,000.00 GB-s
Max (-35000.00 GB-s, 0 ) = 0.00 total billable GB-s
Tiered price for: 0.00 GB-s
Total tier cost = 0.00 USD (monthly compute charges)
730,000,000 requests - 1000000 free tier requests = 729,000,000 monthly billable requests
Max (729000000 monthly billable requests, 0 ) = 729,000,000.00 total monthly billable requests
729,000,000.00 total monthly billable requests x 0.0000002 USD = 145.80 USD (monthly request charges)
0.50 GB - 0.5 GB (no additional charge) = 0.00 GB billable ephemeral storage per function
Lambda costs - With Free Tier (monthly): 145.80 USD

######################## SUGGESTIONS ######################

S3 Storage Classes: Evaluate if using S3 Glacier or S3 Glacier Deep Archive storage classes for less frequently accessed data could be more cost-effective.

Data Transfer Acceleration: Use Amazon S3 Transfer Acceleration if you have clients accessing the S3 bucket from different geographical locations.

Optimize Lambda Memory: If the Lambda function can run with less memory, you can reduce the cost per execution.

Compression: Optimize the compression algorithm to reduce the output file size, which can lead to lower storage and transfer costs.

#########################################################################################

####################### TASK 5 #####################################

The Lambda function can handle the basic requirements of converting JSON files to ZIP, uploading to S3, and deleting the original JSON file. However, there are some concerns and potential bottlenecks that need to be addressed to ensure scalability and efficiency:

Concurrency Limits: AWS Lambda has concurrency limits per region, which may impact the scalability of your solution. If your S3 bucket receives a large number of objects simultaneously, you could run into issues where Lambda functions are queued, leading to delays in processing.

Cold Starts: Lambda functions may experience cold starts, where the initial execution can take longer due to the need to provision resources. This can impact the responsiveness of your system, especially if there is a sudden influx of objects to process.

Execution Time Limit: Lambda functions have a maximum execution time limit (15 minutes by default). If your video processing and compression take a significant amount of time, you might hit this limit, causing the Lambda function to be terminated before completion.

Resource Allocation: Lambda has limited CPU and memory resources. Depending on the size and complexity of the video processing task, you might need to fine-tune the Lambda function's memory allocation to ensure optimal performance.

Error Handling: Ensure your Lambda function has robust error handling. If there's an issue during processing, such as a failure to convert the JSON to ZIP or an S3 upload failure, it's crucial to handle these errors gracefully and possibly trigger retries.

S3 Event Rate Limiting: S3 has event rate limiting, and if there is a high volume of objects being added to the bucket, you may encounter delays in triggering the Lambda function for each object.

S3 Bucket Throughput: The scalability of your solution is also dependent on the throughput of your S3 bucket. Ensure that the bucket can handle the rate of incoming and outgoing data without becoming a bottleneck.

Monitoring and Logging: Implement comprehensive monitoring and logging to identify any issues promptly. Utilize AWS CloudWatch metrics and logs to keep track of Lambda function executions, errors, and resource usage.

To address these concerns and bottlenecks, you might consider implementing solutions such as using Different S3 class to archive the Video files which I think is the best solution.

Thanks
######################################################################################
########################################################################################################################################


