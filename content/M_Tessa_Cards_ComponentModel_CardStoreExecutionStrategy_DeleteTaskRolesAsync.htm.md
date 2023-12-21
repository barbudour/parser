# CardStoreExecutionStrategy.DeleteTaskRolesAsync - метод
Удаляет роли заданий с заданными идентификаторами.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteTaskRolesAsync(
    	IList<Guid> roleIDs,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteTaskRolesAsync ( 
    	roleIDs As IList(Of Guid),
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteTaskRolesAsync(
    	IList<Guid>^ roleIDs, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteTaskRolesAsync : 
            roleIDs : IList<Guid> * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteTaskRolesAsync : 
            roleIDs : IList<Guid> * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
roleIDs
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Список идентификаторов удаляемых ролей заданий.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, выполняющий SQL-команды по удалению ролей заданий.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExecutionStrategy.DeleteTaskRolesAsync(IList<Guid>, IQueryExecutor,
IQueryBuilderFactory,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_DeleteTaskRolesAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
