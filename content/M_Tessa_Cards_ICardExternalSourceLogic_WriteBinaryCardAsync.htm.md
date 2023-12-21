# ICardExternalSourceLogic.WriteBinaryCardAsync - метод
Запись карточки в Binary формате.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task WriteBinaryCardAsync(
    	ISourceContentProvider targetContentProvider,
    	CardStoreRequest storeRequest,
    	CardHeader header,
    	CardFile[] cardFiles,
    	ValidationStorageResultBuilder validationStorageResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function WriteBinaryCardAsync ( 
    	targetContentProvider As ISourceContentProvider,
    	storeRequest As CardStoreRequest,
    	header As CardHeader,
    	cardFiles As CardFile(),
    	validationStorageResult As ValidationStorageResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ WriteBinaryCardAsync(
    	ISourceContentProvider^ targetContentProvider, 
    	CardStoreRequest^ storeRequest, 
    	CardHeader^ header, 
    	array<CardFile^>^ cardFiles, 
    	ValidationStorageResultBuilder^ validationStorageResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract WriteBinaryCardAsync : 
            targetContentProvider : ISourceContentProvider * 
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
targetContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса, куда производится запись.
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
##  __См. также
#### Ссылки
[ICardExternalSourceLogic - ](T_Tessa_Cards_ICardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
