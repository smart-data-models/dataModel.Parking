from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class AcceptedPaymentMethodEnum(Enum):
    ByBankTransferInAdvance = 'ByBankTransferInAdvance'
    ByInvoice = 'ByInvoice'
    Cash = 'Cash'
    CheckInAdvance = 'CheckInAdvance'
    COD = 'COD'
    DirectDebit = 'DirectDebit'
    GoogleCheckout = 'GoogleCheckout'
    PayPal = 'PayPal'
    PaySwarm = 'PaySwarm'


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AllowedVehicleTypeEnum(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    anyVehicle = 'anyVehicle'
    bicycle = 'bicycle'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    lorry = 'lorry'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    tanker = 'tanker'
    trailer = 'trailer'
    van = 'van'


class CategoryEnum(Enum):
    barrierAccess = 'barrierAccess'
    feeCharged = 'feeCharged'
    forCustomers = 'forCustomers'
    forDisabled = 'forDisabled'
    forElectricalCharging = 'forElectricalCharging'
    forEmployees = 'forEmployees'
    forMembers = 'forMembers'
    forResidents = 'forResidents'
    forStudents = 'forStudents'
    forVisitors = 'forVisitors'
    free = 'free'
    freeAccess = 'freeAccess'
    gateAccess = 'gateAccess'
    guarded = 'guarded'
    ground = 'ground'
    longTerm = 'longTerm'
    mediumTerm = 'mediumTerm'
    onlyResidents = 'onlyResidents'
    onlyWithPermit = 'onlyWithPermit'
    parkingGarage = 'parkingGarage'
    parkingLot = 'parkingLot'
    private = 'private'
    public = 'public'
    publicPrivate = 'publicPrivate'
    shortTerm = 'shortTerm'
    staffed = 'staffed'
    underground = 'underground'
    urbanDeterrentParking = 'urbanDeterrentParking'
    other = 'other'


class ChargeTypeEnum(Enum):
    additionalIntervalPrice = 'additionalIntervalPrice'
    annualPayment = 'annualPayment'
    firstIntervalPrice = 'firstIntervalPrice'
    flat = 'flat'
    free = 'free'
    minimum = 'minimum'
    maximum = 'maximum'
    monthlyPayment = 'monthlyPayment'
    other = 'other'
    seasonTicket = 'seasonTicket'
    temporaryPrice = 'temporaryPrice'


class Facility(Enum):
    bikeParking = 'bikeParking'
    cashMachine = 'cashMachine'
    copyMachineOrService = 'copyMachineOrService'
    defibrillator = 'defibrillator'
    dumpingStation = 'dumpingStation'
    electricChargingStation = 'electricChargingStation'
    elevator = 'elevator'
    faxMachineOrService = 'faxMachineOrService'
    fireHose = 'fireHose'
    fireExtinguisher = 'fireExtinguisher'
    fireHydrant = 'fireHydrant'
    firstAidEquipment = 'firstAidEquipment'
    freshWater = 'freshWater'
    iceFreeScaffold = 'iceFreeScaffold'
    informationPoint = 'informationPoint'
    internetWireless = 'internetWireless'
    luggageLocker = 'luggageLocker'
    payDesk = 'payDesk'
    paymentMachine = 'paymentMachine'
    playground = 'playground'
    publicPhone = 'publicPhone'
    refuseBin = 'refuseBin'
    safeDeposit = 'safeDeposit'
    shower = 'shower'
    toilet = 'toilet'
    tollTerminal = 'tollTerminal'
    vendingMachine = 'vendingMachine'
    wasteDisposal = 'wasteDisposal'


class FourWheelerSlots(BaseModel):
    availableSlotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber',
    )
    occupiedSlotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber',
    )
    totalSlotNumber: Optional[float] = Field(
        None,
        description='The total number of spots offered by the parking site corresponding to this observation',
    )


