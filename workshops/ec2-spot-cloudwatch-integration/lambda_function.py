import boto3
import os

def handler(event, context):
  print("This is test code1")
  print("event={} context={}".format(str(event), str(context)))
  
  client = boto3.client('autoscaling')
  
  asg_name=os.getenv('ASG_NAME')
  
  response = client.describe_auto_scaling_groups(
      AutoScalingGroupNames=[
        asg_name,
      ]
  )

  DesiredCapacity=response['AutoScalingGroups'][0]['DesiredCapacity']
  DesiredCapacity += 1


  print("DesiredCapacity={}".format(DesiredCapacity))
  response = client.set_desired_capacity(
    AutoScalingGroupName='asg_cwt_od2',
    DesiredCapacity=DesiredCapacity,
    HonorCooldown=True
  )
  print(response)
  #print(response['AutoScalingGroups'][0]['DesiredCapacity'])
  
  #json_string = json.loads(str(response))
  
 # print("response={}".format(str(json_string)))

  return