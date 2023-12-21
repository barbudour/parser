# CardExternalSourceLogic.WriteJsonCardAsync - метод
Запись карточки в формате Json.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task WriteJsonCardAsync(
    	ISourceContentProvider targetContentProvider,
    	CardStoreRequest storeRequest,
    	CardFile[] cardFiles,
    	IList<IStorageContentMapping> cardStoragePathFileMappings,
    	IValidationResultBuilder validationStorageResult,
    	Dictionary<Guid, Func<CancellationToken, ValueTask<Stream>>> fileStreams = null,
    	ISourceDirectoryProvider subDirectoryProvider = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function WriteJsonCardAsync ( 
    	targetContentProvider As ISourceContentProvider,
    	storeRequest As CardStoreRequest,
    	cardFiles As CardFile(),
    	cardStoragePathFileMappings As IList(Of IStorageContentMapping),
    	validationStorageResult As IValidationResultBuilder,
    	Optional fileStreams As Dictionary(Of Guid, Func(Of CancellationToken, ValueTask(Of Stream))) = Nothing,
    	Optional subDirectoryProvider As ISourceDirectoryProvider = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ WriteJsonCardAsync(
    	ISourceContentProvider^ targetContentProvider, 
    	CardStoreRequest^ storeRequest, 
    	array<CardFile^>^ cardFiles, 
    	IList<IStorageContentMapping^>^ cardStoragePathFileMappings, 
    	IValidationResultBuilder^ validationStorageResult, 
    	Dictionary<Guid, Func<CancellationToken, ValueTask<Stream^>>^>^ fileStreams = nullptr, 
    	ISourceDirectoryProvider^ subDirectoryProvider = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract WriteJsonCardAsync : 
            targetContentProvider : ISourceContentProvider * 
            storeRequest : CardStoreRequest * 
            cardFiles : CardFile[] * 
            cardStoragePathFileMappings : IList<IStorageContentMapping> * 
            validationStorageResult : IValidationResultBuilder * 
            ?fileStreams : Dictionary<Guid, Func<CancellationToken, ValueTask<Stream>>> * 
            ?subDirectoryProvider : ISourceDirectoryProvider * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _fileStreams = defaultArg fileStreams null
            let _subDirectoryProvider = defaultArg subDirectoryProvider null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override WriteJsonCardAsync : 
            targetContentProvider : ISourceContentProvider * 
            storeRequest : CardStoreRequest * 
            cardFiles : CardFile[] * 
            cardStoragePathFileMappings : IList<IStorageContentMapping> * 
            validationStorageResult : IValidationResultBuilder * 
            ?fileStreams : Dictionary<Guid, Func<CancellationToken, ValueTask<Stream>>> * 
            ?subDirectoryProvider : ISourceDirectoryProvider * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _fileStreams = defaultArg fileStreams null
            let _subDirectoryProvider = defaultArg subDirectoryProvider null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
targetContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса, куда производится запись.
storeRequest [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
cardFiles [CardFile](T_Tessa_Cards_CardFile.htm)[]
    Массив объектов, прикрепленных к карточке файлов.
cardStoragePathFileMappings
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IStorageContentMapping](T_Tessa_Platform_Storage_IStorageContentMapping.htm)>
    Список storage-маппингов для выгружаемого контента.
validationStorageResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    [ValidationStorageResultBuilder](T_Tessa_Platform_Validation_ValidationStorageResultBuilder.htm)
fileStreams
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>>
(Optional)
    Контент прикрепленных к карточке файлов.
subDirectoryProvider
[ISourceDirectoryProvider](T_Tessa_Platform_SourceProviders_ISourceDirectoryProvider.htm)
(Optional)
     Провайдер для поддиректории карточки, если null, то будет вычислен и использован стандартный.>
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardExternalSourceLogic.WriteJsonCardAsync(ISourceContentProvider,
CardStoreRequest, CardFile[], IList<IStorageContentMapping>,
IValidationResultBuilder, Dictionary<Guid, Func<CancellationToken,
ValueTask<Stream>>>, ISourceDirectoryProvider,
CancellationToken)](M_Tessa_Cards_ICardExternalSourceLogic_WriteJsonCardAsync.htm)  
##  __См. также
#### Ссылки
[CardExternalSourceLogic - ](T_Tessa_Cards_CardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
