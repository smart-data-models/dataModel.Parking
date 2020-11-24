Entidad: OffStreetParking  
=========================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Aparcamiento en la calle**  

## Lista de propiedades  

`acceptedPaymentMethod`: Método(s) de pago aceptado(s).  `accessModified`: Sello de tiempo cuando "Cuenta de Entrada de Vehículo" y "Cuenta de Salida de Vehículo" fueron actualizadas. Valores permitidos: ISO8601  `address`: La dirección postal.  `aggregateRating`: Clasificación agregada para este sitio de estacionamiento.  `allowedVehicleType`:  Tipo de vehículo(s) permitido(s). El primer elemento de este  
 la matriz _Debe ser el principal tipo de vehículo permitido. Los números de plaza libre de  
 otros tipos de vehículos permitidos podrían ser reportados bajo el atributo  
 y a través de entidades específicas del tipo "ParkingGroup". Los siguientes valores definidos por _VehicleTypeEnum_,  
 [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)Valores permitidos (`Vehículo agrícola`, `bicicleta`, `autobús`, `coche`, `caravana`, `coche con caravana`, `coche con remolque`,"Construcción o mantenimiento de vehículos", "camión", "ciclomotor", "motocicleta", "motocicleta con carro lateral", "motoneta", "camión cisterna", "remolque", "furgoneta", "cualquier vehículo".)  `alternateName`: Un nombre alternativo para este artículo  `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `availableSpotNumber`: El número de plazas disponibles (_incluyendo_ todos los tipos de vehículos o espacios reservados, como los destinados a personas discapacitadas, aparcamientos de larga duración, etc.). Esto podría ser más difícil de estimar en aquellos lugares de estacionamiento en los que los límites de las plazas no están claramente marcados por líneas. Valores permitidos: Un número entero positivo, incluyendo el 0. Debe ser menor o igual que "totalSpotNumber".  `averageSpotLength`: La longitud media de las plazas de aparcamiento.  `averageSpotWidth`: El ancho promedio de las plazas de aparcamiento.  `category`: Categoría(s) del sitio de estacionamiento. El propósito de este campo es permitir etiquetar, en términos generales, entidades de estacionamiento fuera de la calle. Las particularidades y las descripciones detalladas deben encontrarse bajo los atributos específicos correspondientes. Valores permitidos: - (público, privado, público y privado, estacionamiento disuasivo en la ciudad, estacionamiento en el garaje, estacionamiento en el lote, corto plazo, mediano y largo plazo), "gratis", "con cargo", "con personal", "con guardia", "acceso a la barrera", "acceso a la puerta", "acceso libre", "para carga eléctrica", "sólo residentes", "Sólo con permiso", "para empleados", "para visitantes", "para clientes", "para estudiantes", "para miembros", "para discapacitados", "para residentes", "subterráneo", "subterráneo") - La semántica de los valores "para xxx" es que el estacionamiento ofrece lugares específicos sujetos a esa condición particular. - La semántica de los valores "sólo xxxx" es que el estacionamiento sólo permite aparcar en esa condición particular. - Otras aplicaciones específicas  `chargeType`: Tipo(s) de cargo realizado por el sitio de estacionamiento. Valores permitidos: Algunos de los definidos por el DATEX II versión 2.3 _ ChargeTypeEnum_ enumeración:  
 (`flat`, `minimo`, `máximo`, `aditionalIntervalPrice`, `seasonTicket` `temporaryPrice` `firstIntervalPrice`, `annualPayment`, `monthlyPayment`, `free`, `other`) o cualquier otra aplicación específica  `contactPoint`: Punto de contacto del lugar de estacionamiento.  `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `extCategory`:   `extraSpotNumber`: El número de plazas extra _disponibles_, es decir, gratuitas. Este valor debe agregar las manchas libres de todos los grupos mencionados a continuación: A/ Los reservados para fines especiales y que normalmente requieren un permiso. Los detalles del permiso se encontrarán en el nivel de grupo de aparcamiento (entidad de tipo "ParkingGroup"). B/ Aquellas reservadas para otros tipos de vehículos diferentes al principal tipo de vehículo permitido. C/ Cualquier otro grupo de plazas de aparcamiento que no esté sujeto a las normas de condiciones generales transmitidas por esta entidad.  `facilities`: Valores permitidos: Los siguientes definidos por la enumeración _EquipmentTypeEnum_ del DATEX II versión 2.3: - (baño, ducha, punto de información, internet inalámbrico, escritorio de pago, máquina de pago, máquina de dinero, máquina de venta...)     "fax, máquina o servicio", "copia, máquina o servicio", "depósito seguro", "depósito de equipaje", "teléfono público", "ascensor", "estación de descarga", "agua fresca", "WasteDisposal", "RefuseBin", "IceFreeScaffold", "Playground", "electricChargingStation", "BikeParking", "tollTerminal", "Defibrillator", "FirstAidEquipment" "FireHose" "FireExtinguisher" "FireHydrant") - Cualquier otra aplicación específica.  `firstAvailableFloor`: Número del piso más cercano al suelo que actualmente tiene plazas de aparcamiento disponibles. Valores permitidos: Las historias están numeradas entre -n y n, siendo 0 la planta baja.  `highestFloor`: Para los aparcamientos de varios pisos, el piso más alto. Un número entero. 0 es el nivel de la planta baja. Los pisos superiores son números positivos. Los pisos inferiores son negativos.  `id`:   `image`: Una URL que contiene una foto de este aparcamiento  `layout`: Diseño del aparcamiento. Da más detalles al atributo "categoría". Valores permitidos: Según el _ParkingLayoutEnum_ de la versión 2.3 de DATEX II: (`automatedParkingGarage`, `surface`, `multiStorey`, `singleLevel`, `multiLevel`, `openSpace`, `covered`, `nested`, `field`, `rooftop`, `sheds`, `carports`, `garageBoxes`, `other`). Ver también [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). O cualquier otro valor útil para la aplicación y que no se haya cubierto anteriormente.  `location`:   `lowestFloor`: Para los aparcamientos de varios pisos, el piso más bajo. Valores permitidos: Un número entero.  `maximumAllowedHeight`: Altura máxima permitida para los vehículos. Si hay varias zonas, será la altura mínima de todas las zonas.  `maximumAllowedWidth`: Ancho máximo permitido para los vehículos. Si hay  
    múltiples zonas, será el ancho mínimo de todas las zonas.  `maximumParkingDuration`: Máxima estancia permitida en el sitio, en general, codificada como una duración ISO8601 o con cualquier otra cadena relevante para el estacionamiento.  Un valor vacío o cuando no está presente indica una duración indefinida  `measuresPeriod`: El período de medición se relacionó con el número de puntos disponibles y el precio por minuto.  `measuresPeriodUnit`: La unidad de período de medición se relacionaba con el número de puntos disponibles y la tasa de precios por minuto.  `name`: El nombre de este artículo.  `occupancy`:   `occupancyDetectionType`: Método(s) de detección de ocupación.  Valores permitidos: Los siguientes de DATEX II versión 2.3 _OccupancyDetectionTypeEnum_:`ninguno`, `equilibrio`, `detección de espacio simple`, `basado en modelos`, `manual`, o cualquier otra aplicación específica  `occupancyModified`: Valor relativo de los lugares ocupados del total de lugares. Valores permitidos: 0 - 1  `occupiedSpotNumber`: Número de plazas ocupadas. Valores permitidos: 0 - "totalSpotNumber  `openingHours`: Horario de apertura del aparcamiento.  `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `parkingMode`: Modo(s) de estacionamiento. Valores permitidos: Los definidos por el DATEX II versión 2.3 _ParkingModeEnum_ enumeración: "Parking perpendicular", "ParallelParking", "echelonParking  `priceCurrency`: Moneda del precio tasa por minuto  `priceRatePerMinute`: Precio por minuto.  `provider`:   `refParkingAccess`: Punto(s) de acceso al aparcamiento.  `refParkingGroup`: Relación. Grupo(s) identificado(s) en el lugar de estacionamiento. Un grupo puede corresponder a una zona, una planta completa, un grupo de lugares, etc.  `refParkingSpot`: Relación. Estacionamientos individuales pertenecientes a este sitio de estacionamiento fuera de la calle.  `requiredPermit`: Este atributo capta qué permiso(s) puede ser necesario para aparcar en este sitio. La semántica es que al menos _uno de estos permisos es necesario para aparcar. Cuando un permiso está compuesto por más de un elemento (y) pueden ser combinados con un ",". Por ejemplo, "residentPermit,disabledPermit" indica que para aparcar se necesitan al mismo tiempo un permiso de residente y uno de discapacitado. Si la lista está vacía, no se necesita ningún permiso. Valores permitidos: Lo siguiente, definido por la enumeración _PermitTypeEnum_ de la versión 2.3 de DATEX II.(`permiso de empleado`, `permiso de estudiante`, `permiso de feria`, `permiso de gobierno`, `permiso de residente`, `permiso de vehículo identificado específico`, `permiso de visitante`, `no se necesita ningún permiso`)o cualquier otra aplicación específica  `reservationType`: lo siguiente especificado por _ReservationTypeEnum_ de DATEX II versión 2.3: (`opcional`, `obligatorio`, `no disponible`, `parcialmente`).  `security`: Aspectos de seguridad proporcionados por este aparcamiento. Valores permitidos: Los siguientes, algunos de ellos, definidos por el _ParkingSecurityEnum_ de la versión 2.3 del DATEX II: (`patrullado`, `securityStaff`, `externalSecurity`, `cctv`, `dog`, `guard24hours`, `lighting`, `floodLight`, `fences` `areaSeperatedFromSurroundings`) o cualquier otra aplicación específica  `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `specialLocation`: Si el lugar de estacionamiento está en un lugar especial (aeropuerto, tienda departamental, etc.) transmite lo que es ese lugar especial.  Valores permitidos: Los definidos por _ParkingSpecialLocationEnum_ de [DATEX II versión 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a): (Terminal del aeropuerto, centro de exhibición, centro de compras, estación de tren, campamento, parque temático, terminal de transbordadores, terminal de vehículos sobre rieles), Estación de autobuses, estación de cable, estación de transporte público, mercado, centro religioso, centro de convenciones, cine, ascensor, hotel, otros.)  `status`: Estado del aparcamiento. Valores permitidos: Los siguientes definidos por las siguientes enumeraciones definidas por el DATEX II versión 2.3 :  
 - _ParkingSiteStatusEnum_  
 - El estado de la apertura es un ejemplo de ello.  
 - "abierto", "cerrado", "cerrado anormal", "tiempo de apertura", "tiempo de fuerza", "completo",  
 "Full At Entrance", "espacios disponibles", "casi lleno")  
 - O cualquier otra aplicación específica  `totalSpotNumber`: El número total de plazas que ofrece este aparcamiento.  Este número puede ser difícil de obtener para aquellos aparcamientos en los que las plazas no están claramente marcadas con líneas. Valores permitidos: Cualquier número entero positivo o 0. Referencias normativas: Atributo DATEX 2 versión 2.3 _parkingNumberOfSpaces_ de la clase _ParkingRecord_.  `type`: Tiene que ser OffStreetParking  `usageScenario`: Escenarios de uso. Da más detalles al atributo "categoría". Valores permitidos: Los definidos por la enumeración _ParkingUsageScenarioEnum_ del DATEX II versión 2.3:(estacionamiento de camiones, estacionamiento y paseo, estacionamiento y bicicleta, estacionamiento y paseo, beso y paseo, compartir el turno, compartir el auto, área de descanso, área de servicio, entrega con el valet, mecánica, estacionamiento de eventos), "AutomaticParkingGuidance", "StaffGuidesToSpace", "VehicleLift", "loadingBay", "dropOff", "overnightParking", "other" o cualquier otro valor útil para la aplicación y que no se haya mencionado anteriormente.  `vehicleEntranceCount`: Número total de vehículos que entran en el aparcamiento en un período de tiempo.  `vehicleExitCount`: Número agregado de vehículos que abandonan el lugar de estacionamiento en un período de tiempo.    
Un sitio, fuera de la calle, destinado a aparcar vehículos, gestionado de forma independiente y con puntos de acceso (entradas y salidas) adecuados y claramente marcados. Si es necesario, y a efectos de gestión o para tratar los aparcamientos de varias plazas, puede dividirse en diferentes zonas modeladas por el tipo de entidad [ParkingGroup](../ParkingGroup/README.md) . En la terminología del DATEX 2 versión 2.3 corresponde a un _UrbanParkingSite_ de tipo _offStreetParking_. Se puede encontrar un diccionario de datos para los términos del DATEX II en [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/).  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
OffStreetParking:    
  description: 'Off street parking'    
  properties:    
    acceptedPaymentMethod:    
      description: 'Accepted payment method(s).'    
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
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/acceptedPaymentMethod    
    accessModified:    
      description: 'Timestamp when `vehicleEntranceCount` and `vehicleExitCount` was updated. Allowed values: ISO8601'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    aggregateRating:    
      description: 'Aggregated rating for this parking site.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/aggregateRating    
    allowedVehicleType:    
      description: |2-    
         Vehicle type(s) allowed. The first element of this    
         array _MUST_ be the principal vehicle type allowed. Free spot numbers of    
         other allowed vehicle types might be reported under the attribute    
         `extraSpotNumber` and through specific entities of type _ParkingGroup_. The following values defined by _VehicleTypeEnum_,    
         [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)Allowed values (`agriculturalVehicle`, `bicycle`, `bus`, `car`, `caravan`,`carWithCaravan`, `carWithTrailer`,`constructionOrMaintenanceVehicle`, `lorry`, `moped`, `motorcycle`, `motorcycleWithSideCar`, `motorscooter`, `tanker`, `trailer`, `van`,`anyVehicle`)    
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
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    availableSpotNumber:    
      description: 'The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    averageSpotLength:    
      description: 'The average length of parking spots.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: meters    
    category:    
      description: 'Parking site''s category(ies). The purpose of this field is to allow to tag, generally speaking, off street parking entities. Particularities and detailed descriptions should be found under the corresponding specific attributes. Allowed values: -   (`public`, `private`, `publicPrivate`, `urbanDeterrentParking`, `parkingGarage`, `parkingLot`, `shortTerm`, `mediumTerm`,     `longTerm`, `free`, `feeCharged`, `staffed`, `guarded`, `barrierAccess`, `gateAccess`, `freeAccess`, `forElectricalCharging`, `onlyResidents`, `onlyWithPermit`, `forEmployees`, `forVisitors`, `forCustomers`, `forStudents`,     `forMembers`, `forDisabled`, `forResidents`, `underground`, `ground`) -   The semantics of the `forxxx` values is that the parking offers specific spots subject to that particular condition. -   The semantics of the `onlyxxx`values is that the parking only allows     to park on that particular condition. -   Other application-specific'    
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
      type: Property    
      uniqueItems: true    
    chargeType:    
      description: |-    
        Type(s) of charge performed by the parking site. Allowed values: Some of those defined by the DATEX II version 2.3 _ ChargeTypeEnum_ enumeration:    
         (`flat`, `minimum`, `maximum`, `additionalIntervalPrice`, `seasonTicket` `temporaryPrice` `firstIntervalPrice`, `annualPayment`, `monthlyPayment`, `free`, `other`) or Any other application-specific    
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
      type: Property    
      uniqueItems: true    
    contactPoint:    
      description: 'Parking site contact point.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/contactPoint    
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
    extCategory:    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    extraSpotNumber:    
      description: 'The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    facilities:    
      description: 'Allowed values: The following defined by the _EquipmentTypeEnum_ enumeration of DATEX II version 2.3: -   (`toilet`, `shower`, `informationPoint`, `internetWireless`,     `payDesk`, `paymentMachine`, `cashMachine`, `vendingMachine`,     `faxMachineOrService`, `copyMachineOrService`, `safeDeposit`,     `luggageLocker`, `publicPhone`, `elevator`, `dumpingStation`     `freshWater`, `wasteDisposal`, `refuseBin`, `iceFreeScaffold`,     `playground`, `electricChargingStation`, `bikeParking`,     `tollTerminal`, `defibrillator`, `firstAidEquipment` `fireHose`     `fireExtinguisher` `fireHydrant`) -   Any other application-specific'    
      items:    
        enum:    
          - toilet    
          - shower    
          - informationPoint    
          - internetWireless    
          - payDesk    
          - paymentMachine    
          - cashMachine    
          - vendingMachine    
          - faxMachineOrService    
          - copyMachineOrService    
          - safeDeposit    
          - luggageLocker    
          - publicPhone    
          - elevator    
          - dumpingStation    
          - freshWater    
          - wasteDisposal    
          - refuseBin    
          - iceFreeScaffold    
          - playground    
          - electricChargingStation    
          - bikeParking    
          - tollTerminal    
          - defibrillator    
          - firstAidEquipment    
          - fireHose    
          - fireExtinguisher    
          - fireHydrant    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: ""    
    firstAvailableFloor:    
      description: 'Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    highestFloor:    
      description: 'For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
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
    image:    
      description: 'A URL containing a photo of this parking site'    
      items:    
        format: uri    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/image    
    layout:    
      description: 'Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3: (`automatedParkingGarage`, `surface`, `multiStorey`, `singleLevel`, `multiLevel`, `openSpace`, `covered`, `nested`, `field`, `rooftop`, `sheds`, `carports`, `garageBoxes`, `other`). See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - automatedParkingGarage    
          - surface    
          - multiStorey    
          - singleLevel    
          - multiLevel    
          - openSpace    
          - covered    
          - nested    
          - field    
          - rooftop    
          - sheds    
          - carports    
          - garageBoxes    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
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
    lowestFloor:    
      description: 'For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: meters    
    maximumAllowedWidth:    
      description: |-    
        Maximum allowed width for vehicles. If there are    
            multiple zones, it will be the minimum width of all the zones.    
      exclusiveMinimum: 0    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: Meters    
    maximumParkingDuration:    
      description: 'Maximum allowed stay at site, on a general basis, encoded as a ISO8601 duration or with any other string relevant for parking.  An empty value or when non present indicates an indefinite duration'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    measuresPeriod:    
      description: 'The measures period related to availableSpotNumber and priceRatePerMinute.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    measuresPeriodUnit:    
      description: 'The measures period unit related to availableSpotNumber and PriceRatePerMinute.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/unitText    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancy:    
      maximum: 1    
      minimum: 0    
      type: number    
    occupancyDetectionType:    
      description: 'Occupancy detection method(s).  Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_:`none`, `balancing`, `singleSpaceDetection`, `modelBased`, `manual`, Or any other application-specific'    
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
        model: ""    
    occupancyModified:    
      description: 'Relative value of occupied spots out of the total spots. Allowed values: 0 - 1'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    occupiedSpotNumber:    
      description: 'Number of spots occupied. Allowed values: 0 - `totalSpotNumber`'    
      minimum: 0    
      type: Property    
    openingHours:    
      description: 'Opening hours of the parking site.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/openingHours    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *offstreetparking_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    parkingMode:    
      description: 'Parking mode(s). Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration: `perpendicularParking`, `parallelParking`, `echelonParking`'    
      items:    
        enum:    
          - perpendicularParking    
          - parallelParking    
          - echelonParking    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    priceCurrency:    
      description: 'Price currency of price rate per minute'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/priceCurrency    
    priceRatePerMinute:    
      description: 'Price rate per minute.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
    provider:    
      type: object    
    refParkingAccess:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Parking site''s access point(s).'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    refParkingGroup:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Relationship. Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc.'    
      x-ngsi:    
        model: http://schema.org/Number    
    refParkingSpot:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Relationship. Individual parking spots belonging to this offstreet parking site.'    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a ",". For instance "residentPermit,disabledPermit" stays that both, at the same time, a resident and a disabled permit are needed to park. If the list is empty no permit is needed. Allowed values: The following, defined by the _PermitTypeEnum_ enumeration of DATEX II version 2.3.(`employeePermit`, `studentPermit`, `fairPermit`, `governmentPermit`, `residentPermit`, `specificIdentifiedVehiclePermit`, `visitorPermit`, `noPermitNeeded`)orb any other application-specific'    
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
      type: Property    
      uniqueItems: true    
    reservationType:    
      description: 'he following specified by _ReservationTypeEnum_ of DATEX II version 2.3: (`optional`, `mandatory`, `notAvailable`, `partly`).'    
      items:    
        enum:    
          - optional    
          - mandatory    
          - notAvailable    
          - partly    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    security:    
      description: 'Security aspects provided by this parking site. Allowed values: The following, some of them, defined by _ParkingSecurityEnum_ of DATEX II version 2.3:  (`patrolled`, `securityStaff`, `externalSecurity`, `cctv`, `dog`, `guard24hours`, `lighting`, `floodLight`, `fences`      `areaSeperatedFromSurroundings`) or any other application-specific'    
      items:    
        enum:    
          - patrolled    
          - securityStaff    
          - externalSecurity    
          - cctv    
          - dog    
          - guard24hours    
          - lighting    
          - floodLight    
          - fences    
          - areaSeperatedFromSurroundings    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
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
    specialLocation:    
      description: 'If the parking site is at a special location (airport, department store, etc.) it conveys what is such special location.  Allowed values: Those defined by _ParkingSpecialLocationEnum_ of   [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a): (`airportTerminal`, `exhibitonCentre`, `shoppingCentre`, `specificFacility`, `trainStation`, `campground`, `themePark`, `ferryTerminal`, `vehicleOnRailTerminal`, `coachStation`,   `cableCarStation`, `publicTransportStation`, `market`, `religiousCentre`, `conventionCentre`, `cinema`, `skilift`, `hotel`, `other`)'    
      items:    
        enum:    
          - airportTerminal    
          - exhibitonCentre    
          - shoppingCentre    
          - specificFacility    
          - trainStation    
          - campground    
          - themePark    
          - ferryTerminal    
          - vehicleOnRailTerminal    
          - coachStation    
          - cableCarStation    
          - publicTransportStation    
          - market    
          - religiousCentre    
          - conventionCentre    
          - cinema    
          - skilift    
          - hotel    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    status:    
      description: |-    
        Status of the parking site. Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3 :    
         -   _ParkingSiteStatusEnum_    
         -   _OpeningStatusEnum_    
         -   (`open`, `closed`, `closedAbnormal`,`openingTimesInForce`, `full`,    
         `fullAtEntrance`, `spacesAvailable`, `almostFull`)    
         -   Or any other application-specific    
      items:    
        enum:    
          - open    
          - closed    
          - closedAbnormal    
          - openingTimesInForce    
          - full    
          - fullAtEntrance    
          - spacesAvailable    
          - almostFull    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    totalSpotNumber:    
      description: 'The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    type:    
      description: 'It has to be OffStreetParking'    
      enum:    
        - OffStreetParking    
      type: Property    
    usageScenario:    
      description: 'Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3:(`truckParking`, `parkAndRide`, `parkAndCycle`, `parkAndWalk`, `kissAndRide`, `liftshare`, `carSharing`, `restArea`, `serviceArea`, `dropOffWithValet`, `dropOffMechanical`, `eventParking`, `automaticParkingGuidance`, `staffGuidesToSpace`, `vehicleLift`, `loadingBay`, `dropOff`, `overnightParking`, `other` Or any other value useful for the application and not covered above.'    
      items:    
        enum:    
          - truckParking    
          - parkAndRide    
          - parkAndCycle    
          - parkAndWalk    
          - kissAndRide    
          - liftshare    
          - carSharing    
          - restArea    
          - serviceArea    
          - dropOffWithValet    
          - dropOffMechanical    
          - eventParking    
          - automaticParkingGuidance    
          - staffGuidesToSpace    
          - vehicleLift    
          - loadingBay    
          - dropOff    
          - overnightParking    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    vehicleEntranceCount:    
      description: 'Aggregated number of vehicle that enter the parking site in a period of time.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    vehicleExitCount:    
      description: 'Aggregated number of vehicle that leave the parking site in a period of time.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
Aquí hay un ejemplo de un OffStreetParking en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
  "extCategory": ["A"],  
  "chargeType": ["temporaryPrice"],  
  "requiredPermit": [],  
  "layout": ["multiLevel"],  
  "maximumParkingDuration": "PT8H",  
  "location": {  
    "coordinates": [-8.60961198807, 41.150691773],  
    "type": "Point"  
  },  
  "allowedVehicleType": ["car"],  
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
  "accessModified": "2018-09-21T12:00:00Z"  
}  
```  
Aquí hay un ejemplo de un OffStreetParking en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "porto-ParkingLot-23889",  
  "type": "OffStreetParking",  
  "category": {  
    "value": [  
      "underground",  
      "public",  
      "feeCharged",  
      "mediumTerm",  
      "barrierAccess"  
    ]  
  },  
  "extCategory": ["A"],  
  "layout": {  
    "value": ["multiLevel"]  
  },  
  "name": {  
    "value": "Parque de estacionamento Trindade"  
  },  
  "requiredPermit": {  
    "value": []  
  },  
  "allowedVehicleType": {  
    "value": ["car"]  
  },  
  "availableSpotNumber": {  
    "value": 132,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-21T12:00:00Z"  
      }  
    }  
  },  
  "totalSpotNumber": {  
    "value": 414  
  },  
  "occupiedSpotNumber": {  
    "type": "number",  
    "value": 282  
  },  
  "occupancyModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  },  
  "occupancy": {  
    "type": "number",  
    "value": 0.68  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-8.60961198807, 41.150691773]  
    }  
  },  
  "chargeType": {  
    "value": ["temporaryPrice"]  
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
    "type": "number",  
    "value": 28  
  },  
  "vehicleExitCount": {  
    "type": "number",  
    "value": 12  
  },  
  "accessModified": {  
    "type": "DateTime",  
    "value": "2018-09-21T12:00:00Z"  
  }  
}  
```  
Aquí hay un ejemplo de un OffStreetParking en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "Portugal",  
             "addressLocality": "Porto",  
             "streetAddress": "Rua de Fernandes TomÃ¡s",  
             "type": "PostalAddress"},  
 "allowedVehicleType": ["car"],  
 "availableSpotNumber": 132,  
 "occupiedSpotNumber": 282,  
 "occupancyModified": "2018-09-21T12:00:00Z",  
 "occupancy": 0.68,  
 "category": ["underground",  
              "public",  
              "feeCharged",  
              "mediumTerm",  
              "barrierAccess"],  
 "chargeType": ["temporaryPrice"],  
 "description": "Municipal car park located near the Trindade metro station and the Town Hall",  
 "extCategory": ["A"],  
 "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
 "layout": ["multiLevel"],  
 "location": {"coordinates": [-8.60961198807, 41.150691773], "type": "Point"},  
 "maximumParkingDuration": "PT8H",  
 "modifiedAt": "2018-09-21T12:00:05Z",  
 "name": "Parque de estacionamento Trindade",  
 "requiredPermit": [],  
 "totalSpotNumber": 414,  
 "vehicleEntranceCount": 28,  
 "vehicleExitCount": 12,  
 "accessModified": "2018-09-21T12:00:00Z",  
 "type": "OffStreetParking"}  
```  
Aquí hay un ejemplo de un OffStreetParking en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
    "type": "OffStreetParking",  
    "modifiedAt": "2018-09-21T12:00:05Z",  
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
    "extCategory": {  
        "type": "Property",  
        "value": ["A"]  
    },  
    "layout": {  
        "type": "Property",  
        "value": [  
            "multiLevel"  
        ]  
    },  
    "name": {  
        "type": "Property",  
        "value": "Parque de estacionamento Trindade"  
    },  
    "requiredPermit": {  
        "type": "Property",  
        "value": []  
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
    "totalSpotNumber": {  
        "type": "Property",  
        "value": 414  
    },  
    "occupiedSpotNumber": {  
        "type": "Property",  
        "value": 282  
    },  
    "occupancyModified": {  
        "type": "Property",  
        "value": "2018-09-21T12:00:00Z"  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.68  
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
    "chargeType": {  
        "type": "Property",  
        "value": [  
            "temporaryPrice"  
        ]  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Porto",  
            "addressCountry": "Portugal",  
            "streetAddress": "Rua de Fernandes TomÃ¡s",  
            "type": "PostalAddress"  
        }  
    },  
    "maximumParkingDuration": {  
        "type": "Property",  
        "value": "PT8H"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Municipal car park located near the Trindade metro station and the Town Hall"  
    },  
    "vehicleEntranceCount": {  
        "type": "Property",  
        "value": 28  
    },  
      "vehicleExitCount": {  
        "type": "Property",  
        "value": 12  
    },  
      "accessModified": {  
        "type": "Property",  
        "value": "2018-09-21T12:00:00Z"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
