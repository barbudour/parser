# ICardGetStrategy.LoadTaskHistoryAsync - метод
Загружает информацию по истории завершённых заданий карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> LoadTaskHistoryAsync(
    	Guid cardID,
    	Card card,
    	DbManager db,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	Dictionary<Guid, CardTask> tasksByRowID,
    	IEnumerable<Guid> itemRowIDList = null,
    	IEnumerable<Guid> itemTypeIDList = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function LoadTaskHistoryAsync ( 
    	cardID As Guid,
    	card As Card,
    	db As DbManager,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	tasksByRowID As Dictionary(Of Guid, CardTask),
    	Optional itemRowIDList As IEnumerable(Of Guid) = Nothing,
    	Optional itemTypeIDList As IEnumerable(Of Guid) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ LoadTaskHistoryAsync(
    	Guid cardID, 
    	Card^ card, 
    	DbManager^ db, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	Dictionary<Guid, CardTask^>^ tasksByRowID, 
    	IEnumerable<Guid>^ itemRowIDList = nullptr, 
    	IEnumerable<Guid>^ itemTypeIDList = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract LoadTaskHistoryAsync : 
            cardID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            tasksByRowID : Dictionary<Guid, CardTask> * 
            ?itemRowIDList : IEnumerable<Guid> * 
            ?itemTypeIDList : IEnumerable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _itemRowIDList = defaultArg itemRowIDList null
            let _itemTypeIDList = defaultArg itemTypeIDList null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, информацию по истории завершённых заданий которой требуется загрузить.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую добавляется информацию по истории завершённых заданий.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по загружаемым типам заданий. Передайте объект с метаинформацией по всем типам.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
tasksByRowID
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardTask](T_Tessa_Cards_CardTask.htm)>
     Хеш-таблица, содержащая задания, доступ к которым осуществляется по их идентификаторам, для которых должен быть выставлен флаг [CardTaskFlags.HistoryItemCreated], если у задания существует элемент истории, или значение null, если данный флаг не должен выставляться. 
itemRowIDList
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Список идентификаторов записей, которые разрешено загружать среди доступных пользователю записей, или null, если список записей не ограничивается их идентификаторами. 
itemTypeIDList
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Список идентификаторов типов заданий в записях, которые разрешено загружать среди доступных пользователю записей, или null, если список записей не ограничивается типами их заданий. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если информация по истории завершённых заданий была успешно загружена;
false в противном случае.
## __См. также
#### Ссылки
[ICardGetStrategy - ](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
