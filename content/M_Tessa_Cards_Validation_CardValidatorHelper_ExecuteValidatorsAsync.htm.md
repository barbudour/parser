# CardValidatorHelper.ExecuteValidatorsAsync - метод
Выполняет валидаторы для заданной карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task ExecuteValidatorsAsync(
    	Card card,
    	CardType cardType,
    	ICardMetadata cardMetadata,
    	IValidationResultBuilder validationResult,
    	ICardValidationManager validationManager,
    	ISerializableObject externalContextInfo = null,
    	CardValidationMode cardValidationMode = CardValidationMode.Card,
    	CardValidationMode taskValidationMode = CardValidationMode.Task,
    	Func<ICardMetadataBinder, ICardMetadataBinder> createCardMetadataBinderAdapterFunc = null,
    	bool skipFiles = false,
    	bool skipTasks = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function ExecuteValidatorsAsync ( 
    	card As Card,
    	cardType As CardType,
    	cardMetadata As ICardMetadata,
    	validationResult As IValidationResultBuilder,
    	validationManager As ICardValidationManager,
    	Optional externalContextInfo As ISerializableObject = Nothing,
    	Optional cardValidationMode As CardValidationMode = CardValidationMode.Card,
    	Optional taskValidationMode As CardValidationMode = CardValidationMode.Task,
    	Optional createCardMetadataBinderAdapterFunc As Func(Of ICardMetadataBinder, ICardMetadataBinder) = Nothing,
    	Optional skipFiles As Boolean = false,
    	Optional skipTasks As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ ExecuteValidatorsAsync(
    	Card^ card, 
    	CardType^ cardType, 
    	ICardMetadata^ cardMetadata, 
    	IValidationResultBuilder^ validationResult, 
    	ICardValidationManager^ validationManager, 
    	ISerializableObject^ externalContextInfo = nullptr, 
    	CardValidationMode cardValidationMode = CardValidationMode::Card, 
    	CardValidationMode taskValidationMode = CardValidationMode::Task, 
    	Func<ICardMetadataBinder^, ICardMetadataBinder^>^ createCardMetadataBinderAdapterFunc = nullptr, 
    	bool skipFiles = false, 
    	bool skipTasks = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member ExecuteValidatorsAsync : 
            card : Card * 
            cardType : CardType * 
            cardMetadata : ICardMetadata * 
            validationResult : IValidationResultBuilder * 
            validationManager : ICardValidationManager * 
            ?externalContextInfo : ISerializableObject * 
            ?cardValidationMode : CardValidationMode * 
            ?taskValidationMode : CardValidationMode * 
            ?createCardMetadataBinderAdapterFunc : Func<ICardMetadataBinder, ICardMetadataBinder> * 
            ?skipFiles : bool * 
            ?skipTasks : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _externalContextInfo = defaultArg externalContextInfo null
            let _cardValidationMode = defaultArg cardValidationMode CardValidationMode.Card
            let _taskValidationMode = defaultArg taskValidationMode CardValidationMode.Task
            let _createCardMetadataBinderAdapterFunc = defaultArg createCardMetadataBinderAdapterFunc null
            let _skipFiles = defaultArg skipFiles false
            let _skipTasks = defaultArg skipTasks false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой выполняются валидаторы.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, для которого выполняются валидаторы.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам файлов и заданий.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации, в который будут добавлены все сообщения.
validationManager
[ICardValidationManager](T_Tessa_Cards_Validation_ICardValidationManager.htm)
    Объект, управляющий валидацией карточки.
externalContextInfo
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
(Optional)
     Информация из внешнего контекста валидации или null, если внешний контекст не указан. 
cardValidationMode
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)
(Optional)
    Способ выполнения валидации для карточек и файлов.
taskValidationMode
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)
(Optional)
    Способ выполнения валидации для заданий.
createCardMetadataBinderAdapterFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm),
[ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)>
(Optional)
     Функция, создающая адаптер для объекта [ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm), используемого для основной карточки или для карточки задания, или null, если адаптер не требуется. Создайте объект x => new CardUIMetadataBinder(x), чтобы выполнять действия с карточками в потоке UI. 
skipFiles [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что валидацию файлов не требуется выполнять.
skipTasks [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что валидацию заданий не требуется выполнять.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
