# CardValidationManager - конструктор
Создаёт экземпляр класса с указанием используемого реестра экземпляров
валидаторов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardValidationManager(
    	ICardValidatorRegistry registry,
    	ICardMetadata cardMetadata,
    	ISession session
    )
VB __Копировать
     Public Sub New ( 
    	registry As ICardValidatorRegistry,
    	cardMetadata As ICardMetadata,
    	session As ISession
    )
C++ __Копировать
     public:
    CardValidationManager(
    	ICardValidatorRegistry^ registry, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session
    )
F# __Копировать
     new : 
            registry : ICardValidatorRegistry * 
            cardMetadata : ICardMetadata * 
            session : ISession -> CardValidationManager
#### Параметры
registry
[ICardValidatorRegistry](T_Tessa_Cards_Validation_ICardValidatorRegistry.htm)
    Реестр экземпляров валидаторов, который будет использоваться при валидации.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек, используемая в процессе валидации.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, в процессе работы которого выполняется валидация.
##  __См. также
#### Ссылки
[CardValidationManager - ](T_Tessa_Cards_Validation_CardValidationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
