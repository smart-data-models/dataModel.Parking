Entität: ParkingSpot  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingSpot/LICENSE.md)  
Globale Beschreibung: **Ein Parkplatz ist ein gut abgegrenzter Bereich, in dem ein Fahrzeug abgestellt werden kann.**  

## Liste der Eigenschaften  

- `TimeInstant`: Zeitstempel, der von FIWAREs IoT-Agent gespeichert wird. Es kann Produktionsumgebungen geben, in denen der Attributtyp gleich der Zeichenkette `ISO8601` ist. Wenn dies der Fall ist, muss es als Synonym von `DateTime` betrachtet werden. Hinweis: Dieses Attribut wurde nicht harmonisiert, um die Abwärtskompatibilität mit aktuellen FIWARE-Referenzimplementierungen zu wahren.  - `address`: Die Postanschrift.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `category`: Kategorie(n) des Parkplatzes. onStreet` : Der Parkplatz gehört zu einem onStreet-Parkplatz. OffStreet": Der Parkplatz gehört zu einem OffStreet-Parkplatz.  - `color`: Die Farbe des Produkts  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `length`: Länge des Stellplatzes.  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `refDevice`: Das Gerät, das den physischen Sensor darstellt, der zur Überwachung dieses Parkplatzes verwendet wird.  - `refParkingGroup`: Gruppe, zu der der Stellplatz gehört. Aus Gründen der Modellvereinfachung ist nur eine Gruppe pro Parkplatz zulässig.  - `refParkingSite`: Parkplatz, zu dem der Stellplatz gehört.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `status`: Status des Parkplatzes unter dem Gesichtspunkt der Belegung. Enum:'geschlossen, frei, belegt, unbekannt'  - `type`: NGSI Entity-Typ. Es muss ParkingSpot sein  - `width`: Breite des Stellplatzes.    
Erforderliche Eigenschaften  
- `category`  - `id`  - `location`  - `refParkingSite`  - `status`  - `type`    
Das Ziel dieses Entitätstyps ist es, den Status von Parkplätzen individuell zu überwachen. Daher kann eine Entität vom Typ ParkingSpot nicht ohne eine enthaltende Entität vom Typ (OnStreetParking, OffStreetParking) existieren. Ein ParkingSpot kann zu einer Gruppe gehören.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ParkingSpot:    
  description: 'A parking spot is an area well delimited where one vehicle can be parked.'    
  properties:    
    TimeInstant:    
      description: 'Timestamp saved by FIWARE''s IoT Agent. There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. Note: This attribute has not been harmonized to keep backwards compatibility with current FIWARE reference implementations.'    
      format: date-time    
      type: Property    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: 'Category(ies) of the parking spot. `onStreet` : The parking spot belongs to an onStreet parking site. `offStreet` : The parking spot belongs to an offStreet parking site.'    
      items:    
        enum:    
          - onStreet    
          - offStreet    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
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
      anyOf: &parkingspot_-_properties_-_owner_-_items_-_anyof    
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
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    length:    
      description: 'Length of the parking spot.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *parkingspot_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refDevice:    
      description: 'The device representing the physical sensor used to monitor this parking spot.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      minItems: 1    
      type: Relationship    
      uniqueItems: true    
    refParkingGroup:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Group to which the parking spot belongs to. For model simplification purposes only one group is allowed per parking spot.'    
      type: Relationship    
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
      description: 'Parking site to which the parking spot belongs to.'    
      type: Relationship    
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
    status:    
      description: 'Status of the parking spot from the point of view of occupancy. Enum:''closed, free, occupied, unknown'''    
      enum:    
        - closed    
        - free    
        - occupied    
        - unknown    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be ParkingSpot'    
      enum:    
        - ParkingSpot    
      type: Property    
    width:    
      description: 'Width of the parking spot.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
  required:    
    - id    
    - location    
    - type    
    - status    
    - category    
    - refParkingSite    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### ParkingSpot NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen ParkingSpot im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "santander:daoiz_velarde_1_5:3",  
  "type": "ParkingSpot",  
  "name": "A-13",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.80356167695194, 43.46296641666926]  
  },  
  "status": "free",  
  "category": ["onStreet"],  
  "refParkingSite": "santander:daoiz_velarde_1_5"  
}  
```  
#### ParkingSpot NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen ParkingSpot im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "santander:daoiz_velarde_1_5:3",  
  "type": "ParkingSpot",  
  "status": {  
    "value": "free",  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-21T12:00:00"  
      },  
      "parkingPermit": {  
        "type": "Property",  
        "value": "yes"  
      }  
    }  
  },  
  "category": {  
    "value": ["onStreet"]  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "object": "santander:daoiz_velarde_1_5"  
  },  
  "name": {  
    "value": "A-13"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.80356167695194, 43.46296641666926]  
    }  
  }  
}  
```  
#### ParkingSpot NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen ParkingSpot im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:ParkingSpot:santander:daoiz_velarde_1_5:3",  
  "type": "ParkingSpot",  
  "status": {  
    "type": "Property",  
    "value": "free",  
    "observedAt": "2018-09-21T12:00:00Z",  
    "parkingPermit": {  
      "type": "Property",  
      "value": "yes"  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "onStreet"  
    ]  
  },  
  "refParkingSite": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ParkingSite:santander:daoiz_velarde_1_5"  
  },  
  "name": {  
    "type": "Property",  
    "value": "A-13"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.80356167695194,  
        43.46296641666926  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### ParkingSpot NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen ParkingSpot im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "category": [  
    "onStreet"  
  ],  
  "id": "urn:ngsi-ld:ParkingSpot:santander:daoiz_velarde_1_5:3",  
  "location": {  
    "coordinates": [  
      -3.80356167695194,  
      43.46296641666926  
    ],  
    "type": "Point"  
  },  
  "name": "A-13",  
  "refParkingSite": "urn:ngsi-ld:ParkingSite:santander:daoiz_velarde_1_5",  
  "status": "free",  
  "type": "ParkingSpot"  
}  
```  
