# Set Configure
```dockerfile
aws configure
```
# Login
```dockerfile
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 463470967025.dkr.ecr.ap-northeast-1.amazonaws.com
```
# tag
```dockerfile
tag buyside-lambda-0212ver1:latest 463470967025.dkr.ecr.ap-northeast-1.amazonaws.com/ecr/buysidedocker:latest
```
# Push
```dockerfile
push 463470967025.dkr.ecr.ap-northeast-1.amazonaws.com/ecr/buysidedocker:latest
```
# build
```dockerfile
docker build -t buyside-lambda-0212ver1 .
```
# describe image
```dockerfile
aws ecr describe-images --repository-name ecr/buysidedocker --region ap-northeast-1
```
```dockerfile
aws lambda update-function-code \
  --function-name my-lambda-function \
  --image-uri 463470967025.dkr.ecr.ap-northeast-1.amazonaws.com/ecr/buysidedocker:latest
```
# update Lambda function
```dockerfile
cmd /c "aws lambda update-function-code --function-name buyside-ETL-lambda --image-uri 463470967025.dkr.ecr.ap-northeast-1.amazonaws.com/ecr/buysidedocker:latest"
```
# Invoke
```dockerfile
aws lambda invoke --function-name buyside-ETL-lambda --payload '{}' response.json
```
# print log
```dockerfile
aws logs tail /aws/lambda/buyside-ETL-lambda --follow
```