<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=====================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `acceptedPaymentMethod[array]`: 열거형:'ByBankTransferInAdvance, ByInvoice, 현금, CheckInAdvance, COD, 직불, 구글체크아웃, 페이팔, 페이스웜'. 허용되는 결제 수단  . Model: [https://schema.org/acceptedPaymentMethod](https://schema.org/acceptedPaymentMethod)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `aggregateRating[object]`: 이 주차장에 대한 종합 평점  . Model: [https://schema.org/aggregateRating](https://schema.org/aggregateRating)
	- `occupiedSlotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에 점유된 주차 공간의 수입니다. 이 값은 총 스팟 수보다 낮거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `totalSlotNumber[number]`: 이 관측에 해당하는 주차 사이트에서 제공하는 총 자리 수입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `highestFloor[number]`: 여러 층으로 구성된 주차장의 경우 가장 높은 층입니다. 정수입니다. 0은 지상층입니다. 위층은 양수입니다. 낮은 층은 음수입니다.  . Model: [http://schema.org/Number](http://schema.org/Number)
	- `cityName[string]`: 이 관측에 해당하는 도시 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `district[string]`: 이 관측에 해당하는 지구 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `stateName[string]`: 이 관찰에 해당하는 상태의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `ulbName[string]`: 이 관측에 해당하는 도시 지역 기관의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardId[string]`: 이 관찰에 해당하는 병동 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardName[string]`: 이 관찰에 해당하는 병동 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardNum[number]`: 이 관찰에 해당하는 병동 번호  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `zoneId[string]`: 이 관측에 해당하는 구역 ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `zoneName[string]`: 이 관측에 해당하는 구역 이름  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: 이 항목의 이름  
	- `occupiedSpotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에 점유된 주차 공간의 수입니다. 이 값은 총 스팟 수보다 낮거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `totalSpotNumber[number]`: 이 관측에 해당하는 주차 사이트에서 제공하는 총 자리 수입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: 노외주차장이어야 합니다.  
	- `occupiedSpotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에 점유된 주차 공간의 수입니다. 이 값은 총 스팟 수보다 낮거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `totalSpotNumber[number]`: 이 관측에 해당하는 주차 사이트에서 제공하는 총 자리 수입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `usageScenario[array]`: 사용 시나리오. 카테고리` 속성에 대한 자세한 정보를 제공합니다. 허용되는 값: DATEX II 버전 2.3의 열거형 _ParkingUsageScenarioEnum_에 정의된 값입니다. 열거형: '자동주차 안내, 카셰어링, 드롭오프위드발렛, 드롭오프메카니컬, 드롭오프, 이벤트주차, 키스앤라이드, 리프트쉐어, 로딩베이, 오버나이트파킹, 파크앤사이클, 파크앤라이드, 파크앤워크, 휴식공간, 서비스공간, 직원 가이드, 트럭파킹, 차량 리프트, 기타'. 또는 애플리케이션에 유용하고 위에서 다루지 않은 다른 값도 가능합니다.  . Model: [http://schema.org/Text](http://schema.org/Text)
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

OffStreetParking:    
  description: Off street parking    
  properties:    
    acceptedPaymentMethod:    
      description: 'Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm''. Accepted payment method(s)'    
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
    aggregateRating:    
      description: Aggregated rating for this parking site    
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
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableSpotNumber:    
      description: 'The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: The average length of parking spots    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: The average width of parking spots    
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
      description: Parking site contact point    
      type: object    
      x-ngsi:    
        model: https://schema.org/contactPoint    
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
    extCategory:    
      description: External category to complement category    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    extraSpotNumber:    
      description: 'The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity'    
      minimum: 0    
      type: number    
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
      description: 'Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    fourWheelerSlots:    
      description: Four wheeler parking spot availability status in parking site corresponding to this observation    
      properties:    
        availableSlotNumber:    
          description: Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber    
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
    highestFloor:    
      description: 'For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
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
    images:    
      description: A URL containing a photo of this parking site    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/image    
        type: Property    
    layout:    
      description: 'Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3. Enum:''automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other''. See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above'    
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
    lowestFloor:    
      description: 'For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of all the zones'    
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
      description: The measures period related to availableSpotNumber and priceRatePerMinute    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    measuresPeriodUnit:    
      description: The measures period unit related to availableSpotNumber and PriceRatePerMinute    
      type: string    
      x-ngsi:    
        model: http://schema.org/unitText    
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
    occupancy:    
      description: 'Relative value of occupied spots out of the total spots. Allowed values: 0 - 1'    
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
      description: 'Last time the occupancy values were modified. Allowed values: ISO 8601'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    occupiedSpotNumber:    
      description: Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    openingHours:    
      description: Opening hours of the parking site    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
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
      description: The unique ID of the parking site or parking lot corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    priceCurrency:    
      description: Price currency of price rate per minute    
      type: string    
      x-ngsi:    
        model: https://schema.org/priceCurrency    
        type: Property    
    priceRatePerMinute:    
      description: Price rate per minute    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
    provider:    
      description: Parking site service provider    
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
      description: Parking site's access point(s)    
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
      description: 'Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc'    
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
      description: Individual parking spots belonging to this offStreet parking site    
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
      description: 'The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class'    
      minimum: 1    
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
      description: It has to be OffStreetParking    
      enum:    
        - OffStreetParking    
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
      description: 'Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3. Enum:''automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other''. Or any other value useful for the application and not covered above'    
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
      description: Aggregated number of vehicle that enter the parking site in a period of time    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    vehicleExitCount:    
      description: Aggregated number of vehicle that leave the parking site in a period of time    
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
  x-version: 0.1.3    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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
    "type": "array",  
    "value": ["A"]  
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


<details><summary><strong>show/hide example</strong></summary>    


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
    "observationDateTime": "2021-03-11T15:51:02Z",  
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
            "@value": "2021-03-11T15:51:02Z"  
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Parking/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->
<!-- 90-FooterNotes -->
<!-- /90-FooterNotes -->
<!-- 95-Units -->

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
