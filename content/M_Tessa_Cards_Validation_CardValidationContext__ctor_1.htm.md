# CardValidationContext(Card, CardType, CardStoreMode, ICardMetadata,
ISession, ISerializableObject, ICardValidationLimitationManager,
CardValidationMode, ICardMetadataBinder, CancellationToken) - конструктор
Создаёт экземпляр класса с указанием основной карточки, валидацию которых
требуется выполнить. После вызова конструктора используется асинхронную
инициализацию в методе
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardValidationContext(
    	Card mainCard,
    	CardType mainCardType,
    	CardStoreMode storeMode,
    	ICardMetadata cardMetadata,
    	ISession session,
    	ISerializableObject externalContextInfo = null,
    	ICardValidationLimitationManager limitations = null,
    	CardValidationMode validationMode = CardValidationMode.Card,
    	ICardMetadataBinder mainCardMetadataBinder = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	mainCard As Card,
    	mainCardType As CardType,
    	storeMode As CardStoreMode,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional externalContextInfo As ISerializableObject = Nothing,
    	Optional limitations As ICardValidationLimitationManager = Nothing,
    	Optional validationMode As CardValidationMode = CardValidationMode.Card,
    	Optional mainCardMetadataBinder As ICardMetadataBinder = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardValidationContext(
    	Card^ mainCard, 
    	CardType^ mainCardType, 
    	CardStoreMode storeMode, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ISerializableObject^ externalContextInfo = nullptr, 
    	ICardValidationLimitationManager^ limitations = nullptr, 
    	CardValidationMode validationMode = CardValidationMode::Card, 
    	ICardMetadataBinder^ mainCardMetadataBinder = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            mainCard : Card * 
            mainCardType : CardType * 
            storeMode : CardStoreMode * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?externalContextInfo : ISerializableObject * 
            ?limitations : ICardValidationLimitationManager * 
            ?validationMode : CardValidationMode * 
            ?mainCardMetadataBinder : ICardMetadataBinder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _externalContextInfo = defaultArg externalContextInfo null
            let _limitations = defaultArg limitations null
            let _validationMode = defaultArg validationMode CardValidationMode.Card
            let _mainCardMetadataBinder = defaultArg mainCardMetadataBinder null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardValidationContext
#### Параметры
mainCard [Card](T_Tessa_Cards_Card.htm)
    Основная карточка, валидацию которой требуется выполнить.
mainCardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип основной карточки, валидацию которой требуется выполнить.
storeMode [CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)
    Способ сохранения проверяемого объекта - карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек, используемая в процессе валидации.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, в процессе работы которого выполняется валидация.
externalContextInfo
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
(Optional)
     Произвольно структурированная информация из внешнего контекста (например, контекста сохранения карточки), которая может быть заполнена валидатором и использована либо другими валидаторами, либо внешними расширениями. Значение null определяет, что внешний контекст неизвестен и для свойства будет создан пустой объект. 
limitations
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)
(Optional)
     Объект, ограничивающий доступность объектов для валидации, или null, если будет создан объект по умолчанию, в котором отсутствуют ограничения. 
validationMode
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)
(Optional)
     Способ выполнения валидации. По умолчанию рекомендуется использовать [Card](T_Tessa_Cards_Validation_CardValidationMode.htm). 
mainCardMetadataBinder
[ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)
(Optional)
     Объект, выполняющий действия с основной карточкой, для которой выполняется валидация, или null, если объект создаётся с параметрами по умолчанию. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[CardValidationContext -
перегрузка](Overload_Tessa_Cards_Validation_CardValidationContext__ctor.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