class LayoutEnum(Enum):
    automatedParkingGarage = 'automatedParkingGarage'
    carports = 'carports'
    covered = 'covered'
    field = 'field'
    garageBoxes = 'garageBoxes'
    multiLevel = 'multiLevel'
    multiStorey = 'multiStorey'
    nested = 'nested'
    openSpace = 'openSpace'
    rooftop = 'rooftop'
    sheds = 'sheds'
    singleLevel = 'singleLevel'
    surface = 'surface'
    other = 'other'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class MunicipalityInfo(BaseModel):
    cityId: Optional[str] = Field(
        None, description='City ID corresponding to this observation'
    )
    cityName: Optional[str] = Field(
        None, description='City name corresponding to this observation'
    )
    district: Optional[str] = Field(
        None, description='District name corresponding to this observation'
    )
    stateName: Optional[str] = Field(
        None, description='Name of the state corresponding to this observation'
    )
    ulbName: Optional[str] = Field(
        None,
        description='Name of the Urban Local Body corresponding to this observation',
    )
    wardId: Optional[str] = Field(
        None, description='Ward ID corresponding to this observation'
    )
    wardName: Optional[str] = Field(
        None, description='Ward name corresponding to this observation'
    )
    wardNum: Optional[float] = Field(
        None, description='Ward number corresponding to this observation'
    )
    zoneId: Optional[str] = Field(
        None, description='Zone ID corresponding to this observation'
    )
    zoneName: Optional[str] = Field(
        None, description='Zone name corresponding to this observation'
    )


class OccupancyDetectionTypeEnum(Enum):
    balancing = 'balancing'
    manual = 'manual'
    modelBased = 'modelBased'
    none = 'none'
    singleSpaceDetection = 'singleSpaceDetection'


class ParkingModeEnum(Enum):
    echelonParking = 'echelonParking'
    parallelParking = 'parallelParking'
    perpendicularParking = 'perpendicularParking'


class RequiredPermitEnum(Enum):
    employeePermit = 'employeePermit'
    fairPermit = 'fairPermit'
    governmentPermit = 'governmentPermit'
    noPermitNeeded = 'noPermitNeeded'
    residentPermit = 'residentPermit'
    specificIdentifiedVehiclePermit = 'specificIdentifiedVehiclePermit'
    studentPermit = 'studentPermit'
    visitorPermit = 'visitorPermit'


class ReservationTypeEnum(Enum):
    mandatory = 'mandatory'
    notAvailable = 'notAvailable'
    optional = 'optional'
    partly = 'partly'


class SecurityEnum(Enum):
    areaSeparatedFromSurroundings = 'areaSeparatedFromSurroundings'
    cctv = 'cctv'
    dog = 'dog'
    externalSecurity = 'externalSecurity'
    fences = 'fences'
    floodLight = 'floodLight'
    guard24hours = 'guard24hours'
    lighting = 'lighting'
    patrolled = 'patrolled'
    securityStaff = 'securityStaff'


class SpecialLocationEnum(Enum):
    airportTerminal = 'airportTerminal'
    cableCarStation = 'cableCarStation'
    campground = 'campground'
    cinema = 'cinema'
    coachStation = 'coachStation'
    conventionCentre = 'conventionCentre'
    exhibitionCentre = 'exhibitionCentre'
    ferryTerminal = 'ferryTerminal'
    hotel = 'hotel'
    market = 'market'
    publicTransportStation = 'publicTransportStation'
    religiousCentre = 'religiousCentre'
    shoppingCentre = 'shoppingCentre'
    skilift = 'skilift'
    specificFacility = 'specificFacility'
    themePark = 'themePark'
    trainStation = 'trainStation'
    vehicleOnRailTerminal = 'vehicleOnRailTerminal'
    other = 'other'


class StatusEnum(Enum):
    almostFull = 'almostFull'
    closed = 'closed'
    closedAbnormal = 'closedAbnormal'
    full = 'full'
    fullAtEntrance = 'fullAtEntrance'
    open = 'open'
    openingTimesInForce = 'openingTimesInForce'
    spacesAvailable = 'spacesAvailable'


