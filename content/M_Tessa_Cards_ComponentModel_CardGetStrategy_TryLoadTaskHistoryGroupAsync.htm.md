# CardGetStrategy.TryLoadTaskHistoryGroupAsync - метод
Загружает информацию по группе в истории завершённых заданий карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardTaskHistoryGroup> TryLoadTaskHistoryGroupAsync(
    	Guid rowID,
    	Card card,
    	DbManager db,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryLoadTaskHistoryGroupAsync ( 
    	rowID As Guid,
    	card As Card,
    	db As DbManager,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardTaskHistoryGroup)
C++ __Копировать
     public:
    virtual Task<CardTaskHistoryGroup^>^ TryLoadTaskHistoryGroupAsync(
    	Guid rowID, 
    	Card^ card, 
    	DbManager^ db, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryLoadTaskHistoryGroupAsync : 
            rowID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardTaskHistoryGroup> 
    override TryLoadTaskHistoryGroupAsync : 
            rowID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardTaskHistoryGroup> 
#### Параметры
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор группы в истории завершённых заданий, которую требуется загрузить.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую добавляется информация о загруженной группе в истории завершённых заданий.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по загружаемым типам заданий. Передайте объект с метаинформацией по всем типам.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)>  
Загруженная информация по группе в истории завершённых заданий карточки или
null, если запись не найдена по идентификатору или при загрузке произошла
ошибка.
#### Реализации
[ICardGetStrategy.TryLoadTaskHistoryGroupAsync(Guid, Card, DbManager,
ICardMetadata, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadTaskHistoryGroupAsync.htm)  
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
