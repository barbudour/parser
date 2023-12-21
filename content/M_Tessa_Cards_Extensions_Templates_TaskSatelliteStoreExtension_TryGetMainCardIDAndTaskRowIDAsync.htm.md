# TaskSatelliteStoreExtension.TryGetMainCardIDAndTaskRowIDAsync - метод
Возвращает идентификатор основной карточки и идентификатор задания по
идентификатору карточки-сателлита. Значение false возвращается в том случае,
если сателлит не существует.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<(bool result, Guid mainCardID, Guid taskRowID)> TryGetMainCardIDAndTaskRowIDAsync(
    	IDbScope dbScope,
    	Guid satelliteID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGetMainCardIDAndTaskRowIDAsync ( 
    	dbScope As IDbScope,
    	satelliteID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (result As Boolean, mainCardID As Guid, taskRowID As Guid))
C++ __Копировать
     protected:
    virtual Task<ValueTuple<bool, Guid, Guid>>^ TryGetMainCardIDAndTaskRowIDAsync(
    	IDbScope^ dbScope, 
    	Guid satelliteID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGetMainCardIDAndTaskRowIDAsync : 
            dbScope : IDbScope * 
            satelliteID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Guid, Guid>> 
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
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
true, если метод вернул значения и карточка-сателлит существует; false в
противном случае.
## __См. также
#### Ссылки
[TaskSatelliteStoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
