# terraform/main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "spamoverflow_instance" {
  ami           = "ami-12345678" # Replace with your AMI ID
  instance_type = "t2.micro"
}

output "public_ip" {
  value = aws_instance.spamoverflow_instance.public_ip
}
