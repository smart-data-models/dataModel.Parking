<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ路上駐車  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Parking/blob/master/OffStreetParking/LICENSE.md)  
[文書が自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**オフストリートパーキング**  
バージョン: 0.1.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `acceptedPaymentMethod[array]`: Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'.ご利用可能なお支払い方法  . Model: [https://schema.org/acceptedPaymentMethod](https://schema.org/acceptedPaymentMethod)- `accessModified[string]`: vehicleEntranceCount` と `vehicleExitCount` が更新されたタイムスタンプ。許容される値：ISO8601  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `aggregateRating[object]`: この駐車場の総合評価  . Model: [https://schema.org/aggregateRating](https://schema.org/aggregateRating)- `allowedVehicleType[array]`: 許可される車種。この配列の最初の要素は、許可される主要な車種でなければならない。他の許可された車種のフリースポット番号は、`extraSpotNumber`属性や_ParkingGroup_型の特定のエンティティを通して報告されるかもしれない。以下の値は_VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html)によって定義される。Enum:'agriculturalVehicle, anyVehicle, bicycle, bus, car, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: 利用可能なスポットの数（すべての車種、または身体障害者用、長期駐車者用などの予約スペースを含む）。スポットの境界線が線で明確に示されていない駐車場では、これは推定しにくいかもしれません。許容される値：totalSpotNumber`以下でなければならない。  . Model: [http://schema.org/Number](http://schema.org/Number)- `averageSpotLength[number]`: 駐車場の平均長さ  . Model: [http://schema.org/length](http://schema.org/length)- `averageSpotWidth[number]`: 駐車場の平均幅  . Model: [http://schema.org/width](http://schema.org/width)- `category[array]`: 駐車場のカテゴリー。このフィールドの目的は、一般的に言えば、路上駐車のエンティティをタグ付けできるようにすることです。  - `chargeType[array]`: 駐車場が行う料金の種類。許容される値：DATEX II version 2.3 _ ChargeTypeEnum_列挙によって定義されるものの一部。Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice'。または、その他のアプリケーション固有の  - `contactPoint[object]`: 駐車場連絡先  . Model: [https://schema.org/contactPoint](https://schema.org/contactPoint)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `extCategory[array]`: カテゴリーを補完する外部カテゴリー  - `extraSpotNumber[number]`: 利用可能な、つまり空いている追加スポットの数。この値は、以下のすべてのグループのフリースポットを合計したものでなければならない：A/ 特別な目的のために予約され、通常は許可証が必要なもの。許可証の詳細はパーキンググループレベル（`ParkingGroup`型のエンティティ）で確認できる。B/ 主な許可車種とは異なる他の車種のために予約されているもの。C/ このエンティティによって伝達される一般的な条件ルールに従わない、その他の駐車場グループ。  . Model: [http://schema.org/Number](http://schema.org/Number)- `facilities[array]`: 許容される値：DATEX II version 2.3の_EquipmentTypeEnum_列挙型で定義される以下のもの。列挙：駐輪場、現金自動預け払い機、コピー機またはサービス、除細動器、ダンプステーション、充電ステーション、エレベータ、ファックス機またはサービス、消火ホース、消火器、消火栓、救急設備、清水、アイスフリー足場、インフォメーションポイント、インターネットワイヤレス、ラゲッジロッカー、ペイデスク、精算機、遊び場、公衆電話、ゴミ箱、セーフティボックス、シャワー、トイレ、有料ターミナル、自動販売機、ゴミ処理'。その他のアプリケーション固有の  . Model: []()- `firstAvailableFloor[number]`: 現在利用可能な駐車場がある、地面に最も近い階の番号。許容される値：階数は-nからnの間で、0階とする。  . Model: [http://schema.org/Number](http://schema.org/Number)- `fourWheelerSlots[object]`: 本観測に対応する駐車場の四輪車駐車場の空き状況  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSlotNumber[number]`: このオブザベーションに対応するスマートパーキングサイトで使用可能な駐車スポットの数。これはtotalSpotNumber以下の正の数でなければならない。  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `occupiedSlotNumber[number]`: このオブザベーションに対応するスマートパーキングサイトの駐車スポット数。これはtotalSpotNumber以下の正の数でなければならない。  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `highestFloor[number]`: 複数のフロアがある駐車場の場合、最上階。整数。0は地上階。上階は正の数。低層階は負の数。  . Model: [http://schema.org/Number](http://schema.org/Number)- `id[*]`: エンティティの一意識別子  - `images[array]`: この駐車場の写真を含むURL  . Model: [https://schema.org/image](https://schema.org/image)- `layout[array]`: 駐車場のレイアウト。category`属性に詳細を与えます。許容される値：DATEX II バージョン2.3の_ParkingLayoutEnum_に従う。Enum:'automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, shed, singleLevel, surface, other'.OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking)も参照。または、アプリケーションに有用で、上記でカバーされていないその他の値。  . Model: [http://schema.org/Text](http://schema.org/Text)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `lowestFloor[number]`: 複数のフロアがある駐車場の場合は、最下階。許容される値：整数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `maximumAllowedHeight[number]`: 車両の最大許容高さ。複数のゾーンがある場合は、すべてのゾーンの最小高さとなる。  . Model: [http://schema.org/heigth](http://schema.org/heigth)- `maximumAllowedWidth[number]`: 車両の最大許容幅。複数のゾーンがある場合は、すべてのゾーンの最小幅となります。  . Model: [http://schema.org/width](http://schema.org/width)- `maximumParkingDuration[string]`: ISO8601 の期間または駐車に関連するその他の文字列でエンコードされる。  空の値または存在しない場合は、無期限であることを示す。  . Model: [http://schema.org/Text](http://schema.org/Text)- `measuresPeriod[number]`: 利用可能なスポット数（availableSpotNumber）と分単位の価格（priceRatePerMinute）に関する測定期間。  . Model: [http://schema.org/Number](http://schema.org/Number)- `measuresPeriodUnit[string]`: 利用可能スポット数（availableSpotNumber）および価格単価（PriceRatePerMinute）に関する測定期間単位。  . Model: [http://schema.org/unitText](http://schema.org/unitText)- `municipalityInfo[object]`: この観測に対応する自治体情報  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: この観測に対応する都市ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityName[string]`: この観測に対応する都市名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `district[string]`: この観測に対応する地区名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `stateName[string]`: この観測に対応する州名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `ulbName[string]`: この観測に対応する都市自治体の名称  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardId[string]`: この観察に対応する病棟ID  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardName[string]`: この観測に対応する区名  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardNum[number]`: この観測に対応する病棟番号  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `zoneId[string]`: この観測に対応するゾーンID  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: このアイテムの名前  - `observationDateTime[date-time]`: 最終観測報告時刻  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancy[number]`: 全スポットに占める占有スポットの相対値。許容値：0 - 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `occupancyDetectionType[array]`: 居住者検知方法。  許容される値：DATEX II version 2.3 _OcupancyDetectionTypeEnum_の以下のもの。Enum:'balancing、manual、modelBased、none、singleSpaceDetection'。またはその他のアプリケーション固有の  . Model: [http://schema.org/Text](http://schema.org/Text)- `occupancyModified[date-time]`: 稼働率の値が最後に変更された時刻。許容される値ISO 8601  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `occupiedSpotNumber[number]`: このオブザベーションに対応するスマートパーキングサイトの総駐車スポット数。これはtotalSpotNumber以下の正の数でなければならない。  . Model: [http://schema.org/Number](http://schema.org/Number)- `openingHours[string]`: 駐車場の営業時間  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `outOfServiceSlotNumber[number]`: この観測に対応する自転車ドッキングステーションまたは駐車場で、自転車ラック/自転車ドッキングスロットまたは駐車スロットが故障しており、自転車のレンタルまたは駐輪に使用できない台数。  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `parkingMode[array]`: 駐車モード（複数可）。許可される値：DATEX II version 2.3 _ParkingModeEnum_列挙で定義されているもの。列挙:'echelonParking, parallelParking, perpendicularParking'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `parkingSiteId[string]`: この観察に対応する駐車場サイトまたは駐車場の固有ID。  . Model: [https://schema.org/Text](https://schema.org/Text)- `priceCurrency[string]`: 1分あたりの料金通貨  . Model: [https://schema.org/priceCurrency](https://schema.org/priceCurrency)- `priceRatePerMinute[number]`: 1分あたりの料金  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `provider[object]`: 駐車場サービス・プロバイダー  . Model: [https://schema.org/provider](https://schema.org/provider)- `refParkingAccess[*]`: 駐車場のアクセスポイント  . Model: [http://schema.org/URL](http://schema.org/URL)- `refParkingGroup[*]`: 駐車場の特定グループ。グループは、ゾーン、完全な階、スポットのグループなどに対応することができます。  . Model: [http://schema.org/URL](http://schema.org/URL)- `refParkingSpot[*]`: この路外駐車場に属する個別駐車場  - `requiredPermit[array]`: この属性は、このサイトで駐車するために必要な許可証をキャプチャする。意味的には、駐車するためには、これらの許可証の少なくとも一つが必要です。許可証が複数の項目（and）で構成されている場合、それらは','で結合することができます。例えば、「residentPermit,disabledPermit」は、駐車に居住者許可証と身体障害者許可証の両方が同時に必要であることを示す。リストが空の場合、許可証は必要ありません。許可される値：DATEX IIバージョン2.3の_PermitTypeEnum_列挙によって定義される。Enum:'employeePermit、fairPermit、governmentPermit、noPermitNeeded、residentPermit、specificIdentifiedVehiclePermit、studentPermit、visitorPermit'。または、その他のアプリケーション固有の  - `reservationType[array]`: DATEX II version 2.3の_ReservationTypeEnum_で規定されている。Enum:'mandatory, notAvailable, optional, partly'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `security[array]`: この駐車場サイトが提供するセキュリティの側面。許容される値：DATEX II version 2.3の_ParkingSecurityEnum_で定義されている。Enum:'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' ...またはその他のアプリケーション固有の値。  . Model: [http://schema.org/Text](http://schema.org/Text)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `specialLocation[array]`: 駐車場が特別な場所（空港、デパートなど）にある場合、そのような特別な場所が何であるかを伝えます。  許容される値：DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a)の_ParkingSpecialLocationEnum_で定義されているもの。Enum:'airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `status[array]`: 駐車場のステータス。許容される値：DATEX II バージョン 2.3 で定義されている以下の列挙型で定義される。列挙型：'almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable'.または、その他のアプリケーション固有の  . Model: [http://schema.org/Text](http://schema.org/Text)- `totalSpotNumber[number]`: この駐車場が提供しているスポットの総数。  スポットが線で明確に示されていない駐車場では、この数を取得するのは難しいかもしれません。許容される値：任意の正の整数値または 0：DATEX 2 バージョン 2.3 _ParkingRecord_クラスの_parkingNumberOfSpaces_属性。  . Model: [http://schema.org/Number](http://schema.org/Number)- `twoWheelerSlots[object]`: 本観測に対応する駐車場の二輪車駐車可能状況  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: このオブザベーションに対応するスマートパーキングサイトで使用可能な駐車スポットの数。これはtotalSpotNumber以下の正の数でなければならない。  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `occupiedSpotNumber[number]`: このオブザベーションに対応するスマートパーキングサイトの駐車スポット数。これはtotalSpotNumber以下の正の数でなければならない。  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `type[string]`: OffStreetParkingでなければならない。  - `unclassifiedSlots[object]`: この観測に対応する駐車場の未分類車両またはその他の車両の駐車場の空き状況  . Model: [https://schema.org/Text](https://schema.org/Text)	- `availableSpotNumber[number]`: このオブザベーションに対応するスマートパーキングサイトで使用可能な駐車スポットの数。これはtotalSpotNumber以下の正の数でなければならない。  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `occupiedSpotNumber[number]`: このオブザベーションに対応するスマートパーキングサイトの駐車スポット数。これはtotalSpotNumber以下の正の数でなければならない。  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `usageScenario[array]`: 使用シナリオ（複数可）。category`属性に詳細を与える。許容される値：DATEX II version 2.3の列挙_ParkingUsageScenarioEnum_で定義されているもの。Enum:'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other'.または、アプリケーションに有用で、上記でカバーされていないその他の値  . Model: [http://schema.org/Text](http://schema.org/Text)- `vehicleEntranceCount[number]`: 一定期間に駐車場に入庫した車両数の集計  . Model: [http://schema.org/Number](http://schema.org/Number)- `vehicleExitCount[number]`: 一定期間内に駐車場から退出した車両数の集計  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
車両を駐車することを目的とし、独立して管理され、適切かつ明確にマークされたアクセスポイント（出入口）を持つ、路上に面していない敷地。必要であれば、管理のため、または複数の駐車場を扱うために、エンティティタイプ[ParkingGroup](../ParkingGroup/README.md)によってモデル化された異なるゾーンに分割することができる。DATEX2バージョン2.3の用語では、_offStreetParking_型の_UrbanParkingSite_に相当します。DATEX II用語のデータ辞書は[http://datexbrowser.tamtamresearch.com/](http://datexbrowser.tamtamresearch.com/)にある。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
## ペイロードの例  
#### OffStreetParking NGSI-v2 キー値の例  
以下はOffStreetParkingをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### OffStreetParking NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のOffStreetParkingの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### OffStreetParking NGSI-LD キー値の例  
以下はOffStreetParkingをJSON-LD形式でkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使うと個々のエンティティのコンテキストデータを返す。  
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
#### オフストリートパーキング NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のOffStreetParkingの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
