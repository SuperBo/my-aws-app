import aws_cdk as cdk
from constructs import Construct

from my_pipeline.my_pipeline_lambda_stack import MyLambdaStack
from my_aws_app.my_aws_app_stack import MyAwsAppStack


class MyPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myAppStack = MyAwsAppStack(self, "MyAwsAppStack")
