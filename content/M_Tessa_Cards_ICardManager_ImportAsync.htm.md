# ICardManager.ImportAsync(CardStoreRequest, CardHeader,
IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>>,
Dictionary<String, Object>, CardFileFormat, Card, ICardMergeOptions, ILogger,
Boolean, CancellationToken) - метод
Выполняет административный импорт карточки со всем её содержимым, включая
файлы и задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardStoreResponse> ImportAsync(
    	CardStoreRequest request,
    	CardHeader cardHeader = null,
    	IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> fileStreams = null,
    	Dictionary<string, Object> importInfo = null,
    	CardFileFormat format = CardFileFormat.Binary,
    	Card destinationCard = null,
    	ICardMergeOptions mergeOptions = null,
    	ILogger logger = null,
    	bool wipeDeleted = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ImportAsync ( 
    	request As CardStoreRequest,
    	Optional cardHeader As CardHeader = Nothing,
    	Optional fileStreams As IReadOnlyCollection(Of Func(Of CancellationToken, ValueTask(Of Stream))) = Nothing,
    	Optional importInfo As Dictionary(Of String, Object) = Nothing,
    	Optional format As CardFileFormat = CardFileFormat.Binary,
    	Optional destinationCard As Card = Nothing,
    	Optional mergeOptions As ICardMergeOptions = Nothing,
    	Optional logger As ILogger = Nothing,
    	Optional wipeDeleted As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreResponse)
C++ __Копировать
    Task<CardStoreResponse^>^ ImportAsync(
    	CardStoreRequest^ request, 
    	CardHeader^ cardHeader = nullptr, 
    	IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream^>>^>^ fileStreams = nullptr, 
    	Dictionary<String^, Object^>^ importInfo = nullptr, 
    	CardFileFormat format = CardFileFormat::Binary, 
    	Card^ destinationCard = nullptr, 
    	ICardMergeOptions^ mergeOptions = nullptr, 
    	ILogger^ logger = nullptr, 
    	bool wipeDeleted = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ImportAsync : 
            request : CardStoreRequest * 
            ?cardHeader : CardHeader * 
            ?fileStreams : IReadOnlyCollection<Func<CancellationToken, ValueTask<Stream>>> * 
            ?importInfo : Dictionary<string, Object> * 
            ?format : CardFileFormat * 
            ?destinationCard : Card * 
            ?mergeOptions : ICardMergeOptions * 
            ?logger : ILogger * 
            ?wipeDeleted : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardHeader = defaultArg cardHeader null
            let _fileStreams = defaultArg fileStreams null
            let _importInfo = defaultArg importInfo null
            let _format = defaultArg format CardFileFormat.Binary
            let _destinationCard = defaultArg destinationCard null
            let _mergeOptions = defaultArg mergeOptions null
            let _logger = defaultArg logger null
            let _wipeDeleted = defaultArg wipeDeleted false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreResponse> 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
     Запрос на импорт карточки, который содержит карточку и дополнительные настройки импорта в request.Info. Объект может быть получен вызовом метода экспорта. Не должен быть равен null. 
cardHeader [CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm)
(Optional)
     Объект с заголовком для импортируемой карточки. Содержит информацию по содержимому файлов, приложенных к карточке. Может быть быть получен вызовом метода экспорта. Укажите null, если у импортируемой карточки нет файлов. 
fileStreams
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>>
(Optional)
     Список функций, возвращающих потоки с содержимым файлов, приложенных к карточке. Порядок файлов определяется в объекте cardHeader. Может быть быть получен вызовом метода экспорта. Укажите null, если у импортируемой карточки нет файлов. 
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
