Entidad: OnStreetParking  
========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Parking/blob/master/OnStreetParking/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Un solar, zona de espacio libre, en la calle, (con contador o no) con acceso directo desde una carretera, destinado a aparcar vehículos.**  

## Lista de propiedades  

- `acceptedPaymentMethod`: Tipo de cargo(s) realizado(s) por el aparcamiento. Enum:'Por transferencia bancaria por adelantado, Por factura, En efectivo, Por cheque por adelantado, Contra reembolso, Débito directo, GoogleCheckout, PayPal, PaySwarm'  - `address`: La dirección postal  - `allowedVehicleType`: Tipo de vehículo permitido (sólo uno por aparcamiento en la calle). Enum:"vehículo agrícola, cualquier vehículo, vehículo articulado, bicicleta, autobús, coche, caravana, coche o vehículo ligero, coche con caravana, coche con remolque, vehículo de construcción o mantenimiento, vehículo de cuatro ruedas, vehículo de gran altura, camión, ciclomotor, motocicleta, motocicleta con coche lateral, moto, cisterna, vehículo de tres ruedas, remolque, tranvía, vehículo de dos ruedas, furgoneta, vehículo con convertidor catalítico, vehículo sin convertidor catalítico, vehículo con caravana, vehículo con remolque, con matrícula par, con matrícula añadida, otros".  - `alternateName`: Un nombre alternativo para este artículo  - `areBordersMarked`: Indica si las plazas de aparcamiento están delimitadas (con líneas en blanco o similares) o no  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `availableSpotNumber`: El número de plazas disponibles en todo el mundo, incluidas las plazas reservadas, como las destinadas a discapacitados, personas que aparcan durante mucho tiempo, etc. Esto puede ser más difícil de estimar en aquellos lugares de estacionamiento en los que los límites de las plazas no están claramente marcados por líneas  - `averageSpotLength`: La longitud media de las plazas de aparcamiento  - `averageSpotWidth`: La anchura media de las plazas de aparcamiento  - `category`: Categoría de aparcamiento en la calle. Enum:'blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'  - `chargeType`: Tipo de cargo(s) realizado(s) por el aparcamiento. Enum:'precio adicional por intervalo, pago anual, precio por primer intervalo, tarifa plana, gratuito, mínimo, máximo, pago mensual, abono de temporada, tarifa temporal, precio temporal, desconocido, otro'.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `extraSpotNumber`: El número de plazas extra disponibles, es decir, libres. Las plazas extra son aquellas reservadas para fines especiales y suelen requerir un permiso. Los detalles del permiso se encontrarán a nivel de grupo de aparcamiento (entidad de tipo `ParkingGroup`). Este valor debe agregar las plazas libres de todos los grupos dedicados a condiciones especiales de aparcamiento. Valores permitidos: Un número entero positivo, incluido el 0. `extraSpotNumber` más `availableSpotNumber` debe ser menor o igual que `totalSpotNumber  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maximumParkingDuration`: La estancia máxima permitida en el sitio codificada como una duración ISO8601. Un valor vacío indica una duración indefinida.  - `name`: El nombre de este artículo.  - `occupancyDetectionType`: Método(s) de detección de la ocupación. Enum:'balanceo, manual, modelBased, none, singleSpaceDetection'. Lo siguiente de DATEX II versión 2.3 _OccupancyDetectionTypeEnum_  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `parkingMode`: Modo(s) de aparcamiento. Enum:'echelonParking, parallelParking, perpendicularParking'  - `permitActiveHours`: Este atributo permite capturar situaciones en las que un permiso sólo es necesario en horas o días específicos de la semana.  Es un valor estructurado que debe contener una subpropiedad por cada permiso requerido, indicando cuando el permiso está activo. Si no se especifica nada para un permiso, significará que el permiso es siempre necesario. Un objeto JSON vacío significa que siempre está activo. La sintaxis debe ser conforme a schema.org  - `refParkingGroup`: Referencia a la(s) agrupación(es) de estacionamiento (si la hay) perteneciente(s) a esta zona de estacionamiento en la calle.  - `refParkingSpot`: Plazas de aparcamiento individuales pertenecientes a este sitio de aparcamiento en la calle.  - `requiredPermit`: Este atributo captura qué permiso(s) puede(n) ser necesario(s) para aparcar en este sitio. La semántica es que al menos _uno de estos permisos es necesario para aparcar. Cuando un permiso está compuesto por más de un elemento (y) se pueden combinar con un ','. Por ejemplo, "permiso de residente, permiso de discapacitado" significa que se necesita al mismo tiempo un permiso de residente y un permiso de discapacitado para aparcar. Si la lista está vacía, no se necesita ningún permiso.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `totalSpotNumber`: El número total de plazas que ofrece este aparcamiento. Este número puede ser difícil de obtener para aquellos lugares de estacionamiento en los que las plazas no están claramente marcadas con líneas. Referencias normativas: Atributo _parkingNumberOfSpaces_ de la clase _ParkingRecord_ de DATEX 2 versión 2.3.  - `type`: Tipo de entidad. Debe ser igual a OnStreetParking  - `usageScenario`: Tipo de carga(s) realizada(s) por el aparcamiento. Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'    
Propiedades requeridas  
- `id`  - `location`  - `type`    
En la terminología de DATEX 2 versión 2.3 corresponde a un _UrbanParkingSite_ de tipo _onStreetParking_. Se puede encontrar un diccionario de datos para los términos de DATEX II en [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OnStreetParking:    
  description: 'A site, open space zone, on street, (metered or not) with direct access from a road, intended to park vehicles.'    
  properties:    
    acceptedPaymentMethod:    
      description: 'Type of charge(s) performed by the parking site. Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'''    
      enum:    
        - ByBankTransferInAdvance    
        - ByInvoice    
        - Cash    
        - CheckInAdvance    
        - COD    
        - DirectDebit    
        - GoogleCheckout    
        - PayPal    
        - PaySwarm    
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
    allowedVehicleType:    
      description: 'Vehicle type allowed (only one per on street parking). Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, van, vehicleWithCatalyticConverter, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'''    
      enum:    
        - agriculturalVehicle    
        - anyVehicle    
        - articulatedVehicle    
        - bicycle    
        - bus    
        - car    
        - caravan    
        - carOrLightVehicle    
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
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areBordersMarked:    
      description: 'Denotes whether parking spots are delimited (with blank lines or similar) or not'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    availableSpotNumber:    
      description: 'The number of spots available globally, including reserved spaces, such as those for disabled people, long term parkers and so on. This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines'    
      minvalue: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    averageSpotLength:    
      description: 'The average length of parking spots'    
      minvalue: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
    averageSpotWidth:    
      description: 'The average width of parking spots'    
      minvalue: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
    category:    
      description: 'Street parking category. Enum:''blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'''    
      items:    
        enum:    
          - blueZone    
          - feeCharged    
          - forDisabled    
          - forElectricalCharging    
          - forLoadUnload    
          - forResidents    
          - free    
          - greenZone    
          - mediumTerm    
          - onlyWithPermit    
          - shortTerm    
          - taxiStop    
        type: string    
      type: Property    
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
    extraSpotNumber:    
      description: 'The number of extra spots available, i.e. free. Extra    spots are those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). This value must aggregate free spots from all groups devoted to special parking conditions. Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or equal to `totalSpotNumber'    
      minvalue: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
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
      description: 'Unique identifier of the entity'    
      type: Property    
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
    maximumParkingDuration:    
      description: 'Maximum allowed stay at site encoded as a ISO8601 duration. An empty value indicates an indefinite duration.'    
      format: date-time    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancyDetectionType:    
      description: 'Occupancy detection method(s). Enum:''balancing, manual, modelBased, none, singleSpaceDetection''. The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_'    
      items:    
        enum:    
          - balancing    
          - manual    
          - modelBased    
          - none    
          - singleSpaceDetection    
        type: string    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *onstreetparking_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    parkingMode:    
      description: 'Parking mode(s). Enum:''echelonParking, parallelParking, perpendicularParking'''    
      enum:    
        - echelonParking    
        - parallelParking    
        - perpendicularParking    
      type: Property    
    permitActiveHours:    
      description: 'This attribute allows to capture situations when a permit is only needed at specific hours or days of week.  It is an structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. An empty JSON Object means always active. The syntax must be conformant with schema.org'    
      type: Property    
    refParkingGroup:    
      description: 'Reference to the parking group(s) (if any) belonging to this onstreet parking zone.'    
      items:    
        type: string    
      type: Relationship    
    refParkingSpot:    
      description: 'Individual parking spots belonging to this on street parking site.'    
      items:    
        format: uri    
        type: string    
      type: Relationship    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed.'    
      items:    
        type: string    
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
      description: 'The total number of spots offered by this parking site. This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minvalue: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    type:    
      description: 'Entity type. It must be equal to OnStreetParking'    
      enum:    
        - OnStreetParking    
      type: Property    
    usageScenario:    
      description: 'Type of charge(s) performed by the parking site. Enum:''carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'''    
      enum:    
        - carSharing    
        - dropOff    
        - kissAndRide    
        - liftShare    
        - loadingBay    
        - overnightParking    
        - parkAndRide    
        - parkAndCycle    
        - parkAndWalk    
        - vehicleLift    
        - other    
      type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### OnStreetParking NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un OnStreetParking en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
  "occupiedSpotNumber": 3,  
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
#### OnStreetParking NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un OnStreetParking en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
  },  
  "occupiedSpotNumber": {  
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
#### OnStreetParking NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un OnStreetParking en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
  "occupiedSpotNumber": {  
    "type": "Property",  
    "value": 3,  
    "observedAt": "2018-09-12T12:00:00Z"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### OnStreetParking NGSI-LD normalizado Ejemplo  
Este es un ejemplo de OnStreetParking en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "allowedVehicleType": "car",  
  "areaServed": "Zona Centro",  
  "availableSpotNumber": 3,  
  "occupiedSpotNumber": 3,  
  "category": [  
    "blueZone",  
    "shortTerm",  
    "forDisabled"  
  ],  
  "chargeType": [  
    "temporaryFee"  
  ],  
  "extraSpotNumber": 2,  
  "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
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
  "maximumAllowedStay": "PT2H",  
  "modifiedAt": "2016-06-02T09:25:55.00Z",  
  "permitActiveHours": {  
    "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
  },  
  "refParkingGroup": [  
    "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-main",  
    "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled"  
  ],  
  "requiredPermit": [  
    "blueZonePermit",  
    "disabledPermit"  
  ],  
  "totalSpotNumber": 6,  
  "type": "OnStreetParking"  
}  
```  
