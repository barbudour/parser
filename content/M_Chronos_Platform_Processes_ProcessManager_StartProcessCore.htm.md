# ProcessManager.StartProcessCore - метод
Запускает процесс с заданными параметрами. Метод должен быть потокобезопасным.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Process StartProcessCore(
    	ProcessStartInfo startInfo,
    	Action<Process> setupProcessAction = null
    )
VB __Копировать
     Protected Overridable Function StartProcessCore ( 
    	startInfo As ProcessStartInfo,
    	Optional setupProcessAction As Action(Of Process) = Nothing
    ) As Process
C++ __Копировать
     protected:
    virtual Process^ StartProcessCore(
    	ProcessStartInfo^ startInfo, 
    	Action<Process^>^ setupProcessAction = nullptr
    )
F# __Копировать
     abstract StartProcessCore : 
            startInfo : ProcessStartInfo * 
            ?setupProcessAction : Action<Process> 
    (* Defaults:
            let _setupProcessAction = defaultArg setupProcessAction null
    *)
    -> Process 
    override StartProcessCore : 
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
##  __См. также
#### Ссылки
[ProcessManager - ](T_Chronos_Platform_Processes_ProcessManager.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
