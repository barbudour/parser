# CardSatelliteHelper.TryGetUniversalSatelliteInfoListAsync - метод
Возвращает список объектов
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm),
содержащий информацию по карточкам-сателлитам задач для заданной основной
карточки, или null, если такие список пустой.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<List<SatelliteInfo>> TryGetUniversalSatelliteInfoListAsync(
    	IDbScope dbScope,
    	Guid mainCardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetUniversalSatelliteInfoListAsync ( 
    	dbScope As IDbScope,
    	mainCardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of SatelliteInfo))
C++ __Копировать
     public:
    static Task<List<SatelliteInfo^>^>^ TryGetUniversalSatelliteInfoListAsync(
    	IDbScope^ dbScope, 
    	Guid mainCardID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetUniversalSatelliteInfoListAsync : 
            dbScope : IDbScope * 
            mainCardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<SatelliteInfo>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, предоставляющий доступ к базе данных.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)>>  
Список объектов
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm),
содержащий информацию по карточкам-сателлитам задач для заданной основной
карточки, или null, если такие список пустой.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
