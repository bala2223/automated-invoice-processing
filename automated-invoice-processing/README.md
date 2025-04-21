# 🧾 Automated Serverless Invoice Processing System (AWS)

This project showcases a fully **serverless architecture** built on AWS that automates the processing of invoice images. When a user uploads an invoice (PNG image) to Amazon S3, a Lambda function is triggered, which extracts text using Amazon Textract, stores the results in DynamoDB, and sends an email notification via SNS.

> 🔧 Built using AWS S3, Lambda, Textract, DynamoDB, SNS, and CloudWatch  
> 📦 Project by: Kavinaya Ramesh | MS Student, UMass Dartmouth

---

## 📌 Technologies Used

| AWS Service        | Purpose                                     |
|--------------------|---------------------------------------------|
| **Amazon S3**       | Stores uploaded invoice files               |
| **AWS Lambda**      | Processes each uploaded file serverlessly   |
| **Amazon Textract** | Extracts text (OCR) from uploaded image     |
| **Amazon DynamoDB** | Stores extracted text in NoSQL format       |
| **Amazon SNS**      | Sends email notifications to users          |
| **Amazon CloudWatch** | Logs function execution and errors        |

---

## 🗂 Folder Structure
automated-invoice-processing/ ├── README.md ├── lambda/ │ └── invoice_processor.py # Lambda function code ├── architecture/ │ └── architecture-diagram.png # Visual system design (optional) ├── screenshots/ │ └── cloudwatch-log.png # Log proof (optional)


---

## 📊 Architecture Diagram

 +-------------+
 |   User      |
 | (uploads)   |
 +------+------+
        |
        v
+---------------------+ +----------------------+ | Amazon S3 Bucket | ---------> | AWS Lambda | | invoices/*.png file | (event) | (InvoiceProcessorFunc)| +---------------------+ +----------+-----------+ | v +------------------------+ | Amazon Textract (OCR) | | Extracts invoice text | +------------------------+ | v +--------------------------+ | Amazon DynamoDB | | Stores text with ID | +--------------------------+ | v +--------------------------+ | Amazon SNS (Email) | | Sends notification email | +--------------------------+



---

## ⚙️ Step-by-Step Workflow

1. **File Upload**
   - A user uploads an invoice image (`.png`) into an S3 bucket under a specific prefix (`invoices/`)

2. **Lambda Triggered**
   - The S3 event triggers a Lambda function (`InvoiceProcessorFunction`)

3. **Text Extraction**
   - The function sends the file to **Textract**, which reads all text in the invoice image

4. **Data Storage**
   - The extracted text, along with a unique ID and file name, is saved in the **DynamoDB** table `InvoiceData`

5. **Email Notification**
   - A confirmation email is sent using **Amazon SNS** with details about the processed invoice

6. **Monitoring**
   - All logs, errors, and status info are recorded in **CloudWatch Logs**

---

## 📝 Sample Extracted Output

Here’s an example of what Textract may extract and what gets stored:
ABC TECHNOLOGIES INC
Invoice Number: INV-00123
Date: 2025-04-21
Billed To: Kavinaya Ramesh
Items:
   Cloud Hosting: $200
   Maintenance: $100
Total: $300

## 📬 Email Notification

The SNS email body may look like:
Subject: Invoice Processed
Invoice invoices/invoice_page_1.png processed and stored with ID: 2d1a7e65-9f23-4a92-885b-f1234abcd678

## ✅ Expected Outcomes

- 🔁 **Automated flow**: Just upload → everything else happens automatically
- 📧 **User receives email** with invoice ID
- 💾 **Text is stored** for future lookup or analysis
- 🔍 **CloudWatch shows** end-to-end logging for full traceability

---

## 🧠 Learning Outcomes

Through this project, I learned:

- How to build event-driven serverless apps using **AWS Lambda**
- How to process image files using **Textract OCR**
- How to securely store structured data in **DynamoDB**
- How to automate notifications using **Amazon SNS**
- How to monitor and troubleshoot serverless apps via **CloudWatch Logs**
- Real-world application of AWS architecture principles

---

## 💡 Future Enhancements

- Extract only specific invoice fields like Total, Date, and Vendor Name
- Add frontend UI to display invoice records
- Add support for PDFs using `start_document_text_detection`
- Add IAM role security refinements
- Enable tagging and filtering of invoices by type

---

## ✍️ Author

**Kavinaya Ramesh**  
🎓 MS in Computer & Information Science – University of Massachusetts Dartmouth  
📧 kavinayaramesh2002@gmail.com  












