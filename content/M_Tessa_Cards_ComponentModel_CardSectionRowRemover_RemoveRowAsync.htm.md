# CardSectionRowRemover.RemoveRowAsync - метод
Удаляет строку из секции, для которой был получен текущий объект.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task RemoveRowAsync(
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	Guid rowID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RemoveRowAsync ( 
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	rowID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ RemoveRowAsync(
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	Guid rowID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member RemoveRowAsync : 
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
    Объект, выполняющий SQL-команды к базе данных.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект, выполняющий создание SQL-команды.
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор удаляемой строки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardSectionRowRemover -
](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
