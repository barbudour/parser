# CardStreamClientRepository.CreateExtended - метод
Создаёт экземпляр репозитория с расширенной конфигурацией клиентских
компонентов по умолчанию, с указанием контейнера с используемыми расширениями
и сервиса для потокового управления карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ICardStreamClientRepository CreateExtended(
    	IExtensionContainer extensionContainer,
    	ICardService cardService,
    	IOperationRepository operationRepository,
    	ICardMetadata cardMetadata,
    	ISession session
    )
VB __Копировать
     Public Shared Function CreateExtended ( 
    	extensionContainer As IExtensionContainer,
    	cardService As ICardService,
    	operationRepository As IOperationRepository,
    	cardMetadata As ICardMetadata,
    	session As ISession
    ) As ICardStreamClientRepository
C++ __Копировать
     public:
    static ICardStreamClientRepository^ CreateExtended(
    	IExtensionContainer^ extensionContainer, 
    	ICardService^ cardService, 
    	IOperationRepository^ operationRepository, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session
    )
F# __Копировать
     static member CreateExtended : 
            extensionContainer : IExtensionContainer * 
            cardService : ICardService * 
            operationRepository : IOperationRepository * 
            cardMetadata : ICardMetadata * 
            session : ISession -> ICardStreamClientRepository 
#### Параметры
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер с используемыми расширениями.
cardService [ICardService](T_Tessa_Cards_ICardService.htm)
    Сервис для управления карточками.
operationRepository
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm)
    Репозиторий, управляющий операциями.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия, в рамках которой выполняются операции.
#### Возвращаемое значение
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)  
Созданный экземпляр репозитория.
##  __См. также
#### Ссылки
[CardStreamClientRepository - ](T_Tessa_Cards_CardStreamClientRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
