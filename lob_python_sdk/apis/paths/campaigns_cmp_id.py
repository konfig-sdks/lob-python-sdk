from lob_python_sdk.paths.campaigns_cmp_id.get import ApiForget
from lob_python_sdk.paths.campaigns_cmp_id.delete import ApiFordelete
from lob_python_sdk.paths.campaigns_cmp_id.patch import ApiForpatch


class CampaignsCmpId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
