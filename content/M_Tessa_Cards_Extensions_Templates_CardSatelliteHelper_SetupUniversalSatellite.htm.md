# CardSatelliteHelper.SetupUniversalSatellite - метод
Метод для установки параметров универсального сателлита в секцию сателлита.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetupUniversalSatellite(
    	Card satellite,
    	Guid mainCardID,
    	Guid? taskRowID = null
    )
VB __Копировать
     Public Shared Sub SetupUniversalSatellite ( 
    	satellite As Card,
    	mainCardID As Guid,
    	Optional taskRowID As Guid? = Nothing
    )
C++ __Копировать
     public:
    static void SetupUniversalSatellite(
    	Card^ satellite, 
    	Guid mainCardID, 
    	Nullable<Guid> taskRowID = nullptr
    )
F# __Копировать
     static member SetupUniversalSatellite : 
            satellite : Card * 
            mainCardID : Guid * 
            ?taskRowID : Nullable<Guid> 
    (* Defaults:
            let _taskRowID = defaultArg taskRowID null
    *)
    -> unit 
#### Параметры
satellite [Card](T_Tessa_Cards_Card.htm)
    Карточка сателлита.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки.
taskRowID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
    Идентификатор задания, если сателлит относится к заданию.
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
