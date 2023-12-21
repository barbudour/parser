# LazyProcessManager.HasProcessesRunning - метод
Возвращает признак того, что хотя бы один дочерний процесс ещё запущен.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasProcessesRunning()
VB __Копировать
     Public Function HasProcessesRunning As Boolean
C++ __Копировать
     public:
    virtual bool HasProcessesRunning() sealed
F# __Копировать
     abstract HasProcessesRunning : unit -> bool 
    override HasProcessesRunning : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если хотя бы один дочерний процесс ещё запущен; false в противном
случае.
#### Реализации
[IProcessManager.HasProcessesRunning()](M_Chronos_Platform_Processes_IProcessManager_HasProcessesRunning.htm)  
##  __См. также
#### Ссылки
[LazyProcessManager - ](T_Chronos_Platform_Processes_LazyProcessManager.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
