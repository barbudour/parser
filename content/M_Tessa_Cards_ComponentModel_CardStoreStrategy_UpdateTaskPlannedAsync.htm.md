# CardStoreStrategy.UpdateTaskPlannedAsync - метод
Заполняет в заданиях информацию о плановом завершении на основании срока,
указанного в задании.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task UpdateTaskPlannedAsync(
    	IEnumerable<CardTask> tasks,
    	DateTime storeDateTime,
    	DbManager db,
    	IQueryBuilderFactory builderFactory,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function UpdateTaskPlannedAsync ( 
    	tasks As IEnumerable(Of CardTask),
    	storeDateTime As DateTime,
    	db As DbManager,
    	builderFactory As IQueryBuilderFactory,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ UpdateTaskPlannedAsync(
    	IEnumerable<CardTask^>^ tasks, 
    	DateTime storeDateTime, 
    	DbManager^ db, 
    	IQueryBuilderFactory^ builderFactory, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract UpdateTaskPlannedAsync : 
            tasks : IEnumerable<CardTask> * 
            storeDateTime : DateTime * 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override UpdateTaskPlannedAsync : 
            tasks : IEnumerable<CardTask> * 
            storeDateTime : DateTime * 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
tasks
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTask](T_Tessa_Cards_CardTask.htm)>
    Сохраняемые задания.
storeDateTime
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата/время сохранения.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, посредством которого осуществляется взаимодействие с базой данных.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект для генерации текста запросов.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreStrategy.UpdateTaskPlannedAsync(IEnumerable<CardTask>, DateTime,
DbManager, IQueryBuilderFactory, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_UpdateTaskPlannedAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreStrategy - ](T_Tessa_Cards_ComponentModel_CardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
