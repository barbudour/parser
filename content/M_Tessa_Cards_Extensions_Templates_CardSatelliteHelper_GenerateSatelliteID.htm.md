# CardSatelliteHelper.GenerateSatelliteID - метод
Возвращает идентификатор сателлита, созданный на основе идентификатора типа
сателлита и идентификатора владельца сателлита (карточки или задания).
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid GenerateSatelliteID(
    	Guid satelliteTypeID,
    	Guid ownerID
    )
VB __Копировать
     Public Shared Function GenerateSatelliteID ( 
    	satelliteTypeID As Guid,
    	ownerID As Guid
    ) As Guid
C++ __Копировать
     public:
    static Guid GenerateSatelliteID(
    	Guid satelliteTypeID, 
    	Guid ownerID
    )
F# __Копировать
     static member GenerateSatelliteID : 
            satelliteTypeID : Guid * 
            ownerID : Guid -> Guid 
#### Параметры
satelliteTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
ownerID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор владельца сателлита.
#### Возвращаемое значение
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)  
Идентификатор сателлита, созданный на основе идентификатора типа сателлита и
идентификатора владельца сателлита.
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
