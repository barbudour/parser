# WindowsProcessManagerFactory.CreateWithJob(ProcessJob) - метод
Создаёт объект
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm),
использующий указанный WinAPI Job для контроля за временем жизни дочерних
процессов.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IProcessManager CreateWithJob(
    	ProcessJob job
    )
VB __Копировать
     Public Shared Function CreateWithJob ( 
    	job As ProcessJob
    ) As IProcessManager
C++ __Копировать
     public:
    static IProcessManager^ CreateWithJob(
    	ProcessJob^ job
    )
F# __Копировать
     static member CreateWithJob : 
            job : ProcessJob -> IProcessManager 
#### Параметры
job [ProcessJob](T_Chronos_Platform_Processes_ProcessJob.htm)
    Обёртка для объекта WinAPI Job.
#### Возвращаемое значение
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm)  
Созданный объект
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm).
##  __Исключения
[System.PlatformNotSupportedException]| Операция не поддерживается для текущей
платформы.  
---|---  
##  __См. также
#### Ссылки
[WindowsProcessManagerFactory -
](T_Chronos_Platform_Processes_WindowsProcessManagerFactory.htm)
[CreateWithJob -
перегрузка](Overload_Chronos_Platform_Processes_WindowsProcessManagerFactory_CreateWithJob.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
[System.PlatformNotSupportedException]
