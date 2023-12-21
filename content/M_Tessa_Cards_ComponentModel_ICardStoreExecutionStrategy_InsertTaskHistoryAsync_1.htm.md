# ICardStoreExecutionStrategy.InsertTaskHistoryAsync(IQueryExecutor,
IQueryBuilderFactory, Guid, CardTaskHistoryItem, CancellationToken) - метод
Вставляет запись о завершённом задании в таблицу с историей заданий
TaskHistory. Метод рекомендуется использовать для восстановления записи из
истории заданий после удаления карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task InsertTaskHistoryAsync(
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	Guid cardID,
    	CardTaskHistoryItem historyItem,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InsertTaskHistoryAsync ( 
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	cardID As Guid,
    	historyItem As CardTaskHistoryItem,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ InsertTaskHistoryAsync(
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	Guid cardID, 
    	CardTaskHistoryItem^ historyItem, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InsertTaskHistoryAsync : 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            cardID : Guid * 
            historyItem : CardTaskHistoryItem * 
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
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой записывается история заданий.
historyItem [CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm)
    Запись о завершённом задании, которая в точности переносится в базу данных.
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
[InsertTaskHistoryAsync -
перегрузка](Overload_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_InsertTaskHistoryAsync.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
