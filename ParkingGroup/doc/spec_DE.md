Entität: ParkingGroup  
=====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)  
Globale Beschreibung: **Parken Gruppe **  

## Liste der Eigenschaften  

- `allowedVehicleType`: Erlaubter Fahrzeugtyp (eine Parkgruppe erlaubt nur einen Fahrzeugtyp). Enum:'Fahrrad, Bus, Auto, Wohnwagen, Motorrad, Motorroller, LKW'  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areBordersMarked`: Gibt an, ob Parklücken abgegrenzt sind (mit Leerzeilen oder ähnlichem) oder nicht. Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist  - `availableSpotNumber`: Die Anzahl der verfügbaren Plätze in dieser Gruppe. Sie muss kleiner oder gleich der `totalSpotNumber` sein.  - `averageSpotLength`: Die durchschnittliche Länge von Parkplätzen. Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist.  - `averageSpotWidth`: Die durchschnittliche Breite von Parkplätzen. Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist.  - `category`: Die Kategorie der Parkgruppe. Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermitPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'  - `chargeType`: Art der vom Parkplatz durchgeführten Gebühr(en). Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `maximumAllowedHeight`: Maximal zulässige Höhe für Fahrzeuge.  Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist.  - `maximumAllowedWidth`: Maximal zulässige Breite für Fahrzeuge. Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist.  - `maximumParkingDuration`: Maximal erlaubter Aufenthalt kodiert als ISO8601-Dauer. Wenn sie nicht vorhanden oder gleich dem leeren String ist, bedeutet sie unbestimmt. Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene überprüfen, wenn sie nicht definiert ist.  - `name`: Der Name dieses Elements.  - `occupancyDetectionType`: Erlaubte Werte: Die folgenden aus DATEX II Version 2.3 _OccupancyDetectionTypeEnum_. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. Oder jede andere anwendungsspezifische  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `parkingMode`: Parkmodus(e). Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist. Erlaubte Werte: Die durch die Aufzählung _ParkingModeEnum_ von DATEX II Version 2.3 definierten. Enum:'echelonParking, parallelParking, perpendicularParking'  - `permitActiveHours`: Mit diesem Attribut können Situationen erfasst werden, in denen eine Genehmigung nur zu bestimmten Stunden oder an bestimmten Wochentagen benötigt wird. Es ist ein strukturierter Wert, der für jede erforderliche Genehmigung eine Untereigenschaft enthalten muss, die angibt, wann die Genehmigung aktiv ist. Wenn für eine Genehmigung nichts angegeben ist, bedeutet dies, dass eine Genehmigung immer erforderlich ist. Ein leeres Objekt bedeutet immer aktiv. Die Syntax muss mit schema.org [opening hours specification] (https://schema.org/openingHours) konform sein. Zum Beispiel wird eine blaue Zone, die nur tagsüber aktiv ist, als 'blueZonePermit' kodiert: 'Mo,Di,We,Th,Fr,Sa 09:00-20:00'. Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist  - `refParkingSite`: Parkplatz, zu dem diese Zone gehört. Eine Gruppe kann nicht verwaist sein. Eine Gruppe kann keine Untergruppen haben. Verweis auf ein OffStreetParking oder auf ein OnStreetParking  - `refParkingSpot`: Einzelne Stellplätze, die zu dieser Parkgruppe gehören.  - `requiredPermit`: Mit diesem Attribut wird erfasst, welche Genehmigung(en) zum Parken an diesem Standort erforderlich sein könnte(n). Die Semantik besagt, dass mindestens _eine_ dieser Genehmigungen zum Parken benötigt wird. Wenn eine Genehmigung aus mehr als einem Element (und) besteht, können sie mit einem ',' kombiniert werden. Zum Beispiel bedeutet 'residentPermit,disabledPermit', dass sowohl eine Anwohner- als auch eine Behindertengenehmigung zum Parken benötigt wird. Wenn die Liste leer ist, wird keine Genehmigung benötigt  - `reservationType`: Bedingungen für die Reservierung. Anwendungen _SOLLTEN_ den Wert dieser Eigenschaft auf übergeordneter Ebene prüfen, wenn sie nicht definiert ist. Enum:'mandatory, notAvailable, optional, partly'.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `totalSpotNumber`: Die Gesamtzahl der Spots, die zu dieser Gruppe gehören. Erlaubte Werte: Jede positive ganze Zahl oder 0. Normative Verweise: DATEX 2 Version 2.3 Attribut _ParkingNumberOfSpaces_ der Klasse _ParkingRecord_.  - `type`: NGSI Entity-Typ. Es muss ParkingGroup sein    
Erforderliche Eigenschaften  
- `id`  - `refParkingSite`  - `type`    
Eine Gruppe von Parkplätzen. Die Granularität kann variieren. Es kann eine Etage in einem Parkhaus sein, eine bestimmte Zone, die zu einem großen Parkplatz gehört, oder einfach eine Gruppe von Plätzen, die für das Parken eines bestimmten Fahrzeugtyps vorgesehen sind oder bestimmten Einschränkungen unterliegen (Behinderte, Anwohner, ...). Der Einfachheit halber ist nur ein Fahrzeugtyp pro Parkgruppe erlaubt. Ebenso ist nur eine erforderliche Genehmigung pro Gruppentyp erlaubt.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### ParkingGroup NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine ParkingGroup im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### ParkingGroup NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine ParkingGroup im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### ParkingGroup NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine ParkingGroup im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### ParkingGroup NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine ParkingGroup im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
