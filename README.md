![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fsuperissy%2Fcloud-sec-remediation-practice.git&countColor=%2337d67a&labelStyle=upper)

# Hands-On Session: Cloud Security with AWS - AWS User Group Nigeria

Welcome to this hands-on session designed for cloud professionals and those transitioning into cloud security. This session will focus on **Cloud Security**, **AWS Well-Architected Framework**, and **AWS Cloud Adoption Framework (CAF)**. We'll also dive into **detective and responsive capabilities** in the cloud, and how to **tag and resolve misconfigured or vulnerable resources**. By the end of this session, you'll have practical experience with **AWS Config Rules**, **Security Hub**, and **GuardDuty**, along with a coding walkthrough to remediate findings using **AWS Systems Manager (SSM)**.

---

## **Session Overview**

### **Cloud Security Categories**
Cloud security is a shared responsibility between the cloud provider and the customer. Key categories include:
1. **Identity and Access Management (IAM)**: Control who can access what.
2. **Data Protection**: Encrypt data at rest and in transit.
3. **Threat Detection and Monitoring**: Identify and respond to threats in real-time.
4. **Compliance and Governance**: Ensure adherence to regulatory standards.
5. **Infrastructure Security**: Secure compute, storage, and networking resources.

### **AWS Well-Architected Framework**
The AWS Well-Architected Framework provides best practices for building secure, high-performing, resilient, and efficient infrastructure. The **Security Pillar** focuses on:
- Protecting data and systems.
- Setting up strong identity foundations.
- Enabling traceability.
- Applying security at all layers.

### **AWS Cloud Adoption Framework (CAF)**
The AWS CAF helps organizations plan and execute their cloud journey. The **Security Perspective** of CAF emphasizes:
- Establishing a security baseline.
- Implementing detective and responsive controls.
- Automating security processes.

### **Detective and Responsive Capabilities in Cloud**
- **Detective Capabilities**: Tools like **AWS Config**, **Security Hub**, and **GuardDuty** help identify misconfigurations, vulnerabilities, and threats.
- **Responsive Capabilities**: Automate remediation using tools like **AWS Systems Manager (SSM)** and **Lambda**.


---

## **List of AWS Config Rule Scenarios**
We'll focus on the following AWS Config Rules to identify misconfigurations:
1. **s3-bucket-public-read-prohibited**: Ensures S3 buckets are not publicly readable.
2. **s3-bucket-logging-enabled**: Ensures S3 bucket logging is enabled.
3. **s3_bucket_key_enabled**: Ensures S3 bucket default encryption is enabled.

---

## **Hands-On Topics**
### 1. **AWS Config Rules**
   - Create and manage Config Rules to monitor resource compliance.
   - Evaluate configurations and identify non-compliant resources.

### 2. **AWS Security Hub**
   - Aggregate and prioritize findings from multiple AWS services.
   - Centralize security insights and compliance status.

### 3. **Amazon GuardDuty**
   - Detect threats and malicious activity using machine learning.
   - Analyze findings and integrate with Security Hub.

---

## **Coding Walkthrough: Remediate Config Findings**

### **Scenario: Remediate `s3-bucket-logging-enabled` Findings Using SSM Automation**
In this walkthrough, we'll remediate an S3 bucket that does not have logging enabled using **AWS Systems Manager (SSM)**.

#### **Steps:**
1. **Identify Non-Compliant Resources**:
   - Use AWS Config to identify S3 buckets without logging enabled.

2. **Create an SSM Automation Document**:
   - Define an automation workflow to enable S3 bucket logging.

3. **Trigger Remediation**:
   - Automatically remediate non-compliant resources using SSM.


## **Key Takeaways**
- Understand the importance of **detective and responsive capabilities** in cloud security.
- Learn how to use **AWS Config**, **Security Hub**, and **GuardDuty** to monitor and secure your environment.
- Automate remediation using **SSM** and **Lambda**.
- Apply tagging strategies to efficiently manage and resolve misconfigured or vulnerable resources.

---

## **Next Steps**
- Explore additional AWS Config Rules and Security Hub integrations.
- Experiment with other remediation techniques using Lambda and SSM.
- Dive deeper into the **AWS Well-Architected Framework** and **Cloud Adoption Framework** for advanced security practices.

Let’s get started and secure your cloud environment! 🚀
