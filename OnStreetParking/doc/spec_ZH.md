<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。街头停车服务  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Parking/blob/master/OnStreetParking/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**一个场地，开放空间区，在街道上，（无论是否收费），从道路上直接进入，用于停放车辆。  
版本：0.1.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `acceptedPaymentMethod[string]`: 泊车场的收费类型。Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm' 。  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `allowedVehicleType[array]`: 允许的车辆类型。这个数组的第一个元素_必须是允许的主要车辆类型。以下值由_VehicleTypeEnum_定义，[DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html).枚举。农业车辆，任何车辆，铰接式车辆，自行车，公共汽车，汽车，大篷车，汽车或轻型车辆，有大篷车的汽车，有拖车的汽车，建筑或维修车辆，四轮驱动，高边车辆，货车，轻便摩托车，摩托车，有边车的摩托车，摩托。油罐车、三轮车、拖车、有轨电车、两轮车、面包车、带催化转换器的车辆、不带催化转换器的车辆、带房车的车辆、带拖车的车辆、有编号的登记牌照、有编号的登记牌照、其他  - `alternateName[string]`: 这个项目的一个替代名称  - `areBordersMarked[boolean]`: 表示停车位是否被划定（用空白线或类似的方式）。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[integer]`: 全球范围内可用的车位数量，包括保留的车位，如残疾人、长期停车者等。在那些停车位边界没有明确标线的地方，这可能更难估计。  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: 停车位的平均长度  . Model: [https://schema.org/length](https://schema.org/length)- `averageSpotWidth[number]`: 停车位的平均宽度  . Model: [https://schema.org/width](https://schema.org/width)- `category[array]`: 街头停车类别。Enum:'blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop' 。  - `chargeType[array]`: 停车点的收费类型。Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other' 。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `extraSpotNumber[integer]`: 可用的额外位置的数量，即免费。额外的位置是为特殊目的保留的，通常需要许可证。许可证的详细信息将在停车组层面上找到（"停车组 "类型的实体）。这个值必须将所有专门用于特殊停车条件的组的免费停车位汇总起来。允许的值。一个正整数，包括0。`额外停车位数量`加上`可用停车位数量`必须低于或等于`总停车位数量`。  . Model: [http://schema.org/Number](http://schema.org/Number)- `fourWheelerSlots[object]`: 与此观察相对应的是停车场内四轮车停车位的可用性状况。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `layout[array]`: 停车场布局的通用分类  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `maximumParkingDuration[string]`: 允许在现场停留的最长时间，以ISO8601的期限编码。空值表示不确定的期限。  - `municipalityInfo[object]`: 与此观察相对应的市镇信息。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 这个项目的名称。  - `observationDateTime[string]`: 最后报告的观察时间。  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancyDetectionType[array]`: 占用检测方法。Enum:'balancing, manual, modelBased, none, singleSpaceDetection'。以下是DATEX II 2.3版的_OccupancyDetectionTypeEnum_。  - `occupancyModified[string]`: 最后一次修改停车位占用率的日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `occupiedSpotNumber[number]`: 与该观察值相对应的智能停车场中被占用的总停车位的数量。这必须是一个低于或等于totalSpotNumber的正数。  . Model: [https://schema.org/Number](https://schema.org/Number)- `outOfServiceSlotNumber[number]`: 在该观察点对应的自行车停靠站或停车点中，自行车架/自行车停靠槽或停车槽失灵，不能用于租用或停放自行车的数量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `parkingMode[string]`: 泊车模式（s）。Enum:'echelonParking, parallelParking, perpendicularParking'（梯形停车，平行停车，垂直停车）。  - `parkingSiteId[string]`: 与该观察结果相对应的停车地点或停车场的唯一ID。  . Model: [https://schema.org/Text](https://schema.org/Text)- `permitActiveHours[object]`: 这个属性可以捕捉到只有在一周的特定时间或日子里需要许可证的情况。它是一个结构化的值，必须包含每一个所需的许可证的子属性，表明该许可证何时有效。如果没有为许可证指定任何东西，这将意味着始终需要一个许可证。一个空的JSON对象意味着总是活动的。语法必须符合schema.org的规定。  - `refParkingGroup[array]`: 指属于该路边停车区的停车组（如有）。  - `refParkingSpot[array]`: 属于这个路边停车点的个人停车位。  - `requiredPermit[array]`: 这个属性反映了在这个地方停车可能需要什么许可证。语义是，至少需要这些许可证中的一个才能停车。当一个许可证由一个以上的项目（和）组成时，它们可以用','来组合。例如，'residentPermit,disabledPermit'表示同时需要一个居民和一个残疾人许可证来停车。如果列表为空，则不需要许可证。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `totalSpotNumber[integer]`: 该停车场提供的停车位总数。对于那些没有明确标线的停车点，这个数字可能难以获得。规范性引用。DATEX 2版本2.3的_ParkingRecord_类的_ParkingNumberOfSpaces_属性。  . Model: [http://schema.org/Number](http://schema.org/Number)- `twoWheelerSlots[object]`: 与此观察相对应的是停车场内两轮车停车位的可用性状况。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: 实体类型。它必须等于OnStreetParking。  - `unclassifiedSlots[object]`: 未分类的车辆或其他车辆在停车点的可用状态与此观察相对应。  . Model: [https://schema.org/Text](https://schema.org/Text)- `usageScenario[string]`: 停车点的收费类型。Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
在DATEX 2 2.3版本的术语中，它对应于类型为_onStreetParking_的_UrbanParkingSite_。DATEX II术语的数据字典可以在[http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/)找到。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areBordersMarked:    
      description: 'Denotes whether parking spots are delimited (with blank lines or similar) or not'    
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
      description: 'The number of spots available globally, including reserved spaces, such as those for disabled people, long term parkers and so on. This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: 'The average length of parking spots'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
    averageSpotWidth:    
      description: 'The average width of parking spots'    
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
    extraSpotNumber:    
      description: 'The number of extra spots available, i.e. free. Extra    spots are those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). This value must aggregate free spots from all groups devoted to special parking conditions. Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or equal to `totalSpotNumber'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    fourWheelerSlots:    
      description: 'Four wheeler parking spot availability status in parking site corresponding to this observation.'    
      properties:    
        availableSlotNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber.'    
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
      x-ngsi:    
        type: Property    
    layout:    
      description: 'Generic classification of the layout of the parking'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        type: Geoproperty    
    maximumParkingDuration:    
      description: 'Maximum allowed stay at site encoded as a ISO8601 duration. An empty value indicates an indefinite duration.'    
      format: date-time    
      type: string    
      x-ngsi:    
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
      description: 'Date last time the occupancy of the parking has being modified'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    occupiedSpotNumber:    
      description: 'Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        anyOf: *onstreetparking_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      description: 'The unique ID of the parking site or parking lot corresponding to this observation.'    
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
      description: 'Reference to the parking group(s) (if any) belonging to this onstreet parking zone.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    refParkingSpot:    
      description: 'Individual parking spots belonging to this on street parking site.'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    requiredPermit:    
      description: 'This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed.'    
      items:    
        type: string    
      type: array    
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
      description: 'The total number of spots offered by this parking site. This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 0    
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
      description: 'Entity type. It must be equal to OnStreetParking'    
      enum:    
        - OnStreetParking    
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
## ＃＃＃＃有效载荷的例子  
#### OnStreetParking NGSI-v2 关键值示例  
这里是一个以JSON-LD格式作为key-values的OnStreetParking的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### OnStreetParking NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的OnStreetParking的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "santander:daoiz_velarde_1_5",  
  "type": "OnStreetParking",  
  "category": {  
    "type": "array",  
    "value": [  
      "blueZone",  
      "shortTerm",  
      "forDisabled"  
    ]  
  },  
  "permitActiveHours": {  
    "type": "array",  
    "value": {  
      "blueZonePermit": "Mo, Tu, We, Th, Fr, Sa 09:00-20:00"  
    }  
  },  
  "requiredPermit": {  
    "type": "array",  
    "value": [  
      "blueZonePermit",  
      "disabledPermit"  
    ]  
  },  
  "allowedVehicleType": {  
    "type": "Text",  
    "value": [  
      "car"  
    ]  
  },  
  "chargeType": {  
    "type": "array",  
    "value": [  
      "temporaryFee"  
    ]  
  },  
  "refParkingGroup": {  
    "type": "Relationship",  
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
#### OnStreetParking NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的OnStreetParking的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
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
#### OnStreetParking NGSI-LD规范化示例  
这里是一个以JSON-LD格式规范化的OnStreetParking的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
        "type": "Geoproperty",  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
