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
        cred = credential.Credential("XXX", "XX")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cls.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cls_client.ClsClient(cred, logMaster, clientProfile)

        req = models.CreateLogsetRequest()
        params = {
            "LogsetName": "Cluster-"+region,
            "Tags": [
                {
                    "Key": "业务类型",
                    "Value": "MyBus1"
                }
            ]
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreateLogset(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)