class TwoWheelerSlots(BaseModel):
    availableSpotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber',
    )
    occupiedSpotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber',
    )
    totalSpotNumber: Optional[float] = Field(
        None,
        description='The total number of spots offered by the parking site corresponding to this observation',
    )


class Type6(Enum):
    OffStreetParking = 'OffStreetParking'


class UnclassifiedSlots(BaseModel):
    availableSpotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber',
    )
    occupiedSpotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber',
    )
    totalSpotNumber: Optional[float] = Field(
        None,
        description='The total number of spots offered by the parking site corresponding to this observation',
    )


class UsageScenarioEnum(Enum):
    automaticParkingGuidance = 'automaticParkingGuidance'
    carSharing = 'carSharing'
    dropOffWithValet = 'dropOffWithValet'
    dropOffMechanical = 'dropOffMechanical'
    dropOff = 'dropOff'
    eventParking = 'eventParking'
    kissAndRide = 'kissAndRide'
    liftShare = 'liftShare'
    loadingBay = 'loadingBay'
    overnightParking = 'overnightParking'
    parkAndCycle = 'parkAndCycle'
    parkAndRide = 'parkAndRide'
    parkAndWalk = 'parkAndWalk'
    restArea = 'restArea'
    serviceArea = 'serviceArea'
    staffGuidesToSpace = 'staffGuidesToSpace'
    truckParking = 'truckParking'
    vehicleLift = 'vehicleLift'
    other = 'other'


