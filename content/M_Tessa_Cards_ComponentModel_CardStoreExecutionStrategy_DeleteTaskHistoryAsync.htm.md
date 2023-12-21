# CardStoreExecutionStrategy.DeleteTaskHistoryAsync - метод
Удаляет запись в истории заданий TaskHistory с заданным идентификатором.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteTaskHistoryAsync(
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	Guid rowID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteTaskHistoryAsync ( 
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	rowID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteTaskHistoryAsync(
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	Guid rowID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteTaskHistoryAsync : 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            rowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteTaskHistoryAsync : 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            rowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, выполняющий SQL-команды.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект для генерации текста запросов.
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор удаляемой записи.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExecutionStrategy.DeleteTaskHistoryAsync(IQueryExecutor,
IQueryBuilderFactory, Guid,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_DeleteTaskHistoryAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
