# CardGetStrategy.LoadFileVersionsAsync - метод
Загружает информацию по версиям файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task LoadFileVersionsAsync(
    	Guid fileID,
    	ListStorage<CardFileVersion> versions,
    	DbManager db,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function LoadFileVersionsAsync ( 
    	fileID As Guid,
    	versions As ListStorage(Of CardFileVersion),
    	db As DbManager,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ LoadFileVersionsAsync(
    	Guid fileID, 
    	ListStorage<CardFileVersion^>^ versions, 
    	DbManager^ db, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract LoadFileVersionsAsync : 
            fileID : Guid * 
            versions : ListStorage<CardFileVersion> * 
            db : DbManager * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override LoadFileVersionsAsync : 
            fileID : Guid * 
            versions : ListStorage<CardFileVersion> * 
            db : DbManager * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла, версии которого требуется загрузить.
versions
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFileVersion](T_Tessa_Cards_CardFileVersion.htm)>
    Список, в который добавляется информация по загруженным версиям файла.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект осуществляющий построение результата валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetStrategy.LoadFileVersionsAsync(Guid, ListStorage<CardFileVersion>,
DbManager, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadFileVersionsAsync.htm)  
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
