# ICardExternalSourceLogic.ReadJsonCardAsync - метод
Чтение Json карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<(CardStoreRequest CardStoreRequest, List<Object> Storage, IList<string> StorageRelativeFilePaths)> ReadJsonCardAsync(
    	ISourceContentProvider sourceContentProvider,
    	IValidationResultBuilder validationResult,
    	ISourceDirectoryProvider subContentSourceProvider = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ReadJsonCardAsync ( 
    	sourceContentProvider As ISourceContentProvider,
    	validationResult As IValidationResultBuilder,
    	Optional subContentSourceProvider As ISourceDirectoryProvider = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of (CardStoreRequest As CardStoreRequest, Storage As List(Of Object), StorageRelativeFilePaths As IList(Of String)))
C++ __Копировать
    ValueTask<ValueTuple<CardStoreRequest^, List<Object^>^, IList<String^>^>> ReadJsonCardAsync(
    	ISourceContentProvider^ sourceContentProvider, 
    	IValidationResultBuilder^ validationResult, 
    	ISourceDirectoryProvider^ subContentSourceProvider = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ReadJsonCardAsync : 
            sourceContentProvider : ISourceContentProvider * 
            validationResult : IValidationResultBuilder * 
            ?subContentSourceProvider : ISourceDirectoryProvider * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _subContentSourceProvider = defaultArg subContentSourceProvider null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<CardStoreRequest, List<Object>, IList<string>>> 
#### Параметры
sourceContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса - источинка, откуда производится чтение.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации.
subContentSourceProvider
[ISourceDirectoryProvider](T_Tessa_Platform_SourceProviders_ISourceDirectoryProvider.htm)
(Optional)
    Провайдер поддиректории карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm),
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Object](https://learn.microsoft.com/dotnet/api/system.object)>,
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>>>  
Объект запроса на сохранение карточки. Объект storage в котором содержится
информация о файлах, прикрепленых к карточке. Список относительных путей до
файлов с внешним storage-контентом карточки.
## __См. также
#### Ссылки
[ICardExternalSourceLogic - ](T_Tessa_Cards_ICardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
