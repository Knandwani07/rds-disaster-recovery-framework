import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    source_region = 'us-east-1'
    target_region = 'us-west-2'
    db_identifier = 'dr-primary-db'
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']
    target_kms_key_id = os.environ['TARGET_KMS_KEY_ARN']  

    source_client = boto3.client('rds', region_name=source_region)
    target_client = boto3.client('rds', region_name=target_region)
    sns_client = boto3.client('sns', region_name=source_region)

    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M')
    snapshot_id = f'dr-snapshot-{timestamp}'

    try:
        print(f"Creating snapshot: {snapshot_id}")
        source_client.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_id,
            DBInstanceIdentifier=db_identifier
        )

        waiter = source_client.get_waiter('db_snapshot_available')
        waiter.wait(DBSnapshotIdentifier=snapshot_id)
        print(f"Snapshot {snapshot_id} is available")

        response = source_client.describe_db_snapshots(
            DBSnapshotIdentifier=snapshot_id
        )
        snapshot_arn = response['DBSnapshots'][0]['DBSnapshotArn']

        target_snapshot_id = f'dr-replica-{timestamp}'
        print(f"Copying snapshot to {target_region}")
        target_client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=snapshot_arn,
            TargetDBSnapshotIdentifier=target_snapshot_id,
            SourceRegion=source_region,
            KmsKeyId=target_kms_key_id,   
            CopyTags=True
        )

        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject='DR Snapshot Replication Successful',
            Message=f'Snapshot {target_snapshot_id} successfully replicated to {target_region} at {timestamp}'
        )

        return {
            'statusCode': 200,
            'body': f'Snapshot replicated successfully: {target_snapshot_id}'
        }

    except Exception as e:
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject='DR Snapshot Replication FAILED',
            Message=f'Replication failed at {timestamp}. Error: {str(e)}'
        )
        raise e
