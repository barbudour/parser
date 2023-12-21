# CardStoreDeletionStrategy.DeleteFileAsync - метод
Удаляет файл с заданным идентификатором. Не удаляет данные секций файла и
контент файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteFileAsync(
    	Guid fileID,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteFileAsync ( 
    	fileID As Guid,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteFileAsync(
    	Guid fileID, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteFileAsync : 
            fileID : Guid * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteFileAsync : 
            fileID : Guid * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор удаляемого файла.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, выполняющий SQL-команды по удалению файла.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreDeletionStrategy.DeleteFileAsync(Guid, IQueryExecutor,
IQueryBuilderFactory, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy_DeleteFileAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreDeletionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreDeletionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
