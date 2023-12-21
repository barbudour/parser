# Tessa.Platform.Caching - пространство имён
Классы и вспомогательные методы для организации кэширования.
##  __Классы
[ConcurrentKeyCache<T>](T_Tessa_Platform_Caching_ConcurrentKeyCache_1.htm)|
Кэш, осуществляющий перевод строго типизированных ключей в строки и наоборот.
К кэшу возможен неблокирующий доступ из нескольких потоков.  
---|---  
[ConcurrentKeyCache<T>.Global](T_Tessa_Platform_Caching_ConcurrentKeyCache_1_Global.htm)|
Класс, содержащий ссылку на глобальный кэш объектов типа T.  
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm)|
Потокобезопасный кэш, обеспечивающий синхронный сброс кэша всех экземпляров с
заданным именем независимо от того, располагаются ли такие экземпляры в том же
приложении или в другом процессе.  
[GlobalCacheInvalidator<TEventArgs>](T_Tessa_Platform_Caching_GlobalCacheInvalidator_1.htm)|
Производит сброс всех экземпляров кэша
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm) с
заданными именем и типом.  
[GlobalCacheLock](T_Tessa_Platform_Caching_GlobalCacheLock.htm)|  Объект,
отвечающий за глобальную блокировку кэшей между собой. В отличии от
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
[GlobalCacheNames](T_Tessa_Platform_Caching_GlobalCacheNames.htm)|  Глобальный
список имён экземпляров кэша, являющихся наследниками класса
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm).  
## __Интерфейсы
[IGlobalCacheLock](T_Tessa_Platform_Caching_IGlobalCacheLock.htm)|  Объект,
отвечающий за глобальную блокировку кэшей между собой. В отличии от
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
---|---  
[IKeyCache<T>](T_Tessa_Platform_Caching_IKeyCache_1.htm)|  Кэш, осуществляющий
перевод строго типизированных ключей в строки и наоборот.
