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


class AcceptedPaymentMethod(Enum):
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
    articulatedVehicle = 'articulatedVehicle'
    bicycle = 'bicycle'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carOrLightVehicle = 'carOrLightVehicle'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    fourWheelDrive = 'fourWheelDrive'
    highSidedVehicle = 'highSidedVehicle'
    lorry = 'lorry'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    tanker = 'tanker'
    threeWheeledVehicle = 'threeWheeledVehicle'
    trailer = 'trailer'
    tram = 'tram'
    twoWheeledVehicle = 'twoWheeledVehicle'
    van = 'van'
    vehicleWithCatalyticConverter = 'vehicleWithCatalyticConverter'
    vehicleWithoutCatalyticConverter = 'vehicleWithoutCatalyticConverter'
    vehicleWithCaravan = 'vehicleWithCaravan'
    vehicleWithTrailer = 'vehicleWithTrailer'
    withEvenNumberedRegistrationPlates = 'withEvenNumberedRegistrationPlates'
    withOddNumberedRegistrationPlates = 'withOddNumberedRegistrationPlates'
    other = 'other'


class CategoryEnum(Enum):
    barrierAccess = 'barrierAccess'
    blueZone = 'blueZone'
    feeCharged = 'feeCharged'
    forDisabled = 'forDisabled'
    forElectricalCharging = 'forElectricalCharging'
    forLoadUnload = 'forLoadUnload'
    forResidents = 'forResidents'
    free = 'free'
    greenZone = 'greenZone'
    mediumTerm = 'mediumTerm'
    onlyWithPermit = 'onlyWithPermit'
    public = 'public'
    shortTerm = 'shortTerm'
    taxiStop = 'taxiStop'
    underground = 'underground'


class ChargeTypeEnum(Enum):
    additionalIntervalPrice = 'additionalIntervalPrice'
    annualPayment = 'annualPayment'
    firstIntervalPrice = 'firstIntervalPrice'
    flat = 'flat'
    free = 'free'
    minimum = 'minimum'
    maximum = 'maximum'
    monthlyPayment = 'monthlyPayment'
    seasonTicket = 'seasonTicket'
    temporaryFee = 'temporaryFee'
    temporaryPrice = 'temporaryPrice'
    unknown = 'unknown'
    other = 'other'


class FourWheelerSlots(BaseModel):
    availableSlotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots available for use in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber',
    )
    occupiedSlotNumber: Optional[float] = Field(
        None,
        description='Number of parking spots occupied in the smart parking site corresponding to this observation. This must a positve number lower than or equal to the totalSpotNumber',
    )
    totalSlotNumber: Optional[float] = Field(
        None,
        description='The total number of spots offered by the parking site corresponding to this observation',
    )


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


class ParkingMode(Enum):
    echelonParking = 'echelonParking'
    parallelParking = 'parallelParking'
    perpendicularParking = 'perpendicularParking'


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
    OnStreetParking = 'OnStreetParking'


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


class UsageScenario(Enum):
    carSharing = 'carSharing'
    dropOff = 'dropOff'
    kissAndRide = 'kissAndRide'
    liftShare = 'liftShare'
    loadingBay = 'loadingBay'
    overnightParking = 'overnightParking'
    parkAndRide = 'parkAndRide'
    parkAndCycle = 'parkAndCycle'
    parkAndWalk = 'parkAndWalk'
    vehicleLift = 'vehicleLift'
    other = 'other'


