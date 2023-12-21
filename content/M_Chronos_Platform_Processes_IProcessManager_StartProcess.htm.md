# IProcessManager.StartProcess - метод
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     Process StartProcess(
    	ProcessStartInfo startInfo,
    	Action<Process> setupProcessAction = null
    )
VB __Копировать
     Function StartProcess ( 
    	startInfo As ProcessStartInfo,
    	Optional setupProcessAction As Action(Of Process) = Nothing
    ) As Process
C++ __Копировать
    Process^ StartProcess(
    	ProcessStartInfo^ startInfo, 
    	Action<Process^>^ setupProcessAction = nullptr
    )
F# __Копировать
     abstract StartProcess : 
            startInfo : ProcessStartInfo * 
            ?setupProcessAction : Action<Process> 
    (* Defaults:
            let _setupProcessAction = defaultArg setupProcessAction null
    *)
    -> Process 
#### Параметры
startInfo
[ProcessStartInfo](https://learn.microsoft.com/dotnet/api/system.diagnostics.processstartinfo)
    Параметры запуска процесса.
setupProcessAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-1)<[Process](https://learn.microsoft.com/dotnet/api/system.diagnostics.process)>
(Optional)
     Метод, изменяющий объект процесса перед запуском, или null, если изменение объекта процесса не требуется. 
#### Возвращаемое значение
[Process](https://learn.microsoft.com/dotnet/api/system.diagnostics.process)  
Ссылка на запущенный процесс.
##  __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[IProcessManager - ](T_Chronos_Platform_Processes_IProcessManager.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
[System.ObjectDisposedException]
