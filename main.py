from azure.identity import DefaultAzureCredential
from azure.mgmt.quota import QuotasClient
from azure.mgmt.quota.models import RequestResponse
from region_list import region_list
# PREREQUISITES
# pip install azure-identity
# pip install azure-mgmt-quota

# USAGE
# python quotas_put_request_for_compute.py
# Before running the sample, please set the values of the client ID, tenant ID, and client secret
# of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET.
# For more info about how to get the value, please see: https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal

sub_id = input("Please add your subscription ID: ")
region = input("Please add your quota region: ")
family = input("Please add your quota family: ")
value = int(input("Please add your quota value: "))  
while family is 
def main():
    client = QuotasClient(
        credential=DefaultAzureCredential(),
    )

    create_quota_request = {
        "properties": {
            "limit": {"limitObjectType": "LimitValue", "value": value},  # Use the 'value' variable
            "name": {"value": family},  # Use the 'family' variable
        }
    }

    response: RequestResponse = client.create_or_update(
        resource_id=f"/subscriptions/{sub_id}/providers/Microsoft.Compute/locations/{region}/quotas/{family}",
        parameters=create_quota_request
    )

    print(response)

if __name__ == "__main__":
    main()
