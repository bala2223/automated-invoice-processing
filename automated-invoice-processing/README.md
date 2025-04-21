# 🧾 Automated Serverless Invoice Processing System (AWS)

This project demonstrates a fully serverless application on AWS to automatically process invoice images, extract text using Textract, and notify users via email.

## 📌 Technologies Used
- Amazon S3
- AWS Lambda
- Amazon Textract
- Amazon DynamoDB
- Amazon SNS
- CloudWatch

## ✅ Workflow

1. Upload invoice image (PNG) to S3
2. Triggers the Lambda function
3. Extracts text → saves to DynamoDB
4. Sends email using SNS
5. Logs saved to CloudWatch

## 🧠 Folder Structure

