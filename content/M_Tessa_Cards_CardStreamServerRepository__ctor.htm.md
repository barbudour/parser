# CardStreamServerRepository - конструктор
Создаёт новый экземпляр класса с указанием метаинформации по типам карточек,
объекта сессии и компонентов репозитория.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamServerRepository(
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardStreamServerGetComponent streamServerGetComponent,
    	ICardStreamServerStoreComponent streamServerStoreComponent
    )
VB __Копировать
     Public Sub New ( 
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	streamServerGetComponent As ICardStreamServerGetComponent,
    	streamServerStoreComponent As ICardStreamServerStoreComponent
    )
C++ __Копировать
     public:
    CardStreamServerRepository(
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardStreamServerGetComponent^ streamServerGetComponent, 
    	ICardStreamServerStoreComponent^ streamServerStoreComponent
    )
F# __Копировать
     new : 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            streamServerGetComponent : ICardStreamServerGetComponent * 
            streamServerStoreComponent : ICardStreamServerStoreComponent -> CardStreamServerRepository
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия, в рамках которой выполняются операции.
streamServerGetComponent
[ICardStreamServerGetComponent](T_Tessa_Cards_ComponentModel_ICardStreamServerGetComponent.htm)
    Компонент потокового получения контента файлов на сервере.
streamServerStoreComponent
[ICardStreamServerStoreComponent](T_Tessa_Cards_ComponentModel_ICardStreamServerStoreComponent.htm)
    Компонент потокового сохранения карточки на сервере.
##  __См. также
#### Ссылки
[CardStreamServerRepository - ](T_Tessa_Cards_CardStreamServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
