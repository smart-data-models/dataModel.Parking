Entité : ParkingAccess  
======================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Accès au parking - TODO : Fournir un schéma complet**  

## Liste des biens  

`address`: L'adresse postale.  `alternateName`: Un autre nom pour cet article  `areaServed`: La zone géographique où un service ou un article offert est fourni.  `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  `description`: Une description de cet article  `id`:   `location`:   `name`: Le nom de cet article.  `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  `seeAlso`:   `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  `type`: NGSI Type d'entité  ## Modèle de données description des biens  
Classement par ordre alphabétique  
```yaml  
ParkingAccess:    
  description: 'Parking Access - TODO: Provide a complete Schema'    
  properties:    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
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
      anyOf: &parkingaccess_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *parkingaccess_-_properties_-_owner_-_items_-_anyof    
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
        - ParkingAccess    
      type: string    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
Voici un exemple d'accès au parking en format JSON comme valeurs clés. Ce format est compatible avec la version 2 du NGSI lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "accesspoint-trinidade-1",  
  "type": "ParkingAccess",  
  "name": "Trinidade main entrance",  
  "location": {  
    "coordinates": [-8.60961198807, 41.150691773],  
    "type": "Point"  
  },  
  "category": ["vehicleEntrance"],  
  "refOffStreetParking": "porto-OffStreetParking-23889",  
  "features": ["barrier"]  
}  
```  
Voici un exemple d'accès au parking au format JSON normalisé. Il est compatible avec la version 2 du NGSI lorsque l'on utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "accesspoint-trinidade-1",  
  "type": "ParkingAccess",  
  "category": {  
    "value": ["vehicleEntrance"]  
  },  
  "name": {  
    "value": "Trinidade main entrance"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-8.60961198807, 41.150691773]  
    }  
  },  
  "refOffStreetParking": {  
    "type": "Relationship",  
    "value": "porto-OffStreetParking-23889"  
  },  
  "features": {  
    "value": ["barrier"]  
  }  
}  
```  
Voici un exemple d'accès au parking au format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "category": ["vehicleEntrance"],  
 "features": ["barrier"],  
 "id": "urn:ngsi-ld:ParkingAccess:accesspoint-trinidade-1",  
 "location": {"coordinates": [-8.60961198807, 41.150691773], "type": "Point"},  
 "name": "Trinidade main entrance",  
 "refOffStreetParking": "urn:ngsi-ld:OffStreetParking:porto-OffStreetParking-23889",  
 "type": "ParkingAccess"}  
```  
Voici un exemple d'accès au parking au format JSON-LD tel que normalisé. Ce format est compatible avec JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:ParkingAccess:accesspoint-trinidade-1",  
    "type": "ParkingAccess",  
    "category": {  
        "type": "Property",  
        "value": [  
            "vehicleEntrance"  
        ]  
    },  
    "name": {  
        "type": "Property",  
        "value": "Trinidade main entrance"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -8.60961198807,  
                41.150691773  
            ]  
        }  
    },  
    "refOffStreetParking": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:OffStreetParking:porto-OffStreetParking-23889"  
    },  
    "features": {  
        "type": "Property",  
        "value": [  
            "barrier"  
        ]  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
