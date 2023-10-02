# Script.io: OpenAI Completions API Integration

This README provides an overview of the deployment process. Be sure to customize your Lambda function's configuration, environment variables, and IAM permissions according to your specific requirements.

## AWS Lambda using AWS CLI

Follow these steps to deploy and run this Lambda function on AWS:

1. **Set up your AWS Account:**

   If you haven't already, create an AWS account or use an existing one.

2. **Configure AWS CLI:**

   Install the AWS Command Line Interface (CLI) and configure it with your AWS credentials.

   ```bash
   pip install awscli
   aws configure
   ```

3. **Package Dependencies:**

   Package your Lambda function along with its dependencies into a deployment package.

   ```bash
   pip install -r requirements.txt -t ./
   ```

4. **Create a Deployment Package:**

   Create a ZIP archive containing your Lambda function and its dependencies.

   ```bash
   zip -r lambda_function.zip ./*
   ```

5. **Create an IAM Role:**

   Create an IAM Role with permissions for your Lambda function. Ensure it has permissions to call the OpenAI API and any other AWS services you might use.

6. **Deploy the Lambda Function:**

   Use the AWS CLI to create the Lambda function. Replace `YOUR_ROLE_ARN` with the ARN of the IAM Role you created.

   ```bash
   aws lambda create-function --function-name openai-api-lambda \
     --runtime python3.8 \
     --role YOUR_ROLE_ARN \
     --handler lambda_function.lambda_handler \
     --zip-file fileb://lambda_function.zip
   ```

## AWS Lambda Setup on lambda console

To deploy this script as an AWS Lambda function, follow these steps:

1. Create an AWS Lambda function using the AWS Management Console or AWS CLI.

2. Upload the Lambda deployment package, including your code and any required dependencies.

3. Set the environment variable `OPENAI_API_KEY` in your Lambda function configuration with your OpenAI API key.

4. Configure the Lambda function's handler to be `lambda_function.lambda_handler`, where `lambda_function` is the name of your script.

5. Monitor your Lambda function's execution and use AWS CloudWatch Logs for troubleshooting.

Certainly, here are steps 5 to 11 related to setting up the API Gateway:

## API Gateway Setup

1. **Create an API Gateway:**

   - In the AWS Management Console, navigate to API Gateway.
   - Click on "Create API" and choose "HTTP API" or "REST API" based on your requirements.

2. **Create a New Resource and Method:**

   - Inside your API, create a new resource (e.g., `/myresource`) and a method (e.g., POST) under that resource.

3. **Enable CORS for Your API Gateway Resource:**

   - Select the resource you just created.
   - In the "Actions" dropdown, click on "Enable CORS."
   - Configure CORS settings as needed to allow cross-origin requests.
4. **Enable Lambda Proxy Integration:**

   - In the method configuration, under "Integration," choose "Lambda Function" as the integration type.
   - Select the Lambda function you previously created.

5. **Use the Mapping Template:**

   - In the method configuration, under "Integration Request," choose "Mapping Templates."
   - Add a new mapping template with content:

     ```json
      #set($allParams = $input.params())
      {
        "body-json": $input.json('$'),
        "context" : {
          "http-method" : "$context.httpMethod"
        }
      }
     ```

   - Save the mapping template.

6. **Deploy Your API:**

    - In the API Gateway menu, select "Deployments."
    - Create a new deployment stage (e.g., "prod" or "test").
    - Deploy your API to the stage you created.

7. **Obtain the Endpoint URL:**

    - After deployment, your API will have an endpoint URL (e.g., https://your-api-id.execute-api.us-east-1.amazonaws.com/your-stage).
    - This URL is where you will make API requests.

With these steps completed, your API Gateway is configured to pass incoming requests to your Lambda function. You can now make API requests to your endpoint URL, and the Lambda function will process them.

## Example Request

To generate code using the API, make a POST request to your API Gateway endpoint with the following JSON payload:

```json
{
  "action": "GenerateCode",
  "language": "Java",
  "package": "",
  "request": {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "java binary search for an array of 10 elements"
      }
    ],
    "temperature": 1,
    "max_tokens": 2048,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
  }
}
```
### ACTIONS: GenerateCode, AnalyseCode, GenerateTest

The Lambda function will process the request and return the generated code.