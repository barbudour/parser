# CardStreamClientRepository - конструктор
Создаёт новый экземпляр класса с указанием компонентов репозитория.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamClientRepository(
    	ICardStreamClientGetComponent streamClientGetComponent,
    	ICardStreamClientStoreComponent streamClientStoreComponent,
    	ICardMetadata cardMetadata,
    	ISession session
    )
VB __Копировать
     Public Sub New ( 
    	streamClientGetComponent As ICardStreamClientGetComponent,
    	streamClientStoreComponent As ICardStreamClientStoreComponent,
    	cardMetadata As ICardMetadata,
    	session As ISession
    )
C++ __Копировать
     public:
    CardStreamClientRepository(
    	ICardStreamClientGetComponent^ streamClientGetComponent, 
    	ICardStreamClientStoreComponent^ streamClientStoreComponent, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session
    )
F# __Копировать
     new : 
            streamClientGetComponent : ICardStreamClientGetComponent * 
            streamClientStoreComponent : ICardStreamClientStoreComponent * 
            cardMetadata : ICardMetadata * 
            session : ISession -> CardStreamClientRepository
#### Параметры
streamClientGetComponent
[ICardStreamClientGetComponent](T_Tessa_Cards_ComponentModel_ICardStreamClientGetComponent.htm)
    Компонент потокового получения контента файлов на клиенте.
streamClientStoreComponent
[ICardStreamClientStoreComponent](T_Tessa_Cards_ComponentModel_ICardStreamClientStoreComponent.htm)
    Компонент потокового сохранения карточки на клиенте.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия, в рамках которой выполняются операции.
##  __См. также
#### Ссылки
[CardStreamClientRepository - ](T_Tessa_Cards_CardStreamClientRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
