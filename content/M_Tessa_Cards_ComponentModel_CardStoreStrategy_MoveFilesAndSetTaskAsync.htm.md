# CardStoreStrategy.MoveFilesAndSetTaskAsync - метод
Перемещает записи в секции по файлам из карточки с идентификатором
sourceCardID в карточку с идентификатором targetCardID с изменением ссылки на
задание targetTaskID. При этом контент файлов не перемещается между
карточками, для этого используйте метод
[Tessa.Cards.ComponentModel.ICardContentStrategy.MoveFiles].
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task MoveFilesAndSetTaskAsync(
    	Guid sourceCardID,
    	Guid targetCardID,
    	Guid? sourceTaskID,
    	Guid? targetTaskID,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function MoveFilesAndSetTaskAsync ( 
    	sourceCardID As Guid,
    	targetCardID As Guid,
    	sourceTaskID As Guid?,
    	targetTaskID As Guid?,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ MoveFilesAndSetTaskAsync(
    	Guid sourceCardID, 
    	Guid targetCardID, 
    	Nullable<Guid> sourceTaskID, 
    	Nullable<Guid> targetTaskID, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract MoveFilesAndSetTaskAsync : 
            sourceCardID : Guid * 
            targetCardID : Guid * 
            sourceTaskID : Nullable<Guid> * 
            targetTaskID : Nullable<Guid> * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override MoveFilesAndSetTaskAsync : 
            sourceCardID : Guid * 
            targetCardID : Guid * 
            sourceTaskID : Nullable<Guid> * 
            targetTaskID : Nullable<Guid> * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
sourceCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор исходной карточки, из которой требуется переместить файлы.
targetCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор целевой карточки, в которую требуется переместить файлы.
sourceTaskID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор задания, к которому должны принадлежать переносимые файлы на момент переноса, или null, если файлы должны принадлежать карточке, но не её заданию. 
targetTaskID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор задания, к которому должны принадлежать переносимые файлы после переноса, или null, если файлы будут принадлежать карточке. 
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
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
[ICardStoreStrategy.MoveFilesAndSetTaskAsync(Guid, Guid, Nullable<Guid>,
Nullable<Guid>, IQueryExecutor, IQueryBuilderFactory,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_MoveFilesAndSetTaskAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreStrategy - ](T_Tessa_Cards_ComponentModel_CardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
