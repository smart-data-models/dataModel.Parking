Entidad: ParkingSpot  
====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingSpot/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Una plaza de aparcamiento es una zona bien delimitada donde se puede estacionar un vehículo.**  

## Lista de propiedades  

- `TimeInstant`: Marca de tiempo guardada por el Agente IoT de FIWARE. Puede haber entornos de producción donde el tipo de atributo sea igual a la cadena `ISO8601`. Si es así, debe considerarse como un sinónimo de `DateTime`. Nota: Este atributo no ha sido armonizado para mantener la compatibilidad con las implementaciones actuales de referencia de FIWARE.  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `category`: Categoría(s) de la plaza de aparcamiento. onStreet": la plaza de aparcamiento pertenece a un aparcamiento onStreet. offStreet` : La plaza de aparcamiento pertenece a un aparcamiento offStreet.  - `color`: El color del producto  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `length`: Longitud de la plaza de aparcamiento.  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refDevice`: El dispositivo que representa el sensor físico utilizado para supervisar esta plaza de aparcamiento.  - `refParkingGroup`: Grupo al que pertenece la plaza de aparcamiento. Para simplificar el modelo, sólo se permite un grupo por plaza de aparcamiento.  - `refParkingSite`: Sitio de estacionamiento al que pertenece la plaza.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `status`: Estado de la plaza de aparcamiento desde el punto de vista de la ocupación. Enum:'cerrado, libre, ocupado, desconocido'  - `type`: Tipo de entidad NGSI. Tiene que ser ParkingSpot  - `width`: Anchura de la plaza de aparcamiento.    
Propiedades requeridas  
- `category`  - `id`  - `location`  - `refParkingSite`  - `status`  - `type`    
El objetivo de este tipo de entidad es controlar el estado de las plazas de aparcamiento de forma individual. Así, una entidad de tipo ParkingSpot no puede existir sin una entidad contenedora de tipo (OnStreetParking, OffStreetParking). Una plaza de aparcamiento puede pertenecer a un grupo.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      type: Geoproperty    
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
## Ejemplo de carga útil  
#### ParkingSpot NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un ParkingSpot en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### ParkingSpot NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un ParkingSpot en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### ParkingSpot NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un ParkingSpot en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### ParkingSpot NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un ParkingSpot en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
