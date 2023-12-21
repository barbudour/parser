# TaskSatelliteGetFileContentExtension.TryGetMainCardIDFromSatelliteIDAsync -
метод
Возвращает идентификатор основной карточки по идентификатору сателлита на
основании данных в базе данных или null, если сателлит ещё не создан.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<Guid?> TryGetMainCardIDFromSatelliteIDAsync(
    	IDbScope dbScope,
    	Guid satelliteID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGetMainCardIDFromSatelliteIDAsync ( 
    	dbScope As IDbScope,
    	satelliteID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     protected:
    virtual Task<Nullable<Guid>>^ TryGetMainCardIDFromSatelliteIDAsync(
    	IDbScope^ dbScope, 
    	Guid satelliteID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGetMainCardIDFromSatelliteIDAsync : 
            dbScope : IDbScope * 
            satelliteID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий выполнение запросов к базе данных.
satelliteID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки-сателлита.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор основной карточки по идентификатору сателлита на основании
данных в базе данных или null, если сателлит ещё не создан.
## __См. также
#### Ссылки
[TaskSatelliteGetFileContentExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetFileContentExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
