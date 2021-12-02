エンティティOffStreetParking  
======================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Parking/blob/master/OffStreetParking/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**オフ・ストリート・パーキング  

## プロパティのリスト  

- `acceptedPaymentMethod`: Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'.承認された支払い方法（複数可）  - `accessModified`: vehicleEntranceCount`と`vehicleExitCount`が更新された時のタイムスタンプです。許可された値ISO8601  - `address`: 郵送先住所  - `aggregateRating`: この駐車場の評価を集計しています。  - `allowedVehicleType`: 許可される車両タイプ。この配列の最初の要素は、許可された主要な車両タイプでなければなりません（MUST）。許可されている他の車両タイプのフリースポット番号は、属性 `extraSpotNumber` や _ParkingGroup_ タイプの特定のエンティティを通して報告されるかもしれません。以下の値は、_VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)で定義されています。Enum:'agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'.  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `availableSpotNumber`: 利用可能な駐車場の数（すべての車両タイプや、障害者用、長時間駐車者用などの予約スペースを含む）。これは、スポットの境界が線で明確に示されていない駐車場では、推定するのが難しいかもしれません。許容される値0を含む正の整数で、`totalSpotNumber`より小さいか、同じでなければなりません。  - `averageSpotLength`: 駐車場の平均的な長さです。  - `averageSpotWidth`: 駐車場の平均的な幅です。  - `category`: 駐車場サイトのカテゴリ。このフィールドの目的は、一般的に言って、路上駐車のエンティティをタグ付けできるようにすることです。  - `chargeType`: パーキングサイトで行われるチャージのタイプ（複数可）。許容される値DATEX II version 2.3 _ ChargeTypeEnum_ enumerationで定義されているものの一部。Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice'.またはその他のアプリケーション固有の  - `contactPoint`: 駐車場の連絡先です。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `extCategory`: 外的なカテゴリーから補完的なカテゴリーへ  - `extraSpotNumber`: 利用可能な追加スポットの数、つまり無料です。この値は、以下のすべてのグループの無料スポットを合計する必要があります。A/ 特別な目的のために予約されたもので、通常は許可証が必要です。許可証の詳細はパーキンググループレベル（`ParkingGroup`タイプのエンティティ）で確認できます。B/ 主要な許可された車両タイプとは異なる他の車両タイプのために予約されたもの。C/ このエンティティによって伝えられる一般的な条件規則に従わない、その他の駐車場グループ。  - `facilities`: 許可された値DATEX IIバージョン2.3の_EquipmentTypeEnum_列挙で定義された以下のもの。列挙します。自転車置き場、現金自動預け払い機、コピー機またはサービス、除細動器、ゴミ捨て場、電気充電場、エレベーター、ファックス機またはサービス、消防ホース、消火器、消火栓、救急設備、淡水、氷のない足場、情報ポイント、インターネットワイヤーレス、荷物置き場。氷のない足場、情報ポイント、インターネット・ワイヤレス、荷物ロッカー、有料デスク、支払いマシン、遊び場、公衆電話、ごみ箱、セーフティデポジット、シャワー、トイレ、有料ターミナル、自動販売機、廃棄物処理」。その他のアプリケーション固有の  - `firstAvailableFloor`: 現在利用可能な駐車場がある地上に最も近いフロアの番号。許可された値。ストーリーは-nからnの間で番号付けされ、0階が1階となります。  - `highestFloor`: 複数の階数がある駐車場の場合は、最上階。整数値です。0は地上階。上層階は正の数。下の階は負の数です。  - `id`: エンティティのユニークな識別子  - `images`: この駐車場の写真を含むURL  - `layout`: 駐車場のレイアウト。category`属性にさらに詳細を与える。許容される値DATEX II バージョン 2.3 の _ParkingLayoutEnum_ に従います。Enum:'automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other'.OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking)も参照してください。または、アプリケーションに有用で、上記でカバーされていないその他の値。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `lowestFloor`: 複数の階数がある駐車場の場合は、最下階。許容される値整数である。  - `maximumAllowedHeight`: 車両の最大許容高さ。複数のゾーンがある場合は、すべてのゾーンの最小高さとなります。  - `maximumAllowedWidth`: 車両の最大許容幅です。複数のゾーンがある場合は、すべてのゾーンの最小幅となります。  - `maximumParkingDuration`: 一般的にサイトで許容される最大の滞在時間で、ISO8601の期間または駐車場に関連するその他の文字列でエンコードされる。  空の値または存在しない場合は、無期限であることを示す。  - `measuresPeriod`: メジャーの期間は、availableSpotNumber と priceRatePerMinute に関連しています。  - `measuresPeriodUnit`: availableSpotNumberとPriceRatePerMinuteに関連したメジャー期間単位です。  - `name`: このアイテムの名前です。  - `occupancy`: 全スポットのうち、占有されているスポットの相対値。  - `occupancyDetectionType`: オキュパンシー検出方法（複数可）。  許可された値。DATEX II version 2.3 _OccupancyDetectionTypeEnum_からの以下のもの。Enum:'balancing, manual, modelBased, none, singleSpaceDetection'.またはその他のアプリケーション固有の  - `occupancyModified`: 全スポットのうち、占有されているスポットの相対値。許容される値0 - 1  - `occupiedSpotNumber`: 占有されているスポットの数。許可された値0 - `totalSpotNumber` です。  - `openingHours`: 駐車場の営業時間です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `parkingMode`: パーキングモード（複数可）許容される値。DATEX IIバージョン2.3の_ParkingModeEnum_列挙で定義されたもの。Enum:'echelonParking, parallelParking, perpendicularParking' (エシュロンパーキング、パラレルパーキング、パーペンディキュラーパーキング)  - `priceCurrency`: 1分あたりの価格レートの価格通貨  - `priceRatePerMinute`: 1分あたりの価格レートです。  - `provider`: パーキングサイトサービスプロバイダー  - `refParkingAccess`: 駐車場のアクセスポイント。  - `refParkingGroup`: パーキングサイトが特定されたグループ（複数可）。グループは、ゾーン、階数、スポットのグループなどに対応します。  - `refParkingSpot`: このoffStreet parking siteに属する個々の駐車場。  - `requiredPermit`: この属性は、このサイトに駐車するためにどのような許可証が必要であるかを示す。意味としては、これらの許可証のうち少なくとも_1つが駐車に必要であるということです。許可証が複数の項目（and）で構成されている場合、それらは「,」で結合することができます。例えば、「residentPermit,disabledPermit」は、駐車するためにresidentとdisabledの両方の許可証が同時に必要であることを示します。リストが空の場合、許可証は必要ありません。許可される値DATEX IIバージョン2.3の_PermitTypeEnum_列挙で定義された以下のもの。Enum:'employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit'.またはその他のアプリケーション固有の  - `reservationType`: DATEX IIバージョン2.3の_ReservationTypeEnumで指定された以下の項目。Enum:'mandatory, notAvailable, optional, partly'.  - `security`: このパーキングサイトで提供されるセキュリティ面許可された値DATEX II バージョン 2.3 の _ParkingSecurityEnum_ で定義された以下の項目とその一部。Enum:'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' ... or any other application-specific  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `specialLocation`: 駐車場が特別な場所（空港、デパートなど）にある場合、そのような特別な場所であることを伝えます。  許容される値DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a)の_ParkingSpecialLocationEnum_で定義されたもの。Enum:'airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'.  - `status`: パーキングサイトのステータス。許可された値。DATEX II version 2.3で定義された以下の列挙式で定義されたもの。Enum:'almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable'.またはその他のアプリケーション固有の  - `totalSpotNumber`: この駐車場で提供されているスポットの総数です。  この数は、スポットが線で明確に示されていない駐車場では、取得するのが難しい場合があります。許容される値任意の正の整数値または0。DATEX 2 version 2.3 _ParkingRecord_クラスの属性_parkingNumberOfSpaces_。  - `type`: それはOffStreetParkingでなければならない。  - `usageScenario`: 利用シーンcategory`属性に詳細を与える。許容される値DATEX II バージョン 2.3 の _ParkingUsageScenarioEnum_ の列挙で定義されたもの。Enum:'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other'.または、アプリケーションに有用で、上記に含まれないその他の値。  - `vehicleEntranceCount`: 一定期間に駐車場に入庫した車両の数を集計したもの。  - `vehicleExitCount`: 一定期間に駐車場を出た車両の数を集計したもの。    
必須項目  
- `id`  - `location`  - `type`    
独立して管理され、適切かつ明確にマークされたアクセスポイント（入口と出口）を持つ、車両を駐車することを目的とした、路上のサイト。必要に応じて、管理目的や複数の場所にある駐車場に対応するために、エンティティタイプ[ParkingGroup](../ParkingGroup/README.md)でモデル化された異なるゾーンに分割することができます。DATEX 2バージョン2.3の用語では、_offStreetParking_タイプの_UrbanParkingSite_に相当します。DATEX II用語のデータ辞書は[http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/)にあります。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
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
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/length    
        type: Property    
        units: meters    
    averageSpotWidth:    
      description: 'The average width of parking spots.'    
      exclusiveMinimum: 0    
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
    lowestFloor:    
      description: 'For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number.'    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones.'    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/heigth    
        type: Property    
        units: meters    
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of all the zones.'    
      exclusiveMinimum: 0    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
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
      description: 'Number of spots occupied. Allowed values: 0 - `totalSpotNumber`'    
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
    type:    
      description: 'It has to be OffStreetParking'    
      enum:    
        - OffStreetParking    
      type: string    
      x-ngsi:    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Parking/blob/master/OffStreetParking/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Parking/OffStreetParking/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### OffStreetParking NGSI-v2 キーバリューの例  
OffStreetParkingをkey-valuesとしてJSON-LD形式で表現した例を示します。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### OffStreetParking NGSI-v2の正規化例  
ここでは、正規化されたJSON-LD形式のOffStreetParkingの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### OffStreetParking NGSI-LDのキー・バリューの例  
OffStreetParkingをkey-valuesとしてJSON-LD形式で表現した例です。これは、`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "value": [  
      "A"  
    ]  
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
      "streetAddress": "Rua de Fernandes Tom\u00e1s",  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### OffStreetParking NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のOffStreetParkingの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "occupiedSpotNumber": 282,  
  "occupancyModified": "2018-09-21T12:00:00Z",  
  "occupancy": 0.68,  
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
  "extCategory": [  
    "A"  
  ],  
  "id": "urn:ngsi-ld:OffStreetParking:porto-ParkingLot-23889",  
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
  "name": "Parque de estacionamento Trindade",  
  "requiredPermit": [],  
  "totalSpotNumber": 414,  
  "vehicleEntranceCount": 28,  
  "vehicleExitCount": 12,  
  "accessModified": "2018-09-21T12:00:00Z",  
  "type": "OffStreetParking"  
}  
```  

マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。
