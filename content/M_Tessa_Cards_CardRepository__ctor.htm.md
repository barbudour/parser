# CardRepository - конструктор
Создаёт экземпляр репозитория с указанием метаинформации по типам карточек,
объекта сессии текущего пользователя и используемых компонентов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardRepository(
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardNewComponent newComponent,
    	ICardGetComponent getComponent,
    	ICardStoreComponent storeComponent,
    	ICardDeleteComponent deleteComponent,
    	ICardRequestComponent requestComponent
    )
VB __Копировать
     Public Sub New ( 
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	newComponent As ICardNewComponent,
    	getComponent As ICardGetComponent,
    	storeComponent As ICardStoreComponent,
    	deleteComponent As ICardDeleteComponent,
    	requestComponent As ICardRequestComponent
    )
C++ __Копировать
     public:
    CardRepository(
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardNewComponent^ newComponent, 
    	ICardGetComponent^ getComponent, 
    	ICardStoreComponent^ storeComponent, 
    	ICardDeleteComponent^ deleteComponent, 
    	ICardRequestComponent^ requestComponent
    )
F# __Копировать
     new : 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            newComponent : ICardNewComponent * 
            getComponent : ICardGetComponent * 
            storeComponent : ICardStoreComponent * 
            deleteComponent : ICardDeleteComponent * 
            requestComponent : ICardRequestComponent -> CardRepository
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия, в рамках которой выполняются операции.
newComponent
[ICardNewComponent](T_Tessa_Cards_ComponentModel_ICardNewComponent.htm)
    Компонент для создания заполненной структуры карточки.
getComponent
[ICardGetComponent](T_Tessa_Cards_ComponentModel_ICardGetComponent.htm)
    Компонент для чтения карточки.
storeComponent
[ICardStoreComponent](T_Tessa_Cards_ComponentModel_ICardStoreComponent.htm)
    Компонент для сохранения карточки.
deleteComponent
[ICardDeleteComponent](T_Tessa_Cards_ComponentModel_ICardDeleteComponent.htm)
    Компонент для удаления карточки.
requestComponent
[ICardRequestComponent](T_Tessa_Cards_ComponentModel_ICardRequestComponent.htm)
    Компонент, универсальный запрос к сервису карточек.
##  __См. также
#### Ссылки
[CardRepository - ](T_Tessa_Cards_CardRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
