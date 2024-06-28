import json
from jschon import create_catalog, JSON, JSONSchema

create_catalog('2020-12')

demo_case_schema = JSONSchema({
    "$id": "https://vidistrictattorney.com/docpkg_case",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Case",
    "description": "top-level root object for case document package",
    "type": "object",
    "properties": {
            "CaseId": {
                "description": "",
                "type": "string"
            },
            "DueDate": {
                "description": "",
                "type": "string"
            },
            "ChargingAttorney": {
                "description": "",
                "type": "string"
            },
            "ChargeReviewMessage": {
                "description": "",
                "type": "string"
            },
    },
    "required": [ "CaseId", "ChargingAttorney", "ChargeReviewMessage" ]
})

demo_report_schema = JSONSchema({
    "$id": "https://vidistrictattorney.com/docpkg_report",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Report",
    "description": "report object associated with case with associated data",
    "type": "object",
    "properties": {
            "CaseID" : {
                "Description": "Identifier of case to which this report belongs",
                "type": "string"
            },
            "ReportInternalId" : {
                "Description": "Identifer for report within case",
                "type": "String"
            },
            "OriginalReportS3URL" : {
                "Description": "S3 URL locating original uploaded report",
                "type": "string"
            },
            "OriginalNarrativeS3URL" : {
                "Description": "S3 URL locating original uploaded narrative (if provided, optional)",
                "type": "string"
            },
            "RedactionTemplate" : {
                "Description": "Template of redacted narrative (once generated, optional)",
                "type": "string"
            },
            "RedactionList" : {
                "Description": "List mapping redacted names to labels (once generated, optional)",
                "type": "string"
            },

    },
    "required": ["CaseID","ReportInternalId","OriginalReportS3URL"]
})
