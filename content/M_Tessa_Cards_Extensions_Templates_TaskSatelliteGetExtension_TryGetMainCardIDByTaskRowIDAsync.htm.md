# TaskSatelliteGetExtension.TryGetMainCardIDByTaskRowIDAsync - метод
Возвращает идентификатор основной карточки по идентификатору задания или null,
если карточка не найдена.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<Guid?> TryGetMainCardIDByTaskRowIDAsync(
    	IDbScope dbScope,
    	Guid taskRowID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGetMainCardIDByTaskRowIDAsync ( 
    	dbScope As IDbScope,
    	taskRowID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     protected:
    virtual Task<Nullable<Guid>>^ TryGetMainCardIDByTaskRowIDAsync(
    	IDbScope^ dbScope, 
    	Guid taskRowID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGetMainCardIDByTaskRowIDAsync : 
            dbScope : IDbScope * 
            taskRowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий выполнение запросов к базе данных.
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор идентификатор основной карточки по идентификатору задания или
null, если карточка не найдена.
## __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
