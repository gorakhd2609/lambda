# 🚀 AWS Serverless Image Resizer

This project is a serverless image processing pipeline built using AWS Lambda and Amazon S3.

## 📌 How it Works

1. User uploads an image to the source S3 bucket (`myf1`)
2. This triggers an AWS Lambda function
3. Lambda resizes the image using Pillow
4. The resized image is stored in another S3 bucket (`myf1-resize`)

---

## ⚙️ Tech Stack

- AWS Lambda
- Amazon S3
- Python
- Pillow (Python Imaging Library)

---

## 🧱 Architecture

![Architecture](architecture.png)

---

## 🔥 Features

- Automatic image resizing
- Event-driven architecture
- Serverless (no server management)
- Fast and scalable

---

## 🛠️ Setup Steps

1. Create two S3 buckets:
   - Source: `myf1`
   - Destination: `myf1-resize`

2. Create Lambda function (Python 3.x)

3. Add Pillow using Lambda Layer

4. Attach IAM Role with permissions:
   - s3:GetObject (source bucket)
   - s3:PutObject (destination bucket)

5. Add S3 trigger on `myf1` (PUT event)

---

## 🧪 Testing

Upload an image to the source bucket (`myf1`) and check the resized output in `myf1-resize`.

---

## 📸 Output

Original Image → Resized Image (100x100)

---

## 💡 Learnings

- Handling dependencies in AWS Lambda using Layers
- Fixing IAM permission issues (AccessDenied)
- Working with S3 event triggers
- Debugging using CloudWatch logs

---

## 👨‍💻 Author

Your Name
