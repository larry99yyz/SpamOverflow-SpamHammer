#  SpamOverflow-SpamHammer Email Filtering Service

 SpamOverflow-SpamHammer is a microservices-based email filtering platform designed to scan and filter malicious emails. This project implements a scalable web API for scanning emails using the spamhammer tool provided.

## Introduction

For this assignment, you are working for  SpamOverflow-SpamHammer, a new competitor in the email security space.  SpamOverflow-SpamHammer uses a microservices-based architecture to implement their new malicious email filtering platform.

## Requirements

### Email Filtering Software

 SpamOverflow-SpamHammer will implement a service that does not impede the flow of traffic (i.e., does not prevent the email arriving). It will receive an API call when the mail server receives an email message. The service then pulls the email from the user’s inbox as fast as it can to prevent the user from seeing the malicious email or clicking any links.

### Interface

The interface specification is available to all service owners online: [ SpamOverflow-SpamHammer API Specification](https://csse6400.uqcloud.net/assessment/ SpamOverflow-SpamHammer)

### Implementation

#### SpamHammer

You have been provided with a command-line tool called spamhammer that can be used to scan emails for malicious content. This tool is developed by Dr. Richardson who is an AI and linguistic expert. The tool has varying performance, roughly related to the length of the content. Your service must utilize the spamhammer command-line tool provided for this assignment. You are not allowed to reimplement or modify this tool.

#### Similarity

Dr. Richardson has also provided some advice to help you with filtering through the emails. She has suggested that you use a similarity metric to compare the body of emails to previously known bad emails.

#### AWS Services

Please make note of the [AWS services](https://labs.vocareum.com/web/2460291/1564816.0/ASNLIB/public/docs/lang/en-us/README.html#services) that you can use in the AWS Learner Lab.

#### External Services

You may not use services or products from outside of the AWS Learner Lab environment.

## Directory Structure
```

- **app/**: Contains the Flask application code.
- **Dockerfile**: Defines the Docker image for containerization.
- **requirements.txt**: Specifies Python dependencies.
- **terraform/**: Contains Terraform configuration for provisioning AWS resources.
- **local.sh**: Script for building and running the Docker container locally.
- **README.md**: Comprehensive documentation about the project.

## Installation and Setup

### Prerequisites

- Docker installed on your local machine
- AWS account for deployment

### Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ SpamOverflow-SpamHammer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd  SpamOverflow-SpamHammer
   ```

3. Build and run the Docker container locally:

   ```bash
   ./local.sh
   ```

   This will build the Docker image and run the Flask application on `http://localhost:8080`.

## Usage

### API Endpoints

- **POST /scan/**: Initiates the email scanning process.

  Request Body:
  ```json
  {
    "email_id": "example@email.com"
  }
  ```

  Response:
  ```json
  {
    "message": "Email scan initiated.",
    "result": "Clean"
  }
  ```

## Deployment to AWS

1. Set up AWS credentials with appropriate permissions.

2. Navigate to the `terraform/` directory:

   ```bash
   cd terraform
   ```

3. Initialize Terraform:

   ```bash
   terraform init
   ```

4. Deploy the infrastructure:

   ```bash
   terraform apply
   ```

5. Access the deployed API using the public IP address provided in the Terraform output.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or bug fixes.

## License



You can copy this entire markdown content and save it as `README.md` in your project directory. Adjustments can be made based on specific project requirements.
