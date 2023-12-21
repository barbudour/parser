# MultitypeSatelliteBackupExtension.TryGetSatelliteInfoListAsync - метод
Возвращает список данных о карточек-сателлитах обрабатываемого типа, которые
относятся к текущему расширению, где список получен из базы данных, или null,
если карточки не найдены (аналогично пустому списку).
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<List<SatelliteInfo>> TryGetSatelliteInfoListAsync(
    	IDbScope dbScope,
    	Guid mainCardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGetSatelliteInfoListAsync ( 
    	dbScope As IDbScope,
    	mainCardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of SatelliteInfo))
C++ __Копировать
     protected:
    virtual Task<List<SatelliteInfo^>^>^ TryGetSatelliteInfoListAsync(
    	IDbScope^ dbScope, 
    	Guid mainCardID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGetSatelliteInfoListAsync : 
            dbScope : IDbScope * 
            mainCardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<SatelliteInfo>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий выполнение запросов к базе данных.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)>>  
Список данных о карточек-сателлитах обрабатываемого типа, которые относятся к
текущему расширению, где список получен из базы данных, или null, если
карточки не найдены (аналогично пустому списку).
## __См. также
#### Ссылки
[MultitypeSatelliteBackupExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
