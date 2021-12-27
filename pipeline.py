import aws_cdk as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

from deployment import MyPipelineAppStage


class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        github_arn = self.format_arn(
            region='us-east-1',
            service='codestar-connections',
            resource='connection',
            resource_name='83c4a42b-31db-4655-9dc4-9576a0058bb7'
        )

        pipeline = CodePipeline(self, 'MyPipeline',
            pipeline_name="MyPipeline",
            synth=ShellStep("Synth", 
                input=CodePipelineSource.connection('SuperBo/my-aws-app', 'main',
                    connection_arn=github_arn
                ),
                commands=[
                    'npm install -g aws-cdk', 
                    'python -m pip install -r requirements.txt', 
                    'cdk synth'
                ]
            ),
            cross_account_keys=False,
        )

        pipeline.add_stage(MyPipelineAppStage(self, 'production'))