class OffStreetParking(BaseModel):
    acceptedPaymentMethod: Optional[List[AcceptedPaymentMethodEnum]] = Field(
        None,
        description="Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'. Accepted payment method(s)",
        min_length=1,
    )
    accessModified: Optional[str] = Field(
        None,
        description='Timestamp when `vehicleEntranceCount` and `vehicleExitCount` was updated. Allowed values: ISO8601',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    aggregateRating: Optional[Dict[str, Any]] = Field(
        None, description='Aggregated rating for this parking site'
    )
    allowedVehicleType: Optional[List[AllowedVehicleTypeEnum]] = Field(
        None,
        description=" Vehicle type(s) allowed. The first element of this array _MUST_ be the principal vehicle type allowed. Free spot numbers of other allowed vehicle types might be reported under the attribute `extraSpotNumber` and through specific entities of type _ParkingGroup_. The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html). Enum:'agriculturalVehicle, anyVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van'",
        min_length=1,
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    availableSpotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of spots available (_including_ all  vehicle types or reserved spaces, such as those for disabled people, long term parkers and so on). This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines. Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`',
    )
    averageSpotLength: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None, description='The average length of parking spots'
    )
    averageSpotWidth: Optional[confloat(ge=0.0)] = Field(
        None, description='The average width of parking spots'
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Parking site's category(ies). The purpose of this field is to allow to tag, generally speaking, off street parking entities",
        min_length=1,
    )
    chargeType: Optional[List[ChargeTypeEnum]] = Field(
        None,
        description="Type(s) of charge performed by the parking site. Allowed values: Some of those defined by the DATEX II version 2.3 _ ChargeTypeEnum_ enumeration. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, other, seasonTicket, temporaryPrice'. Or any other application-specific",
        min_length=1,
    )
    contactPoint: Optional[Dict[str, Any]] = Field(
        None, description='Parking site contact point'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    extCategory: Optional[List[str]] = Field(
        None, description='External category to complement category', min_length=1
    )
    extraSpotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of extra spots _available_, i.e. free. This value must aggregate free spots from all groups mentioned below: A/ Those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). B/ Those reserved for other vehicle types different than the principal allowed vehicle type. C/ Any other group of parking spots not subject to the general condition rules conveyed by this entity',
    )
    facilities: Optional[List[Facility]] = Field(
        None,
        description="Allowed values: The following defined by the _EquipmentTypeEnum_ enumeration of DATEX II version 2.3. Enum:'bikeParking, cashMachine, copyMachineOrService, defibrillator, dumpingStation, electricChargingStation, elevator, faxMachineOrService, fireHose, fireExtinguisher, fireHydrant, firstAidEquipment, freshWater, iceFreeScaffold, informationPoint, internetWireless, luggageLocker, payDesk, paymentMachine, playground, publicPhone, refuseBin, safeDeposit, shower, toilet, tollTerminal, vendingMachine, wasteDisposal' . Any other application-specific",
        min_length=1,
    )
    firstAvailableFloor: Optional[float] = Field(
        None,
        description='Number of the floor closest to the ground which currently has available parking spots. Allowed values: Stories are numbered between -n and n, being 0 ground floor',
    )
    fourWheelerSlots: Optional[FourWheelerSlots] = Field(
        None,
        description='Four wheeler parking spot availability status in parking site corresponding to this observation',
    )
    highestFloor: Optional[float] = Field(
        None,
        description='For parking sites with multiple floor levels, highest floor. An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    images: Optional[List[AnyUrl]] = Field(
        None, description='A URL containing a photo of this parking site'
    )
    layout: Optional[List[LayoutEnum]] = Field(
        None,
        description="Parking layout. Gives more details to the `category` attribute. Allowed values: As per the _ParkingLayoutEnum_ of DATEX II version 2.3. Enum:'automatedParkingGarage, carports, covered, field, garageBoxes, multiLevel, multiStorey, nested, openSpace, rooftop, sheds, singleLevel, surface, other'. See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). Or any other value useful for the application and not covered above",
        min_length=1,
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    lowestFloor: Optional[float] = Field(
        None,
        description='For parking sites with multiple floor levels, lowest floor. Allowed values: An integer number',
    )
    maximumAllowedHeight: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None,
        description='Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of all the zones',
    )
    maximumAllowedWidth: Optional[confloat(ge=0.0, gt=0.0)] = Field(
        None,
        description='Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of all the zones',
    )
    maximumParkingDuration: Optional[str] = Field(
        None,
        description='Maximum allowed stay at site, on a general basis, encoded as a ISO8601 duration or with any other string relevant for parking.  An empty value or when non present indicates an indefinite duration',
    )
    measuresPeriod: Optional[float] = Field(
        None,
        description='The measures period related to availableSpotNumber and priceRatePerMinute',
    )
    measuresPeriodUnit: Optional[str] = Field(
        None,
        description='The measures period unit related to availableSpotNumber and PriceRatePerMinute',
    )
    municipalityInfo: Optional[MunicipalityInfo] = Field(
        None, description='Municipality information corresponding to this observation'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    occupancy: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Relative value of occupied spots out of the total spots. Allowed values: 0 - 1',
    )
    occupancyDetectionType: Optional[List[OccupancyDetectionTypeEnum]] = Field(
        None,
        description="Occupancy detection method(s).  Allowed values: The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_. Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. Or any other application-specific",
        min_length=1,
    )
    occupancyModified: Optional[AwareDatetime] = Field(
        None,
        description='Last time the occupancy values were modified. Allowed values: ISO 8601',
    )
    occupiedSpotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber',
    )
    openingHours: Optional[str] = Field(
        None, description='Opening hours of the parking site'
    )
    outOfServiceSlotNumber: Optional[float] = Field(
        None,
        description='The number of bike racks/bike-docking slots or parking slots that are out of order and cannot be used to hire or park a bike in the bike docking station or parking site corresponding to this observation',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    parkingMode: Optional[List[ParkingModeEnum]] = Field(
        None,
        description="Parking mode(s). Allowed values: Those defined by the DATEX II version 2.3 _ParkingModeEnum_ enumeration. Enum:'echelonParking, parallelParking, perpendicularParking'",
        min_length=1,
    )
    parkingSiteId: Optional[str] = Field(
        None,
        description='The unique ID of the parking site or parking lot corresponding to this observation',
    )
    priceCurrency: Optional[str] = Field(
        None, description='Price currency of price rate per minute'
    )
    priceRatePerMinute: Optional[float] = Field(
        None, description='Price rate per minute'
    )
    provider: Optional[Dict[str, Any]] = Field(
        None, description='Parking site service provider'
    )
    refParkingAccess: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description="Parking site's access point(s)")
    refParkingGroup: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Parking site identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc',
    )
    refParkingSpot: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Individual parking spots belonging to this offStreet parking site',
    )
    requiredPermit: Optional[List[RequiredPermitEnum]] = Field(
        None,
        description="This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a ','. For instance 'residentPermit,disabledPermit' stays that both, at the same time, a resident and a disabled permit are needed to park. If the list is empty no permit is needed. Allowed values: The following, defined by the _PermitTypeEnum_ enumeration of DATEX II version 2.3. Enum:'employeePermit, fairPermit, governmentPermit, noPermitNeeded, residentPermit, specificIdentifiedVehiclePermit, studentPermit, visitorPermit'. Or any other application-specific",
        min_length=0,
    )
    reservationType: Optional[List[ReservationTypeEnum]] = Field(
        None,
        description="he following specified by _ReservationTypeEnum_ of DATEX II version 2.3. Enum:'mandatory, notAvailable, optional, partly'",
        min_length=1,
    )
    security: Optional[List[SecurityEnum]] = Field(
        None,
        description="Security aspects provided by this parking site. Allowed values: The following, some of them, defined by _ParkingSecurityEnum_ of DATEX II version 2.3. Enum:'areaSeparatedFromSurroundings, cctv, dog, externalSecurity, fences, floodLight, guard24hours, lighting, patrolled, securityStaff' . or any other application-specific",
        min_length=1,
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    specialLocation: Optional[List[SpecialLocationEnum]] = Field(
        None,
        description="If the parking site is at a special location (airport, department store, etc.) it conveys what is such special location.  Allowed values: Those defined by _ParkingSpecialLocationEnum_ of [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). Enum:'airportTerminal, cableCarStation, campground, cinema, coachStation, conventionCentre, exhibitionCentre, ferryTerminal, hotel, market, publicTransportStation, religiousCentre, shoppingCentre, skilift, specificFacility, themePark, trainStation, vehicleOnRailTerminal, other'",
        min_length=1,
    )
    status: Optional[List[StatusEnum]] = Field(
        None,
        description="Status of the parking site. Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3. Enum:'almostFull, closed, closedAbnormal, full, fullAtEntrance, open, openingTimesInForce, spacesAvailable'. Or any other application-specific",
        min_length=1,
    )
    totalSpotNumber: Optional[confloat(ge=1.0)] = Field(
        None,
        description='The total number of spots offered by this parking site.  This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Allowed values: Any positive integer number or 0. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class',
    )
    twoWheelerSlots: Optional[TwoWheelerSlots] = Field(
        None,
        description='Two wheeler parking spot availability status in parking site corresponding to this observation',
    )
    type: Optional[Type6] = Field(None, description='It has to be OffStreetParking')
    unclassifiedSlots: Optional[UnclassifiedSlots] = Field(
        None,
        description='Unclassified vehicles or other vehicles parking spot availability status in parking site corresponding to this observation',
    )
    usageScenario: Optional[List[UsageScenarioEnum]] = Field(
        None,
        description="Usage scenario(s). Gives more details to the `category` attribute. Allowed values: Those defined by the enumeration _ParkingUsageScenarioEnum_ of DATEX II version 2.3. Enum:'automaticParkingGuidance, carSharing, dropOffWithValet, dropOffMechanical, dropOff, eventParking, kissAndRide, liftShare, loadingBay, overnightParking, parkAndCycle, parkAndRide, parkAndWalk, restArea, serviceArea, staffGuidesToSpace, truckParking, vehicleLift, other'. Or any other value useful for the application and not covered above",
        min_length=1,
    )
    vehicleEntranceCount: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Aggregated number of vehicle that enter the parking site in a period of time',
    )
    vehicleExitCount: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Aggregated number of vehicle that leave the parking site in a period of time',
    )
