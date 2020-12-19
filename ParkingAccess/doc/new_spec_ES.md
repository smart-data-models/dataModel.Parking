Entidad: ParkingAcceso  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingAccess/LICENSE.md)  
Descripción global: **Acceso al estacionamiento - TODO: Proporcionar un esquema completo**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `category`: Categoría del punto de acceso (entrada, salida, etc.). Valores permitidos: Los especificados por el DATEX II _AccessCategoryEnum_ u otros valores significativos para la aplicación.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `features`: Los especificados por el DATEX II _essEquipmentEnum_ y por el _AccessibilityEnum_ u otros valores significativos para la aplicación.  - `height`: La altura del punto de acceso  - `id`: Identificador único de la entidad  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refOffStreetParking`: El aparcamiento de la calle al que da acceso este punto de acceso.  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `slope`: Pendiente del punto de acceso (en términos relativos)  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser ParkingAccess  - `width`: El ancho del punto de acceso    
Propiedades requeridas  
- `id`  - `location`  - `type`    
Representa un punto de acceso a un sitio de estacionamiento, normalmente un estacionamiento fuera de la calle.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ParkingAccess:    
  description: 'Parking Access - TODO: Provide a complete Schema'    
  properties:    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: 'Category of the access point (entrance, exit, etc.). Allowed values: Those specified by the DATEX II _AccessCategoryEnum_ or other values meaningful to the application.'    
      items:    
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
    features:    
      description: 'Those specified by the DATEX II _essEquipmentEnum_ and by _AccessibilityEnum_ or other values meaningful to the application.'    
      items:    
        type: string    
      type: Property    
    height:    
      description: 'Height of the access point'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/height    
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
      description: 'Unique identifier of the entity'    
      type: Property    
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
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refOffStreetParking:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The offstreet parking site this access point gives access to.'    
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
    slope:    
      description: 'Slope of the access point (in relative terms)'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ParkingAccess'    
      enum:    
        - ParkingAccess    
      type: Property    
    width:    
      description: 'Width of the access point'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### ParkingAcceso a las claves NGSI V2 Ejemplo  
Aquí hay un ejemplo de un ParkingAccess en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### ParkingAccess NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un ParkingAccess en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### ParkingAcceso a las llaves NGSI-LD Ejemplo  
Aquí hay un ejemplo de un ParkingAccess en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### ParkingAcceso NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un ParkingAccess en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
