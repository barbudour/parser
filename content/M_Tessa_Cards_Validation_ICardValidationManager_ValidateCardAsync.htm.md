# ICardValidationManager.ValidateCardAsync - метод
Выполняет валидацию основной карточки для заданного списка валидаторов.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ICardValidationResult> ValidateCardAsync(
    	IEnumerable<CardTypeValidator> validators,
    	Guid mainCardTypeID,
    	Card mainCard,
    	CardStoreMode storeMode,
    	ISerializableObject externalContextInfo = null,
    	Func<ICardValidationContext, ValueTask> modifyContextActionAsync = null,
    	CardValidationMode validationMode = CardValidationMode.Card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ValidateCardAsync ( 
    	validators As IEnumerable(Of CardTypeValidator),
    	mainCardTypeID As Guid,
    	mainCard As Card,
    	storeMode As CardStoreMode,
    	Optional externalContextInfo As ISerializableObject = Nothing,
    	Optional modifyContextActionAsync As Func(Of ICardValidationContext, ValueTask) = Nothing,
    	Optional validationMode As CardValidationMode = CardValidationMode.Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ICardValidationResult)
C++ __Копировать
    Task<ICardValidationResult^>^ ValidateCardAsync(
    	IEnumerable<CardTypeValidator^>^ validators, 
    	Guid mainCardTypeID, 
    	Card^ mainCard, 
    	CardStoreMode storeMode, 
    	ISerializableObject^ externalContextInfo = nullptr, 
    	Func<ICardValidationContext^, ValueTask>^ modifyContextActionAsync = nullptr, 
    	CardValidationMode validationMode = CardValidationMode::Card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ValidateCardAsync : 
            validators : IEnumerable<CardTypeValidator> * 
            mainCardTypeID : Guid * 
            mainCard : Card * 
            storeMode : CardStoreMode * 
            ?externalContextInfo : ISerializableObject * 
            ?modifyContextActionAsync : Func<ICardValidationContext, ValueTask> * 
            ?validationMode : CardValidationMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _externalContextInfo = defaultArg externalContextInfo null
            let _modifyContextActionAsync = defaultArg modifyContextActionAsync null
            let _validationMode = defaultArg validationMode CardValidationMode.Card
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
    Способ сохранения проверяемого объекта - карточки или файла.
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
     Способ выполнения валидации. По умолчанию рекомендуется использовать [CardValidationMode.Card]. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ICardValidationResult](T_Tessa_Cards_Validation_ICardValidationResult.htm)>  
Результат валидации основной карточки для заданного списка валидаторов.
##  __См. также
#### Ссылки
[ICardValidationManager -
](T_Tessa_Cards_Validation_ICardValidationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
