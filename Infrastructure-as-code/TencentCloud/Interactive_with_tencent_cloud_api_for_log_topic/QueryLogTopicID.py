import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cls.v20201016 import cls_client, models

logMaster="ap-guangzhou"
regions=[ "sh", "bj"]

# logMaster="ap-singapore"
# regions=[ "sg","usw"]

EKS_meta_components=["apiserver","cbs-provisioner","controller-manager","hpa-metrics-server","ingress-controller","scheduler","service-controller"]

for region in regions:
    print("Cluster-"+region)

    try:
        cred = credential.Credential("***", "***")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cls.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cls_client.ClsClient(cred, logMaster, clientProfile)

        req = models.DescribeLogsetsRequest()
        params = {
            "Filters": [
                {
                    "Key": "logsetName",
                    "Values": [ "Cluster-"+region ],
                    "Offset": 1
                }
            ]
        }
        
        req.from_json_string(json.dumps(params))
        resp = client.DescribeLogsets(req)

        import pyjq
        import json
        import requests

        data = json.loads(resp.to_json_string())["Logsets"]
        for item in data:
            print("LogsetId: " + item["LogsetId"])
            current_LogsetId=item["LogsetId"]

            for component in EKS_meta_components:
                req = models.DescribeTopicsRequest()
                params = {
                    "Filters": [
                        {
                            "Key": "logsetName",
                            "Values": [ "Cluster-"+region ]
                        },
                        {
                            "Key": "topicName",
                            "Values": [ component ]
                        }
                    ]
                }
                req.from_json_string(json.dumps(params))

                resp = client.DescribeTopics(req)
                resp_dict = pyjq.first('.[]',json.loads(resp.to_json_string()))
                for i in range(0, len(resp_dict)):
                    LogsetId = pyjq.first('.LogsetId',resp_dict[i])
                    if LogsetId == current_LogsetId:
                        print(region + " "  + component + " TopicId: " + pyjq.first('.TopicId',resp_dict[i]))
                        break

     

    except TencentCloudSDKException as err:
        print(err)