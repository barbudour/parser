# Tessa.Cards.Caching - пространство имён
API для взаимодействия с кэшем карточек.
##  __Классы
[CardCacheCollection<T>](T_Tessa_Cards_Caching_CardCacheCollection_1.htm)|
Потокобезопасная коллекция объектов для карточек, кэшируемых по строковому
ключу и создаваемых единым способом для всех объектов.  
---|---  
[CardCacheCollectionBase<T>](T_Tessa_Cards_Caching_CardCacheCollectionBase_1.htm)|
Базовый класс для потокобезопасной коллекции объектов для карточек, кэшируемых
по строковому ключу.  
[CardCacheCollectionProxy<T>](T_Tessa_Cards_Caching_CardCacheCollectionProxy_1.htm)|
Прокси для потокобезопасной коллекции объектов для карточек, кэшируемых по
строковому ключу и создаваемых единым способом для всех объектов.  
[CardCacheEventArgs](T_Tessa_Cards_Caching_CardCacheEventArgs.htm)|  Аргументы
события сброса кэша [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm),
разделяемые между процессами.  
[CardCacheHelper](T_Tessa_Cards_Caching_CardCacheHelper.htm)|  Вспомогательные
методы и константы для кэша карточек.  
[CardCacheProxy](T_Tessa_Cards_Caching_CardCacheProxy.htm)|  Прокси для
потокобезопасного кэша с карточками и дополнительными настройками.  
[CardCacheSettings](T_Tessa_Cards_Caching_CardCacheSettings.htm)|
Потокобезопасная коллекция определяемых пользователем настроек, содержащихся в
кэше карточек и доступных по строковому ключу.  
[CardCacheSettingsProxy](T_Tessa_Cards_Caching_CardCacheSettingsProxy.htm)|
Прокси для потокобезопасной коллекции определяемых пользователем настроек,
содержащихся в кэше карточек и доступных по строковому ключу.  
[CardContextRoleCache](T_Tessa_Cards_Caching_CardContextRoleCache.htm)|  Кэш
для карточек контекстных ролей.  
[CardGlobalCache](T_Tessa_Cards_Caching_CardGlobalCache.htm)|  Глобальный кэш
для кэша карточек [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)  
[CardSingletonCache](T_Tessa_Cards_Caching_CardSingletonCache.htm)|
Потокобезопасный кэш с карточками-синглтонами и дополнительными настройками.  
[SingletonNotFoundInCacheException](T_Tessa_Cards_Caching_SingletonNotFoundInCacheException.htm)|
Исключение, возникающее в случае, когда невозможно получить карточку-синглтон
из кэша (такую, как карточка настроек), т.к. при её загрузке возникли ошибки.  
## __Структуры
[CardCacheValue<T>](T_Tessa_Cards_Caching_CardCacheValue_1.htm)|  Значение
кэша с объектом API карточек. Получить значение можно с использованием метода
[GetValue()](M_Tessa_Cards_Caching_CardCacheValue_1_GetValue.htm). Для
создания объекта вызовите статические методы.  
---|---  
## __Интерфейсы
[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)|  Потокобезопасный кэш с
карточками и дополнительными настройками.  
---|---  
[ICardCacheCollection<T>](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)|
Потокобезопасная коллекция объектов для карточек, кэшируемых по строковому
ключу и создаваемых единым способом для всех объектов.  
[ICardCacheSettings](T_Tessa_Cards_Caching_ICardCacheSettings.htm)|
Потокобезопасная коллекция определяемых пользователем настроек, содержащихся в
кэше карточек и доступных по строковому ключу.  
[ICardContextRoleCache](T_Tessa_Cards_Caching_ICardContextRoleCache.htm)|  Кэш
для карточек контекстных ролей.  
## __Перечисления
[CardCacheInvalidationType](T_Tessa_Cards_Caching_CardCacheInvalidationType.htm)|
Тип операции по сбросу кэша.  
---|---  
[CardCacheResult](T_Tessa_Cards_Caching_CardCacheResult.htm)|  Результат
обращения к кэшу с объектами API карточек.
