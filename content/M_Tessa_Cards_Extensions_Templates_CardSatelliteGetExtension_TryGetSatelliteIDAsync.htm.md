# CardSatelliteGetExtension.TryGetSatelliteIDAsync - метод
Возвращает идентификатор сателлита по идентификатору основной карточки или
null, если сателлит ещё не создан.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<Guid?> TryGetSatelliteIDAsync(
    	IDbScope dbScope,
    	Guid mainCardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGetSatelliteIDAsync ( 
    	dbScope As IDbScope,
    	mainCardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     protected:
    virtual Task<Nullable<Guid>>^ TryGetSatelliteIDAsync(
    	IDbScope^ dbScope, 
    	Guid mainCardID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGetSatelliteIDAsync : 
            dbScope : IDbScope * 
            mainCardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
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
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор сателлита, полученный по идентификатору основной карточки, или
null, если сателлит ещё не создан.
## __См. также
#### Ссылки
[CardSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
