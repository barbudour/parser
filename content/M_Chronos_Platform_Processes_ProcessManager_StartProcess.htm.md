# ProcessManager.StartProcess - метод
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Process StartProcess(
    	ProcessStartInfo startInfo,
    	Action<Process> setupProcessAction = null
    )
VB __Копировать
     Public Function StartProcess ( 
    	startInfo As ProcessStartInfo,
    	Optional setupProcessAction As Action(Of Process) = Nothing
    ) As Process
C++ __Копировать
     public:
    virtual Process^ StartProcess(
    	ProcessStartInfo^ startInfo, 
    	Action<Process^>^ setupProcessAction = nullptr
    ) sealed
F# __Копировать
     abstract StartProcess : 
            startInfo : ProcessStartInfo * 
            ?setupProcessAction : Action<Process> 
    (* Defaults:
            let _setupProcessAction = defaultArg setupProcessAction null
    *)
    -> Process 
    override StartProcess : 
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
#### Реализации
[IProcessManager.StartProcess(ProcessStartInfo,
Action<Process>)](M_Chronos_Platform_Processes_IProcessManager_StartProcess.htm)  
##  __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[ProcessManager - ](T_Chronos_Platform_Processes_ProcessManager.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
[System.ObjectDisposedException]
