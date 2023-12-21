# GlobalStorageBase - класс
Базовая реализация интерфейса
[IGlobalStorage](T_Tessa_Platform_IPC_IGlobalStorage.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class GlobalStorageBase : IGlobalStorage, 
    	IAsyncDisposable
VB __Копировать
     Public MustInherit Class GlobalStorageBase
    	Implements IGlobalStorage, IAsyncDisposable
C++ __Копировать
     public ref class GlobalStorageBase abstract : IGlobalStorage, 
    	IAsyncDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type GlobalStorageBase = 
        class
            interface IGlobalStorage
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalStorageBase
Derived
[Tessa.Platform.IPC.DefaultGlobalStorage](T_Tessa_Platform_IPC_DefaultGlobalStorage.htm)
[Tessa.Platform.IPC.FileSystemGlobalStorage](T_Tessa_Platform_IPC_FileSystemGlobalStorage.htm)
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IGlobalStorage](T_Tessa_Platform_IPC_IGlobalStorage.htm)
##  __Конструкторы
[GlobalStorageBase](M_Tessa_Platform_IPC_GlobalStorageBase__ctor.htm)|
Инициализирует новый экземпляр класса GlobalStorageBase  
---|---  
##  __Свойства
[IsDisposed](P_Tessa_Platform_IPC_GlobalStorageBase_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
---|---  
##  __Методы
[CheckDisposed](M_Tessa_Platform_IPC_GlobalStorageBase_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
---|---  
[DisposeAsync()](M_Tessa_Platform_IPC_GlobalStorageBase_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_GlobalStorageBase_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[OpenAsync](M_Tessa_Platform_IPC_GlobalStorageBase_OpenAsync.htm)|  Открывает
разделяемое хранилище для записи или чтения. При необходимости некоторое время
ожидается снятие блокировки от других процессов.  
[OpenCoreAsync](M_Tessa_Platform_IPC_GlobalStorageBase_OpenCoreAsync.htm)|
Открывает разделяемое хранилище для записи или чтения. При необходимости
некоторое время ожидается снятие блокировки от других процессов.  
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