class OnStreetParking(BaseModel):
    acceptedPaymentMethod: Optional[AcceptedPaymentMethod] = Field(
        None,
        description="Type of charge(s) performed by the parking site. Enum:'ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'",
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    allowedVehicleType: Optional[List[AllowedVehicleTypeEnum]] = Field(
        None,
        description="Vehicle type(s) allowed. The first element of this array _MUST_ be the principal vehicle type allowed. The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/downloads/modelv23.html).. Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, van, vehicleWithCatalyticConverter, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'",
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areBordersMarked: Optional[bool] = Field(
        None,
        description='Denotes whether parking spots are delimited (with blank lines or similar) or not',
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    availableSpotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of spots available globally, including reserved spaces, such as those for disabled people, long term parkers and so on. This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines',
    )
    averageSpotLength: Optional[confloat(ge=0.0)] = Field(
        None, description='The average length of parking spots'
    )
    averageSpotWidth: Optional[confloat(ge=0.0)] = Field(
        None, description='The average width of parking spots'
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Street parking category. Enum:'blueZone, feeCharged, forDisabled, forElectricalCharging, forLoadUnload, forResidents, free, greenZone, mediumTerm, onlyWithPermit, shortTerm, taxiStop'",
    )
    chargeType: Optional[List[ChargeTypeEnum]] = Field(
        None,
        description="Type of charge(s) performed by the parking site. Enum:'additionalIntervalPrice, annualPayment, firstIntervalPrice, flat, free, minimum, maximum, monthlyPayment, seasonTicket, temporaryFee, temporaryPrice, unknown, other'",
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
    extraSpotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The number of extra spots available, i.e. free. Extra    spots are those reserved for special purposes and usually require a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`). This value must aggregate free spots from all groups devoted to special parking conditions. Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or equal to `totalSpotNumber',
    )
    fourWheelerSlots: Optional[FourWheelerSlots] = Field(
        None,
        description='Four wheeler parking spot availability status in parking site corresponding to this observation',
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
    layout: Optional[List[str]] = Field(
        None, description='Generic classification of the layout of the parking'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maximumParkingDuration: Optional[AwareDatetime] = Field(
        None,
        description='Maximum allowed stay at site encoded as a ISO8601 duration. An empty value indicates an indefinite duration',
    )
    municipalityInfo: Optional[MunicipalityInfo] = Field(
        None, description='Municipality information corresponding to this observation'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
    occupancyDetectionType: Optional[List[OccupancyDetectionTypeEnum]] = Field(
        None,
        description="Occupancy detection method(s). Enum:'balancing, manual, modelBased, none, singleSpaceDetection'. The following from DATEX II version 2.3 _OccupancyDetectionTypeEnum_",
    )
    occupancyModified: Optional[AwareDatetime] = Field(
        None,
        description='Date last time the occupancy of the parking has being modified',
    )
    occupiedSpotNumber: Optional[float] = Field(
        None,
        description='Number of total parking spots occupied in the smart parking site corresponding to this observation. This must a positive number lower than or equal to the totalSpotNumber',
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
    parkingMode: Optional[ParkingMode] = Field(
        None,
        description="Parking mode(s). Enum:'echelonParking, parallelParking, perpendicularParking'",
    )
    parkingSiteId: Optional[str] = Field(
        None,
        description='The unique ID of the parking site or parking lot corresponding to this observation',
    )
    permitActiveHours: Optional[Dict[str, Any]] = Field(
        None,
        description='This attribute allows to capture situations when a permit is only needed at specific hours or days of week. It is a structured value which must contain a subproperty per each required permit, indicating when the permit is active. If nothing specified for a permit it will mean that a permit is always required. An empty JSON Object means always active. The syntax must be conformant with schema.org',
    )
    refParkingGroup: Optional[List[str]] = Field(
        None,
        description='Reference to the parking group(s) (if any) belonging to this onstreet parking zone',
    )
    refParkingSpot: Optional[List[AnyUrl]] = Field(
        None,
        description='Individual parking spots belonging to this on street parking site',
    )
    requiredPermit: Optional[List[str]] = Field(
        None,
        description="This attribute captures what permit(s) might be needed to park at this site. Semantics is that at least _one of_ these permits is needed to park. When a permit is composed by more than one item (and) they can be combined with a ','. For instance 'residentPermit,disabledPermit' stays that both, at the same time, a resident and a disabled permit are needed to park. If list is empty, no permit is needed",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    totalSpotNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The total number of spots offered by this parking site. This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines. Normative references: DATEX 2 version 2.3 attribute _parkingNumberOfSpaces_ of the _ParkingRecord_ class',
    )
    twoWheelerSlots: Optional[TwoWheelerSlots] = Field(
        None,
        description='Two wheeler parking spot availability status in parking site corresponding to this observation',
    )
    type: Optional[Type6] = Field(
        None, description='Entity type. It must be equal to OnStreetParking'
    )
    unclassifiedSlots: Optional[UnclassifiedSlots] = Field(
        None,
        description='Unclassified vehicles or other vehicles parking spot availability status in parking site corresponding to this observation',
    )
    usageScenario: Optional[UsageScenario] = Field(
        None,
        description="Type of charge(s) performed by the parking site. Enum:'carSharing, dropOff, kissAndRide, liftShare, loadingBay, overnightParking, parkAndRide, parkAndCycle, parkAndWalk, vehicleLift,'",
    )
