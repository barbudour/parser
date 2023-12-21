# RedisConnectionProvider - класс
Объект, предоставляющий доступ к соединению Redis.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RedisConnectionProvider : IRedisConnectionProvider, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class RedisConnectionProvider
    	Implements IRedisConnectionProvider, IAsyncDisposable
C++ __Копировать
     public ref class RedisConnectionProvider sealed : IRedisConnectionProvider, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type RedisConnectionProvider = 
        class
            interface IRedisConnectionProvider
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RedisConnectionProvider
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IRedisConnectionProvider](T_Tessa_Platform_IPC_IRedisConnectionProvider.htm)
##  __Конструкторы
[RedisConnectionProvider(Func<CancellationToken,
ValueTask<String>>)](M_Tessa_Platform_IPC_RedisConnectionProvider__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
[RedisConnectionProvider(ITessaServerSettings,
IUnityDisposableContainer)](M_Tessa_Platform_IPC_RedisConnectionProvider__ctor_1.htm)|
Создаёт экземпляр класса с указанием настроек сервера из Unity.  
## __Методы
[DisposeAsync](M_Tessa_Platform_IPC_RedisConnectionProvider_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetOpenedConnectionAsync](M_Tessa_Platform_IPC_RedisConnectionProvider_GetOpenedConnectionAsync.htm)|
Возвращает открытое соединение к Redis.  
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
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
