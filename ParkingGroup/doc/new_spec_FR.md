Entité : ParkingGroup  
=====================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)  
Description globale : **Groupe de stationnement **  

## Liste des biens  

- `allowedVehicleType`: Type de véhicule autorisé (un groupe de stationnement n'autorise qu'un seul type de véhicule). Enum : "bicyclette, bus, voiture, caravane, moto, scooter, camion".  - `alternateName`: Un autre nom pour cet article  - `areBordersMarked`: Indique si les places de stationnement sont délimitées (avec des lignes blanches ou similaires) ou non. Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie  - `availableSpotNumber`: Le nombre de places disponibles dans ce groupe. Il doit être inférieur ou égal à "totalSpotNumber".  - `averageSpotLength`: La longueur moyenne des places de stationnement. Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau des parents si elle n'est pas définie.  - `averageSpotWidth`: La largeur moyenne des places de stationnement. Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau des parents si elle n'est pas définie.  - `category`: Catégorie du groupe de stationnement. Enum : "adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces".  - `chargeType`: Type d'accusation(s) effectuée(s) par le site de stationnement. Enumération : "additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other".  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `maximumAllowedHeight`: Hauteur maximale autorisée pour les véhicules.  Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `maximumAllowedWidth`: Largeur maximale autorisée pour les véhicules. Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `maximumParkingDuration`: Durée maximale de séjour autorisée encodée comme une durée ISO8601. Lorsque non présent ou égal à la chaîne vide, cela signifie indéfini. Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `name`: Le nom de cet article.  - `occupancyDetectionType`: Valeurs autorisées : Les valeurs suivantes de la version 2.3 de DATEX II _OccupancyDetectionTypeEnum_. Enum : "balancing, manual, modelBased, none, singleSpaceDetection". Ou toute autre application spécifique  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `parkingMode`: Mode(s) de stationnement. Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie. Valeurs autorisées : Celles définies par l'énumération _ParkingModeEnum_ de DATEX II version 2.3. Enum : "echelonParking, parallelParking, perpendicularParking".  - `permitActiveHours`: Cet attribut permet de saisir les situations où un permis n'est nécessaire qu'à des heures ou des jours précis de la semaine. Il s'agit d'une valeur structurée qui doit contenir un sous-propriété pour chaque permis requis, indiquant quand le permis est actif. Si rien n'est spécifié pour un permis, cela signifie qu'un permis est toujours nécessaire. Un objet vide signifie qu'il est toujours actif. La syntaxe doit être conforme à schema.org [spécification des heures d'ouverture] (https://schema.org/openingHours). Par exemple, une zone bleue qui n'est active que pendant les semaines de la journée sera codée comme "blueZonePermit" : "Mo,Tu,We,Th,Fr,Sa 09:00-20:00". Les applications _DEVRAIENT_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie  - `refParkingSite`: Site de stationnement auquel cette zone appartient. Un groupe ne peut pas être orphelin. Un groupe ne peut pas avoir de sous-groupes. Référence à un OffStreetParking ou à un OnStreetParking  - `refParkingSpot`: Les places de stationnement individuelles appartenant à ce groupe de stationnement.  - `requiredPermit`: Cet attribut indique le ou les permis qui pourraient être nécessaires pour se garer sur ce site. La sémantique est qu'au moins _un de_ ces permis est nécessaire pour se garer. Lorsqu'un permis est composé de plusieurs éléments (et) ils peuvent être combinés avec un ",". Par exemple, le "permis de séjour, permis pour handicapés" indique que le stationnement nécessite à la fois un permis de séjour et un permis pour handicapés. Si la liste est vide, aucun permis n'est nécessaire.  - `reservationType`: Conditions de réservation. Les demandes _DEVRAIENT_ inspecter la valeur de cette propriété au niveau des parents si elle n'est pas définie. Enumération : "obligatoire, non disponible, optionnel, partiellement".  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `totalSpotNumber`: Le nombre total de spots relatifs à ce groupe. Valeurs autorisées : Tout nombre entier positif ou 0. Références normatives : DATEX 2 version 2.3 attribut _parkingNumberOfSpaces_ de la classe _ParkingRecord_.  - `type`: Type d'entité NGSI. Il doit s'agir de ParkingGroup    
Propriétés requises  
- `id`  - `refParkingSite`  - `type`    
Un groupe de places de parking. Le niveau de granularité peut varier. Il peut s'agir d'un étage sur un parking, d'une zone spécifique appartenant à un grand parking, ou simplement d'un groupe de places destinées au stationnement d'un certain type de véhicule ou soumises à certaines restrictions (handicapés, résidents, ...). Par souci de simplicité, un seul type de véhicule par groupe de stationnement est autorisé. De même, une seule autorisation est requise par type de groupe.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ParkingGroup:    
  description: 'Parking Group '    
  properties:    
    allowedVehicleType:    
      description: 'Vehicle type allowed (a parking group only allows one vehicle type). Enum:''bicycle, bus, car, caravan, motorcycle, motorscooter, truck'' '    
      enum:    
        - bicycle    
        - bus    
        - car    
        - caravan    
        - motorcycle    
        - motorscooter    
        - truck    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areBordersMarked:    
      description: 'Denotes whether parking spots are delimited (with blank lines or similar) or not. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    availableSpotNumber:    
      description: 'The number of spots available in this group. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    averageSpotLength:    
      description: 'The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/length    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/width    
        units: meters    
    category:    
      description: 'Parking Group''s category. Enum:''adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'''    
      items:    
        enum:    
          - adjacentSpaces    
          - blueZone    
          - completeFloor    
          - free    
          - feeCharged    
          - greenZone    
          - loadUnloadZone    
          - nonAdjacentSpaces    
          - offStreet    
          - onlyDisabled    
          - onlyElectricalCharging    
          - onlyResidents    
          - onlyWithPermit    
          - onStreet    
          - particularConditionsSpaces    
          - shortTermMediumTermLongTerm    
          - statisticsOnly    
          - vehicleTypeSpaces    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    chargeType:    
      description: 'Type of charge(s) performed by the parking site. Enum:''additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'''    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/heigth    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/width    
        units: Meters    
    maximumParkingDuration:    
      description: 'Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      format: date-time    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancyDetectionType:    
      description: 'Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:''balancing, manual, modelBased, none, singleSpaceDetection''. Or any other application-specific'    
      items:    
        enum:    
          - balancing    
          - manual    
          - modelBased    
          - none    
          - singleSpaceDetection    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *parkinggroup_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    parkingMode:    
      description: 'Parking mode(s). Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined. Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:''echelonParking, parallelParking, perpendicularParking'''    
      items:    
        enum:    
          - echelonParking    
          - parallelParking    
          - perpendicularParking    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    permitActiveHours:    
      description: 'This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is an structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. Empty object means always active. The syntax must be conformant with schema.org [opening hours specification](https://schema.org/openingHours). For instance, a blue zone which is only active on dayweeks will be encoded as ''blueZonePermit'': ''Mo,Tu,We,Th,Fr,Sa 09:00-20:00''. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHours    
    refParkingSite:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Parking site to which this zone belongs to. A group cannot be orphan. A group cannot have subgroups. Reference to an OffStreetParking or to an OnStreetParking'    
      type: Relationship    
    refParkingSpot:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Individual parking spots belonging to this parking group.'    
      type: Relationship    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed'    
      items:    
        enum:    
          - employeePermit    
          - studentPermit    
          - fairPermit    
          - governmentPermit    
          - residentPermit    
          - specificIdentifiedVehiclePermit    
          - disabledPermit    
          - visitorPermit    
          - blueZonePermit    
          - careTakingPermit    
          - carpoolingPermit    
          - carSharingPermit    
          - emergencyVehiclePermit    
          - maintenanceVehiclePermit    
          - roadWorksPermit    
          - taxiPermit    
          - transportationPermit    
          - noPermitNeeded    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    reservationType:    
      description: 'Conditions for reservation. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined. Enum:''mandatory, notAvailable, optional, partly''.'    
      enum:    
        - mandatory    
        - notAvailable    
        - optional    
        - partly    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    totalSpotNumber:    
      description: 'The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    type:    
      description: 'NGSI Entity type. It has to be ParkingGroup'    
      enum:    
        - ParkingGroup    
      type: Property    
  required:    
    - id    
    - type    
    - refParkingSite    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### ParkingGroup NGSI V2 valeurs clés Exemple  
Voici un exemple de ParkingGroup au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### ParkingGroup NGSI V2 normalisé Exemple  
Voici un exemple de ParkingGroup au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### ParkingGroup NGSI-LD valeurs clés Exemple  
Voici un exemple de ParkingGroup au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### ParkingGroup NGSI-LD normalisé Exemple  
Voici un exemple de ParkingGroup au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
