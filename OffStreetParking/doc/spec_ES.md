<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: OffStreetParking  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Parking/blob/master/OffStreetParking/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Estacionamiento en la calle**  
versión: 0.1.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `acceptedPaymentMethod[array]`: Enum:'Transferencia bancaria por adelantado, Por factura, En efectivo, Cheque por adelantado, Contra reembolso, Débito directo, GoogleCheckout, PayPal, PaySwarm'. Método(s) de pago aceptado(s).  . Model: [https://schema.org/acceptedPaymentMethod](https://schema.org/acceptedPaymentMethod)- `accessModified[string]`: Marca de tiempo cuando se actualizó `vehicleEntranceCount` y `vehicleExitCount`. Valores permitidos: ISO8601  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `aggregateRating[object]`: Valoración agregada de este aparcamiento.  . Model: [https://schema.org/aggregateRating](https://schema.org/aggregateRating)- `allowedVehicleType[array]`:  Tipo(s) de vehículo permitido(s). El primer elemento de esta matriz _DEBE_ ser el tipo de vehículo principal permitido. Los números de plaza libre de otros tipos de vehículos permitidos pueden notificarse bajo el atributo `extraSpotNumber` y a través de entidades específicas de tipo _ParkingGroup_. Los siguientes valores definidos por _VehicleTypeEnum_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum:'agriculturalVehicle, anyVehicle, bicycle, bus, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[integer]`: El número de plazas disponibles (_incluyendo_ todos los tipos de vehículos o las plazas reservadas, como las de discapacitados, las de larga duración, etc.). Esto puede ser más difícil de estimar en aquellos aparcamientos en los que los límites de las plazas no están claramente marcados por líneas. Valores permitidos: Un número entero positivo, incluyendo el 0. Debe ser menor o igual que `totalSpotNumber`.  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: La longitud media de las plazas de aparcamiento.  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: La anchura media de las plazas de aparcamiento.  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: Categoría(s) del aparcamiento. El propósito de este campo es permitir etiquetar, en términos generales, las entidades de estacionamiento fuera de la calle  - `chargeType[array]`: Tipo(s) de carga realizado(s) por el aparcamiento. Valores permitidos: Algunos de los definidos por la enumeración DATEX II versión 2.3 _ ChargeTypeEnum_. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice'. O cualquier otra aplicación específica  - `contactPoint[object]`: Punto de contacto del aparcamiento.  . Model: [https://schema.org/contactPoint](https://schema.org/contactPoint)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `extCategory[array]`: Categoría externa para complementar la categoría.  - `extraSpotNumber[integer]`: El número de plazas adicionales _disponibles_, es decir, libres. Este valor debe sumar las plazas libres de todos los grupos mencionados a continuación: A/ Las reservadas para fines especiales y que suelen requerir un permiso. Los detalles del permiso se encontrarán a nivel de grupo de aparcamiento (entidad de tipo `ParkingGroup`). B/ Las reservadas para otros tipos de vehículos diferentes al tipo de vehículo principal permitido. C/ Cualquier otro grupo de plazas de aparcamiento que no esté sujeto a las normas de condición general transmitidas por esta entidad.  . Model: [http://schema.org/Number](http://schema.org/Number)- `facilities[array]`: Valores permitidos: Los siguientes definidos por la enumeración _EquipmentTypeEnum_ de DATEX II versión 2.3. Enum:'bikeParking, cashMachine, copyMachineOrService, defibrillator, dumpingStation, electricChargingStation, elevator, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, andamio sin hielo, punto de información, internet inalámbrico, consigna de equipaje, mostrador de pago, máquina de pago, parque infantil, teléfono público, cubo de basura, caja fuerte, ducha, aseo, terminal de peaje, máquina expendedora, eliminación de residuos". Cualquier otra aplicación específica  . Model: []()- `firstAvailableFloor[integer]`: Número de la planta más cercana al suelo que tiene actualmente plazas de aparcamiento disponibles. Valores permitidos: Las plantas se numeran entre -n y n, siendo 0 la planta baja.  . Model: [http://schema.org/Number](http://schema.org/Number)- `fourWheelerSlots[object]`: Estado de disponibilidad de plazas de aparcamiento para vehículos de cuatro ruedas en el lugar de estacionamiento correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `highestFloor[integer]`: En el caso de los aparcamientos con varias plantas, la planta más alta. Un número entero. El 0 es la planta baja. Las plantas superiores son números positivos. Las plantas inferiores son números negativos.  . Model: [http://schema.org/Number](http://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `images[array]`: Una URL que contenga una foto de este aparcamiento  . Model: [https://schema.org/image](https://schema.org/image)- `layout[array]`: Disposición del aparcamiento. Da más detalles al atributo `categoría`. Valores permitidos: Según el _ParkingLayoutEnum_ de DATEX II versión 2.3. Enum:'automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other'. Véase también [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). O cualquier otro valor útil para la aplicación y que no esté contemplado anteriormente.  . Model: [http://schema.org/Text](http://schema.org/Text)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `lowestFloor[integer]`: En los aparcamientos con varias plantas, la planta más baja. Valores permitidos: Un número entero.  . Model: [http://schema.org/Number](http://schema.org/Number)- `maximumAllowedHeight[number]`: Altura máxima permitida para los vehículos. Si hay varias zonas, será la altura mínima de todas ellas.  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: Anchura máxima permitida para los vehículos. Si hay varias zonas, será la anchura mínima de todas ellas.  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[string]`: La estancia máxima permitida en el sitio, de forma general, codificada como una duración ISO8601 o con cualquier otra cadena relevante para el estacionamiento.  Un valor vacío o no presente indica una duración indefinida  . Model: [http://schema.org/Text](http://schema.org/Text)- `measuresPeriod[number]`: El período de medidas relacionadas con availableSpotNumber y priceRatePerMinute.  . Model: [http://schema.org/Number](http://schema.org/Number)- `measuresPeriodUnit[string]`: La unidad de período de medidas relacionadas con availableSpotNumber y PriceRatePerMinute.  . Model: [http://schema.org/unitText](http://schema.org/unitText)- `municipalityInfo[object]`: Información del municipio correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo.  - `observationDateTime[string]`: Última hora de observación comunicada.  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancy[number]`: Valor relativo de las plazas ocupadas sobre el total de plazas.  . Model: [http://schema.org/Number](http://schema.org/Number)- `occupancyDetectionType[array]`: Método(s) de detección de la ocupación.  Valores permitidos: Los siguientes de DATEX II versión 2.3 _OccupancyDetectionTypeEnum_. Enum:'balanceo, manual, modelBased, none, singleSpaceDetection'. O cualquier otro específico de la aplicación  . Model: [http://schema.org/Text](http://schema.org/Text)- `occupancyModified[string]`: Valor relativo de los puntos ocupados sobre el total de puntos. Valores permitidos: 0 - 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `occupiedSpotNumber[integer]`: Número de plazas totales ocupadas en el aparcamiento inteligente correspondiente a esta observación. Debe ser un número positivo inferior o igual al totalSpotNumber  . Model: [http://schema.org/Number](http://schema.org/Number)- `openingHours[string]`: Horario de apertura del aparcamiento.  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `outOfServiceSlotNumber[number]`: El número de aparcabicicletas/plazas de estacionamiento de bicicletas o plazas de aparcamiento que están fuera de servicio y no pueden utilizarse para alquilar o aparcar una bicicleta en la estación de estacionamiento de bicicletas o en el lugar de estacionamiento correspondiente a esta observación.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `parkingMode[array]`: Modo(s) de aparcamiento. Valores permitidos: Los definidos por la enumeración _ParkingModeEnum_ de DATEX II versión 2.3. Enum:'echelonParking, parallelParking, perpendicularParking'  . Model: [http://schema.org/Text](http://schema.org/Text)- `parkingSiteId[string]`: El ID único del aparcamiento o estacionamiento correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `priceCurrency[string]`: Moneda de precio de la tarifa por minuto  . Model: [https://schema.org/priceCurrency](https://schema.org/priceCurrency)- `priceRatePerMinute[number]`: Precio por minuto.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `provider[object]`: Proveedor de servicios de aparcamiento  . Model: [https://schema.org/provider](https://schema.org/provider)- `refParkingAccess[*]`: Punto(s) de acceso al aparcamiento.  . Model: [http://schema.org/URL](http://schema.org/URL)- `refParkingGroup[*]`: Grupo(s) identificado(s) del sitio de estacionamiento. Un grupo puede corresponder a una zona, una planta completa, un grupo de plazas, etc.  . Model: [http://schema.org/URL](http://schema.org/URL)- `refParkingSpot[*]`: Plazas de aparcamiento individuales que pertenecen a este sitio de estacionamiento fuera de la calle.  - `requiredPermit[array]`: Este atributo captura qué permiso(s) puede(n) ser necesario(s) para aparcar en este sitio. La semántica es que al menos _uno de estos permisos es necesario para aparcar. Cuando un permiso está compuesto por más de un elemento (y) se pueden combinar con un ','. Por ejemplo, "permiso de residente, permiso de discapacitado" significa que se necesita al mismo tiempo un permiso de residente y un permiso de discapacitado para aparcar. Si la lista está vacía, no se necesita ningún permiso. Valores permitidos: Los siguientes, definidos por la enumeración _PermitTypeEnum_ de DATEX II versión 2.3. Enum:'employeePermit, fairPermit, governmentPermit, noPermitNeed, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit'. O cualquier otra aplicación específica  - `reservationType[array]`: a siguiente especificada por _ReservationTypeEnum_ de DATEX II versión 2.3. Enum:'obligatorio, no disponible, opcional, parcialmente'  . Model: [http://schema.org/Text](http://schema.org/Text)- `security[array]`: Aspectos de seguridad proporcionados por este aparcamiento. Valores permitidos: Los siguientes, algunos de ellos, definidos por _ParkingSecurityEnum_ de DATEX II versión 2.3. Enum:'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' . o cualquier otro específico de la aplicación  . Model: [http://schema.org/Text](http://schema.org/Text)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `specialLocation[array]`: Si el aparcamiento se encuentra en un lugar especial (aeropuerto, grandes almacenes, etc.) transmite cuál es ese lugar especial.  Valores permitidos: Los definidos por _ParkingSpecialLocationEnum_ de [DATEX II versión 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). Enum:'terminal de aeropuerto, estación de cable, camping, cine, estación de autocares, centro de convenciones, centro de exposiciones, terminal de ferry, hotel, mercado, estación de transporte público, centro religioso, centro comercial, ascensor, instalación específica, parque temático, estación de tren, terminal de vehículos sobre raíles, otros'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `status[array]`: Estado del aparcamiento. Valores permitidos: Los siguientes definidos por las siguientes enumeraciones definidas por DATEX II versión 2.3. Enum:'casiLleno, cerrado, cerradoAnormal, lleno, llenoEnEntrada, abierto, aperturaTiempoEnFuerza, plazasDisponibles'. O cualquier otra aplicación específica  . Model: [http://schema.org/Text](http://schema.org/Text)- `totalSpotNumber[integer]`: El número total de plazas que ofrece este aparcamiento.  Este número puede ser difícil de obtener para aquellos aparcamientos en los que las plazas no están claramente marcadas con líneas. Valores permitidos: Cualquier número entero positivo o 0. Referencias normativas: Atributo _parkingNumberOfSpaces_ de la clase _ParkingRecord_ de DATEX 2 versión 2.3.  . Model: [http://schema.org/Number](http://schema.org/Number)- `twoWheelerSlots[object]`: Estado de disponibilidad de plazas de aparcamiento de dos ruedas en el lugar de estacionamiento correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tiene que ser OffStreetParking  - `unclassifiedSlots[object]`: Estado de disponibilidad de plazas de aparcamiento de vehículos no clasificados u otros vehículos en el lugar de aparcamiento correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `usageScenario[array]`: Escenario(s) de uso. Da más detalles al atributo `categoría`. Valores permitidos: Los definidos por la enumeración _ParkingUsageScenarioEnum_ de DATEX II versión 2.3. Enum: 'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other'. O cualquier otro valor útil para la aplicación y que no esté contemplado anteriormente.  . Model: [http://schema.org/Text](http://schema.org/Text)- `vehicleEntranceCount[number]`: Número agregado de vehículos que entran en el aparcamiento en un periodo de tiempo.  . Model: [http://schema.org/Number](http://schema.org/Number)- `vehicleExitCount[number]`: Número agregado de vehículos que salen del aparcamiento en un periodo de tiempo.  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Un sitio, fuera de la calle, destinado al estacionamiento de vehículos, gestionado de forma independiente y con puntos de acceso adecuados y claramente señalizados (entradas y salidas). Si es necesario, y con fines de gestión o para tratar sitios de estacionamiento con varias ubicaciones, puede dividirse en diferentes zonas modeladas por el tipo de entidad [ParkingGroup](../ParkingGroup/README.md) . En la terminología de DATEX 2 versión 2.3 corresponde a un _UrbanParkingSite_ de tipo _offStreetParking_. Un diccionario de datos para los términos de DATEX II puede encontrarse en [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OffStreetParking:    
  description: 'Off street parking'    
  properties:    
    acceptedPaymentMethod:    
      description: 'Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm''. Accepted payment method(s).'    
      items:    
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
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/acceptedPaymentMethod    
        type: Property    
    accessModified:    
      description: 'Timestamp when `vehicleEntranceCount` and `vehicleExitCount` was updated. Allowed values: ISO8601'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    aggregateRating:    
      description: 'Aggregated rating for this parking site.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/aggregateRating    
        type: Property    
    allowedVehicleType:    
      description: ' Vehicle type(s) allowed. The first element of this array _MUST_ be the principal vehicle type allowed. Free spot numbers of other allowed vehicle types might be reported under the attribute `extraSpotNumber` and through specific entities of type _ParkingGroup_. The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum:''agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'''    
      items:    
        enum:    
          - agriculturalVehicle    
          - anyVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - tanker    
          - trailer    
          - van    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableSpotNumber:    
      description: 'The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: 'The average length of parking spots.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: meters    
    category:    
      description: 'Parking site''s category(ies). The purpose of this field is to allow to tag, generally speaking, off street parking entities'    
      items:    
        enum:    
          - barrierAccess    
          - feeCharged    
          - forCustomers    
          - forDisabled    
          - forElectricalCharging    
          - forEmployees    
          - forMembers    
          - forResidents    
          - forStudents    
          - forVisitors    
          - free    
          - freeAccess    
          - gateAccess    
          - guarded    
          - ground    
          - longTerm    
          - mediumTerm    
          - onlyResidents    
          - onlyWithPermit    
          - parkingGarage    
          - parkingLot    
          - private    
          - public    
          - publicPrivate    
          - shortTerm    
          - staffed    
          - underground    
          - urbanDeterrentParking    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    chargeType:    
      description: 'Type(s) of charge performed by the parking site. Allowed values: Some of those defined by the DATEX II version 2.3 _ ChargeTypeEnum_ enumeration. Enum:''additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice''. Or any other application-specific'    
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
          - other    
          - seasonTicket    
          - temporaryPrice    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    contactPoint:    
      description: 'Parking site contact point.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/contactPoint    
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
    extCategory:    
      description: 'External category to complement category.'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    extraSpotNumber:    
      description: 'The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    facilities:    
      description: 'Allowed values: The following defined by the _EquipmentTypeEnum_ enumeration of DATEX II version 2.3. Enum:''bikeParking, cashMachine, copyMachineOrService, defibrillator, dumpingStation, electricChargingStation, elevator, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, iceFreeScaffold, informationPoint, internetWireless, luggageLocker, payDesk, paymentMachine, playground, publicPhone, refuseBin, safeDeposit, shower, toilet, tollTerminal, vendingMachine, wasteDisposal'' . Any other application-specific'    
      items:    
        enum:    
          - bikeParking    
          - cashMachine    
          - copyMachineOrService    
          - defibrillator    
          - dumpingStation    
          - electricChargingStation    
          - elevator    
          - faxMachineOrService    
          - fireHose    
          - fireExtinguisher    
          - fireHydrant    
          - firstAidEquipment    
          - freshWater    
          - iceFreeScaffold    
          - informationPoint    
          - internetWireless    
          - luggageLocker    
          - payDesk    
          - paymentMachine    
          - playground    
          - publicPhone    
          - refuseBin    
          - safeDeposit    
          - shower    
          - toilet    
          - tollTerminal    
          - vendingMachine    
          - wasteDisposal    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: ""    
        type: Property    
    firstAvailableFloor:    
      description: 'Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor.'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    fourWheelerSlots:    
      description: 'Four wheeler parking spot availability status in parking site corresponding to this observation.'    
      properties:    
        availableSlotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber.'    
          type: number    
        occupiedSlotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        totalSlotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. The total number of spots offered by the parking site corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    highestFloor:    
      description: 'For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones.'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    id:    
      anyOf: &offstreetparking_-_properties_-_owner_-_items_-_anyof    
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
    images:    
      description: 'A URL containing a photo of this parking site'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/image    
        type: Property    
    layout:    
      description: 'Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3. Enum:''automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other''. See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - automatedParkingGarage    
          - carports    
          - covered    
          - field    
          - garageBoxes    
          - multiLevel    
          - multiStorey    
          - nested    
          - openSpace    
          - rooftop    
          - sheds    
          - singleLevel    
          - surface    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
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
    lowestFloor:    
      description: 'For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number.'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of all the zones.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: Meters    
    maximumParkingDuration:    
      description: 'Maximum allowed stay at site, on a general basis, encoded as a ISO8601 duration or with any other string relevant for parking.  An empty value or when non present indicates an indefinite duration'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    measuresPeriod:    
      description: 'The measures period related to availableSpotNumber and priceRatePerMinute.'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    measuresPeriodUnit:    
      description: 'The measures period unit related to availableSpotNumber and PriceRatePerMinute.'    
      type: string    
      x-ngsi:    
        model: http://schema.org/unitText    
        type: Property    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        cityId:    
          description: 'Property. Model:''https://schema.org/Text''. City ID corresponding to this observation.'    
          type: string    
        cityName:    
          description: 'Property. Model:''https://schema.org/Text''. City name corresponding to this observation'    
          type: string    
        district:    
          description: 'Property. Model:''https://schema.org/Text''. District name corresponding to this observation.'    
          type: string    
        stateName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the state corresponding to this observation.'    
          type: string    
        ulbName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the Urban Local Body corresponding to this observation.'    
          type: string    
        wardId:    
          description: 'Property. Model:''https://schema.org/Text''. Ward ID corresponding to this observation.'    
          type: string    
        wardName:    
          description: 'Property. Model:''https://schema.org/Text''. Ward name corresponding to this observation.'    
          type: string    
        wardNum:    
          description: 'Property. Model:''https://schema.org/Number''. Ward number corresponding to this observation.'    
          type: number    
        zoneId:    
          description: 'Property. Model:''https://schema.org/Text''. Zone ID corresponding to this observation.'    
          type: string    
        zoneName:    
          description: 'Property. Model:''https://schema.org/Text''. Zone name corresponding to this observation.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    occupancy:    
      description: 'Relative value of occupied spots out of the total spots.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    occupancyDetectionType:    
      description: 'Occupancy detection method(s).  Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:''balancing, manual, modelBased, none, singleSpaceDetection''. Or any other application-specific'    
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
    occupancyModified:    
      description: 'Relative value of occupied spots out of the total spots. Allowed values: 0 - 1'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    occupiedSpotNumber:    
      description: 'Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    openingHours:    
      description: 'Opening hours of the parking site.'    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
        type: Property    
    outOfServiceSlotNumber:    
      description: 'The number of bike racks/bike-docking slots or parking slots that are out of order and cannot be used to hire or park a bike in the bike docking station or parking site corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *offstreetparking_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    parkingMode:    
      description: 'Parking mode(s). Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:''echelonParking, parallelParking, perpendicularParking'''    
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
    parkingSiteId:    
      description: 'The unique ID of the parking site or parking lot corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    priceCurrency:    
      description: 'Price currency of price rate per minute'    
      type: string    
      x-ngsi:    
        model: https://schema.org/priceCurrency    
        type: Property    
    priceRatePerMinute:    
      description: 'Price rate per minute.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
    provider:    
      description: 'Parking site service provider'    
      type: object    
      x-ngsi:    
        model: https://schema.org/provider    
        type: Property    
    refParkingAccess:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site''s access point(s).'    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    refParkingGroup:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc.'    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    refParkingSpot:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Individual parking spots belonging to this offStreet parking site.'    
      x-ngsi:    
        type: Relationship    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If the list is empty no permit is needed. Allowed values: The following, defined by the _PermitTypeEnum_ enumeration of DATEX II version 2.3. Enum:''employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit''. Or any other application-specific'    
      items:    
        enum:    
          - employeePermit    
          - fairPermit    
          - governmentPermit    
          - noPermitNeeded    
          - residentPermit    
          - specificIdentifiedVehiclePermit    
          - studentPermit    
          - visitorPermit    
        type: string    
      minItems: 0    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    reservationType:    
      description: 'he following specified by _ReservationTypeEnum_ of DATEX II version 2.3. Enum:''mandatory, notAvailable, optional, partly'''    
      items:    
        enum:    
          - mandatory    
          - notAvailable    
          - optional    
          - partly    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    security:    
      description: 'Security aspects provided by this parking site. Allowed values: The following, some of them, defined by _ParkingSecurityEnum_ of DATEX II version 2.3. Enum:''areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff'' . or any other application-specific'    
      items:    
        enum:    
          - areaSeparatedFromSurroundings    
          - cctv    
          - dog    
          - externalSecurity    
          - fences    
          - floodLight    
          - guard24hours    
          - lighting    
          - patrolled    
          - securityStaff    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
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
    specialLocation:    
      description: 'If the parking site is at a special location (airport, department store, etc.) it conveys what is such special location.  Allowed values: Those defined by _ParkingSpecialLocationEnum_ of [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). Enum:''airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'''    
      items:    
        enum:    
          - airportTerminal    
          - cableCarStation    
          - campground    
          - cinema    
          - coachStation    
          - conventionCentre    
          - exhibitionCentre    
          - ferryTerminal    
          - hotel    
          - market    
          - publicTransportStation    
          - religiousCentre    
          - shoppingCentre    
          - skilift    
          - specificFacility    
          - themePark    
          - trainStation    
          - vehicleOnRailTerminal    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    status:    
      description: 'Status of the parking site. Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3. Enum:''almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable''. Or any other application-specific'    
      items:    
        enum:    
          - almostFull    
          - closed    
          - closedAbnormal    
          - full    
          - fullAtEntrance    
          - open    
          - openingTimesInForce    
          - spacesAvailable    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    totalSpotNumber:    
      description: 'The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    twoWheelerSlots:    
      description: 'Two wheeler parking spot availability status in parking site corresponding to this observation.'    
      properties:    
        availableSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        occupiedSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        totalSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. The total number of spots offered by the parking site corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It has to be OffStreetParking'    
      enum:    
        - OffStreetParking    
      type: string    
      x-ngsi:    
        type: Property    
    unclassifiedSlots:    
      description: 'Unclassified vehicles or other vehicles parking spot availability status in parking site corresponding to this observation.'    
      properties:    
        availableSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        occupiedSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
          type: number    
        totalSpotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. The total number of spots offered by the parking site corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    usageScenario:    
      description: 'Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3. Enum:''automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other''. Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - automaticParkingGuidance    
          - carSharing    
          - dropOffWithValet    
          - dropOffMechanical    
          - dropOff    
          - eventParking    
          - kissAndRide    
          - liftShare    
          - loadingBay    
          - overnightParking    
          - parkAndCycle    
          - parkAndRide    
          - parkAndWalk    
          - restArea    
          - serviceArea    
          - staffGuidesToSpace    
          - truckParking    
          - vehicleLift    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    vehicleEntranceCount:    
      description: 'Aggregated number of vehicle that enter the parking site in a period of time.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    vehicleExitCount:    
      description: 'Aggregated number of vehicle that leave the parking site in a period of time.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/OffStreetParking/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/OffStreetParking/schema.json    
  x-model-tags: IUDX    
  x-version: 0.1.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### OffStreetParking NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un OffStreetParking en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "porto-ParkingLot-23889",  
  "type": "OffStreetParking",  
  "name": "Parque de estacionamento Trindade",  
  "category": [  
    "underground",  
    "public",  
    "feeCharged",  
    "mediumTerm",  
    "barrierAccess"  
  ],  
  "extCategory": [  
    "A"  
  ],  
  "chargeType": [  
    "temporaryPrice"  
  ],  
  "requiredPermit": [],  
  "layout": [  
    "multiLevel"  
  ],  
  "maximumParkingDuration": "PT8H",  
  "location": {  
    "coordinates": [  
      -8.60961198807,  
      41.150691773  
    ],  
    "type": "Point"  
  },  
  "allowedVehicleType": [  
    "car"  
  ],  
  "totalSpotNumber": 414,  
  "availableSpotNumber": 132,  
  "occupiedSpotNumber": 282,  
  "occupancyModified": "2018-09-21T12:00:00Z",  
  "occupancy": 0.68,  
  "address": {  
    "streetAddress": "Rua de Fernandes Tomás",  
    "addressLocality": "Porto",  
    "addressCountry": "Portugal"  
  },  
  "description": "Municipal car park located near the Trindade metro station and the Town Hall",  
  "dateModified": "2018-09-21T12:00:05Z",  
  "vehicleEntranceCount": 28,  
  "vehicleExitCount": 12,  
  "accessModified": "2018-09-21T12:00:00Z",  
  "outOfServiceSlotNumber": 0,  
  "parkingSiteId": "P2",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
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
#### OffStreetParking NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de OffStreetParking en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "porto-ParkingLot-23889",  
  "type": "OffStreetParking",  
  "category": {  
    "type": "array",  
    "value": [  
      "underground",  
      "public",  
      "feeCharged",  
      "mediumTerm",  
      "barrierAccess"  
    ]  
  },  
  "extCategory": {  
    "type": "Text",  
    "value": "A"  
  },  
  "layout": {  
    "type": "array",  
    "value": [  
      "multiLevel"  
    ]  
  },  
  "name": {  
    "type": "Text",  
    "value": "Parque de estacionamento Trindade"  
  },  
  "requiredPermit": {  
    "type": "array",  
    "value": []  
  },  
  "allowedVehicleType": {  
    "type": "array",  
    "value": [  
      "car"  
    ]  
  },  
  "availableSpotNumber": {  
    "type": "Number",  
    "value": 132,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-21T12:00:00Z"  
      }  
    }  
  },  
  "totalSpotNumber": {  
    "type": "Number",  
    "value": 414  
  },  
  "occupiedSpotNumber": {  
    "type": "Number",  
    "value": 282  
  },  
  "occupancyModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  },  
  "occupancy": {  
    "type": "Number",  
    "value": 0.68  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.60961198807,  
        41.150691773  
      ]  
    }  
  },  
  "chargeType": {  
    "type": "array",  
    "value": [  
      "temporaryPrice"  
    ]  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Porto",  
      "addressCountry": "Portugal",  
      "streetAddress": "Rua de Fernandes Tom\u00e1s"  
    }  
  },  
  "maximumParkingDuration": {  
    "type": "Text",  
    "value": "PT8H"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:05Z"  
  },  
  "description": {  
    "value": "Municipal car park located near the Trindade metro station and the Town Hall"  
  },  
  "vehicleEntranceCount": {  
    "type": "Number",  
    "value": 28  
  },  
  "vehicleExitCount": {  
    "type": "Number",  
    "value": 12  
  },  
  "accessModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
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
#### OffStreetParking NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un OffStreetParking en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
    "type": "OffStreetParking",  
    "accessModified": "2018-09-21T12:00:00Z",  
    "address": {  
        "addressCountry": "Portugal",  
        "addressLocality": "Porto",  
        "streetAddress": "Rua de Fernandes Tom\u00e1s",  
        "type": "PostalAddress"  
    },  
    "allowedVehicleType": [  
        "car"  
    ],  
    "availableSpotNumber": 132,  
    "category": [  
        "underground",  
        "public",  
        "feeCharged",  
        "mediumTerm",  
        "barrierAccess"  
    ],  
    "chargeType": [  
        "temporaryPrice"  
    ],  
    "description": "Municipal car park located near the Trindade metro station and the Town Hall",  
    "fourWheelerSlots": {  
        "availableSpotNumber": 25,  
        "totalSpotNumber": 25,  
        "occupiedSpotNumber": 0  
    },  
    "layout": [  
        "multiLevel"  
    ],  
    "location": {  
        "coordinates": [  
            -8.60961198807,  
            41.150691773  
        ],  
        "type": "Point"  
    },  
    "maximumParkingDuration": "PT8H",  
    "modifiedAt": "2018-09-21T12:00:05Z",  
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
    "name": "Parque de estacionamento Trindade",  
    "observationDateTime": "2021-03-11T15:51:02+05:30",  
    "occupancy": 0.68,  
    "occupancyModified": "2018-09-21T12:00:00Z",  
    "occupiedSpotNumber": 282,  
    "outOfServiceSlotNumber": 0,  
    "parkingSiteId": "P2",  
    "requiredPermit": [],  
    "totalSpotNumber": 414,  
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
    "vehicleEntranceCount": 28,  
    "vehicleExitCount": 12,  
    "@context": [  
        "iudx:SmartParking",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### OffStreetParking NGSI-LD normalizado Ejemplo  
Este es un ejemplo de OffStreetParking en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
    "type": "OffStreetParking",  
    "accessModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-09-21T12:00:00Z"  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Porto",  
            "addressCountry": "Portugal",  
            "streetAddress": "Rua de Fernandes Tomas",  
            "type": "PostalAddress"  
        }  
    },  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": [  
            "car"  
        ]  
    },  
    "availableSpotNumber": {  
        "type": "Property",  
        "value": 132,  
        "observedAt": "2018-09-21T12:00:00Z"  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "underground",  
            "public",  
            "feeCharged",  
            "mediumTerm",  
            "barrierAccess"  
        ]  
    },  
    "chargeType": {  
        "type": "Property",  
        "value": [  
            "temporaryPrice"  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "Municipal car park located near the Trindade metro station and the Town Hall"  
    },  
    "extCategory": {  
        "type": "Property",  
        "value": [  
            "A"  
        ]  
    },  
    "fourWheelerSlots": {  
        "type": "Property",  
        "value": {  
            "availableSpotNumber": 25,  
            "totalSpotNumber": 25,  
            "occupiedSpotNumber": 0  
        }  
    },  
    "layout": {  
        "type": "Property",  
        "value": [  
            "multiLevel"  
        ]  
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
    "maximumParkingDuration": {  
        "type": "Property",  
        "value": "PT8H"  
    },  
    "modifiedAt": "2018-09-21T12:00:05Z",  
    "municipalityInfo": {  
        "type": "Property",  
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
    },  
    "name": {  
        "type": "Property",  
        "value": "Parque de estacionamento Trindade"  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.68  
    },  
    "occupancyModified": {  
        "type": "Property",  
        "value": "2018-09-21T12:00:00Z"  
    },  
    "occupiedSpotNumber": {  
        "type": "Property",  
        "value": 282  
    },  
    "parkingSiteID": {  
        "type": "Property",  
        "value": "P2"  
    },  
    "requiredPermit": {  
        "type": "Property",  
        "value": []  
    },  
    "totalSpotNumber": {  
        "type": "Property",  
        "value": 414  
    },  
    "twoWheelerSlots": {  
        "type": "Property",  
        "value": {  
            "availableSpotNumber": 20,  
            "totalSpotNumber": 20,  
            "occupiedSpotNumber": 0  
        }  
    },  
    "unclassifiedSlots": {  
        "type": "Property",  
        "value": {  
            "availableSpotNumber": 0,  
            "totalSpotNumber": 0,  
            "occupiedSpotNumber": 0  
        }  
    },  
    "vehicleEntranceCount": {  
        "type": "Property",  
        "value": 28  
    },  
    "vehicleExitCount": {  
        "type": "Property",  
        "value": 12  
    },  
    "@context": [  
        "iudx:SmartParking",  
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
