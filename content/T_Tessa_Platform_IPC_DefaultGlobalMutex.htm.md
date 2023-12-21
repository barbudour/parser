# DefaultGlobalMutex - класс
Мьютекс с глобально уникальным именем, используемый для синхронизации между
процессами. Эта версия использует стандартный объект
[Mutex](https://learn.microsoft.com/dotnet/api/system.threading.mutex) с
глобальным именем, который будет функционировать только при запуске на
Windows.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DefaultGlobalMutex : GlobalMutexBase
VB __Копировать
     Public Class DefaultGlobalMutex
    	Inherits GlobalMutexBase
C++ __Копировать
     public ref class DefaultGlobalMutex : public GlobalMutexBase
F# __Копировать
     type DefaultGlobalMutex = 
        class
            inherit GlobalMutexBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm) __ DefaultGlobalMutex
##  __Конструкторы
[DefaultGlobalMutex](M_Tessa_Platform_IPC_DefaultGlobalMutex__ctor.htm)|
Создаёт экземпляр класса с указанием глобально уникального имени мьютекса.  
---|---  
## __Свойства
[IsDisposed](P_Tessa_Platform_IPC_GlobalMutexBase_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
(Унаследован от [GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm))  
---|---  
[Semaphore](P_Tessa_Platform_IPC_DefaultGlobalMutex_Semaphore.htm)|  Семафор,
используемый для синхронизации.  
## __Методы
[CheckDisposed](M_Tessa_Platform_IPC_GlobalMutexBase_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
(Унаследован от [GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm))  
---|---  
[CleanAsync](M_Tessa_Platform_IPC_GlobalMutexBase_CleanAsync.htm)|
Освобождает ресурсы мьютекса, делая невозможным его дальнейшее использование,
и удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
(Унаследован от [GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm))  
[CleanCoreAsync](M_Tessa_Platform_IPC_GlobalMutexBase_CleanCoreAsync.htm)|
Освобождает ресурсы мьютекса, делая невозможным его дальнейшее использование,
и удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
(Унаследован от [GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm))  
[DisposeAsync()](M_Tessa_Platform_IPC_GlobalMutexBase_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm))  
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_DefaultGlobalMutex_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Переопределяет
[GlobalMutexBase.DisposeAsync(Boolean)](M_Tessa_Platform_IPC_GlobalMutexBase_DisposeAsync_1.htm))  
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
[ReleaseAsync](M_Tessa_Platform_IPC_GlobalMutexBase_ReleaseAsync.htm)|
Освобождает блокировку на текущий мьютекс. Не выполняет действий, если
блокировка не была взята.  
(Унаследован от [GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm))  
[ReleaseCoreAsync](M_Tessa_Platform_IPC_DefaultGlobalMutex_ReleaseCoreAsync.htm)|
Освобождает блокировку на текущий мьютекс. Не выполняет действий, если
блокировка не была взята.  
(Переопределяет
[GlobalMutexBase.ReleaseCoreAsync(CancellationToken)](M_Tessa_Platform_IPC_GlobalMutexBase_ReleaseCoreAsync.htm))  
[ToString](M_Tessa_Platform_IPC_DefaultGlobalMutex_ToString.htm)|  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[WaitAsync](M_Tessa_Platform_IPC_GlobalMutexBase_WaitAsync.htm)|  Ожидает и
получает блокировку на текущий мьютекс. После взятия блокировки её необходимо
освободить методом Release.  
(Унаследован от [GlobalMutexBase](T_Tessa_Platform_IPC_GlobalMutexBase.htm))  
[WaitCoreAsync](M_Tessa_Platform_IPC_DefaultGlobalMutex_WaitCoreAsync.htm)|
Ожидает и получает блокировку на текущий мьютекс. После взятия блокировки её
необходимо освободить методом Release.  
(Переопределяет [GlobalMutexBase.WaitCoreAsync(Int32,
CancellationToken)](M_Tessa_Platform_IPC_GlobalMutexBase_WaitCoreAsync.htm))  
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
