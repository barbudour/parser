# CardHelper.CreateFromExportedCardAsync - метод
Создаёт карточку по экспортированной карточке и информации из карточки-
источника, из которой выполнялся экспорт и которая используется для связи с
файлами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(CardNewRequest Request, CardNewResponse Response)> CreateFromExportedCardAsync(
    	Card exportedCard,
    	ListStorage<CardFile> sourceFileList,
    	Guid sourceCardID,
    	Guid sourceCardTypeID,
    	ICardManager cardManager,
    	Func<CardFile, Guid, Guid, bool> sourceFileIsMatchFunc = null,
    	bool creatingCopy = false,
    	Dictionary<string, Object> templateInfo = null,
    	ICardServerPermissionsProvider serverPermissionsProvider = null,
    	CardServiceType serviceType = CardServiceType.Default,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateFromExportedCardAsync ( 
    	exportedCard As Card,
    	sourceFileList As ListStorage(Of CardFile),
    	sourceCardID As Guid,
    	sourceCardTypeID As Guid,
    	cardManager As ICardManager,
    	Optional sourceFileIsMatchFunc As Func(Of CardFile, Guid, Guid, Boolean) = Nothing,
    	Optional creatingCopy As Boolean = false,
    	Optional templateInfo As Dictionary(Of String, Object) = Nothing,
    	Optional serverPermissionsProvider As ICardServerPermissionsProvider = Nothing,
    	Optional serviceType As CardServiceType = CardServiceType.Default,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (Request As CardNewRequest, Response As CardNewResponse))
C++ __Копировать
     public:
    static Task<ValueTuple<CardNewRequest^, CardNewResponse^>>^ CreateFromExportedCardAsync(
    	Card^ exportedCard, 
    	ListStorage<CardFile^>^ sourceFileList, 
    	Guid sourceCardID, 
    	Guid sourceCardTypeID, 
    	ICardManager^ cardManager, 
    	Func<CardFile^, Guid, Guid, bool>^ sourceFileIsMatchFunc = nullptr, 
    	bool creatingCopy = false, 
    	Dictionary<String^, Object^>^ templateInfo = nullptr, 
    	ICardServerPermissionsProvider^ serverPermissionsProvider = nullptr, 
    	CardServiceType serviceType = CardServiceType::Default, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateFromExportedCardAsync : 
            exportedCard : Card * 
            sourceFileList : ListStorage<CardFile> * 
            sourceCardID : Guid * 
            sourceCardTypeID : Guid * 
            cardManager : ICardManager * 
            ?sourceFileIsMatchFunc : Func<CardFile, Guid, Guid, bool> * 
            ?creatingCopy : bool * 
            ?templateInfo : Dictionary<string, Object> * 
            ?serverPermissionsProvider : ICardServerPermissionsProvider * 
            ?serviceType : CardServiceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _sourceFileIsMatchFunc = defaultArg sourceFileIsMatchFunc null
            let _creatingCopy = defaultArg creatingCopy false
            let _templateInfo = defaultArg templateInfo null
            let _serverPermissionsProvider = defaultArg serverPermissionsProvider null
            let _serviceType = defaultArg serviceType CardServiceType.Default
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<CardNewRequest, CardNewResponse>> 
#### Параметры
exportedCard [Card](T_Tessa_Cards_Card.htm)
    Экспортированная карточка, по которой требуется создать карточку.
sourceFileList
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardFile](T_Tessa_Cards_CardFile.htm)>
     Список файлов в карточке-источнике, из которой выполнялся экспорт. Может быть равен null, если файлы отсутствуют. Карточка-источник должна существовать в базе данных. 
sourceCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор карточки-источника, из которой выполнялся экспорт. Это должна быть та же карточка, что и карточка в параметре sourceFileList. 
sourceCardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор типа карточки-источника, из которой выполнялся экспорт. Это должна быть та же карточка, что и карточка в параметре sourceFileList. 
cardManager [ICardManager](T_Tessa_Cards_ICardManager.htm)
    Объект, управляющий операциями с карточками.
sourceFileIsMatchFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[CardFile](T_Tessa_Cards_CardFile.htm),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)> (Optional)
     Функция, которая принимает файл из списка sourceFileList, идентификатор файла и идентификатор типа файла в карточке exportedCard и возвращает признак того, что файл подходит для заданных идентификаторов. Значение null использует функцию по умолчанию, которая сравнивает идентификатор файла и идентификатор типа файла. 
creatingCopy [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что выполняется создание копии карточки, а не создание карточки по шаблону. 
templateInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительная информация, помещаемая в запрос на создание карточки по шаблону, или null, если дополнительная информация отсутствует. 
serverPermissionsProvider
[ICardServerPermissionsProvider](T_Tessa_Cards_ICardServerPermissionsProvider.htm)
(Optional)
     Объект, используемый для установки полных прав доступа на запросы по созданию карточки, или null, если права не устанавливаются и рассчитываются в соответствии с правами в сессии. Такой объект доступен только на сервере. 
serviceType [CardServiceType](T_Tessa_Cards_CardServiceType.htm) (Optional)
     Тип сервиса, от которого был получен текущий объект запроса. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm),
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>>  
Результат операции, т.е. внутренний запрос на создание карточки по шаблону и
ответ на него. Внутренний запрос может иметь значение null, если его не
удалось создать.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
