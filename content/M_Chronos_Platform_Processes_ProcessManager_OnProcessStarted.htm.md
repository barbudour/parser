# ProcessManager.OnProcessStarted - метод
Метод, вызываемый после того, как процесс был запущен. Метод выполняется в
потокобезопасном контексте.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void OnProcessStarted(
    	Process process
    )
VB __Копировать
     Protected Overridable Sub OnProcessStarted ( 
    	process As Process
    )
C++ __Копировать
     protected:
    virtual void OnProcessStarted(
    	Process^ process
    )
F# __Копировать
     abstract OnProcessStarted : 
            process : Process -> unit 
    override OnProcessStarted : 
            process : Process -> unit 
#### Параметры
process
[Process](https://learn.microsoft.com/dotnet/api/system.diagnostics.process)
     Запущенный процесс. Не равен null. 
## __См. также
#### Ссылки
[ProcessManager - ](T_Chronos_Platform_Processes_ProcessManager.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
