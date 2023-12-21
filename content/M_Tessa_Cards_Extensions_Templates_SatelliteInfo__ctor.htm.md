# SatelliteInfo - конструктор
Инициализирует новый экземпляр класса
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SatelliteInfo(
    	Guid satelliteID,
    	Guid satelliteTypeID,
    	Guid taskRowID,
    	IReadOnlyCollection<Guid> fileRowIDList = null
    )
VB __Копировать
     Public Sub New ( 
    	satelliteID As Guid,
    	satelliteTypeID As Guid,
    	taskRowID As Guid,
    	Optional fileRowIDList As IReadOnlyCollection(Of Guid) = Nothing
    )
C++ __Копировать
     public:
    SatelliteInfo(
    	Guid satelliteID, 
    	Guid satelliteTypeID, 
    	Guid taskRowID, 
    	IReadOnlyCollection<Guid>^ fileRowIDList = nullptr
    )
F# __Копировать
     new : 
            satelliteID : Guid * 
            satelliteTypeID : Guid * 
            taskRowID : Guid * 
            ?fileRowIDList : IReadOnlyCollection<Guid> 
    (* Defaults:
            let _fileRowIDList = defaultArg fileRowIDList null
    *)
    -> SatelliteInfo
#### Параметры
satelliteID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
satelliteTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
fileRowIDList
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
## __См. также
#### Ссылки
[SatelliteInfo - ](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
