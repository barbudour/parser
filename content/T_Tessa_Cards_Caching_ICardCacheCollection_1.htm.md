# ICardCacheCollection<T> \- интерфейс
Потокобезопасная коллекция объектов для карточек, кэшируемых по строковому
ключу и создаваемых единым способом для всех объектов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardCacheCollection<T>
    where T : class
VB __Копировать
     Public Interface ICardCacheCollection(Of T As Class)
C++ __Копировать
    generic<typename T>
    where T : ref class
    public interface class ICardCacheCollection
F# __Копировать
     type ICardCacheCollection<'T when 'T : not struct> = interface end
#### Параметры типа
T
    Тип кэшируемого объекта.
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
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
