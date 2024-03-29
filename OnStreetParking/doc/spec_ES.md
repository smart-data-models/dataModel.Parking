<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: OnStreetParking    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Parking/blob/master/OnStreetParking/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Un sitio, zona de espacio abierto, en la calle, (con contador o no) con acceso directo desde una carretera, destinado al estacionamiento de vehículos.**    
versión: 0.1.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `acceptedPaymentMethod[string]`: Tipo de cargo(s) realizado(s) por el aparcamiento. Enum:'Por transferencia bancaria por adelantado, Por factura, En efectivo, Cheque por adelantado, Contra reembolso, Débito directo, GoogleCheckout, PayPal, PaySwarm'.  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `allowedVehicleType[array]`: Tipo(s) de vehículo(s) permitido(s). El primer elemento de esta matriz _DEBE_ ser el tipo de vehículo principal permitido. Los siguientes valores definidos por _VehicleTypeEnum_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html).. Enum:vehículo agrícola, cualquier vehículo, vehículo articulado, bicicleta, autobús, coche, caravana, coche o vehículo ligero, coche con caravana, coche con remolque, vehículo de construcción o mantenimiento, tracción en las cuatro ruedas, vehículo de gran altura, camión, ciclomotor, motocicleta, motocicleta con coche lateral, motocarro, cisterna, vehículo de tres ruedas, remolque, tranvía, vehículo de dos ruedas, furgoneta, vehículo con catalizador, vehículo sin catalizador, vehículo con caravana, vehículo con remolque, con matrícula par, con matrícula adicional, otros".  - `alternateName[string]`: Un nombre alternativo para este artículo  - `areBordersMarked[boolean]`: Indica si las plazas de aparcamiento están delimitadas (con líneas en blanco o similares) o no.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: El número de plazas disponibles globalmente, incluidas las plazas reservadas, como las destinadas a discapacitados, estacionamientos de larga duración, etc. Esto puede ser más difícil de estimar en aquellos aparcamientos en los que los límites de las plazas no están claramente marcados por líneas.  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: La longitud media de las plazas de aparcamiento  . Model: [https://schema.org/length](https://schema.org/length)- `averageSpotWidth[number]`: La anchura media de las plazas de aparcamiento  . Model: [https://schema.org/width](https://schema.org/width)- `category[array]`: Categoría de aparcamiento en la calle. Enum:'blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'  - `chargeType[array]`: Tipo de tarifa(s) aplicada(s) por el aparcamiento. Enum:'precioIntervaloAdicional, pagoAnual, precioPrimerIntervalo, tarifa plana, gratuito, mínimo, máximo, pagoMensual, abonoTemporada, tarifaTemporal, precioTemporal, desconocido, otro'.  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `extraSpotNumber[number]`: El número de plazas extra disponibles, es decir, libres. Las plazas adicionales son aquellas reservadas para fines especiales y normalmente requieren un permiso. Los detalles del permiso se encontrarán a nivel de grupo de aparcamiento (entidad de tipo `ParkingGroup`). Este valor debe agregar las plazas libres de todos los grupos dedicados a condiciones especiales de aparcamiento. Valores permitidos: Un número entero positivo, incluido 0. `extraSpotNumber` más `availableSpotNumber` debe ser menor o igual que `totalSpotNumber  . Model: [http://schema.org/Number](http://schema.org/Number)- `fourWheelerSlots[object]`: Estado de disponibilidad de plazas de estacionamiento para vehículos de cuatro ruedas en el aparcamiento correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSlotNumber[number]`: Número de plazas de aparcamiento disponibles para su uso en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al número total de plazas.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSlotNumber[number]`: Número de plazas ocupadas en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al número total de plazas.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `id[*]`: Identificador único de la entidad  - `layout[array]`: Clasificación genérica de la disposición del aparcamiento  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `maximumParkingDuration[date-time]`: Estancia máxima permitida en el lugar codificada como duración ISO8601. Un valor vacío indica una duración indefinida  - `municipalityInfo[object]`: Información municipal correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: ID de la ciudad correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: Nombre de la ciudad correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: Nombre del distrito correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: Nombre del estado correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: Nombre de la Entidad Local Urbana correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: ID de pabellón correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: Nombre del pabellón correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: Número de pabellón correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: ID de zona correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: El nombre de este artículo  - `observationDateTime[date-time]`: Última hora de observación comunicada  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancyDetectionType[array]`: Método(s) de detección de ocupación. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. Lo siguiente de DATEX II versión 2.3 _OccupancyDetectionTypeEnum_  - `occupancyModified[date-time]`: Fecha de la última modificación de la ocupación del aparcamiento  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `occupiedSpotNumber[number]`: Número total de plazas de aparcamiento ocupadas en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al totalSpotNumber.  . Model: [https://schema.org/Number](https://schema.org/Number)- `outOfServiceSlotNumber[number]`: El número de aparcabicicletas/plazas de aparcamiento o estacionamiento de bicicletas que están averiados y no se pueden utilizar para alquilar o aparcar una bicicleta en la estación de aparcamiento o estacionamiento de bicicletas correspondiente a esta observación.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `parkingMode[string]`: Modo(s) de aparcamiento. Enum:'aparcamiento en escalón, aparcamiento en paralelo, aparcamiento en perpendicular'  - `parkingSiteId[string]`: ID único del aparcamiento o estacionamiento correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `permitActiveHours[object]`: Este atributo permite capturar situaciones en las que un permiso sólo es necesario a determinadas horas o días de la semana. Es un valor estructurado que debe contener una subpropiedad por cada permiso requerido, indicando cuándo está activo el permiso. Si no se especifica nada para un permiso, significará que siempre se necesita un permiso. Un objeto JSON vacío significa que siempre está activo. La sintaxis debe ser conforme con schema.org  - `refParkingGroup[array]`: Referencia al grupo o grupos de estacionamiento (en su caso) pertenecientes a esta zona de estacionamiento en la vía pública  - `refParkingSpot[array]`: Plazas individuales pertenecientes a este aparcamiento en la calle  - `requiredPermit[array]`: Este atributo indica qué permiso(s) puede(n) ser necesario(s) para aparcar en este lugar. La semántica es que se necesita al menos _uno_ de estos permisos para aparcar. Cuando un permiso está compuesto por más de un elemento (y) pueden combinarse con un ','. Por ejemplo, 'permisoresidente,permisodiscapacitados' significa que se necesita al mismo tiempo un permiso de residente y un permiso de discapacitado para aparcar. Si la lista está vacía, no se necesita ningún permiso  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `totalSpotNumber[number]`: El número total de plazas que ofrece este aparcamiento. Este número puede ser difícil de obtener para aquellos lugares de estacionamiento en los que las plazas no están claramente marcadas con líneas. Referencias normativas: Atributo _parkingNumberOfSpaces_ de la clase _ParkingRecord_ de DATEX 2 versión 2.3  . Model: [http://schema.org/Number](http://schema.org/Number)- `twoWheelerSlots[object]`: Estado de disponibilidad de plazas de estacionamiento para vehículos de dos ruedas en el aparcamiento correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: Número de plazas de aparcamiento disponibles para su uso en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al número total de plazas.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSpotNumber[number]`: Número de plazas ocupadas en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al número total de plazas.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `type[string]`: Tipo de entidad. Debe ser igual a OnStreetParking  - `unclassifiedSlots[object]`: Estado de disponibilidad de plazas de estacionamiento de vehículos no clasificados u otros vehículos en el lugar de estacionamiento correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: Número de plazas de aparcamiento disponibles para su uso en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al número total de plazas.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSpotNumber[number]`: Número de plazas ocupadas en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al número total de plazas.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `usageScenario[string]`: Tipo de cargo(s) realizado(s) por el aparcamiento. Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
En la terminología de DATEX 2 versión 2.3 corresponde a un _UrbanParkingSite_ de tipo _onStreetParking_. Puede consultarse un diccionario de datos para los términos DATEX II en [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
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
      type: string      
      x-ngsi:      
        type: Property      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    allowedVehicleType:      
      description: 'Vehicle type(s) allowed. The first element of this array _MUST_ be the principal vehicle type allowed. The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html).. Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, van, vehicleWithCatalyticConverter, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'''      
      items:      
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
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areBordersMarked:      
      description: Denotes whether parking spots are delimited (with blank lines or similar) or not      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    availableSpotNumber:      
      description: 'The number of spots available globally, including reserved spaces, such as those for disabled people, long term parkers and so on. This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    averageSpotLength:      
      description: The average length of parking spots      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/length      
        type: Property      
    averageSpotWidth:      
      description: The average width of parking spots      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/width      
        type: Property      
    category:      
      description: 'Street parking category. Enum:''blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'''      
      items:      
        enum:      
          - barrierAccess      
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
          - public      
          - shortTerm      
          - taxiStop      
          - underground      
        type: string      
      type: array      
      x-ngsi:      
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
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    extraSpotNumber:      
      description: 'The number of extra spots available, i.e. free. Extra    spots are those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). This value must aggregate free spots from all groups devoted to special parking conditions. Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or equal to `totalSpotNumber'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    fourWheelerSlots:      
      description: Four wheeler parking spot availability status in parking site corresponding to this observation      
      properties:      
        availableSlotNumber:      
          description: Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        occupiedSlotNumber:      
          description: Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        totalSlotNumber:      
          description: The total number of spots offered by the parking site corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    layout:      
      description: Generic classification of the layout of the parking      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    maximumParkingDuration:      
      description: Maximum allowed stay at site encoded as a ISO8601 duration. An empty value indicates an indefinite duration      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    municipalityInfo:      
      description: Municipality information corresponding to this observation      
      properties:      
        cityId:      
          description: City ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        cityName:      
          description: City name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        district:      
          description: District name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        stateName:      
          description: Name of the state corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        ulbName:      
          description: Name of the Urban Local Body corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardId:      
          description: Ward ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardName:      
          description: Ward name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        wardNum:      
          description: Ward number corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        zoneId:      
          description: Zone ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        zoneName:      
          description: Zone name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
      type: array      
      x-ngsi:      
        type: Property      
    occupancyModified:      
      description: Date last time the occupancy of the parking has being modified      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    occupiedSpotNumber:      
      description: Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    outOfServiceSlotNumber:      
      description: The number of bike racks/bike-docking slots or parking slots that are out of order and cannot be used to hire or park a bike in the bike docking station or parking site corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    parkingMode:      
      description: 'Parking mode(s). Enum:''echelonParking, parallelParking, perpendicularParking'''      
      enum:      
        - echelonParking      
        - parallelParking      
        - perpendicularParking      
      type: string      
      x-ngsi:      
        type: Property      
    parkingSiteId:      
      description: The unique ID of the parking site or parking lot corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    permitActiveHours:      
      description: 'This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is a structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. An empty JSON Object means always active. The syntax must be conformant with schema.org'      
      type: object      
      x-ngsi:      
        type: Property      
    refParkingGroup:      
      description: Reference to the parking group(s) (if any) belonging to this onstreet parking zone      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Relationship      
    refParkingSpot:      
      description: Individual parking spots belonging to this on street parking site      
      items:      
        format: uri      
        type: string      
      type: array      
      x-ngsi:      
        type: Relationship      
    requiredPermit:      
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed'      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    totalSpotNumber:      
      description: 'The total number of spots offered by this parking site. This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    twoWheelerSlots:      
      description: Two wheeler parking spot availability status in parking site corresponding to this observation      
      properties:      
        availableSpotNumber:      
          description: Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        occupiedSpotNumber:      
          description: Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        totalSpotNumber:      
          description: The total number of spots offered by the parking site corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: Entity type. It must be equal to OnStreetParking      
      enum:      
        - OnStreetParking      
      type: string      
      x-ngsi:      
        type: Property      
    unclassifiedSlots:      
      description: Unclassified vehicles or other vehicles parking spot availability status in parking site corresponding to this observation      
      properties:      
        availableSpotNumber:      
          description: Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        occupiedSpotNumber:      
          description: Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        totalSpotNumber:      
          description: The total number of spots offered by the parking site corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
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
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - location      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/OnStreetParking/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/OnStreetParking/schema.json      
  x-model-tags: IUDX      
  x-version: 0.1.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### OnStreetParking NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de un OnStreetParking en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": [  
    "blueZone",  
    "shortTerm",  
    "forDisabled"  
  ],  
  "allowedVehicleType": [  
    "car"  
  ],  
  "chargeType": [  
    "temporaryFee"  
  ],  
  "requiredPermit": [  
    "blueZonePermit",  
    "disabledPermit"  
  ],  
  "permitActiveHours": {  
    "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
  },  
  "maximumParkingDuration": "PT2H",  
  "availableSpotNumber": 3,  
  "occupiedSpotNumber": 3,  
  "totalSpotNumber": 6,  
  "extraSpotNumber": 2,  
  "dateModified": "2016-06-02T09:25:55.00Z",  
  "location": {  
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
  },  
  "areaServed": "Zona Centro",  
  "refParkingGroup": [  
    "daoiz-velarde-1-5-main",  
    "daoiz-velarde-1-5-disabled"  
  ],  
  "outOfServiceSlotNumber": 0,  
  "parkingSiteId": "P2",  
  "observationDateTime": "2021-03-11T15:51:02Z",  
  "fourWheelerSlots": {  
    "availableSpotNumber": 25,  
    "totalSpotNumber": 25,  
    "occupiedSpotNumber": 0  
  },  
  "unclassifiedSlots": {  
    "availableSpotNumber": 0,  
    "totalSpotNumber": 0,  
    "occupiedSpotNumber": 0  
  },  
  "twoWheelerSlots": {  
    "availableSpotNumber": 20,  
    "totalSpotNumber": 20,  
    "occupiedSpotNumber": 0  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
</details>    
#### OnStreetParking NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de OnStreetParking en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "blueZone",  
      "shortTerm",  
      "forDisabled"  
    ]  
  },  
  "permitActiveHours": {  
    "type": "StructuredValue",  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "requiredPermit": {  
    "type": "StructuredValue",  
    "value": [  
      "blueZonePermit",  
      "disabledPermit"  
    ]  
  },  
  "allowedVehicleType": {  
    "type": "StructuredValue",  
    "value": [  
      "car"  
    ]  
  },  
  "chargeType": {  
    "type": "StructuredValue",  
    "value": [  
      "temporaryFee"  
    ]  
  },  
  "refParkingGroup": {  
    "type": "StructuredValue",  
    "value": [  
      "daoiz-velarde-1-5-main",  
      "daoiz-velarde-1-5-disabled"  
    ]  
  },  
  "totalSpotNumber": {  
    "type": "Number",  
    "value": 6  
  },  
  "location": {  
    "type": "geo:json",  
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
    "type": "Text",  
    "value": "Zona Centro"  
  },  
  "maximumAllowedStay": {  
    "type": "Text",  
    "value": "PT2H"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2016-06-02T09:25:55.00Z"  
  },  
  "extraSpotNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "availableSpotNumber": {  
    "type": "Number",  
    "value": 3,  
    "metadata": {  
      "timestamp": {  
        "value": "2018-09-12T12:00:00",  
        "type": "DateTime"  
      }  
    }  
  },  
  "occupiedSpotNumber": {  
    "type": "Number",  
    "value": 3,  
    "metadata": {  
      "timestamp": {  
        "value": "2018-09-12T12:00:00",  
        "type": "DateTime"  
      }  
    }  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02Z"  
  },  
  "fourWheelerSlots": {  
    "type": "StructuredValue",  
    "value": {  
      "availableSpotNumber": 25,  
      "totalSpotNumber": 25,  
      "occupiedSpotNumber": 0  
    }  
  },  
  "unclassifiedSlots": {  
    "type": "StructuredValue",  
    "value": {  
      "availableSpotNumber": 0,  
      "totalSpotNumber": 0,  
      "occupiedSpotNumber": 0  
    }  
  },  
  "twoWheelerSlots": {  
    "type": "StructuredValue",  
    "value": {  
      "availableSpotNumber": 20,  
      "totalSpotNumber": 20,  
      "occupiedSpotNumber": 0  
    }  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
</details>    
#### OnStreetParking NGSI-LD key-values Ejemplo    
He aquí un ejemplo de un OnStreetParking en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "allowedVehicleType": [  
    "car"  
  ],  
  "areaServed": "Zona Centro",  
  "availableSpotNumber": 3,  
  "category": [  
    "blueZone",  
    "shortTerm",  
    "forDisabled"  
  ],  
  "chargeType": [  
    "temporaryFee"  
  ],  
  "extraSpotNumber": 2,  
  "fourWheelerSlots": {  
    "availableSpotNumber": 25,  
    "totalSpotNumber": 25,  
    "occupiedSpotNumber": 0  
  },  
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
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  },  
  "observationDateTime": "2021-03-11T15:51:02Z",  
  "occupiedSpotNumber": 3,  
  "parkingSiteId": "P2",  
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
  "twoWheelerSlots": {  
    "availableSpotNumber": 20,  
    "totalSpotNumber": 20,  
    "occupiedSpotNumber": 0  
  },  
  "unclassifiedSlots": {  
    "availableSpotNumber": 0,  
    "totalSpotNumber": 0,  
    "occupiedSpotNumber": 0  
  },  
  "@context": [  
    "iudx:SmartParking",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### OnStreetParking NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de OnStreetParking en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:OnStreetParking:santander:daoiz_velarde_1_5",  
    "type": "OnStreetParking",  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": [  
            "car"  
        ]  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Zona Centro"  
    },  
    "availableSpotNumber": {  
        "type": "Property",  
        "value": 3,  
        "observedAt": "2018-09-12T12:00:00Z"  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "blueZone",  
            "shortTerm",  
            "forDisabled"  
        ]  
    },  
    "chargeType": {  
        "type": "Property",  
        "value": [  
            "temporaryFee"  
        ]  
    },  
    "extraSpotNumber": {  
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
    "maximumAllowedStay": {  
        "type": "Property",  
        "value": "PT2H"  
    },  
    "occupiedSpotNumber": {  
        "type": "Property",  
        "value": 3,  
        "observedAt": "2018-09-12T12:00:00Z"  
    },  
    "permitActiveHours": {  
        "type": "Property",  
        "value": {  
            "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
        }  
    },  
    "refParkingGroup": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-main",  
            "urn:ngsi-ld:ParkingGroup:daoiz-velarde-1-5-disabled"  
        ]  
    },  
    "requiredPermit": {  
        "type": "Property",  
        "value": [  
            "blueZonePermit",  
            "disabledPermit"  
        ]  
    },  
    "totalSpotNumber": {  
        "type": "Property",  
        "value": 6  
    },  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
