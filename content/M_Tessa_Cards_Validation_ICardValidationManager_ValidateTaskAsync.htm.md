# ICardValidationManager.ValidateTaskAsync - метод
Выполняет валидацию основной карточки и её карточки задания для заданного
списка валидаторов.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ICardValidationResult> ValidateTaskAsync(
    	IEnumerable<CardTypeValidator> validators,
    	Guid mainCardTypeID,
    	Card mainCard,
    	CardStoreMode storeMode,
    	Guid taskCardTypeID,
    	Card taskCard,
    	ISerializableObject externalContextInfo = null,
    	Func<ICardValidationContext, ValueTask> modifyContextActionAsync = null,
    	CardValidationMode validationMode = CardValidationMode.Task,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ValidateTaskAsync ( 
    	validators As IEnumerable(Of CardTypeValidator),
    	mainCardTypeID As Guid,
    	mainCard As Card,
    	storeMode As CardStoreMode,
    	taskCardTypeID As Guid,
    	taskCard As Card,
    	Optional externalContextInfo As ISerializableObject = Nothing,
    	Optional modifyContextActionAsync As Func(Of ICardValidationContext, ValueTask) = Nothing,
    	Optional validationMode As CardValidationMode = CardValidationMode.Task,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardValidationResult)
C++ __Копировать
    Task<ICardValidationResult^>^ ValidateTaskAsync(
    	IEnumerable<CardTypeValidator^>^ validators, 
    	Guid mainCardTypeID, 
    	Card^ mainCard, 
    	CardStoreMode storeMode, 
    	Guid taskCardTypeID, 
    	Card^ taskCard, 
    	ISerializableObject^ externalContextInfo = nullptr, 
    	Func<ICardValidationContext^, ValueTask>^ modifyContextActionAsync = nullptr, 
    	CardValidationMode validationMode = CardValidationMode::Task, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ValidateTaskAsync : 
            validators : IEnumerable<CardTypeValidator> * 
            mainCardTypeID : Guid * 
            mainCard : Card * 
            storeMode : CardStoreMode * 
            taskCardTypeID : Guid * 
            taskCard : Card * 
            ?externalContextInfo : ISerializableObject * 
            ?modifyContextActionAsync : Func<ICardValidationContext, ValueTask> * 
            ?validationMode : CardValidationMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _externalContextInfo = defaultArg externalContextInfo null
            let _modifyContextActionAsync = defaultArg modifyContextActionAsync null
            let _validationMode = defaultArg validationMode CardValidationMode.Task
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ICardValidationResult> 
#### Параметры
validators
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)>
    Список валидаторов, посредством которых будет выполняться валидация.
mainCardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа основной карточки, валидация которой выполняется.
mainCard [Card](T_Tessa_Cards_Card.htm)
    Основная карточка, валидация которой выполняется.
storeMode [CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)
    Способ сохранения проверяемого объекта - задания.
taskCardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки задания, валидация которой выполняется.
taskCard [Card](T_Tessa_Cards_Card.htm)
     Карточка задания, валидация которой выполняется, или null, если задание завершается без данных карточки. 
externalContextInfo
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
(Optional)
     Произвольно структурированная информация из внешнего контекста (например, контекста сохранения карточки), которая может быть заполнена валидатором и использована либо другими валидаторами, либо внешними расширениями. Значение null определяет, что внешний контекст неизвестен и для свойства будет создан пустой объект. 
modifyContextActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Действие, выполняющее изменение контекста валидации перед его использованием, или null, если такое действие не требуется. Действие может использоваться, например, для указания ограничений по секциям валидации. 
validationMode
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)
(Optional)
     Способ выполнения валидации. По умолчанию рекомендуется использовать [CardValidationMode.Task]. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardValidationResult](T_Tessa_Cards_Validation_ICardValidationResult.htm)>  
Результат валидации основной карточки и её карточки задания для заданного
списка валидаторов.
##  __См. также
#### Ссылки
[ICardValidationManager -
](T_Tessa_Cards_Validation_ICardValidationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
