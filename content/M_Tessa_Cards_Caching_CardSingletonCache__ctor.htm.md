# CardSingletonCache - конструктор
Создаёт экземпляр класса с указанием требуемых зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSingletonCache(
    	ICardRepository cardRepository,
    	ICardMetadata cardMetadata,
    	ISession session,
    	[OptionalDependencyAttribute] ITessaServerSettings serverSettings = null,
    	[OptionalDependencyAttribute] IDbScope dbScope = null
    )
VB __Копировать
     Public Sub New ( 
    	cardRepository As ICardRepository,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	<OptionalDependencyAttribute> Optional serverSettings As ITessaServerSettings = Nothing,
    	<OptionalDependencyAttribute> Optional dbScope As IDbScope = Nothing
    )
C++ __Копировать
     public:
    CardSingletonCache(
    	ICardRepository^ cardRepository, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	[OptionalDependencyAttribute] ITessaServerSettings^ serverSettings = nullptr, 
    	[OptionalDependencyAttribute] IDbScope^ dbScope = nullptr
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            [<OptionalDependencyAttribute>] ?serverSettings : ITessaServerSettings * 
            [<OptionalDependencyAttribute>] ?dbScope : IDbScope 
    (* Defaults:
            let _serverSettings = defaultArg serverSettings null
            let _dbScope = defaultArg dbScope null
    *)
    -> CardSingletonCache
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия текущего пользователя.
serverSettings
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm) (Optional)
    Настройки сервера.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
     Объект для взаимодействия с базой данных или null, если объект не имеет соединения с базой данных. 
## __См. также
#### Ссылки
[CardSingletonCache - ](T_Tessa_Cards_Caching_CardSingletonCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
