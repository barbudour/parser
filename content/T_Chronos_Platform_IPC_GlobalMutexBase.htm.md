# GlobalMutexBase - класс
Базовая реализация интерфейса
[IGlobalMutex](T_Chronos_Platform_IPC_IGlobalMutex.htm).
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class GlobalMutexBase : IGlobalMutex, 
    	IAsyncDisposable
VB __Копировать
     Public MustInherit Class GlobalMutexBase
    	Implements IGlobalMutex, IAsyncDisposable
C++ __Копировать
     public ref class GlobalMutexBase abstract : IGlobalMutex, 
    	IAsyncDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type GlobalMutexBase = 
        class
            interface IGlobalMutex
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalMutexBase
Derived
[Chronos.Platform.IPC.DefaultGlobalMutex](T_Chronos_Platform_IPC_DefaultGlobalMutex.htm)
[Chronos.Platform.IPC.LinuxGlobalMutex](T_Chronos_Platform_IPC_LinuxGlobalMutex.htm)
Implements
    [IGlobalMutex](T_Chronos_Platform_IPC_IGlobalMutex.htm), [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Конструкторы
[GlobalMutexBase](M_Chronos_Platform_IPC_GlobalMutexBase__ctor.htm)|
Инициализирует новый экземпляр класса GlobalMutexBase  
---|---  
##  __Свойства
[IsDisposed](P_Chronos_Platform_IPC_GlobalMutexBase_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
---|---  
##  __Методы
[CheckDisposed](M_Chronos_Platform_IPC_GlobalMutexBase_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
---|---  
[CleanAsync](M_Chronos_Platform_IPC_GlobalMutexBase_CleanAsync.htm)|
Освобождает ресурсы мьютекса, делая невозможным его дальнейшее использование,
и удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
[CleanCoreAsync](M_Chronos_Platform_IPC_GlobalMutexBase_CleanCoreAsync.htm)|
Освобождает ресурсы мьютекса, делая невозможным его дальнейшее использование,
и удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
[DisposeAsync()](M_Chronos_Platform_IPC_GlobalMutexBase_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
[DisposeAsync(Boolean)](M_Chronos_Platform_IPC_GlobalMutexBase_DisposeAsync_1.htm)|
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
[ReleaseAsync](M_Chronos_Platform_IPC_GlobalMutexBase_ReleaseAsync.htm)|
Освобождает блокировку на текущий мьютекс. Не выполняет действий, если
блокировка не была взята.  
[ReleaseCoreAsync](M_Chronos_Platform_IPC_GlobalMutexBase_ReleaseCoreAsync.htm)|
Освобождает блокировку на текущий мьютекс. Не выполняет действий, если
блокировка не была взята.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WaitAsync](M_Chronos_Platform_IPC_GlobalMutexBase_WaitAsync.htm)|  Ожидает и
получает блокировку на текущий мьютекс. После взятия блокировки её необходимо
освободить методом Release.  
[WaitCoreAsync](M_Chronos_Platform_IPC_GlobalMutexBase_WaitCoreAsync.htm)|
Ожидает и получает блокировку на текущий мьютекс. После взятия блокировки её
необходимо освободить методом Release.  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
