# CardStoreStrategy.MoveFilesAsync - метод
Перемещает записи в секции по файлам из карточки с идентификатором
sourceCardID в карточку с идентификатором targetCardID. При этом контент
файлов не перемещается между карточками, для этого используйте метод
[Tessa.Cards.ComponentModel.ICardContentStrategy.MoveFiles].
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task MoveFilesAsync(
    	Guid sourceCardID,
    	Guid targetCardID,
    	IQueryExecutor executor,
    	IQueryBuilderFactory queryFactory,
    	Guid[] fileIDs = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function MoveFilesAsync ( 
    	sourceCardID As Guid,
    	targetCardID As Guid,
    	executor As IQueryExecutor,
    	queryFactory As IQueryBuilderFactory,
    	Optional fileIDs As Guid() = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ MoveFilesAsync(
    	Guid sourceCardID, 
    	Guid targetCardID, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ queryFactory, 
    	array<Guid>^ fileIDs = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract MoveFilesAsync : 
            sourceCardID : Guid * 
            targetCardID : Guid * 
            executor : IQueryExecutor * 
            queryFactory : IQueryBuilderFactory * 
            ?fileIDs : Guid[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _fileIDs = defaultArg fileIDs null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override MoveFilesAsync : 
            sourceCardID : Guid * 
            targetCardID : Guid * 
            executor : IQueryExecutor * 
            queryFactory : IQueryBuilderFactory * 
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
queryFactory
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
#### Реализации
[ICardStoreStrategy.MoveFilesAsync(Guid, Guid, IQueryExecutor,
IQueryBuilderFactory, Guid[],
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_MoveFilesAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreStrategy - ](T_Tessa_Cards_ComponentModel_CardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
