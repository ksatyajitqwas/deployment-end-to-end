# Example: create the secret container (value is set outside Terraform)
resource "aws_secretsmanager_secret" "db_credentials" {
  name        = "prod/demo-app/db"
  description = "Database credentials for demo-app"
}

# Rotation can be attached via aws_secretsmanager_secret_rotation
