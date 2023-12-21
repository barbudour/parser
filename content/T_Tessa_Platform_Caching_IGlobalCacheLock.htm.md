# IGlobalCacheLock - интерфейс
Объект, отвечающий за глобальную блокировку кэшей между собой. В отличии от
[AsyncLock](T_Tessa_Platform_AsyncLock.htm), последующие вызовы
[!:ExecuteAsync] ниже по стеку будут выполняться в рамках уже взятой
блокировки. Рекомендуется использовать в методах, которые могут использовать
другие кэши (например,
[!:GlobalCache<TEventArgs>.GetAsync<T>(Func<CancellationToken, Task<T>>,
Func<CancellationToken, Task<T>>, CancellationToken)] при заполнении кэша или
[InvalidateLocalCacheAsync(TEventArgs,
CancellationToken)](M_Tessa_Platform_Caching_GlobalCache_1_InvalidateLocalCacheAsync.htm)
при сбрасывании локального кэша), для исключения ситуации, когда два разных
кэша могут брать блокировку друг на друга.
## __Definition
 **Пространство имён:** [Tessa.Platform.Caching](N_Tessa_Platform_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IGlobalCacheLock
VB __Копировать
     Public Interface IGlobalCacheLock
C++ __Копировать
     public interface class IGlobalCacheLock
F# __Копировать
     type IGlobalCacheLock = interface end
##  __Методы
[ExecuteReaderAsync](M_Tessa_Platform_Caching_IGlobalCacheLock_ExecuteReaderAsync.htm)|
Выполняет делегат в блокировке на чтение, при этом последующие вызовы
[!:ExecuteAsync] ниже по стеку будут выполняться в рамках уже взятой
блокировки.  
---|---  
[ExecuteWriterAsync](M_Tessa_Platform_Caching_IGlobalCacheLock_ExecuteWriterAsync.htm)|
Выполняет делегат в блокировке на запись, при этом последующие вызовы
[!:ExecuteAsync] ниже по стеку будут выполняться в рамках уже взятой
блокировки.  
## __См. также
#### Ссылки
[Tessa.Platform.Caching - пространство имён](N_Tessa_Platform_Caching.htm)
