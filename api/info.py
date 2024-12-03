from fastapi import APIRouter

router=APIRouter(tags=['General Info'])

@router.get('/info')
def info():
    return {
        "author": "Daryna Borodenko",
        "description": "This app provides quick access to CVE data from a local JSON file. It helps find and filter vulnerabilities easily.",
        "features": [
            "View CVE data from the last 15 days",
            "Get the 10 newest CVEs",
            "Filter knownRansomwareCampaignUse - Known",
            "Search CVEs by keywords"
        ],
        "version": "1.0.1",
        "contact": "For feedback, email darinab200426@gmail.com"
    }
