# CardContextRoleCache - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardContextRoleCache(
    	ICardCache cardCache,
    	ICardRepository cardRepository,
    	ISession session
    )
VB __Копировать
     Public Sub New ( 
    	cardCache As ICardCache,
    	cardRepository As ICardRepository,
    	session As ISession
    )
C++ __Копировать
     public:
    CardContextRoleCache(
    	ICardCache^ cardCache, 
    	ICardRepository^ cardRepository, 
    	ISession^ session
    )
F# __Копировать
     new : 
            cardCache : ICardCache * 
            cardRepository : ICardRepository * 
            session : ISession -> CardContextRoleCache
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Потокобезопасный кэш с карточками.
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий карточек, используемый для загрузки контекстной роли при её отсутствии в кэше.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия текущего пользователя.
##  __См. также
#### Ссылки
[CardContextRoleCache - ](T_Tessa_Cards_Caching_CardContextRoleCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
