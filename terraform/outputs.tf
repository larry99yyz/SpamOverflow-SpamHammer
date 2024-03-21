# terraform/outputs.tf
output "public_ip" {
  value = aws_instance.spamoverflow_instance.public_ip
}
