# CardFileSystemContentStrategy.MoveFileAsync - метод
Перемещает контент файла sourceFileID (но не записи по файлу) из карточки с
идентификатором sourceCardID в файл targetFileID в карточку с идентификатором
targetCardID. Содержимое не может быть перемещено между разными хранилищами
посредством этого метода, для этого долежн быть создан файл, в который
копируется содержимое исходного файла.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task MoveFileAsync(
    	Guid sourceCardID,
    	Guid sourceFileID,
    	Guid targetCardID,
    	Guid targetFileID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function MoveFileAsync ( 
    	sourceCardID As Guid,
    	sourceFileID As Guid,
    	targetCardID As Guid,
    	targetFileID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ MoveFileAsync(
    	Guid sourceCardID, 
    	Guid sourceFileID, 
    	Guid targetCardID, 
    	Guid targetFileID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract MoveFileAsync : 
            sourceCardID : Guid * 
            sourceFileID : Guid * 
            targetCardID : Guid * 
            targetFileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override MoveFileAsync : 
            sourceCardID : Guid * 
            sourceFileID : Guid * 
            targetCardID : Guid * 
            targetFileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
sourceCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор исходной карточки, из которой требуется переместить файл.
sourceFileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор исходного файла, который требуется переместить.
targetCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор целевой карточки, в которую требуется переместить файл.
targetFileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор целевого файла, в который должен быть перемещено содержимое исходного файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardContentStrategy.MoveFileAsync(Guid, Guid, Guid, Guid,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardContentStrategy_MoveFileAsync.htm)  
##  __См. также
#### Ссылки
[CardFileSystemContentStrategy -
](T_Tessa_Cards_ComponentModel_CardFileSystemContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
