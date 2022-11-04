<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: ParkingGroup  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Grupo de aparcamientos**  
versión: 0.1.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `allowedVehicleType[string]`: Tipo de vehículo permitido (un grupo de aparcamiento sólo permite un tipo de vehículo). Enum:'bicicleta, autobús, coche, caravana, motocicleta, moto, camión'  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areBordersMarked[boolean]`: Indica si las plazas de aparcamiento están delimitadas (con líneas en blanco o similares) o no. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[integer]`: El número de plazas disponibles en este grupo. Debe ser menor o igual que `totalSpotNumber`.  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: La longitud media de las plazas de aparcamiento. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida.  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: La anchura media de las plazas de aparcamiento. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida.  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: Categoría del grupo de aparcamiento. Enum:'espacios adyacentes, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'  . Model: [http://schema.org/Text](http://schema.org/Text)- `chargeType[array]`: Tipo de cargo(s) realizado(s) por el aparcamiento. Enum:'precio adicional por intervalo, pago anual, precio por primer intervalo, tarifa plana, gratuito, mínimo, máximo, pago mensual, abono de temporada, tarifa temporal, precio temporal, desconocido, otro'.  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maximumAllowedHeight[number]`: Altura máxima permitida para los vehículos.  Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida.  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: Ancho máximo permitido para los vehículos. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida.  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[string]`: Estancia máxima permitida codificada como duración ISO8601. Cuando no está presente o es igual a la cadena vacía, significa indefinido. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida.  - `name[string]`: El nombre de este artículo.  - `occupancyDetectionType[array]`: Valores permitidos: Los siguientes de DATEX II versión 2.3 _OccupancyDetectionTypeEnum_. Enum:'balanceo, manual, modelBased, none, singleSpaceDetection'. O cualquier otro específico de la aplicación  . Model: [http://schema.org/Text](http://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `parkingMode[array]`: Modo(s) de estacionamiento. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida. Valores permitidos: Los definidos por la enumeración _ParkingModeEnum_ de DATEX II versión 2.3. Enum:'echelonParking, parallelParking, perpendicularParking'  . Model: [http://schema.org/Text](http://schema.org/Text)- `permitActiveHours[object]`: Este atributo permite capturar situaciones en las que un permiso sólo se necesita en horas o días específicos de la semana. Es un valor estructurado que debe contener una subpropiedad por cada permiso requerido, indicando cuando el permiso está activo. Si no se especifica nada para un permiso, significará que el permiso es siempre necesario. Un objeto vacío significa que siempre está activo. La sintaxis debe ser conforme a schema.org [open hours specification](https://schema.org/openingHours). Por ejemplo, una zona azul que sólo esté activa en las semanas de día se codificará como 'blueZonePermit': 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `refParkingSite[*]`: Sitio de estacionamiento al que pertenece esta zona. Un grupo no puede ser huérfano. Un grupo no puede tener subgrupos. Referencia a un OffStreetParking o a un OnStreetParking  - `refParkingSpot[*]`: Plazas de aparcamiento individuales que pertenecen a este grupo de aparcamiento.  - `requiredPermit[array]`: Este atributo captura qué permiso(s) puede(n) ser necesario(s) para aparcar en este sitio. La semántica es que al menos _uno de estos permisos es necesario para aparcar. Cuando un permiso está compuesto por más de un elemento (y) se pueden combinar con un ','. Por ejemplo, "permiso de residente, permiso de discapacitado" significa que se necesita al mismo tiempo un permiso de residente y un permiso de discapacitado para aparcar. Si la lista está vacía, no se necesita ningún permiso  . Model: [http://schema.org/Text](http://schema.org/Text)- `reservationType[string]`: Condiciones de reserva. Las aplicaciones _DEBEN_ inspeccionar el valor de esta propiedad a nivel de los padres si no está definida. Enum:'obligatorio, no disponible, opcional, parcialmente'.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `totalSpotNumber[integer]`: El número total de plazas pertenecientes a este grupo. Valores permitidos: Cualquier número entero positivo o 0. Referencias normativas: Atributo _parkingNumberOfSpaces_ de la clase _ParkingRecord_ de DATEX 2 versión 2.3.  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: Tipo de entidad NGSI. Tiene que ser ParkingGroup  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `refParkingSite`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Un grupo de plazas de aparcamiento. El nivel de granularidad puede variar. Puede ser una planta de un aparcamiento, una zona específica perteneciente a un gran aparcamiento, o simplemente un grupo de plazas destinadas a aparcar un determinado tipo de vehículo o sujetas a ciertas restricciones (discapacitados, residentes, ...). Para simplificar, sólo se permite un tipo de vehículo por grupo de aparcamiento. Del mismo modo, sólo se permite un permiso requerido por tipo de grupo.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ParkingGroup:    
  description: 'Parking Group '    
  properties:    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
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
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areBordersMarked:    
      description: 'Denotes whether parking spots are delimited (with blank lines or similar) or not. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableSpotNumber:    
      description: 'The number of spots available in this group. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: 'The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
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
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
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
      type: array    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
      x-ngsi:    
        type: GeoProperty    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: Meters    
    maximumParkingDuration:    
      description: 'Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *parkinggroup_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    permitActiveHours:    
      description: 'This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is an structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. Empty object means always active. The syntax must be conformant with schema.org [opening hours specification](https://schema.org/openingHours). For instance, a blue zone which is only active on dayweeks will be encoded as ''blueZonePermit'': ''Mo,Tu,We,Th,Fr,Sa 09:00-20:00''. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined'    
      type: object    
      x-ngsi:    
        model: https://schema.org/openingHours    
        type: Property    
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
      x-ngsi:    
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
      x-ngsi:    
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
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    reservationType:    
      description: 'Conditions for reservation. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined. Enum:''mandatory, notAvailable, optional, partly''.'    
      enum:    
        - mandatory    
        - notAvailable    
        - optional    
        - partly    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalSpotNumber:    
      description: 'The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ParkingGroup'    
      enum:    
        - ParkingGroup    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - refParkingSite    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/ParkingGroup/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/ParkingGroup/schema.json    
  x-model-tags: ""    
  x-version: 0.1.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### ParkingGroup NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un ParkingGroup en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### ParkingGroup NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un ParkingGroup en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### ParkingGroup NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un ParkingGroup en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
    "type": "ParkingGroup",  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": "car"  
    },  
    "availableSpotNumber": {  
        "type": "Property",  
        "value": 1,  
        "observedAt": "2018-09-12T12:00:00Z"  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "onstreet",  
            "adjacentSpaces",  
            "onlyDisabled"  
        ]  
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
    "permitActiveHours": {  
        "type": "Property",  
        "value": "null"  
    },  
    "refParkingSite": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:ParkingSite:daoiz-velarde-1-5"  
    },  
    "requiredPermit": {  
        "type": "Property",  
        "value": "disabledPermit"  
    },  
    "totalSpotNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### ParkingGroup NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un ParkingGroup en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled",  
    "type": "ParkingGroup",  
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
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
