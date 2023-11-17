<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：停车集团    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Parking/blob/master/ParkingGroup/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**停车组**    
版本： 0.1.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 标识公共街道上特定房产的编号      
- `allowedVehicleType[string]`: 允许的车辆类型（一个停车组只允许一种车辆类型）。枚举：'自行车、公共汽车、汽车、大篷车、摩托车、摩托车、卡车'。  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: 该项目的替代名称  - `areBordersMarked[boolean]`: 表示是否对停车位进行了分隔（用空行或类似方式）。如果没有定义该属性，应用程序_应_在父级检查该属性的值  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: 该组中可用的位置数量。必须小于或等于`totalSpotNumber`。  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: 停车位的平均长度。如果未定义该属性，应用程序应在父级检查该属性的值  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: 停车位的平均宽度。如果未定义该属性，应用程序应在父级检查该属性的值  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: 停车组的类别。Enum:'adjacentSpaces, blueZone, completeFloor, free, feeCharged, greenZone, loadUnloadZone, nonAdjacentSpaces, offStreet, onlyDisabled, onlyElectricalCharging, onlyResidents, onlyWithPermit, onStreet, particularConditionsSpaces, shortTermMediumTermLongTerm, statisticsOnly, vehicleTypeSpaces'  . Model: [http://schema.org/Text](http://schema.org/Text)- `chargeType[array]`: 停车场的收费类型。枚举：'额外间隔价、年付、首次间隔价、统一、免费、最低、最高、月付、季票、临时费用、临时价格、未知、其他'。  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maximumAllowedHeight[number]`: 车辆允许的最大高度。  如果未定义该属性，应用程序应在父级检查该属性的值  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: 车辆允许的最大宽度。如果未定义该属性，应用程序应在父级检查该属性的值  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[date-time]`: 以 ISO8601 时长编码的最长允许停留时间。如果不存在或等于空字符串，则表示不确定。如果未定义该属性，应用程序应在父级检查该属性的值  - `name[string]`: 该项目的名称  - `occupancyDetectionType[array]`: 允许值：以下是 DATEX II 2.3 版中的 _OccupancyDetectionTypeEnum_。枚举：'平衡、手动、基于模型、无、单空间检测'。或任何其他特定于应用程序的  . Model: [http://schema.org/Text](http://schema.org/Text)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `parkingMode[array]`: 停车模式。如果未定义该属性，应用程序应在父级检查该属性的值。允许值：DATEX II 2.3 版 _ParkingModeEnum_ 枚举定义的值。枚举：'echelonParking, parallelParking, perpendicularParking' （梯形泊车、平行泊车、垂直泊车  . Model: [http://schema.org/Text](http://schema.org/Text)- `permitActiveHours[object]`: 该属性可用于捕捉只在特定时间或星期几需要许可证的情况。它是一个结构化的值，必须包含每个所需许可证的子属性，表明许可证的激活时间。如果未指定许可证，则表示始终需要许可证。空对象表示始终处于活动状态。语法必须符合 schema.org [开放时间规范](https://schema.org/openingHours)。例如，只在周日活动的蓝区将编码为 "blueZonePermit"："Mo,Tu,We,Th,Fr,Sa 09:00-20:00"。如果未定义该属性，应用程序应在父级检查该属性的值  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `refParkingSite[*]`: 该区域所属的停车位。组不能是孤儿。组不能有子组。参考路外停车场或路内停车场  - `refParkingSpot[*]`: 属于该停车组的单个停车位  - `requiredPermit[array]`: 该属性记录了在该地点停车可能需要的许可证。其语义是至少需要其中_个许可证才能停车。当一个许可证由多个项目（和）组成时，可以用", "将它们组合起来。例如，"residentPermit,disabledPermit "表示同时需要居民许可证和残疾人许可证才能停车。如果列表为空，则不需要许可证  . Model: [http://schema.org/Text](http://schema.org/Text)- `reservationType[string]`: 保留条件。如果未定义该属性，应用程序应在父级检查该属性的值。枚举：'必须、不可用、可选、部分'。  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `totalSpotNumber[number]`: 与该组相关的点位总数。允许值任何正整数或 0。 规范性引用：DATEX 2 2.3 版 _ParkingRecord_ 类的属性 _parkingNumberOfSpaces_  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI 实体类型。必须是 ParkingGroup  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `refParkingSite`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
一组停车位。详细程度可以不同。它可以是一个停车库的一个楼层，也可以是属于一个大型停车场的一个特定区域，或者只是一组用于停放特定类型车辆或受特定限制（残疾人、居民......）的停车位。为简单起见，每个停车组只允许停放一种车型。同样，每个停车组也只允许使用一张所需的许可证。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ParkingGroup:      
  description: 'Parking Group '      
  properties:      
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
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areBordersMarked:      
      description: Denotes whether parking spots are delimited (with blank lines or similar) or not. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
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
      description: The number of spots available in this group. It must lower or equal than `totalSpotNumber`      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    averageSpotLength:      
      description: The average length of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/length      
        type: Property      
        units: meters      
    averageSpotWidth:      
      description: The average width of parking spots. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
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
    maximumAllowedHeight:      
      description: Maximum allowed height for vehicles.  Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/heigth      
        type: Property      
        units: meters      
    maximumAllowedWidth:      
      description: Maximum allowed width for vehicles. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      exclusiveMinimum: 0      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/width      
        type: Property      
        units: Meters      
    maximumParkingDuration:      
      description: Maximum allowed stay encoded as a ISO8601 duration. When non present or equals to the empty string it means indefinite. Applications _SHOULD_ inspect the value of this property at parent's level if it is not defined      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
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
      description: Parking site to which this zone belongs to. A group cannot be orphan. A group cannot have subgroups. Reference to an OffStreetParking or to an OnStreetParking      
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
      description: Individual parking spots belonging to this parking group      
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
      description: 'Conditions for reservation. Applications _SHOULD_ inspect the value of this property at parent''s level if it is not defined. Enum:''mandatory, notAvailable, optional, partly'''      
      enum:      
        - mandatory      
        - notAvailable      
        - optional      
        - partly      
      type: string      
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
      description: 'The total number of spots pertaining to this group. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class'      
      minimum: 1      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be ParkingGroup      
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
## 有效载荷示例    
#### 停车组 NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 ParkingGroup 示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": [  
    "onStreet",  
    "adjacentSpaces",  
    "onlyDisabled"  
  ],  
  "allowedVehicleType": "car",  
  "chargeType": [  
    "free"  
  ],  
  "refParkingSite": "daoiz-velarde-1-5",  
  "description": "Two parking spots reserved for disabled people",  
  "totalSpotNumber": 2,  
  "availableSpotNumber": 1,  
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
  "requiredPermit": [  
    "disabledPermit"  
  ],  
  "permitActiveHours": {  
    "Monday": "null"  
  }  
}  
```  
</details>    
#### 停车组 NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 ParkingGroup 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "daoiz-velarde-1-5-disabled",  
  "type": "ParkingGroup",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "onStreet",  
      "adjacentSpaces",  
      "onlyDisabled"  
    ]  
  },  
  "refParkingSite": {  
    "type": "Text",  
    "value": "daoiz-velarde-1-5"  
  },  
  "permitActiveHours": {  
    "type": "StructuredValue",  
    "value": {  
      "Monday": "null"  
    }  
  },  
  "requiredPermit": {  
    "type": "StructuredValue",  
    "value": [  
      "disabledPermit"  
    ]  
  },  
  "allowedVehicleType": {  
    "type": "Text",  
    "value": "car"  
  },  
  "availableSpotNumber": {  
    "type": "Boolean",  
    "value": true,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-12T12:00:00"  
      }  
    }  
  },  
  "totalSpotNumber": {  
    "type": "Number",  
    "value": 2  
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
  "chargeType": {  
    "type": "StructuredValue",  
    "value": [  
      "free"  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "Two parking spots reserved for disabled people"  
  }  
}  
```  
</details>    
#### 停车组 NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 ParkingGroup 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
</details>    
#### 停车组 NGSI-LD 标准化示例    
下面是一个规范化 JSON-LD 格式的 ParkingGroup 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
