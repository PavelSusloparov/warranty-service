# Deployment

The service is deployed to AWS Elasticbeanstalk.

## Howto

* Install Elasticbeanstalk CLI locally. Follow readme [here](https://github.com/aws/aws-elastic-beanstalk-cli-setup).
*Important:* Use option to compile cli with your Python 3.7
* Follow steps to deploy the application [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
*Important:* Since the project structure is different than what Elasticbeanstalk expects from Flask project, configure 
`aws:elasticbeanstalk:container:python` option to be `WSGIPath: service:application`. Do it either through AWS console, 
Elasticbeanstalk->Application->Configure or use `eb configure`.

## SSL

### Self-signed cert
* [Generate self signed certificates](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html)
* [Upload self signed cert to iam](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl-upload.html)
* When ssh to EC2 instance, use `aws configure` for AWS auth.
* [Apply self signed cert to beanstalk LB](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html)

### Certificate manager
* Add your domain to AWS Certificate manager
* [Apply self signed cert to beanstalk LB](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html) 