terraform {
  required_version = ">= 1.5"
  backend "s3" {
    # Configure per environment
  }
}

module "vpc" {
  source = "../../modules/vpc"
}

module "eks" {
  source = "../../modules/eks"
}
