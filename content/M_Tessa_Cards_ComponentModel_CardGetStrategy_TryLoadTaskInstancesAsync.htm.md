# CardGetStrategy.TryLoadTaskInstancesAsync - метод
Загружает общую информацию по экземплярам заданий, приложенных к заданной
карточке, и возвращает список контекстов операций по загрузке каждого из
заданий или null, если загрузку произвести не удалось.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IList<CardGetContext>> TryLoadTaskInstancesAsync(
    	Guid cardID,
    	Card card,
    	DbManager db,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	Guid sessionUserID,
    	CardNewMode newMode = CardNewMode.Default,
    	CardGetTaskMode getTaskMode = CardGetTaskMode.Default,
    	bool loadCalendarInfo = true,
    	Dictionary<Guid, CardTask> tasksByRowID = null,
    	IList<Guid> authorTaskRowIDList = null,
    	IEnumerable<Guid> taskRowIDList = null,
    	IEnumerable<Guid> taskTypeIDList = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryLoadTaskInstancesAsync ( 
    	cardID As Guid,
    	card As Card,
    	db As DbManager,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	sessionUserID As Guid,
    	Optional newMode As CardNewMode = CardNewMode.Default,
    	Optional getTaskMode As CardGetTaskMode = CardGetTaskMode.Default,
    	Optional loadCalendarInfo As Boolean = true,
    	Optional tasksByRowID As Dictionary(Of Guid, CardTask) = Nothing,
    	Optional authorTaskRowIDList As IList(Of Guid) = Nothing,
    	Optional taskRowIDList As IEnumerable(Of Guid) = Nothing,
    	Optional taskTypeIDList As IEnumerable(Of Guid) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IList(Of CardGetContext))
C++ __Копировать
     public:
    virtual Task<IList<CardGetContext^>^>^ TryLoadTaskInstancesAsync(
    	Guid cardID, 
    	Card^ card, 
    	DbManager^ db, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	Guid sessionUserID, 
    	CardNewMode newMode = CardNewMode::Default, 
    	CardGetTaskMode getTaskMode = CardGetTaskMode::Default, 
    	bool loadCalendarInfo = true, 
    	Dictionary<Guid, CardTask^>^ tasksByRowID = nullptr, 
    	IList<Guid>^ authorTaskRowIDList = nullptr, 
    	IEnumerable<Guid>^ taskRowIDList = nullptr, 
    	IEnumerable<Guid>^ taskTypeIDList = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryLoadTaskInstancesAsync : 
            cardID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            sessionUserID : Guid * 
            ?newMode : CardNewMode * 
            ?getTaskMode : CardGetTaskMode * 
            ?loadCalendarInfo : bool * 
            ?tasksByRowID : Dictionary<Guid, CardTask> * 
            ?authorTaskRowIDList : IList<Guid> * 
            ?taskRowIDList : IEnumerable<Guid> * 
            ?taskTypeIDList : IEnumerable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _newMode = defaultArg newMode CardNewMode.Default
            let _getTaskMode = defaultArg getTaskMode CardGetTaskMode.Default
            let _loadCalendarInfo = defaultArg loadCalendarInfo true
            let _tasksByRowID = defaultArg tasksByRowID null
            let _authorTaskRowIDList = defaultArg authorTaskRowIDList null
            let _taskRowIDList = defaultArg taskRowIDList null
            let _taskTypeIDList = defaultArg taskTypeIDList null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<CardGetContext>> 
    override TryLoadTaskInstancesAsync : 
            cardID : Guid * 
            card : Card * 
            db : DbManager * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            sessionUserID : Guid * 
            ?newMode : CardNewMode * 
            ?getTaskMode : CardGetTaskMode * 
            ?loadCalendarInfo : bool * 
            ?tasksByRowID : Dictionary<Guid, CardTask> * 
            ?authorTaskRowIDList : IList<Guid> * 
            ?taskRowIDList : IEnumerable<Guid> * 
            ?taskTypeIDList : IEnumerable<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _newMode = defaultArg newMode CardNewMode.Default
            let _getTaskMode = defaultArg getTaskMode CardGetTaskMode.Default
            let _loadCalendarInfo = defaultArg loadCalendarInfo true
            let _tasksByRowID = defaultArg tasksByRowID null
            let _authorTaskRowIDList = defaultArg authorTaskRowIDList null
            let _taskRowIDList = defaultArg taskRowIDList null
            let _taskTypeIDList = defaultArg taskTypeIDList null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IList<CardGetContext>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, информацию по заданиям которой требуется загрузить.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую добавляется информация по заданиям.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по загружаемым типам заданий. Передайте объект с метаинформацией по всем типам.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, осуществляющий построение результата валидации.
sessionUserID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор пользователя, от имени которого выполняется загрузка заданий.
newMode [CardNewMode](T_Tessa_Cards_CardNewMode.htm) (Optional)
    Способ заполнения данных в виртуальных секциях.
getTaskMode [CardGetTaskMode](T_Tessa_Cards_CardGetTaskMode.htm) (Optional)
    Способ загрузки заданий в карточке.
loadCalendarInfo
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что требуется загружать информацию по бизнес-календарю, например, сколько времени осталось до запланированного завершения задания. 
tasksByRowID
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardTask](T_Tessa_Cards_CardTask.htm)> (Optional)
     Dictionary заданий карточки по идентификаторам, если не null - будет заполнен загруженными заданиями и в последствии (при загрузке истории заданий) для заданий с созданным элементом истории будет проставлен соответствующий флаг. 
authorTaskRowIDList
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Список идентификаторов заданий, все данные которых будут полностью загружены, если такие задания доступны от имени автора. 
taskRowIDList
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Список идентификаторов заданий, которые разрешено загружать среди доступных пользователю заданий, или null, если список заданий не ограничивается их идентификаторами. 
taskTypeIDList
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Список идентификаторов типов заданий, которые разрешено загружать среди доступных пользователю заданий, или null, если список заданий не ограничивается их типами. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardGetContext](T_Tessa_Cards_ComponentModel_CardGetContext.htm)>>  
Список контекстов операций по загрузке каждого из заданий заданной карточки
или null, если не удалось загрузить информацию о заданиях карточки.
#### Реализации
[ICardGetStrategy.TryLoadTaskInstancesAsync(Guid, Card, DbManager,
ICardMetadata, IValidationResultBuilder, Guid, CardNewMode, CardGetTaskMode,
Boolean, Dictionary<Guid, CardTask>, IList<Guid>, IEnumerable<Guid>,
IEnumerable<Guid>,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_TryLoadTaskInstancesAsync.htm)  
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
