from aws_cdk import (
    Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as lambda_
)
from constructs import Construct


class MyAwsAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        test_func = lambda_.Function(self, 'MyTestFunction',
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="lambda_handler",
            code=lambda_.Code.from_inline("""
                def lambda_handler(event, context):
                    return {
                        'result': 10
                    }
            """),
            timeout=Duration.minutes(1)
        )
