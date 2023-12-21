# ICardCacheCollection<T> \- методы
##  __Методы
[ContainsAsync](M_Tessa_Cards_Caching_ICardCacheCollection_1_ContainsAsync.htm)|
Возвращает признак того, что значение доступно в кэше по заданному ключу.  
---|---  
[GetAsync](M_Tessa_Cards_Caching_ICardCacheCollection_1_GetAsync.htm)|
Возвращает значение из кэша по заданному ключу, при этом выполняется создание
значения при его отсутствии в кэше. Например, выполняется загрузка карточки из
базы данных или от сервера, если она отсутствовала в кэше.  
[InvalidateAsync(CancellationToken)](M_Tessa_Cards_Caching_ICardCacheCollection_1_InvalidateAsync_1.htm)|
Очищает кэш, при этом удаляются все значения.  
[InvalidateAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_ICardCacheCollection_1_InvalidateAsync.htm)|
Выполняет удаление значения из кэша по заданному ключу.  
[IsAllowedAsync](M_Tessa_Cards_Caching_ICardCacheCollection_1_IsAllowedAsync.htm)|
Возвращает признак того, что заданный ключ допустим для кэша.  
[TryAddAsync](M_Tessa_Cards_Caching_ICardCacheCollection_1_TryAddAsync.htm)|
Добавляет значение в кэш по заданному ключу, если значение отсутствовало в
кэше. Возвращает признак того, что значение было успешно добавлено.  
[TryGetAlreadyCachedAsync](M_Tessa_Cards_Caching_ICardCacheCollection_1_TryGetAlreadyCachedAsync.htm)|
Возвращает значение из кэша по заданному ключу или null, если значение
отсутствует в кэше. Значение может отсутствовать, если оно ещё не было
загружено, например, если карточка с указанным именем не была загружена из
базы данных или от сервера. Используйте индексатор коллекции, если требуется
загрузить значение, когда оно недоступно, например: await
cardCache.Cards.GetAsync("CardTypeName").  
## __См. также
#### Ссылки
[ICardCacheCollection<T> \-
](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
