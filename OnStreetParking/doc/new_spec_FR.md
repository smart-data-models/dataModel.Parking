Entité : OnStreetParking  
========================
  

Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  

Description globale : **Parking dans la rue**  


## Liste des biens  


- `acceptedPaymentMethod`:   
- `address`: L'adresse postale.  
- `allowedVehicleType`:   
- `alternateName`: Un autre nom pour cet article  
- `areBordersMarked`:   
- `areaServed`: La zone géographique où un service ou un article offert est fourni.  
- `availableSpotNumber`:   
- `averageSpotLength`:   
- `averageSpotWidth`:   
- `category`:   
- `chargeType`:   
- `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  
- `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  
- `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  
- `description`: Une description de cet article  
- `extraSpotNumber`:   
- `id`:   
- `location`:   
- `maximumParkingDuration`:   
- `name`: Le nom de cet article.  
- `occupancyDetectionType`:   
- `occupiedSpotNumber`:
- `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  
- `parkingMode`:   
- `permitActiveHours`:   
- `refParkingGroup`:   
- `refParkingSpot`:   
- `requiredPermit`:   
- `seeAlso`:   
- `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  
- `totalSpotNumber`:   
- `type`: NGSI Type d'entité  
- `usageScenario`:   

## Modèle de données description des biens  

Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
OnStreetParking:    
  description: 'On street parking'    
  properties:    
    acceptedPaymentMethod:    
      type: string    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    allowedVehicleType:    
      enum:    
        - agriculturalVehicle    
        - anyVehicle    
        - articulatedVehicle    
        - bicycle    
        - bus    
        - car    
        - caravan    
        - ' carOrLightVehicle'    
        - carWithCaravan    
        - carWithTrailer    
        - constructionOrMaintenanceVehicle    
        - fourWheelDrive    
        - highSidedVehicle    
        - lorry    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - tanker    
        - threeWheeledVehicle    
        - trailer    
        - tram    
        - twoWheeledVehicle    
        - van    
        - vehicleWithCatalyticConverter    
        - vehicleWithoutCatalyticConverter    
        - vehicleWithCaravan    
        - vehicleWithTrailer    
        - withEvenNumberedRegistrationPlates    
        - withOddNumberedRegistrationPlates    
        - other    
      type: string    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areBordersMarked:    
      type: boolean    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    availableSpotNumber:    
      minvalue: 0    
      type: integer    
    averageSpotLength:    
      minvalue: 0    
      type: number    
    averageSpotWidth:    
      minvalue: 0    
      type: number    
    category:    
      items:    
        enum:    
          - forDisabled    
          - forResidents    
          - forLoadUnload    
          - onlyWithPermit    
          - forELectricalCharging    
          - free    
          - feeCharged    
          - blueZone    
          - greenZone    
          - taxiStop    
          - shortTerm    
          - mediumTerm    
        type: string    
      type: array    
    chargeType:    
      items:    
        enum:    
          - additionalIntervalPrice    
          - annualPayment    
          - firstIntervalPrice    
          - flat    
          - free    
          - minimum    
          - maximum    
          - monthlyPayment    
          - seasonTicket    
          - temporaryFee    
          - temporaryPrice    
          - unknown    
          - other    
        type: string    
      type: array    
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
    extraSpotNumber:    
      minvalue: 0    
      type: integer    
    id:    
      anyOf: &onstreetparking_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    maximumParkingDuration:    
      format: date-time    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancyDetectionType:    
      enum:    
        - none    
        - balancing    
        - singleSpaceDetection    
        - modelBased    
        - manual    
      type: string    
    occupiedSpotNumber:    
      minvalue: 0    
      type: integer 
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *onstreetparking_-_properties_-_owner_-_items_-_anyof    
      type: Property         
    parkingMode:    
      enum:    
        - perpendicularParking    
        - parallelParking    
        - echelonParking    
      type: string    
    permitActiveHours:    
      type: object    
    refParkingGroup:    
      items:    
        type: string    
      type: array    
    refParkingSpot:    
      format: uri    
      type: string    
    requiredPermit:    
      items:    
        type: string    
      type: array    
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
    totalSpotNumber:    
      minvalue: 0    
      type: integer    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - OnStreetParking    
      type: string    
    usageScenario:    
      enum:    
        - parkAndRide    
        - parkAndCycle    
        - parkAndWalk    
        - kissAndRide    
        - liftShare    
        - carSharing    
        - vehicleLift    
        - loadingBay    
        - dropOff    
        - overnightParking    
        - other    
      type: string    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    

## Exemples de charges utiles  

#### OnStreetParking NGSI V2 Exemple de valeurs clés  

Voici un exemple de OnStreetParking au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  

```json  

