# CardExternalSourceLogic.WriteBinaryCardAsync - метод
Запись карточки в Binary формате.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task WriteBinaryCardAsync(
    	ISourceContentProvider targetFileSource,
    	CardStoreRequest storeRequest,
    	CardHeader header,
    	CardFile[] cardFiles,
    	ValidationStorageResultBuilder validationStorageResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function WriteBinaryCardAsync ( 
    	targetFileSource As ISourceContentProvider,
    	storeRequest As CardStoreRequest,
    	header As CardHeader,
    	cardFiles As CardFile(),
    	validationStorageResult As ValidationStorageResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ WriteBinaryCardAsync(
    	ISourceContentProvider^ targetFileSource, 
    	CardStoreRequest^ storeRequest, 
    	CardHeader^ header, 
    	array<CardFile^>^ cardFiles, 
    	ValidationStorageResultBuilder^ validationStorageResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract WriteBinaryCardAsync : 
            targetFileSource : ISourceContentProvider * 
            storeRequest : CardStoreRequest * 
            header : CardHeader * 
            cardFiles : CardFile[] * 
            validationStorageResult : ValidationStorageResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override WriteBinaryCardAsync : 
            targetFileSource : ISourceContentProvider * 
            storeRequest : CardStoreRequest * 
            header : CardHeader * 
            cardFiles : CardFile[] * 
            validationStorageResult : ValidationStorageResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
targetFileSource
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
storeRequest [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
header [CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm)
    Заголовок потока карточки, в котором производится сохранение.
cardFiles [CardFile](T_Tessa_Cards_CardFile.htm)[]
    Массив объектов, прикрепленных к карточке файлов.
validationStorageResult
[ValidationStorageResultBuilder](T_Tessa_Platform_Validation_ValidationStorageResultBuilder.htm)
    [ValidationStorageResultBuilder](T_Tessa_Platform_Validation_ValidationStorageResultBuilder.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardExternalSourceLogic.WriteBinaryCardAsync(ISourceContentProvider,
CardStoreRequest, CardHeader, CardFile[], ValidationStorageResultBuilder,
CancellationToken)](M_Tessa_Cards_ICardExternalSourceLogic_WriteBinaryCardAsync.htm)  
##  __См. также
#### Ссылки
[CardExternalSourceLogic - ](T_Tessa_Cards_CardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
