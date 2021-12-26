#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pipeline import MyPipelineStack


app = cdk.App()

env = cdk.Environment(
    account=os.environ['CDK_DEFAULT_ACCOUNT'],
    region='asia-east1'
)

MyPipelineStack(app, "MyPipelineStack", env=env)

app.synth()
