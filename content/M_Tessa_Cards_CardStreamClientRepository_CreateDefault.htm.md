# CardStreamClientRepository.CreateDefault - метод
Создаёт экземпляр репозитория с конфигурацией клиентских компонентов по
умолчанию, с указанием сервиса для потокового управления карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ICardStreamClientRepository CreateDefault(
    	ICardService cardService,
    	IOperationRepository operationRepository,
    	ICardMetadata cardMetadata,
    	ISession session
    )
VB __Копировать
     Public Shared Function CreateDefault ( 
    	cardService As ICardService,
    	operationRepository As IOperationRepository,
    	cardMetadata As ICardMetadata,
    	session As ISession
    ) As ICardStreamClientRepository
C++ __Копировать
     public:
    static ICardStreamClientRepository^ CreateDefault(
    	ICardService^ cardService, 
    	IOperationRepository^ operationRepository, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session
    )
F# __Копировать
     static member CreateDefault : 
            cardService : ICardService * 
            operationRepository : IOperationRepository * 
            cardMetadata : ICardMetadata * 
            session : ISession -> ICardStreamClientRepository 
#### Параметры
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
