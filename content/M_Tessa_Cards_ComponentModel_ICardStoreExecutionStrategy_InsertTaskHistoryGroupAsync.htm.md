# ICardStoreExecutionStrategy.InsertTaskHistoryGroupAsync - метод
Вставляет запись о завершённом задании в таблицу с группами истории заданий
TaskHistoryGroups.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task InsertTaskHistoryGroupAsync(
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	Guid cardID,
    	CardTaskHistoryGroup historyGroup,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InsertTaskHistoryGroupAsync ( 
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	cardID As Guid,
    	historyGroup As CardTaskHistoryGroup,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ InsertTaskHistoryGroupAsync(
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	Guid cardID, 
    	CardTaskHistoryGroup^ historyGroup, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InsertTaskHistoryGroupAsync : 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            cardID : Guid * 
            historyGroup : CardTaskHistoryGroup * 
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
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой записывается история заданий.
historyGroup [CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)
    Запись о группе в истории заданий, которая в точности переносится в базу данных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
