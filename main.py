import subprocess

# Azure Container Registry credentials
azure_username = "myusername"
azure_password = "mypassword"
azure_registry = "myregistry.azurecr.io"

# Amazon Elastic Container Registry credentials
# Set this block with even env vars or tfvars file:
aws_access_key = "myaccesskey"
aws_secret_key = "mysecretkey"
aws_region = "us-west-2"
# - - - - - - - -- - - - - - 
aws_repository = "myrepository.amazonaws.com"

# List of images to pull and push
image_list = [
    "myimage1:latest",
    "myimage2:latest",
    "myimage3:latest"
]

# Authenticate with Azure Container Registry
azure_login_command = f"docker login {azure_registry} -u {azure_username} -p {azure_password}"
subprocess.run(azure_login_command, shell=True)

# Pull and push each image in the list
for image in image_list:
    # Pull image from Azure Container Registry
    pull_command = f"docker pull {azure_registry}/{image}"
    subprocess.run(pull_command, shell=True)

    # Tag image for Amazon Elastic Container Registry
    tag_command = f"docker tag {azure_registry}/{image} {aws_repository}/{image}"
    subprocess.run(tag_command, shell=True)

    # Authenticate with Amazon Elastic Container Registry
    aws_login_command = f"aws ecr get-login-password --region {aws_region} | docker login --username AWS --password-stdin {aws_repository}"
    subprocess.run(aws_login_command, shell=True)

    # Push image to Amazon Elastic Container Registry
    push_command = f"docker push {aws_repository}/{image}"
    subprocess.run(push_command, shell=True)
