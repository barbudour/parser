# CommandLineProcessHost - класс
Хост, передающий данные дочерним процессам через аргументы командной строки.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CommandLineProcessHost : IProcessHost
VB __Копировать
     Public MustInherit Class CommandLineProcessHost
    	Implements IProcessHost
C++ __Копировать
     public ref class CommandLineProcessHost abstract : IProcessHost
F# __Копировать
     [<AbstractClassAttribute>]
    type CommandLineProcessHost = 
        class
            interface IProcessHost
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CommandLineProcessHost
Implements
    [IProcessHost](T_Chronos_Platform_Processes_IProcessHost.htm)
##  __Конструкторы
[CommandLineProcessHost](M_Chronos_Platform_Processes_CommandLineProcessHost__ctor.htm)|
Создаёт экземпляр класса, указывая сборку хоста.  
---|---  
## __Свойства
[CreateConsoleForChildren](P_Chronos_Platform_Processes_CommandLineProcessHost_CreateConsoleForChildren.htm)|
Признак того, нужно ли показывать окно консоли для плагинов, запускаемых с
помощью метода
[StartChildProcess(String[])](M_Chronos_Platform_Processes_CommandLineProcessHost_StartChildProcess.htm).  
---|---  
[HostAssembly](P_Chronos_Platform_Processes_CommandLineProcessHost_HostAssembly.htm)|
Сборка хоста.  
[ProcessManager](P_Chronos_Platform_Processes_CommandLineProcessHost_ProcessManager.htm)|
Менеджер процессов.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetProcessRefContainerMutexName](M_Chronos_Platform_Processes_CommandLineProcessHost_GetProcessRefContainerMutexName.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasProcessesRunning](M_Chronos_Platform_Processes_CommandLineProcessHost_HasProcessesRunning.htm)|
Возвращает признак того, что хотя бы один дочерний процесс ещё запущен.  
[InitiateHostShutdownAsync](M_Chronos_Platform_Processes_CommandLineProcessHost_InitiateHostShutdownAsync.htm)|
Запускает процесс остановки хоста. После вызова этого метода хост не может
быть использован.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnChildStartedAsync](M_Chronos_Platform_Processes_CommandLineProcessHost_OnChildStartedAsync.htm)|
Запущен плагин с указанными параметрами. Метод может выполнять асинхронные
вызовы и должен вернуть задачу, по завершению которой выполнение будет
продолжено.  
[OnChildStartingAsync](M_Chronos_Platform_Processes_CommandLineProcessHost_OnChildStartingAsync.htm)|
Запущен плагин с указанными параметрами. Гарантированно вызывается перед
[OnChildStartedAsync(String[],
CancellationToken)](M_Chronos_Platform_Processes_CommandLineProcessHost_OnChildStartedAsync.htm).
Метод может выполнять асинхронные вызовы и должен вернуть задачу, по
завершению которой выполнение будет продолжено.  
[OnHostShutdownAsync](M_Chronos_Platform_Processes_CommandLineProcessHost_OnHostShutdownAsync.htm)|
Хост остановлен. Вызывается после того, как все ресурсы хоста были
освобождены, а все процессы плагинов остановлены. Предоставляет последний шанс
выполнить некоторую очистку. Метод может выполнять асинхронные вызовы и должен
вернуть задачу, по завершению которой выполнение будет продолжено.  
[OnHostStartedAsync](M_Chronos_Platform_Processes_CommandLineProcessHost_OnHostStartedAsync.htm)|
Хост запущен. Метод может выполнять асинхронные вызовы и должен вернуть
задачу, по завершению которой выполнение будет продолжено.  
[OnHostStartingAsync](M_Chronos_Platform_Processes_CommandLineProcessHost_OnHostStartingAsync.htm)|
Хост запущен. Гарантированно вызывается перед
[OnHostStartedAsync(CancellationToken)](M_Chronos_Platform_Processes_CommandLineProcessHost_OnHostStartedAsync.htm).
Метод может выполнять асинхронные вызовы и должен вернуть задачу, по
завершению которой выполнение будет продолжено.  
[StartAsync](M_Chronos_Platform_Processes_CommandLineProcessHost_StartAsync.htm)|
Запускает асинхронную обработку заданных аргументов командной строки, выбирая
режим хоста или дочернего процесса.  
[StartChildProcess](M_Chronos_Platform_Processes_CommandLineProcessHost_StartChildProcess.htm)|
Запускает дочерний процесс и возвращает ссылку на него.  
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
