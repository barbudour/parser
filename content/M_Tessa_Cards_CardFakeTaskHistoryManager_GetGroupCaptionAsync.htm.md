# CardFakeTaskHistoryManager.GetGroupCaptionAsync - метод
Возвращает название новой группы в истории заданий для заданных параметров.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<string> GetGroupCaptionAsync(
    	Card card,
    	IValidationResultBuilder validationResult,
    	Guid groupTypeID,
    	int iteration,
    	Object placeholderContext = null,
    	bool cardHasNoSections = false,
    	bool noCardInDb = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetGroupCaptionAsync ( 
    	card As Card,
    	validationResult As IValidationResultBuilder,
    	groupTypeID As Guid,
    	iteration As Integer,
    	Optional placeholderContext As Object = Nothing,
    	Optional cardHasNoSections As Boolean = false,
    	Optional noCardInDb As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
     public:
    virtual Task<String^>^ GetGroupCaptionAsync(
    	Card^ card, 
    	IValidationResultBuilder^ validationResult, 
    	Guid groupTypeID, 
    	int iteration, 
    	Object^ placeholderContext = nullptr, 
    	bool cardHasNoSections = false, 
    	bool noCardInDb = false, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetGroupCaptionAsync : 
            card : Card * 
            validationResult : IValidationResultBuilder * 
            groupTypeID : Guid * 
            iteration : int * 
            ?placeholderContext : Object * 
            ?cardHasNoSections : bool * 
            ?noCardInDb : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _placeholderContext = defaultArg placeholderContext null
            let _cardHasNoSections = defaultArg cardHasNoSections false
            let _noCardInDb = defaultArg noCardInDb false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
    override GetGroupCaptionAsync : 
            card : Card * 
            validationResult : IValidationResultBuilder * 
            groupTypeID : Guid * 
            iteration : int * 
            ?placeholderContext : Object * 
            ?cardHasNoSections : bool * 
            ?noCardInDb : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _placeholderContext = defaultArg placeholderContext null
            let _cardHasNoSections = defaultArg cardHasNoSections false
            let _noCardInDb = defaultArg noCardInDb false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
     Карточка, для которой вычисляется название группы. В карточке должны быть загружены значения во всех секциях для корректной работы плейсхолдеров. 
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Результат валидации, содержащий информацию по проблемам, возникшим при вычислении названия группы Caption (при замене плейсхолдеров). 
groupTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа группы, для которой требуется определить название группы. Должно быть равно 1 или больше.
iteration [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Номер итерации группы, для которого определяется название группы.
placeholderContext
[Object](https://learn.microsoft.com/dotnet/api/system.object) (Optional)
     Объект внешнего контекста, передаваемый в плейсхолдеры при формировании названия экземпляра группы. 
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
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Название группы в истории заданий, которое соответствует переданным
параметрами, или null, если не удалось определить название группы (например,
ошибки в плейсхолдерах в карточке типа группы). Возникшие ошибки и
предупреждения будут содержаться в объекте validationResult.
#### Реализации
[ICardTaskHistoryManager.GetGroupCaptionAsync(Card, IValidationResultBuilder,
Guid, Int32, Object, Boolean, Boolean,
CancellationToken)](M_Tessa_Cards_ICardTaskHistoryManager_GetGroupCaptionAsync.htm)  
##  __См. также
#### Ссылки
[CardFakeTaskHistoryManager - ](T_Tessa_Cards_CardFakeTaskHistoryManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
