<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: OnStreetParking    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Parking/blob/master/OnStreetParking/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **도로에서 직접 접근할 수 있고 차량을 주차할 수 있는 거리의 부지, 광장 구역(계량 여부에 관계없이)**.    
버전: 0.1.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `acceptedPaymentMethod[string]`: 주차 사이트에서 수행한 결제 유형입니다. Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'  - `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `allowedVehicleType[array]`: 허용되는 차량 유형입니다. 이 배열의 첫 번째 요소는 허용되는 주요 차량 유형이어야 합니다. 다음 값은 _VehicleTypeEnum_, [DATEX 2 버전 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)에 정의되어 있습니다. Enum:'농업용 차량, 모든 차량, 굴절식 차량, 자전거, 버스, 승용차, 카라반, 승용차 또는 경차, 승용차 포함 카라반, 승용차 포함 트레일러, 건설 또는 유지보수 차량, 4륜 구동, 하이 사이드 차량, 트럭, 오토바이, 오토바이 포함 사이드카, 모터스쿠터, 유조선, 삼륜차, 트레일러, 트램, 이륜차, 밴, 차량지정촉매변환장치, 차량지정촉매변환장치, 차량지정카라반, 차량지정트레일러, 짝수번호등록번호판, 홀수번호등록번호판, 기타'  - `alternateName[string]`: 이 항목의 대체 이름  - `areBordersMarked[boolean]`: 주차 공간이 구분되어 있는지 여부(빈 선 등으로 구분)를 나타냅니다.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: 장애인, 장기 주차자 등 예약된 공간을 포함하여 전 세계적으로 이용 가능한 공간의 수입니다. 주차 구역 경계가 선으로 명확하게 표시되어 있지 않은 주차 위치에서는 추정하기 어려울 수 있습니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: 주차 공간의 평균 길이  . Model: [https://schema.org/length](https://schema.org/length)- `averageSpotWidth[number]`: 주차 공간의 평균 폭  . Model: [https://schema.org/width](https://schema.org/width)- `category[array]`: 노상 주차장 카테고리. Enum:'blueZone, feeCharged, forDisabled, forElectricCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'  - `chargeType[array]`: 주차장에서 부과하는 요금 유형입니다. Enum:'추가요금, 연간요금, 첫요금, 정액, 무료, 최소, 최대, 월정액, 시즌권, 임시요금, 임시요금, 알 수 없음, 기타'  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `extraSpotNumber[number]`: 사용 가능한 추가 좌석 수, 즉 무료 좌석 수입니다. 추가 공간은 특별한 목적을 위해 예약된 공간으로 일반적으로 허가가 필요합니다. 허가 세부 정보는 주차 그룹 수준(유형 '주차 그룹'의 엔티티)에서 확인할 수 있습니다. 이 값은 특수 주차 조건에 할당된 모든 그룹의 여유 공간을 합산해야 합니다. 허용되는 값: 0을 포함한 양의 정수입니다. 'extraSpotNumber'와 'availableSpotNumber'를 더한 값은 'totalSpotNumber'보다 작거나 같아야 합니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `fourWheelerSlots[object]`: 이 관측에 해당하는 주차장의 사륜차 주차 공간 가용성 상태  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSlotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에서 사용할 수 있는 주차 공간 수입니다. 이 값은 총 스팟 수보다 작거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSlotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에 점유된 주차 공간의 수입니다. 이 값은 총 스팟 수보다 낮거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `totalSlotNumber[number]`: 이 관측에 해당하는 주차 사이트에서 제공하는 총 자리 수입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `id[*]`: 엔티티의 고유 식별자  - `layout[array]`: 주차장 레이아웃의 일반적인 분류  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maximumParkingDuration[date-time]`: ISO8601 기간으로 인코딩된 사이트에서 허용되는 최대 체류 기간입니다. 비어 있는 값은 무기한을 나타냅니다.  - `municipalityInfo[object]`: 이 관측에 해당하는 지자체 정보  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: 이 관측에 해당하는 도시 ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: 이 관측에 해당하는 도시 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: 이 관측에 해당하는 지구 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: 이 관찰에 해당하는 상태의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`: 이 관측에 해당하는 도시 지역 기관의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardId[string]`: 이 관찰에 해당하는 병동 ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardName[string]`: 이 관찰에 해당하는 병동 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `wardNum[number]`: 이 관찰에 해당하는 병동 번호  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: 이 관측에 해당하는 구역 ID  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `zoneName[string]`: 이 관측에 해당하는 구역 이름  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: 이 항목의 이름  - `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancyDetectionType[array]`: 재실 감지 방법. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. 다음은 DATEX II 버전 2.3 _OccupancyDetectionTypeEnum_에서 가져온 것입니다.  - `occupancyModified[date-time]`: 주차장의 점유가 마지막으로 변경된 날짜  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `occupiedSpotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에 점유된 총 주차 공간 수입니다. 이 값은 총 스팟 수보다 낮거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `outOfServiceSlotNumber[number]`: 자전거 거치대/자전거 도킹 슬롯 또는 주차 슬롯이 고장나서 해당 자전거 도킹 스테이션 또는 주차장에서 자전거를 대여하거나 주차하는 데 사용할 수 없는 횟수  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `parkingMode[string]`: 주차 모드. Enum:'echelonParking, parallelParking, perpendicularParking'  - `parkingSiteId[string]`: 이 관측에 해당하는 주차 사이트 또는 주차장의 고유 ID입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `permitActiveHours[object]`: 이 속성을 사용하면 특정 시간이나 요일에만 권한이 필요한 상황을 캡처할 수 있습니다. 이 속성은 구조화된 값으로, 필요한 각 권한마다 하위 속성을 포함해야 하며 권한이 활성화된 시점을 나타냅니다. 권한에 대해 지정된 것이 없으면 권한이 항상 필요하다는 의미입니다. 빈 JSON 객체는 항상 활성 상태임을 의미합니다. 구문은 schema.org를 준수해야 합니다.  - `refParkingGroup[array]`: 이 노상 주차 구역에 속한 주차 그룹(있는 경우)에 대한 참조  - `refParkingSpot[array]`: 노상 주차장에 속한 개별 주차 공간  - `requiredPermit[array]`: 이 속성은 이 사이트에 주차하는 데 필요한 허가증을 캡처합니다. 의미는 주차하려면 이러한 허가증 중 적어도 _하나_가 필요하다는 것입니다. 허가증이 두 개 이상의 항목(및)으로 구성되는 경우 ','로 결합할 수 있습니다. 예를 들어 '거주자 허가증, 장애인 허가증'은 주차를 위해 거주자 허가증과 장애인 허가증이 동시에 필요하다는 것을 나타냅니다. 목록이 비어 있으면 허가증이 필요하지 않습니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `totalSpotNumber[number]`: 이 주차장이 제공하는 총 주차 공간 수입니다. 주차 공간이 선으로 명확하게 표시되어 있지 않은 주차 위치의 경우 이 숫자를 구하기 어려울 수 있습니다. 표준 참조: DATEX 2 버전 2.3 _ParkingRecord_ 클래스의 _parkingNumberOfSpaces_ 속성  . Model: [http://schema.org/Number](http://schema.org/Number)- `twoWheelerSlots[object]`: 이 관측에 해당하는 주차장의 이륜차 주차 공간 가용성 상태  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에서 사용할 수 있는 주차 공간 수입니다. 이 값은 총 스팟 수보다 작거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSpotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에 점유된 주차 공간의 수입니다. 이 값은 총 스팟 수보다 낮거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `totalSpotNumber[number]`: 이 관측에 해당하는 주차 사이트에서 제공하는 총 자리 수입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `type[string]`: 엔티티 유형. OnStreetParking과 같아야 합니다.  - `unclassifiedSlots[object]`: 이 관찰에 해당하는 주차장의 미분류 차량 또는 기타 차량 주차 공간 가용성 상태  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에서 사용할 수 있는 주차 공간 수입니다. 이 값은 총 스팟 수보다 작거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `occupiedSpotNumber[number]`: 이 관측에 해당하는 스마트 주차 사이트에 점유된 주차 공간의 수입니다. 이 값은 총 스팟 수보다 낮거나 같은 양수여야 합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `totalSpotNumber[number]`: 이 관측에 해당하는 주차 사이트에서 제공하는 총 자리 수입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
- `usageScenario[string]`: 주차장에서 수행한 요금 유형입니다. Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
DATEX 2 버전 2.3 용어에서는 _온스트리트파킹_ 유형의 _도시주차장_에 해당합니다. DATEX II 용어에 대한 데이터 사전은 [http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/)에서 확인할 수 있습니다.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
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
## 페이로드 예시    
#### OnStreetParking NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 OnStreetParking의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### OnStreetParking NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 OnStreetParking의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### OnStreetParking NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 OnStreetParking의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### OnStreetParking NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 OnStreetParking의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