{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": ["blueZone", "shortTerm", "forDisabled"],  
  "allowedVehicleType": "car",  
  "chargeType": ["temporaryFee"],  
  "requiredPermit": ["blueZonePermit", "disabledPermit"],  
  "permitActiveHours": {  
    "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
  },  
  "maximumAllowedStay": "PT2H",  
  "availableSpotNumber": 3,  
  "totalSpotNumber": 6,  
  "extraSpotNumber": 2,  
  "dateModified": "2016-06-02T09:25:55.00Z",  
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
  "areaServed": "Zona Centro",  
  "refParkingGroup": ["daoiz-velarde-1-5-main", "daoiz-velarde-1-5-disabled"]  
}  
```  

#### OnStreetParking NGSI V2 normalisé Exemple  

Voici un exemple d'un OnStreetParking au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  

```json  

{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": {  
    "value": ["blueZone", "shortTerm", "forDisabled"]  
  },  
  "permitActiveHours": {  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "requiredPermit": {  
    "value": ["blueZonePermit", "disabledPermit"]  
  },  
  "allowedVehicleType": {  
    "value": "car"  
  },  
  "chargeType": {  
    "value": ["temporaryFee"]  
  },  
  "refParkingGroup": {  
    "type": "Relationship",  
    "value": ["daoiz-velarde-1-5-main", "daoiz-velarde-1-5-disabled"]  
  },  
  "totalSpotNumber": {  
    "value": 6  
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
  "areaServed": {  
    "value": "Zona Centro"  
  },  
  "maximumAllowedStay": {  
    "value": "PT2H"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-06-02T09:25:55.00Z"  
  },  
  "extraSpotNumber": {  
    "value": 2  
  },  
  "availableSpotNumber": {  
    "value": 3,  
    "metadata": {  
      "timestamp": {  
        "value": "2018-09-12T12:00:00",  
        "type": "DateTime"  
      }  
    }  
  }  
}  
```  

#### OnStreetParking NGSI-LD valeurs clés Exemple  

Voici un exemple de OnStreetParking au format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  

```json  

{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "allowedVehicleType": "car",  
 "areaServed": "Zona Centro",  
 "availableSpotNumber": 3,  
 "category": ["blueZone", "shortTerm", "forDisabled"],  
 "chargeType": ["temporaryFee"],  
 "extraSpotNumber": 2,  
 "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
 "location": {"coordinates": [[[-3.80356167695194, 43.46296641666926],  
                               [-3.803161973253841, 43.46301091092682],  
                               [-3.803147082548618, 43.462879859445884],  
                               [-3.803536474744068, 43.462838666196674],  
                               [-3.80356167695194, 43.46296641666926]]],  
              "type": "Polygon"},  
 "maximumAllowedStay": "PT2H",  
 "modifiedAt": "2016-06-02T09:25:55.00Z",  
 "permitActiveHours": {"blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"},  
 "refParkingGroup": ["urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-main",  
                     "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled"],  
 "requiredPermit": ["blueZonePermit", "disabledPermit"],  
 "totalSpotNumber": 6,  
 "type": "OnStreetParking"}  
```  

#### OnStreetParking NGSI-LD normalisé Exemple  

Voici un exemple de OnStreetParking au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  

```json  

{  
    "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
    "type": "OnStreetParking",  
    "modifiedAt": "2016-06-02T09:25:55.00Z",  
    "category": {  
        "type": "Property",  
        "value": [  
            "blueZone",  
            "shortTerm",  
            "forDisabled"  
        ]  
    },  
    "permitActiveHours": {  
        "type": "Property",  
        "value": {  
            "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
        }  
    },  
    "requiredPermit": {  
        "type": "Property",  
        "value": [  
            "blueZonePermit",  
            "disabledPermit"  
        ]  
    },  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": "car"  
    },  
    "chargeType": {  
        "type": "Property",  
        "value": [  
            "temporaryFee"  
        ]  
    },  
    "refParkingGroup": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-main",  
            "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled"  
        ]  
    },  
    "totalSpotNumber": {  
        "type": "Property",  
        "value": 6  
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
    "areaServed": {  
        "type": "Property",  
        "value": "Zona Centro"  
    },  
    "maximumAllowedStay": {  
        "type": "Property",  
        "value": "PT2H"  
    },  
    "extraSpotNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "availableSpotNumber": {  
        "type": "Property",  
        "value": 3,  
        "observedAt": "2018-09-12T12:00:00Z"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
