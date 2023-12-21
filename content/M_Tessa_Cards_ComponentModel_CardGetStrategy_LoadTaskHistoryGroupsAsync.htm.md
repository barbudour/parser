# CardGetStrategy.LoadTaskHistoryGroupsAsync - метод
Загружает информацию по группам истории завершённых заданий карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> LoadTaskHistoryGroupsAsync(
    	Guid cardID,
    	Card card,
    	DbManager db,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	IEnumerable<Guid> itemRowIDList = null,
    	IEnumerable<Guid> itemTypeIDList = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function LoadTaskHistoryGroupsAsync ( 
    	cardID As Guid,
    	card As Card,
    	db As DbManager,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	Optional itemRowIDList As IEnumerable(Of Guid) = Nothing,
    	Optional itemTypeIDList As IEnumerable(Of Guid) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ LoadTaskHistoryGroupsAsync(
    	Guid cardID, 
    	Card^ card, 
    	DbManager^ db, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	IEnumerable<Guid>^ itemRowIDList = nullptr, 
    	IEnumerable<Guid>^ itemTypeIDList = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract LoadTaskHistoryGroupsAsync : 
            cardID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?itemRowIDList : IEnumerable<Guid> * 
            ?itemTypeIDList : IEnumerable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _itemRowIDList = defaultArg itemRowIDList null
            let _itemTypeIDList = defaultArg itemTypeIDList null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override LoadTaskHistoryGroupsAsync : 
            cardID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
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
    Идентификатор карточки, информацию по группам истории завершённых заданий которой требуется загрузить.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую добавляется информацию по группам истории завершённых заданий.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по загружаемым типам заданий. Передайте объект с метаинформацией по всем типам.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
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
#### Реализации
[ICardGetStrategy.LoadTaskHistoryGroupsAsync(Guid, Card, DbManager,
ICardMetadata, IValidationResultBuilder, IEnumerable<Guid>, IEnumerable<Guid>,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadTaskHistoryGroupsAsync.htm)  
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
