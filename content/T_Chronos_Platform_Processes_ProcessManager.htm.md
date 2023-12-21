# ProcessManager - класс
Менеджер процессов по умолчанию. Позволяет запускать дочерние процессы и
управлять их временем жизни.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public class ProcessManager : IProcessManager, 
    	IDisposable
VB __Копировать
     Public Class ProcessManager
    	Implements IProcessManager, IDisposable
C++ __Копировать
     public ref class ProcessManager : IProcessManager, 
    	IDisposable
F# __Копировать
     type ProcessManager = 
        class
            interface IProcessManager
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ProcessManager
Derived
[Chronos.Platform.Processes.JobProcessManager](T_Chronos_Platform_Processes_JobProcessManager.htm)
Implements
    [IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[ProcessManager](M_Chronos_Platform_Processes_ProcessManager__ctor.htm)|
Инициализирует новый экземпляр класса ProcessManager  
---|---  
##  __Свойства
[ChildProcessList](P_Chronos_Platform_Processes_ProcessManager_ChildProcessList.htm)|
Список дочерних процессов.  
---|---  
[IsDisposed](P_Chronos_Platform_Processes_ProcessManager_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
[SyncObject](P_Chronos_Platform_Processes_ProcessManager_SyncObject.htm)|
Объект, используемый для синхронизации потоков.  
## __Методы
[Dispose()](M_Chronos_Platform_Processes_ProcessManager_Dispose.htm)|
Освобождает занятые объектом ресурсы.  
---|---  
[Dispose(Boolean)](M_Chronos_Platform_Processes_ProcessManager_Dispose_1.htm)|
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
[HasProcessesRunning](M_Chronos_Platform_Processes_ProcessManager_HasProcessesRunning.htm)|
Возвращает признак того, что хотя бы один дочерний процесс ещё запущен.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnProcessStarted](M_Chronos_Platform_Processes_ProcessManager_OnProcessStarted.htm)|
Метод, вызываемый после того, как процесс был запущен. Метод выполняется в
потокобезопасном контексте.  
[StartProcess](M_Chronos_Platform_Processes_ProcessManager_StartProcess.htm)|
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.  
[StartProcessCore](M_Chronos_Platform_Processes_ProcessManager_StartProcessCore.htm)|
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.  
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
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
