# BirdVision
Assignment of BirdVision for DevOps.


# Prerequisites
Before you begin, ensure you have the following prerequisites installed:

Python (version 3.8 or later)
AWS CLI (Amazon Web Services Command Line Interface)

# Steps to Deploy
1. Develop the Lambda Function.
Create a new Python file named lambda_function.py.
Write the Lambda function code inside lambda_function.py and
Package the function code into a deployable ZIP archive:

2. Define Infrastructure as Code (IaC)
Create a new file named cloudformation.yml.
Write the CloudFormation template to define the Lambda function and IAM role. See the cloudformation.yml file in the repository for an example template.

3. Set Up GitHub Actions Workflow
Create a new directory named .github/workflows.
Inside the workflows directory, create a new YAML file named deploy.yml.
Write the GitHub Actions workflow to automate the deployment process. See the deploy.yml file in the repository for an example workflow.

5. Deploy Lambda Function
Commit your Lambda function code (lambda_function.py and lambda_function.zip) and CloudFormation template (cloudformation.yml) to your GitHub repository.
Push the changes to the main branch of your repository.
GitHub Actions will automatically trigger the deployment workflow on each push to the main branch. The Lambda function will be deployed using the CloudFormation template.
