# ICardCacheSettings - интерфейс
Потокобезопасная коллекция определяемых пользователем настроек, содержащихся в
кэше карточек и доступных по строковому ключу.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardCacheSettings
VB __Копировать
     Public Interface ICardCacheSettings
C++ __Копировать
     public interface class ICardCacheSettings
F# __Копировать
     type ICardCacheSettings = interface end
##  __Методы
[ContainsAsync](M_Tessa_Cards_Caching_ICardCacheSettings_ContainsAsync.htm)|
Возвращает признак того, что настройка доступна в кэше по заданному ключу.  
---|---  
[GetAsync<T>(String, Func<String, T>,
CancellationToken)](M_Tessa_Cards_Caching_ICardCacheSettings_GetAsync__1.htm)|
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.  
[GetAsync<T>(String, Func<String, CancellationToken, Task<T>>,
CancellationToken)](M_Tessa_Cards_Caching_ICardCacheSettings_GetAsync__1_1.htm)|
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.  
[InvalidateAsync(CancellationToken)](M_Tessa_Cards_Caching_ICardCacheSettings_InvalidateAsync_1.htm)|
Очищает кэш, при этом удаляются все настройки.  
[InvalidateAsync(String,
CancellationToken)](M_Tessa_Cards_Caching_ICardCacheSettings_InvalidateAsync.htm)|
Выполняет удаление настройки из кэша по заданному ключу.  
[TryGetAlreadyCachedAsync<T>](M_Tessa_Cards_Caching_ICardCacheSettings_TryGetAlreadyCachedAsync__1.htm)|
Возвращает настройку из кэша по заданному ключу или null, если настройка
отсутствует в кэше.  
## __См. также
#### Ссылки
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
