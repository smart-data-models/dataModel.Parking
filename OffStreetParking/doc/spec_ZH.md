<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：街外停车场  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Parking/blob/master/OffStreetParking/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**路边停车位**  
版本：0.1.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `acceptedPaymentMethod[array]`: 属性。模型:'https://schema.org/acceptedPaymentMethod'。Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm' 。接受的付款方式。  . Model: [https://schema.org/acceptedPaymentMethod](https://schema.org/acceptedPaymentMethod)- `accessModified[string]`: 属性。模型:'https://schema.org/DateTime'。`vehicleEntranceCount'和`vehicleExitCount'被更新的时间戳。允许的值：ISO8601  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `aggregateRating[object]`: 属性。模型:'https://schema.org/aggregateRating'。这个停车点的综合评分。  . Model: [https://schema.org/aggregateRating](https://schema.org/aggregateRating)- `allowedVehicleType[array]`: 属性。模型:'http://schema.org/Text'。  允许的车辆类型。这个数组的第一个元素_必须是允许的主要车辆类型。其他允许的车辆类型的空位号码可以在属性 "extraSpotNumber "下和通过_ParkingGroup_类型的特定实体报告。以下数值由_VehicleTypeEnum_定义，[DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)。枚举:'农业车辆，任何车辆，自行车，公共汽车，汽车，大篷车，有大篷车的汽车，有拖车的汽车，建筑或维修车辆，货车，轻便摩托车，摩托车，有侧车的摩托车，摩托车，油罐车，拖车，货车'  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: 属性。模型:'http://schema.org/Number'。可用车位的数量（包括所有车辆类型或保留车位，如残疾人、长期停车者等）。在那些停车位边界没有明确标线的地方，这可能更难估计。允许的值：一个正整数，包括0。它必须低于或等于`总车位数`。  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: 属性。模型:'http://schema.org/length'。单位:'米'。停车位的平均长度。  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: 属性。模型:'http://schema.org/width'。单位:'米'。停车位的平均宽度。  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: 财产。停车地点的类别。这个字段的目的是允许标记，一般来说，路边停车实体。  - `chargeType[array]`: 财产。泊车场的收费类型。允许的值：DATEX II 2.3版_ChargeTypeEnum_枚举所定义的一些数值。枚举："附加间隔价格、年费、首次间隔价格、统一、免费、最低、最高、月费、其他、季节票、临时价格"。或任何其他特定的应用  - `contactPoint[object]`: 属性。模型:'https://schema.org/contactPoint'。停车地点联系点。  . Model: [https://schema.org/contactPoint](https://schema.org/contactPoint)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `extCategory[array]`: 财产。外部类别的补充类别。  - `extraSpotNumber[number]`: 属性。模型:'http://schema.org/Number'。可用的额外位置的数量，即免费的。这个值必须是下面提到的所有组别中免费位置的总和：A/那些为特殊目的保留的，通常需要许可证。许可证的详细信息将在停车组层面上找到（实体类型为 "停车组"）。B/ 那些为其他车辆类型保留的停车位，与主要允许的车辆类型不同。C/ 任何其他不受该实体所传达的一般条件规则约束的停车位组。  . Model: [http://schema.org/Number](http://schema.org/Number)- `facilities[array]`: 属性。模型:''。允许的值：以下是DATEX II 2.3版的_EquipmentTypeEnum_枚举所定义的。枚举：自行车停车场, 现金机, 复印机或服务, 除颤器, 倾倒站, 电动充电站, 电梯, 传真机或服务, 消防水管, 灭火器, 消防栓, 急救设备, 淡水、无冰脚手架、信息点、无线网络、行李柜、支付台、支付机、游乐场、公共电话、垃圾桶、保险箱、淋浴、厕所、收费终端、自动售货机、废物处理' 。任何其他特定的应用  . Model: []()- `firstAvailableFloor[number]`: 属性。模型:'http://schema.org/Number'。最接近地面的楼层的编号，目前有可用的停车位。允许的值：层数在-n和n之间，为0底层。  . Model: [http://schema.org/Number](http://schema.org/Number)- `fourWheelerSlots[object]`: 属性。模型:'https://schema.org/Text.与此观察相对应的停车场的四轮车停车位可用状态。  . Model: [https://schema.org/Text](https://schema.org/Text)- `highestFloor[number]`: 属性。模型:'http://schema.org/Number'。对于有多个楼层的停车场，最高楼层。一个整数。0是地面层。高层为正数。较低的楼层是负数。  . Model: [http://schema.org/Number](http://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `images[array]`: 属性。模型:'https://schema.org/image'。一个包含该停车场照片的URL  . Model: [https://schema.org/image](https://schema.org/image)- `layout[array]`: 属性。模型:'http://schema.org/Text'。停车布局。给予`类别'属性更多的细节。允许的值：根据DATEX II 2.3版本的_ParkingLayoutEnum_。Enum:'automaticParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other' 。另见[OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking)。或任何其他对应用有用且未涵盖的值。  . Model: [http://schema.org/Text](http://schema.org/Text)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `lowestFloor[number]`: 属性。模型:'http://schema.org/Number'。对于有多个楼层的停车场，最低楼层。允许的值：一个整数。  . Model: [http://schema.org/Number](http://schema.org/Number)- `maximumAllowedHeight[number]`: 属性。模型:'http://schema.org/heigth'。单位:'米'。车辆的最大允许高度。如果有多个区域，它将是所有区域的最小高度。  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: 属性。模型:'http://schema.org/width'。单位:'米'。允许车辆的最大宽度。如果有多个区域，它将是所有区域的最小宽度。  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[string]`: 属性。模型:'http://schema.org/Text'。允许的最大停留时间，在一般的基础上，编码为ISO8601期限或任何其他与停车有关的字符串。  一个空值或不存在时表示一个不确定的期限。  . Model: [http://schema.org/Text](http://schema.org/Text)- `measuresPeriod[number]`: 属性。模型:'http://schema.org/Number'。与availableSpotNumber和priceRatePerMinute有关的措施期。  . Model: [http://schema.org/Number](http://schema.org/Number)- `measuresPeriodUnit[string]`: 属性。模型:'http://schema.org/unitText'。与availableSpotNumber和PriceRatePerMinute有关的措施期单位。  . Model: [http://schema.org/unitText](http://schema.org/unitText)- `municipalityInfo[object]`: 属性。模型:'https://schema.org/Text。与此观察相对应的市镇信息。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 这个项目的名称。  - `observationDateTime[string]`: 属性。模型:'https://schema.org/Text'。最后报告的观察时间。  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancy[number]`: 属性。模型:'http://schema.org/Number'。占用位置在总位置中的相对值。允许的值：0 - 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `occupancyDetectionType[array]`: 属性。模型:'http://schema.org/Text'。占用检测方法。  允许的值：以下是DATEX II 2.3版的_OccupancyDetectionTypeEnum_。枚举：'平衡、手动、基于模型、无、单一空间检测'。或任何其他特定的应用  . Model: [http://schema.org/Text](http://schema.org/Text)- `occupancyModified[string]`: 属性。模型:'http://schema.org/DateTime'。上次修改占用值的时间。允许的值：ISO 8601  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `occupiedSpotNumber[number]`: 属性。模型:'http://schema.org/Number'。与该观察值相对应的智能停车场中所占用的总停车位的数量。这必须是一个低于或等于totalSpotNumber的正数。  . Model: [http://schema.org/Number](http://schema.org/Number)- `openingHours[string]`: 属性。模型:'http://schema.org/openingHours'。停车地点的开放时间。  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `outOfServiceSlotNumber[number]`: 属性。模型:'https://schema.org/Number'。在该观察点对应的自行车停靠站或停车点中，自行车架/自行车停靠槽或停车槽失灵，不能用于租用或停放自行车的数量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `parkingMode[array]`: 属性。模式:'http://schema.org/Text'。泊车模式(s)。允许的值：那些由DATEX II 2.3版_ParkingModeEnum_枚举定义的值。枚举：'梯形停车，平行停车，垂直停车'。  . Model: [http://schema.org/Text](http://schema.org/Text)- `parkingSiteId[string]`: 属性。模型:'https://schema.org/Text'。与该观察值相对应的停车点或停车场的唯一ID。  . Model: [https://schema.org/Text](https://schema.org/Text)- `priceCurrency[string]`: 属性。模型:'https://schema.org/priceCurrency'。每分钟价格率的价格货币  . Model: [https://schema.org/priceCurrency](https://schema.org/priceCurrency)- `priceRatePerMinute[number]`: 财产。模型：'https://schema.org/Number'。每分钟的价格率。  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `provider[object]`: 财产。停车位服务提供者。模型:'https://schema.org/provider'  . Model: [https://schema.org/provider](https://schema.org/provider)- `refParkingAccess[*]`: 关系。模型:'http://schema.org/URL'。停车地点的接入点。  . Model: [http://schema.org/URL](http://schema.org/URL)- `refParkingGroup[*]`: 关系。模型:'http://schema.org/URL'。停车地点确定的组。一个组可以对应一个区域、一个完整的楼层、一组停车位，等等。  . Model: [http://schema.org/URL](http://schema.org/URL)- `refParkingSpot[*]`: 关系。属于该街外停车场的个人停车位。  - `requiredPermit[array]`: 属性。这个属性反映了在这个地方停车可能需要什么许可证。语义是，至少需要这些许可证中的一个才能停车。当一个许可证由一个以上的项目（和）组成时，它们可以用','来组合。例如，"居民许可证，残疾人许可证 "表示同时需要居民许可证和残疾人许可证来停车。如果列表中是空的，则不需要许可证。允许的值：以下是由DATEX II 2.3版的_PermitTypeEnum_枚举定义的。枚举：'employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit' 。或任何其他特定的应用  - `reservationType[array]`: 属性。模型:'http://schema.org/Text'。以下是DATEX II 2.3版的_ReservationTypeEnum_指定的。Enum:'mandatory, notAvailable, optional, partly'（强制性的，不可用的，可选的）。  . Model: [http://schema.org/Text](http://schema.org/Text)- `security[array]`: 属性。模型:'http://schema.org/Text'。该停车场所提供的安全方面。允许的值：以下是DATEX II 2.3版的_ParkingSecurityEnum_所定义的，其中一些。Enum:'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' .或任何其他特定的应用。  . Model: [http://schema.org/Text](http://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `specialLocation[array]`: 属性。模型：'http://schema.org/Text'。如果停车地点在一个特殊的位置（机场、百货公司等），它传达了什么是这种特殊的位置。  允许的值：那些由[DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a)的_ParkingSpecialLocationEnum_定义的值。Enum:'机场终点站, 电缆车站, 露营地, 电影院, 旅游车站, 会议中心, 展览中心, 轮渡终点站, 酒店, 市场, 公共交通站, 宗教中心, 购物中心, 滑雪场, 特定设施, 主题公园, 火车站, 铁路终点站上的车辆, 其他'。  . Model: [http://schema.org/Text](http://schema.org/Text)- `status[array]`: 属性。模型:'http://schema.org/Text'。停车地点的状态。允许的值：以下由DATEX II 2.3版定义的枚举。Enum:'almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable'。或任何其他特定的应用  . Model: [http://schema.org/Text](http://schema.org/Text)- `totalSpotNumber[number]`: 属性。模型:'http://schema.org/Number'。该停车场提供的停车位总数。  对于那些没有明确标线的停车点，这个数字可能难以获得。允许的值：任何正整数或0。 规范性引用：DATEX 2版本2.3的_ParkingRecord_类的_ParkingNumberOfSpaces_属性。  . Model: [http://schema.org/Number](http://schema.org/Number)- `twoWheelerSlots[object]`: 属性。模型:'https://schema.org/Text.与此观察相对应的停车场的两轮车停车位可用状态。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: 财产。必须是路边停车位  - `unclassifiedSlots[object]`: 属性。模型:'https://schema.org/Text。与该观察值相对应的停车场中未分类的车辆或其他车辆的停车位可用性状态。  . Model: [https://schema.org/Text](https://schema.org/Text)- `usageScenario[array]`: 属性。模型:'http://schema.org/Text'。使用场景(s)。给予`category'属性更多的细节。允许的值：那些由DATEX II 2.3版的_ParkingUsageScenarioEnum_枚举定义的值。枚举：'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other' 。或任何其他对应用有用且未涵盖在上面的值。  . Model: [http://schema.org/Text](http://schema.org/Text)- `vehicleEntranceCount[number]`: 属性。模型:'http://schema.org/Number'。在一段时期内进入停车场的车辆总数。  . Model: [http://schema.org/Number](http://schema.org/Number)- `vehicleExitCount[number]`: 属性。模型:'http://schema.org/Number'。在一段时期内离开停车场的车辆总数。  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
一个用于停放车辆、独立管理并有适当和明确标记的入口（入口和出口）的非街道场地。如果有必要，并且为了管理目的或处理多地点的停车场，它可以被划分为不同的区域，由实体类型[ParkingGroup]（.../ParkingGroup/README.md）建模。在DATEX 2 2.3版本的术语中，它对应于类型为_offStreetParking_的_UrbanParkingSite_。关于DATEX II术语的数据字典可以在[http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/)找到。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
OffStreetParking:    
  description: Off street parking    
  properties:    
    acceptedPaymentMethod:    
      description: 'Property. Model:''https://schema.org/acceptedPaymentMethod''. Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm''. Accepted payment method(s).'    
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
      description: 'Property. Model:''https://schema.org/DateTime''. Timestamp when `vehicleEntranceCount` and `vehicleExitCount` was updated. Allowed values: ISO8601'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    aggregateRating:    
      description: 'Property. Model:''https://schema.org/aggregateRating''. Aggregated rating for this parking site.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/aggregateRating    
        type: Property    
    allowedVehicleType:    
      description: 'Property. Model:''http://schema.org/Text''.  Vehicle type(s) allowed. The first element of this array _MUST_ be the principal vehicle type allowed. Free spot numbers of other allowed vehicle types might be reported under the attribute `extraSpotNumber` and through specific entities of type _ParkingGroup_. The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum:''agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'''    
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
      description: 'Property. Model:''http://schema.org/Number''. The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    averageSpotLength:    
      description: 'Property. Model:''http://schema.org/length''. Units:''meters''. The average length of parking spots.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: 'Property. Model:''http://schema.org/width''. Units:''meters''. The average width of parking spots.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: meters    
    category:    
      description: 'Property. Parking site''s category(ies). The purpose of this field is to allow to tag, generally speaking, off street parking entities'    
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
      description: 'Property. Type(s) of charge performed by the parking site. Allowed values: Some of those defined by the DATEX II version 2.3 _ ChargeTypeEnum_ enumeration. Enum:''additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice''. Or any other application-specific'    
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
      description: 'Property. Model:''https://schema.org/contactPoint''. Parking site contact point.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/contactPoint    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
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
      description: Property. External category to complement category.    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    extraSpotNumber:    
      description: 'Property. Model:''http://schema.org/Number''. The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    facilities:    
      description: 'Property. Model:''''. Allowed values: The following defined by the _EquipmentTypeEnum_ enumeration of DATEX II version 2.3. Enum:''bikeParking, cashMachine, copyMachineOrService, defibrillator, dumpingStation, electricChargingStation, elevator, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, iceFreeScaffold, informationPoint, internetWireless, luggageLocker, payDesk, paymentMachine, playground, publicPhone, refuseBin, safeDeposit, shower, toilet, tollTerminal, vendingMachine, wasteDisposal'' . Any other application-specific'    
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
      description: 'Property. Model:''http://schema.org/Number''. Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor.'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    fourWheelerSlots:    
      description: 'Property. Model:''https://schema.org/Text. Four wheeler parking spot availability status in parking site corresponding to this observation.'    
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
      description: 'Property. Model:''http://schema.org/Number''. For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones.'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    id:    
      anyOf: &offstreetparking_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    images:    
      description: 'Property. Model:''https://schema.org/image''. A URL containing a photo of this parking site'    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/image    
        type: Property    
    layout:    
      description: 'Property. Model:''http://schema.org/Text''. Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3. Enum:''automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other''. See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above.'    
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
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    lowestFloor:    
      description: 'Property. Model:''http://schema.org/Number''. For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number.'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    maximumAllowedHeight:    
      description: 'Property. Model:''http://schema.org/heigth''. Units:''meters''. Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: 'Property. Model:''http://schema.org/width''. Units:''Meters''. Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of all the zones.'    
      exclusiveMinimum: true    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/width    
        type: Property    
        units: Meters    
    maximumParkingDuration:    
      description: 'Property. Model:''http://schema.org/Text''. Maximum allowed stay at site, on a general basis, encoded as a ISO8601 duration or with any other string relevant for parking.  An empty value or when non present indicates an indefinite duration'    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    measuresPeriod:    
      description: 'Property. Model:''http://schema.org/Number''. The measures period related to availableSpotNumber and priceRatePerMinute.'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    measuresPeriodUnit:    
      description: 'Property. Model:''http://schema.org/unitText''. The measures period unit related to availableSpotNumber and PriceRatePerMinute.'    
      type: string    
      x-ngsi:    
        model: http://schema.org/unitText    
        type: Property    
    municipalityInfo:    
      description: 'Property. Model:''https://schema.org/Text. Municipality information corresponding to this observation.'    
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
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Property. Model:''https://schema.org/Text''. Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    occupancy:    
      description: 'Property. Model:''http://schema.org/Number''. Relative value of occupied spots out of the total spots. Allowed values: 0 - 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    occupancyDetectionType:    
      description: 'Property. Model:''http://schema.org/Text''. Occupancy detection method(s).  Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:''balancing, manual, modelBased, none, singleSpaceDetection''. Or any other application-specific'    
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
      description: 'Property. Model:''http://schema.org/DateTime''. Last time the occupancy values were modified. Allowed values: ISO 8601'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    occupiedSpotNumber:    
      description: 'Property. Model:''http://schema.org/Number''. Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    openingHours:    
      description: 'Property. Model:''http://schema.org/openingHours''. Opening hours of the parking site.'    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
        type: Property    
    outOfServiceSlotNumber:    
      description: 'Property. Model:''https://schema.org/Number''. The number of bike racks/bike-docking slots or parking slots that are out of order and cannot be used to hire or park a bike in the bike docking station or parking site corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *offstreetparking_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    parkingMode:    
      description: 'Property. Model:''http://schema.org/Text''. Parking mode(s). Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:''echelonParking, parallelParking, perpendicularParking'''    
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
      description: 'Property. Model:''https://schema.org/Text''. The unique ID of the parking site or parking lot corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    priceCurrency:    
      description: 'Property. Model:''https://schema.org/priceCurrency''. Price currency of price rate per minute'    
      type: string    
      x-ngsi:    
        model: https://schema.org/priceCurrency    
        type: Property    
    priceRatePerMinute:    
      description: 'Property. Model: ''https://schema.org/Number''. Price rate per minute.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
    provider:    
      description: 'Property. Parking site service provider. Model:''https://schema.org/provider'''    
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
      description: 'Relationship. Model:''http://schema.org/URL''. Parking site''s access point(s).'    
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
      description: 'Relationship. Model:''http://schema.org/URL''. Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc.'    
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
      description: Relationship. Individual parking spots belonging to this offStreet parking site.    
      x-ngsi:    
        type: Relationship    
    requiredPermit:    
      description: 'Property. This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a '',''. For instance ''residentPermit,disabledPermit'' stays that both, at the same time, a resident and a disabled permit are needed to park. If the list is empty no permit is needed. Allowed values: The following, defined by the _PermitTypeEnum_ enumeration of DATEX II version 2.3. Enum:''employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit''. Or any other application-specific'    
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
      description: 'Property. Model:''http://schema.org/Text''. he following specified by _ReservationTypeEnum_ of DATEX II version 2.3. Enum:''mandatory, notAvailable, optional, partly'''    
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
      description: 'Property. Model:''http://schema.org/Text''. Security aspects provided by this parking site. Allowed values: The following, some of them, defined by _ParkingSecurityEnum_ of DATEX II version 2.3. Enum:''areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff'' . or any other application-specific'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    specialLocation:    
      description: 'Property. Model:''http://schema.org/Text''. If the parking site is at a special location (airport, department store, etc.) it conveys what is such special location.  Allowed values: Those defined by _ParkingSpecialLocationEnum_ of [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). Enum:''airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'''    
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
      description: 'Property. Model:''http://schema.org/Text''. Status of the parking site. Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3. Enum:''almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable''. Or any other application-specific'    
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
      description: 'Property. Model:''http://schema.org/Number''. The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class.'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    twoWheelerSlots:    
      description: 'Property. Model:''https://schema.org/Text. Two wheeler parking spot availability status in parking site corresponding to this observation.'    
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
      description: Property. It has to be OffStreetParking    
      enum:    
        - OffStreetParking    
      type: string    
      x-ngsi:    
        type: Property    
    unclassifiedSlots:    
      description: 'Property. Model:''https://schema.org/Text. Unclassified vehicles or other vehicles parking spot availability status in parking site corresponding to this observation.'    
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
      description: 'Property. Model:''http://schema.org/Text''. Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3. Enum:''automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other''. Or any other value useful for the application and not covered above.'    
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
      description: 'Property. Model:''http://schema.org/Number''. Aggregated number of vehicle that enter the parking site in a period of time.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    vehicleExitCount:    
      description: 'Property. Model:''http://schema.org/Number''. Aggregated number of vehicle that leave the parking site in a period of time.'    
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
## ＃＃＃＃有效载荷的例子  
#### OffStreetParking NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的OffStreetParking的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### OffStreetParking NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的OffStreetParking的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### OffStreetParking NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为关键值的OffStreetParking的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### OffStreetParking NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的OffStreetParking的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
