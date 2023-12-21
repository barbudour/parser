# GlobalCacheLock - класс
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
     public sealed class GlobalCacheLock : IGlobalCacheLock
VB __Копировать
     Public NotInheritable Class GlobalCacheLock
    	Implements IGlobalCacheLock
C++ __Копировать
     public ref class GlobalCacheLock sealed : IGlobalCacheLock
F# __Копировать
     [<SealedAttribute>]
    type GlobalCacheLock = 
        class
            interface IGlobalCacheLock
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalCacheLock
Implements
    [IGlobalCacheLock](T_Tessa_Platform_Caching_IGlobalCacheLock.htm)
##  __Конструкторы
[GlobalCacheLock](M_Tessa_Platform_Caching_GlobalCacheLock__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExecuteReaderAsync](M_Tessa_Platform_Caching_GlobalCacheLock_ExecuteReaderAsync.htm)|
Выполняет делегат в блокировке на чтение, при этом последующие вызовы
[!:ExecuteAsync] ниже по стеку будут выполняться в рамках уже взятой
блокировки.  
[ExecuteWriterAsync](M_Tessa_Platform_Caching_GlobalCacheLock_ExecuteWriterAsync.htm)|
Выполняет делегат в блокировке на запись, при этом последующие вызовы
[!:ExecuteAsync] ниже по стеку будут выполняться в рамках уже взятой
блокировки.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Caching - пространство имён](N_Tessa_Platform_Caching.htm)
