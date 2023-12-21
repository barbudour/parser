# JobProcessManager - класс
Менеджер процессов, использующий
[ProcessJob](T_Tessa_Platform_Runtime_ProcessJob.htm) для объединения
процессов в группу. Позволяет запускать дочерние процессы и управлять их
временем жизни. Используйте класс
[WindowsProcessManagerFactory](T_Tessa_Platform_Runtime_WindowsProcessManagerFactory.htm),
чтобы создать экземпляр класса.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class JobProcessManager : ProcessManager
VB __Копировать
     Public Class JobProcessManager
    	Inherits ProcessManager
C++ __Копировать
     public ref class JobProcessManager : public ProcessManager
F# __Копировать
     type JobProcessManager = 
        class
            inherit ProcessManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm) __ JobProcessManager
##  __Конструкторы
[JobProcessManager](M_Tessa_Platform_Runtime_JobProcessManager__ctor.htm)|
Создаёт экземпляр класса с указанием объекта WinAPI Job, в который будут
добавлены все создаваемые процессы.  
---|---  
## __Свойства
[ChildProcessList](P_Tessa_Platform_Runtime_ProcessManager_ChildProcessList.htm)|
Список дочерних процессов.  
(Унаследован от [ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm))  
---|---  
[IsDisposed](P_Tessa_Platform_Runtime_ProcessManager_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
(Унаследован от [ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm))  
[SyncObject](P_Tessa_Platform_Runtime_ProcessManager_SyncObject.htm)|  Объект,
используемый для синхронизации потоков.  
(Унаследован от [ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm))  
##  __Методы
[Dispose()](M_Tessa_Platform_Runtime_ProcessManager_Dispose.htm)|  Освобождает
занятые объектом ресурсы.  
(Унаследован от [ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm))  
---|---  
[Dispose(Boolean)](M_Tessa_Platform_Runtime_JobProcessManager_Dispose.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Переопределяет
[ProcessManager.Dispose(Boolean)](M_Tessa_Platform_Runtime_ProcessManager_Dispose_1.htm))  
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
[HasProcessesRunning](M_Tessa_Platform_Runtime_ProcessManager_HasProcessesRunning.htm)|
Возвращает признак того, что хотя бы один дочерний процесс ещё запущен.  
(Унаследован от [ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnProcessStarted](M_Tessa_Platform_Runtime_JobProcessManager_OnProcessStarted.htm)|
Метод, вызываемый после того, как процесс был запущен. Метод выполняется в
потокобезопасном контексте.  
(Переопределяет
[ProcessManager.OnProcessStarted(Process)](M_Tessa_Platform_Runtime_ProcessManager_OnProcessStarted.htm))  
[StartProcess](M_Tessa_Platform_Runtime_ProcessManager_StartProcess.htm)|
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.  
(Унаследован от [ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm))  
[StartProcessCore](M_Tessa_Platform_Runtime_ProcessManager_StartProcessCore.htm)|
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.  
(Унаследован от [ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm))  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
