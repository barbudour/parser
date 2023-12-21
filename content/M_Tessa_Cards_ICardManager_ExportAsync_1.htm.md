# ICardManager.ExportAsync(CardGetRequest, ISourceContentProvider,
Dictionary<String, Object>, CardFileFormat,
IReadOnlyCollection<IStorageContentMapping>, Boolean, CancellationToken) -
метод
Выполняет административный экспорт карточки со всем её содержимым, включая
файлы и задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardGetResponse> ExportAsync(
    	CardGetRequest request,
    	ISourceContentProvider targetFileSource,
    	Dictionary<string, Object> importInfo = null,
    	CardFileFormat format = CardFileFormat.Binary,
    	IReadOnlyCollection<IStorageContentMapping> extraContentMapping = null,
    	bool overwriteModifiedValues = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ExportAsync ( 
    	request As CardGetRequest,
    	targetFileSource As ISourceContentProvider,
    	Optional importInfo As Dictionary(Of String, Object) = Nothing,
    	Optional format As CardFileFormat = CardFileFormat.Binary,
    	Optional extraContentMapping As IReadOnlyCollection(Of IStorageContentMapping) = Nothing,
    	Optional overwriteModifiedValues As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardGetResponse)
C++ __Копировать
    Task<CardGetResponse^>^ ExportAsync(
    	CardGetRequest^ request, 
    	ISourceContentProvider^ targetFileSource, 
    	Dictionary<String^, Object^>^ importInfo = nullptr, 
    	CardFileFormat format = CardFileFormat::Binary, 
    	IReadOnlyCollection<IStorageContentMapping^>^ extraContentMapping = nullptr, 
    	bool overwriteModifiedValues = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ExportAsync : 
            request : CardGetRequest * 
            targetFileSource : ISourceContentProvider * 
            ?importInfo : Dictionary<string, Object> * 
            ?format : CardFileFormat * 
            ?extraContentMapping : IReadOnlyCollection<IStorageContentMapping> * 
            ?overwriteModifiedValues : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _importInfo = defaultArg importInfo null
            let _format = defaultArg format CardFileFormat.Binary
            let _extraContentMapping = defaultArg extraContentMapping null
            let _overwriteModifiedValues = defaultArg overwriteModifiedValues false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardGetResponse> 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на выполнение загрузки карточки для экспорта.
targetFileSource
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
     Провайдер для ресурса, в который будет записана карточка, например, файл и т.п. 
importInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, помещаемая в запрос на импорт карточки, или null, если дополнительная информация отсутствует. 
format [CardFileFormat](T_Tessa_Cards_CardFileFormat.htm) (Optional)
    Формат файла для экспорта карточки.
extraContentMapping
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[IStorageContentMapping](T_Tessa_Platform_Storage_IStorageContentMapping.htm)>
(Optional)
    Список опций для сериализации внешнего контента из storage карточки в отдельные файлы.
overwriteModifiedValues
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    В случае, когда экспорт перезаписывает уже существующую карточку на диске, определяет, перезаписать ли некоторые значения, такие как дата/время изменения карточки, или сохранить их такими, как в существующем файле.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)>  
Результат выполнения запроса на экспорт карточки.
##  __См. также
#### Ссылки
[ICardManager - ](T_Tessa_Cards_ICardManager.htm)
[ExportAsync - перегрузка](Overload_Tessa_Cards_ICardManager_ExportAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
