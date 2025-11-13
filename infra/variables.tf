variable "project_name" {
  description = "Base name for ECS, ALB, and other resources"
  type        = string
  default     = "ml-deploy-platform"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "image_uri" {
  description = "ECR image URI with tag"
  type        = string
  default     = "234189402231.dkr.ecr.us-east-1.amazonaws.com/ml-deploy-platform:v1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}
