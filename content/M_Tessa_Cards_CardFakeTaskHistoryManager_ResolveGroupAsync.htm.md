# CardFakeTaskHistoryManager.ResolveGroupAsync - метод
Возвращает группу в истории заданий, вычисленную для заданных параметров. При
необходимости группа будет создана. Также может быть создана родительская
группа, если указан её тип, но в карточке она отсутствует.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardTaskHistoryGroup> ResolveGroupAsync(
    	Card card,
    	ListStorage<CardTaskHistoryGroup> groupsToAdd,
    	IReadOnlyCollection<CardTaskHistoryGroup> allGroups,
    	IValidationResultBuilder validationResult,
    	Guid groupTypeID,
    	Guid? parentGroupTypeID = null,
    	bool newIteration = false,
    	Object placeholderContext = null,
    	bool cardHasNoSections = false,
    	bool noCardInDb = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ResolveGroupAsync ( 
    	card As Card,
    	groupsToAdd As ListStorage(Of CardTaskHistoryGroup),
    	allGroups As IReadOnlyCollection(Of CardTaskHistoryGroup),
    	validationResult As IValidationResultBuilder,
    	groupTypeID As Guid,
    	Optional parentGroupTypeID As Guid? = Nothing,
    	Optional newIteration As Boolean = false,
    	Optional placeholderContext As Object = Nothing,
    	Optional cardHasNoSections As Boolean = false,
    	Optional noCardInDb As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardTaskHistoryGroup)
C++ __Копировать
     public:
    virtual ValueTask<CardTaskHistoryGroup^> ResolveGroupAsync(
    	Card^ card, 
    	ListStorage<CardTaskHistoryGroup^>^ groupsToAdd, 
    	IReadOnlyCollection<CardTaskHistoryGroup^>^ allGroups, 
    	IValidationResultBuilder^ validationResult, 
    	Guid groupTypeID, 
    	Nullable<Guid> parentGroupTypeID = nullptr, 
    	bool newIteration = false, 
    	Object^ placeholderContext = nullptr, 
    	bool cardHasNoSections = false, 
    	bool noCardInDb = false, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ResolveGroupAsync : 
            card : Card * 
            groupsToAdd : ListStorage<CardTaskHistoryGroup> * 
            allGroups : IReadOnlyCollection<CardTaskHistoryGroup> * 
            validationResult : IValidationResultBuilder * 
            groupTypeID : Guid * 
            ?parentGroupTypeID : Nullable<Guid> * 
            ?newIteration : bool * 
            ?placeholderContext : Object * 
            ?cardHasNoSections : bool * 
            ?noCardInDb : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parentGroupTypeID = defaultArg parentGroupTypeID null
            let _newIteration = defaultArg newIteration false
            let _placeholderContext = defaultArg placeholderContext null
            let _cardHasNoSections = defaultArg cardHasNoSections false
            let _noCardInDb = defaultArg noCardInDb false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardTaskHistoryGroup> 
    override ResolveGroupAsync : 
            card : Card * 
            groupsToAdd : ListStorage<CardTaskHistoryGroup> * 
            allGroups : IReadOnlyCollection<CardTaskHistoryGroup> * 
            validationResult : IValidationResultBuilder * 
            groupTypeID : Guid * 
            ?parentGroupTypeID : Nullable<Guid> * 
            ?newIteration : bool * 
            ?placeholderContext : Object * 
            ?cardHasNoSections : bool * 
            ?noCardInDb : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _parentGroupTypeID = defaultArg parentGroupTypeID null
            let _newIteration = defaultArg newIteration false
            let _placeholderContext = defaultArg placeholderContext null
            let _cardHasNoSections = defaultArg cardHasNoSections false
            let _noCardInDb = defaultArg noCardInDb false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardTaskHistoryGroup> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для истории заданий в которой создаётся группа. В карточке достаточно наличие идентификатора, а секции требуются только при указании параметра cardHasNoSections, равного false. В этот объект карточки будут добавлены группы истории заданий. 
groupsToAdd
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)>
Список групп, в которые будет произведено добавление строки с группой для
карточки card. Также по этому списку будет определено, требуется ли создать
группу или использовать существующую, в дополнение к списку allGroups.
Обычно в этом параметре указывается card.TaskHistoryGroups, если карточка card
будет сохранена с новыми группами. Возможны сценарии, когда карточка card
используется как загруженная карточка для плейсхолдеров, а карточка для
сохранения содержится в отдельном объекте, от которого требуется указать
свойство card.TaskHistoryGroups в этом параметре.
allGroups
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)>
Полный список групп в истории заданий для карточки card. По этому списку будет
определено, требуется ли создать группу или использовать существующую, но в
случае создания группа будет добавлена не в эту коллекцию, а в коллекцию
groupsToAdd. Первичный поиск будет выполнен по коллекции groupsToAdd, чтобы
учитывать добавленные группы.
В следующем сценарии вы можете передать значение свойства
card.TaskHistoryGroups в этот параметр: карточка полностью загружается, для
неё добавляются строки в историю заданий, а потом для неё же вызывается метод
card.RemoveAllButChanged() и выполняется сохранение.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Результат валидации, содержащий информацию по проблемам, возникшим при вычислении названия группы Caption (при замене плейсхолдеров). Вычисление названия группы выполняется при добавлении группы, а также при добавлении родительской группы. 
groupTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор типа группы, которую требуется найти или добавить. Информация по уже существующим группам определяется из карточки card. 
parentGroupTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
Идентификатор типа родительской группы.
Если родительская группа указана, то будет выбрана родительская группа
заданного типа с наибольшей итерацией.
Если родительская группа отсутствует, то она будет создана.
newIteration [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
Признак того, что метод всегда добавляет итерацию для группы типа groupTypeID.
Если указано true, то метод создаёт новый экземпляр группы как при её
существовании (тогда увеличивается номер итерации), так и при её отсутствии
(тогда указывается итерация номер 1).
Если указано false, то метод возвращает экземпляр группы без его создания,
если группа заданного типа была найдена (возвращается группа с наибольшей
итерацией); если же группа не найдена, то также создаётся экземпляр группы с
итерацией номер 1.
placeholderContext
[Object](https://learn.microsoft.com/dotnet/api/system.object) (Optional)
     Объект внешнего контекста, передаваемый в плейсхолдеры при формировании названия экземпляра группы (в т.ч. родительской группы). Название формируется только при добавлении соответствующей группы. Если задано null, то в контекст плейсхолдеров не передаётся такой контекст. 
cardHasNoSections
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что карточка card не содержит секций для плейсхолдеров, поэтому плейсхолдеры, использующие строковые и коллекционные секции карточки, будут запрашивать их из базы данных по идентификатору карточки. Если также указан параметр noCardInDb, равный true, то такие плейсхолдеры не будут возвращать данных. 
noCardInDb [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что карточка card по соответствующему идентификатору отсутствует в базе данных (например, карточка ещё не создана или карточка является виртуальной), поэтому при замене плейсхолдеров не будут генерироваться SQL-запросы (не будет возможности выполнять объединение с данными других таблиц). 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)>  
Созданная или найденная строка с информацией по группе в истории заданий,
которая соответствует переданным параметрами, или null, если не удалось
создать группу (например, ошибки в плейсхолдерах в карточке типа группы).
Возникшие ошибки и предупреждения будут содержаться в объекте
validationResult.
#### Реализации
[ICardTaskHistoryManager.ResolveGroupAsync(Card,
ListStorage<CardTaskHistoryGroup>, IReadOnlyCollection<CardTaskHistoryGroup>,
IValidationResultBuilder, Guid, Nullable<Guid>, Boolean, Object, Boolean,
Boolean,
CancellationToken)](M_Tessa_Cards_ICardTaskHistoryManager_ResolveGroupAsync.htm)  
##  __См. также
#### Ссылки
[CardFakeTaskHistoryManager - ](T_Tessa_Cards_CardFakeTaskHistoryManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
