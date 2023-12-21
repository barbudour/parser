# CardDatabaseContentStrategy.MoveFilesAsync - метод
Перемещает контент файлов из карточки с идентификатором sourceCardID в
карточку с идентификатором targetCardID. При этом записи в секции по файлам не
перемещаются между карточками, для этого используйте методы
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFiles] или
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFilesAndSetTask].
Содержимое не может быть перемещено между разными хранилищами посредством
этого метода, для этого долежн быть создан файл, в который копируется
содержимое исходного файла.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task MoveFilesAsync(
    	Guid sourceCardID,
    	Guid targetCardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function MoveFilesAsync ( 
    	sourceCardID As Guid,
    	targetCardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ MoveFilesAsync(
    	Guid sourceCardID, 
    	Guid targetCardID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract MoveFilesAsync : 
            sourceCardID : Guid * 
            targetCardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override MoveFilesAsync : 
            sourceCardID : Guid * 
            targetCardID : Guid * 
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
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardContentStrategy.MoveFilesAsync(Guid, Guid,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardContentStrategy_MoveFilesAsync.htm)  
##  __См. также
#### Ссылки
[CardDatabaseContentStrategy -
](T_Tessa_Cards_ComponentModel_CardDatabaseContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
