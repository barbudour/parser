# IProcessManager - интерфейс
Менеджер процессов. Позволяет запускать дочерние процессы и управлять их
временем жизни.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IProcessManager : IDisposable
VB __Копировать
     Public Interface IProcessManager
    	Inherits IDisposable
C++ __Копировать
     public interface class IProcessManager : IDisposable
F# __Копировать
     type IProcessManager = 
        interface
            interface IDisposable
        end
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
[HasProcessesRunning](M_Chronos_Platform_Processes_IProcessManager_HasProcessesRunning.htm)|
Возвращает признак того, что хотя бы один дочерний процесс ещё запущен.  
[StartProcess](M_Chronos_Platform_Processes_IProcessManager_StartProcess.htm)|
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.  
## __См. также
#### Ссылки
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
