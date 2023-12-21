# CardMetadataCache - методы
##  __Методы
[DisposeAsync()](M_Tessa_Platform_Caching_GlobalCache_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm))  
---|---  
[DisposeAsync(Boolean)](M_Tessa_Platform_Caching_GlobalCache_1_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm))  
[EnsureInvalidateCacheSubscribedAsync](M_Tessa_Platform_Caching_GlobalCache_1_EnsureInvalidateCacheSubscribedAsync.htm)|
Выполняет подписку на глобальное событие сброса кэша, если объект ещё не был
подписан. Метод следует вызывать только в том случае, если доступ к кэшируемым
данным осуществляется не только через методы
[GetAsync<T>(Func<CancellationToken, Task<T>>, Func<CancellationToken,
Task<T>>, Boolean,
CancellationToken)](M_Tessa_Platform_Caching_GlobalCache_1_GetAsync__1.htm) и
[TryGetAsync<T>(Func<CancellationToken, Task<T>>, Boolean,
CancellationToken)](M_Tessa_Platform_Caching_GlobalCache_1_TryGetAsync__1.htm).  
(Унаследован от
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAsync<T>](M_Tessa_Platform_Caching_GlobalCache_1_GetAsync__1.htm)|
Инициирует заполнение кэша при необходимости и возвращает запрошенное из кэша
значение.  
(Унаследован от
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMetadataAsync](M_Tessa_Cards_Metadata_CardMetadataCache_GetMetadataAsync.htm)|
Возвращает доступную только для чтения актуальную метаинформацию по карточкам,
доступную в кэше.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateGlobalAsync](M_Tessa_Cards_Metadata_CardMetadataCache_InvalidateGlobalAsync.htm)|
Сбрасывает глобальный кэш с метаинформацией по карточкам.  
[InvalidateGlobalCacheAsync](M_Tessa_Platform_Caching_GlobalCache_1_InvalidateGlobalCacheAsync.htm)|
Инициирует глобальный сброс кэша, который затрагивает как текущий, так и
другие экземпляры кэша с тем же именем, которые могут располагаться в других
процессах.  
(Унаследован от
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm))  
[InvalidateLocalAsync](M_Tessa_Cards_Metadata_CardMetadataCache_InvalidateLocalAsync.htm)|
Сбрасывает локальный кэш с метаинформацией по карточкам без сброса глобального
кэша. Этот метод следует использовать в случае, если очистка производится
внутри сброса другого глобального кэша, например, глобального кэша схемы.  
[InvalidateLocalCacheAsync](M_Tessa_Platform_Caching_GlobalCache_1_InvalidateLocalCacheAsync.htm)|
Метод, реализующий сброс кэша в текущем экземпляре. Метод является
потокобезопасным и может обращаться к кэшу без дополнительной синхронизации.  
(Унаследован от
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm))  
[InvalidateLocalCacheOverrideAsync](M_Tessa_Cards_Metadata_CardMetadataCache_InvalidateLocalCacheOverrideAsync.htm)|
Метод, реализующий сброс кэша в текущем экземпляре. Метод является
потокобезопасным и может обращаться к кэшу без дополнительной синхронизации.
Любые необработанные исключения, возникшие внутри делегата, игнорируются с
записью в лог.  
(Переопределяет
[GlobalCache<TEventArgs>.InvalidateLocalCacheOverrideAsync(TEventArgs,
CancellationToken)](M_Tessa_Platform_Caching_GlobalCache_1_InvalidateLocalCacheOverrideAsync.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetAsync<T>](M_Tessa_Platform_Caching_GlobalCache_1_TryGetAsync__1.htm)|
Возвращает запрошенное из кэша значение или null, если значение отсутствует.  
(Унаследован от
[GlobalCache<TEventArgs>](T_Tessa_Platform_Caching_GlobalCache_1.htm))  
[TryGetMetadataAsync](M_Tessa_Cards_Metadata_CardMetadataCache_TryGetMetadataAsync.htm)|
Возвращает доступную только для чтения актуальную метаинформацию по карточкам
или null, если метаинформация недоступна.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[RegisterInConstructor<SharedEventArgs>](M_Tessa_Platform_PlatformExtensions_RegisterInConstructor__1.htm)|
Выполняет регистрацию текущего глобального кэша cache в контейнере container.
Все ресурсы глобального кэша могут быть освобождены, если регистрация в
контейнере container завершена по причине того, что все объекты контейнера уже
были освобождены. Возвращает признак того, что ресурсы глобального кэша не
были освобождены.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[CardMetadataCache - ](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
