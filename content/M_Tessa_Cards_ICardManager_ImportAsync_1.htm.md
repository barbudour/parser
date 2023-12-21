# ICardManager.ImportAsync(ISourceContentProvider, Dictionary<String, Object>,
CardFileFormat, Card, ICardMergeOptions, ILogger, Func<String, Boolean>,
Boolean, CancellationToken) - метод
Выполняет административный импорт карточки со всем её содержимым, включая
файлы и задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardStoreResponse> ImportAsync(
    	ISourceContentProvider sourceContentProvider,
    	Dictionary<string, Object> importInfo = null,
    	CardFileFormat format = CardFileFormat.Binary,
    	Card destinationCard = null,
    	ICardMergeOptions mergeOptions = null,
    	ILogger logger = null,
    	Func<string, bool> ignoredFilesFunc = null,
    	bool wipeDeleted = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ImportAsync ( 
    	sourceContentProvider As ISourceContentProvider,
    	Optional importInfo As Dictionary(Of String, Object) = Nothing,
    	Optional format As CardFileFormat = CardFileFormat.Binary,
    	Optional destinationCard As Card = Nothing,
    	Optional mergeOptions As ICardMergeOptions = Nothing,
    	Optional logger As ILogger = Nothing,
    	Optional ignoredFilesFunc As Func(Of String, Boolean) = Nothing,
    	Optional wipeDeleted As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
    Task<CardStoreResponse^>^ ImportAsync(
    	ISourceContentProvider^ sourceContentProvider, 
    	Dictionary<String^, Object^>^ importInfo = nullptr, 
    	CardFileFormat format = CardFileFormat::Binary, 
    	Card^ destinationCard = nullptr, 
    	ICardMergeOptions^ mergeOptions = nullptr, 
    	ILogger^ logger = nullptr, 
    	Func<String^, bool>^ ignoredFilesFunc = nullptr, 
    	bool wipeDeleted = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ImportAsync : 
            sourceContentProvider : ISourceContentProvider * 
            ?importInfo : Dictionary<string, Object> * 
            ?format : CardFileFormat * 
            ?destinationCard : Card * 
            ?mergeOptions : ICardMergeOptions * 
            ?logger : ILogger * 
            ?ignoredFilesFunc : Func<string, bool> * 
            ?wipeDeleted : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _importInfo = defaultArg importInfo null
            let _format = defaultArg format CardFileFormat.Binary
            let _destinationCard = defaultArg destinationCard null
            let _mergeOptions = defaultArg mergeOptions null
            let _logger = defaultArg logger null
            let _ignoredFilesFunc = defaultArg ignoredFilesFunc null
            let _wipeDeleted = defaultArg wipeDeleted false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
sourceContentProvider
[ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm)
    Провайдер для ресурса, представляющего карточку. Например файл и т.п.
importInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
Дополнительная информация, помещаемая в запрос на импорт карточки, или null,
если дополнительная информация отсутствует.
Если при экспорте карточки была задана дополнительная информация, то она
совмещается с заданной в этом параметре, причём при совпадении ключей
информация в параметре переопределяет информацию, заданную при экспорте.
format [CardFileFormat](T_Tessa_Cards_CardFileFormat.htm) (Optional)
    Формат файла для импорта карточки.
destinationCard [Card](T_Tessa_Cards_Card.htm) (Optional)
     Карточка, определяющая текущее состояние в системе (в базе данных). Обычно может быть получена посредством методом экспорта. Укажите null, чтобы экспорт карточки выполнялся средствами системы в этом методе. 
mergeOptions
[ICardMergeOptions](T_Tessa_Cards_SmartMerge_ICardMergeOptions.htm) (Optional)
    Опции слияния или null, если слияние выполняется с настройками по умолчанию.
logger ILogger (Optional)
    Объект для логирования информации при импорте или null, если используется логирование по умолчанию.
ignoredFilesFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)> (Optional)
    Данная функция используется, когда в поддиректории карточки выявлен лишний файл, определяет игнорировать ли этот факт для каонкретного файла.
wipeDeleted [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Очищать удаленные в корзину карточки, если они будут мешать импорту.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Результат выполнения запроса на импорт карточки.
##  __См. также
#### Ссылки
[ICardManager - ](T_Tessa_Cards_ICardManager.htm)
[ImportAsync - перегрузка](Overload_Tessa_Cards_ICardManager_ImportAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
