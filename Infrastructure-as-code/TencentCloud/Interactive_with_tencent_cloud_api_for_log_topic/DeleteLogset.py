import json
import jq
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cls.v20201016 import cls_client, models



logMaster="ap-guangzhou"
regions=[ "sh", "bj"]

# logMaster="ap-singapore"
# regions=[ "sg","usw"]
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
                    "Values": [ "Cluster-"+region ]
                }
            ]
        }
        
        req.from_json_string(json.dumps(params))
        resp = client.DescribeLogsets(req)
        # resp = client.CreateLogset(req)
        # print(jq(".[LogsetId]").transform(resp.to_json_string()))

        # print(type(json.loads(resp.to_json_string())))
        # print(json.loads(resp.to_json_string())["Logsets"])
        data = json.loads(resp.to_json_string())["Logsets"]
        for item in data:
            print(item["LogsetId"])
            current_LogsetId=item["LogsetId"]

            req = models.DeleteLogsetRequest()
            params = {
                "LogsetId": current_LogsetId
            }
            req.from_json_string(json.dumps(params))

            resp = client.DeleteLogset(req)
            print(resp.to_json_string())

        # print(jq(".TotalCount").transform(json.loads(res_pretty)))  
        # print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)