# API Reference

## Test Server
http://stolenbyte.kr:8080

## GET /api/v1/campaigns/[campaign number]

Get Camapaign Data
> **Note:** If the campaign number does not  exist, output all data

## POST /api/v1/campaigns/

Set Camapaign Data

## PUT /api/v1/campaigns/[campaign number]

Update Camapaign Data
> **Note:** "id" value in dataset required

## DELETE /api/v1/campaigns/[campaign number]

Delete Camapaign Data

## Dataset Proof of concept
```
* Content-Type: application/json

* Test Parameter
{
    "company":"Campaigns 2",
    "title":"Campaigns 2",
    "position_x":"1.23",
    "position_y":"1.23",
    "position_z":"1.23",
    "rotation_x":"2.34",
    "rotation_y":"2.34",
    "rotation_z":"2.34",
    "display_stands":[
        {
            "name":"Display 2",
            "type":"Display 2",
            "position_x":"1.23",
            "position_y":"1.23",
            "position_z":"1.23",
            "rotation_x":"2.34",
            "rotation_y":"2.34",
            "rotation_z":"2.34",
            "scale":"2.34",
            "format":"a",
            "click_event":"b",
            "animation":"c",
            "products":[
                {
                    "name":"Product 2",
                    "type":"Product 2",
                    "position_x":"1.23",
                    "position_y":"1.23",
                    "position_z":"1.23",
                    "rotation_x":"2.34",
                    "rotation_y":"2.34",
                    "rotation_z":"2.34",
                    "scale":"1.23",
                    "format":"a",
                    "click_event":"b",
                    "animation":"c"
                }
            ]
        },
        {
            "name":"Display 2",
            "type":"Display 2",
            "position_x":"1.23",
            "position_y":"1.23",
            "position_z":"1.23",
            "rotation_x":"2.34",
            "rotation_y":"2.34",
            "rotation_z":"2.34",
            "scale":"2.34",
            "format":"a",
            "click_event":"b",
            "animation":"c",
            "products":[
                {
                    "name":"Product 2",
                    "type":"Product 2",
                    "position_x":"1.23",
                    "position_y":"1.23",
                    "position_z":"1.23",
                    "rotation_x":"2.34",
                    "rotation_y":"2.34",
                    "rotation_z":"2.34",
                    "scale":"1.23",
                    "format":"a",
                    "click_event":"b",
                    "animation":"c"
                }
            ]
        }
    ]

```
