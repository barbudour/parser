# ICardStoreStrategy.MoveFilesAsync - метод
Перемещает записи в секции по файлам из карточки с идентификатором
sourceCardID в карточку с идентификатором targetCardID. При этом контент
файлов не перемещается между карточками, для этого используйте метод
[Tessa.Cards.ComponentModel.ICardContentStrategy.MoveFiles].
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task MoveFilesAsync(
    	Guid sourceCardID,
    	Guid targetCardID,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	Guid[] fileIDs = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function MoveFilesAsync ( 
    	sourceCardID As Guid,
    	targetCardID As Guid,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	Optional fileIDs As Guid() = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ MoveFilesAsync(
    	Guid sourceCardID, 
    	Guid targetCardID, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	array<Guid>^ fileIDs = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract MoveFilesAsync : 
            sourceCardID : Guid * 
            targetCardID : Guid * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?fileIDs : Guid[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _fileIDs = defaultArg fileIDs null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
sourceCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор исходной карточки, из которой требуется переместить файлы.
targetCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор целевой карточки, в которую требуется переместить файлы.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
fileIDs [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreStrategy - ](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
