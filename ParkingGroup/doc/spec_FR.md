Entité : ParkingGroup  
=====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Groupe de stationnement **  

## Liste des propriétés  

- `allowedVehicleType`: Type de véhicule autorisé (un groupe de stationnement n'autorise qu'un seul type de véhicule). Enum : 'vélo, bus, voiture, caravane, moto, scooter, camion'.  - `alternateName`: Un nom alternatif pour cet élément  - `areBordersMarked`: Indique si les places de stationnement sont délimitées (par des lignes blanches ou autres) ou non. Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `availableSpotNumber`: Le nombre de places disponibles dans ce groupe. Il doit être inférieur ou égal à `totalSpotNumber`.  - `averageSpotLength`: La longueur moyenne des places de stationnement. Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `averageSpotWidth`: La largeur moyenne des places de stationnement. Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `category`: Catégorie du groupe de stationnement. Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'  - `chargeType`: Type de redevance(s) appliquée(s) par le site de stationnement. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `maximumAllowedHeight`: Hauteur maximale autorisée pour les véhicules.  Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `maximumAllowedWidth`: Largeur maximale autorisée pour les véhicules. Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `maximumParkingDuration`: Séjour maximum autorisé encodé comme une durée ISO8601. Lorsqu'elle est inexistante ou égale à la chaîne vide, elle signifie indéfinie. Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `name`: Le nom de cet élément.  - `occupancyDetectionType`: Valeurs autorisées : Les valeurs suivantes de DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum : 'balancing, manual, modelBased, none, singleSpaceDetection'. Ou toute autre application spécifique  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `parkingMode`: Mode(s) de stationnement. Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie. Valeurs autorisées : Celles définies par l'énumération _ParkingModeEnum_ de DATEX II version 2.3. Enum : 'echelonParking, parallelParking, perpendicularParking'.  - `permitActiveHours`: Cet attribut permet de saisir les situations dans lesquelles un permis n'est nécessaire qu'à certaines heures ou certains jours de la semaine. Il s'agit d'une valeur structurée qui doit contenir une sous-propriété pour chaque permis requis, indiquant quand le permis est actif. Si rien n'est spécifié pour un permis, cela signifie qu'un permis est toujours nécessaire. Un objet vide signifie qu'il est toujours actif. La syntaxe doit être conforme à schema.org [opening hours specification] (https://schema.org/openingHours). Par exemple, une zone bleue qui n'est active que les jours de la semaine sera codée comme 'blueZonePermit' : 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'. Les applications _DISENT_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie.  - `refParkingSite`: Parking auquel appartient cette zone. Un groupe ne peut pas être orphelin. Un groupe ne peut pas avoir de sous-groupes. Référence à un OffStreetParking ou à un OnStreetParking.  - `refParkingSpot`: Les places de stationnement individuelles appartenant à ce groupe de stationnement.  - `requiredPermit`: Cet attribut indique le ou les permis qui peuvent être nécessaires pour se garer sur ce site. La sémantique est qu'au moins _un_ de ces permis est nécessaire pour se garer. Lorsqu'un permis est composé de plus d'un élément (et), il peut être combiné avec un ','. Par exemple, 'residentPermit,disabledPermit' signifie qu'il faut à la fois un permis de résident et un permis d'invalide pour stationner. Si la liste est vide, aucun permis n'est nécessaire.  - `reservationType`: Conditions de réservation. Les applications _Devraient_ inspecter la valeur de cette propriété au niveau du parent si elle n'est pas définie. Enum : 'mandatory, notAvailable, optional, partly'.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `totalSpotNumber`: Le nombre total de spots appartenant à ce groupe. Valeurs autorisées : Tout nombre entier positif ou 0. Références normatives : DATEX 2 version 2.3 attribut _parkingNumberOfSpaces_ de la classe _ParkingRecord_.  - `type`: Type d'entité NGSI. Il doit s'agir de ParkingGroup    
Propriétés requises  
- `id`  - `refParkingSite`  - `type`    
Un groupe de places de stationnement. Le niveau de granularité peut varier. Il peut s'agir d'un étage d'un parking, d'une zone spécifique appartenant à un grand parking, ou simplement d'un groupe de places destinées au stationnement d'un certain type de véhicule ou soumises à certaines restrictions (handicapés, résidents, ...). Par souci de simplicité, un seul type de véhicule est autorisé par groupe de stationnement. De même, un seul permis obligatoire est autorisé par type de groupe.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
            format: uri    
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
#### ParkingGroup Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'un ParkingGroup au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": ["onStreet", "adjacentSpaces", "onlyDisabled"],  
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
  "requiredPermit": ["disabledPermit"],  
  "permitActiveHours": {"Monday":"null"}  
}  
```  
#### Groupe de stationnement NGSI-v2 normalisé Exemple  
Voici un exemple d'un ParkingGroup au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Valeurs-clés NGSI-LD du groupe de stationnement Exemple  
Voici un exemple d'un ParkingGroup au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Groupe de stationnement NGSI-LD normalisé Exemple  
Voici un exemple de ParkingGroup au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "allowedVehicleType": "car",  
  "availableSpotNumber": 1,  
  "category": [  
    "onStreet",  
    "adjacentSpaces",  
    "onlyDisabled"  
  ],  
  "chargeType": [  
    "free"  
  ],  
  "description": "Two parking spots reserved for disabled people",  
  "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
  "location": {  
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
    ],  
    "type": "Polygon"  
  },  
  "permitActiveHours": {  
    "Monday": "null"  
  },  
  "refParkingSite": "urn:ngsi-ld:ParkingSite:daoiz-velarde-1-5",  
  "requiredPermit": [  
    "disabledPermit"  
  ],  
  "totalSpotNumber": 2,  
  "type": "ParkingGroup"  
}  
```  
