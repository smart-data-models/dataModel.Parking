Entity: ParkingGroup  
====================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **Parking Group - TODO: Provide a complete Schema**  

## List of properties  

`alternateName`: An alternative name for this item  `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  `description`: A description of this item  `id`:   `name`: The name of this item.  `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  `seeAlso`:   `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  `type`: NGSI Entity type  ## Data Model description of properties  
Sorted alphabetically  
```yaml  
ParkingGroup:    
  description: 'Parking Group - TODO: Provide a complete Schema'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &parkinggroup_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *parkinggroup_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - ParkingGroup    
      type: string    
  required:    
    - id    
    - type    
  type: object    
```  
Here is an example of a ParkingGroup in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": ["onstreet", "adjacentSpaces", "onlyDisabled"],  
  "allowedVehicleType": "car",  
  "chargeType": ["free"],  
  "refParkingSite": "daoiz-velarde-1-5",  
  "description": "Two parking spots reserved for disabled people",  
  "totalSpotNumber": 2,  
  "availableSpotNumber": 1,  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [-3.80356167695194, 43.46296641666926],  
        [-3.803161973253841, 43.46301091092682],  
        [-3.803147082548618, 43.462879859445884],  
        [-3.803536474744068, 43.462838666196674],  
        [-3.80356167695194, 43.46296641666926]  
      ]  
    ]  
  },  
  "requiredPermit": "disabledPermit",  
  "permitActiveHours": "null"  
}  
```  
Here is an example of a ParkingGroup in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": {  
    "value": ["onstreet", "adjacentSpaces", "onlyDisabled"]  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "value": "daoiz-velarde-1-5"  
  },  
  "permitActiveHours": {  
    "value": "null"  
  },  
  "requiredPermit": {  
    "value": "disabledPermit"  
  },  
  "allowedVehicleType": {  
    "value": "car"  
  },  
  "availableSpotNumber": {  
    "value": 1,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-12T12:00:00"  
      }  
    }  
  },  
  "totalSpotNumber": {  
    "value": 2  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [-3.80356167695194, 43.46296641666926],  
          [-3.803161973253841, 43.46301091092682],  
          [-3.803147082548618, 43.462879859445884],  
          [-3.803536474744068, 43.462838666196674],  
          [-3.80356167695194, 43.46296641666926]  
        ]  
      ]  
    }  
  },  
  "chargeType": {  
    "value": ["free"]  
  },  
  "description": {  
    "value": "Two parking spots reserved for disabled people"  
  }  
}  
```  
Here is an example of a ParkingGroup in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "allowedVehicleType": "car",  
 "availableSpotNumber": 1,  
 "category": ["onstreet", "adjacentSpaces", "onlyDisabled"],  
 "chargeType": ["free"],  
 "description": "Two parking spots reserved for disabled people",  
 "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
 "location": {"coordinates": [[[-3.80356167695194, 43.46296641666926],  
                               [-3.803161973253841, 43.46301091092682],  
                               [-3.803147082548618, 43.462879859445884],  
                               [-3.803536474744068, 43.462838666196674],  
                               [-3.80356167695194, 43.46296641666926]]],  
              "type": "Polygon"},  
 "permitActiveHours": "null",  
 "refParkingSite": "urn:ngsi-ld:ParkingSite:daoiz-velarde-1-5",  
 "requiredPermit": "disabledPermit",  
 "totalSpotNumber": 2,  
 "type": "ParkingGroup"}  
```  
Here is an example of a ParkingGroup in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
    "type": "ParkingGroup",  
    "category": {  
        "type": "Property",  
        "value": [  
            "onstreet",  
            "adjacentSpaces",  
            "onlyDisabled"  
        ]  
    },  
    "refParkingSite": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:ParkingSite:daoiz-velarde-1-5"  
    },  
    "permitActiveHours": {  
        "type": "Property",  
        "value": "null"  
    },  
    "requiredPermit": {  
        "type": "Property",  
        "value": "disabledPermit"  
    },  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": "car"  
    },  
    "availableSpotNumber": {  
        "type": "Property",  
        "value": 1,  
        "observedAt": "2018-09-12T12:00:00Z"  
    },  
    "totalSpotNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Polygon",  
            "coordinates": [  
                [  
                    [  
                        -3.80356167695194,  
                        43.46296641666926  
                    ],  
                    [  
                        -3.803161973253841,  
                        43.46301091092682  
                    ],  
                    [  
                        -3.803147082548618,  
                        43.462879859445884  
                    ],  
                    [  
                        -3.803536474744068,  
                        43.462838666196674  
                    ],  
                    [  
                        -3.80356167695194,  
                        43.46296641666926  
                    ]  
                ]  
            ]  
        }  
    },  
    "chargeType": {  
        "type": "Property",  
        "value": [  
            "free"  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "Two parking spots reserved for disabled people"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
