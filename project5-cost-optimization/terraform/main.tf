# Lambda + EventBridge + IAM for the cost scanner
resource "aws_lambda_function" "cost_scanner" {
  function_name = "cost-optimization-scanner"
  runtime       = "python3.12"
  handler       = "scanner.handler"
  # ...
}
