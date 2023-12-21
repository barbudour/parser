# WindowsProcessManagerFactory.CreateWithJob - метод
Создаёт объект
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm),
использующий WinAPI Job для контроля за временем жизни дочерних процессов.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IProcessManager CreateWithJob()
VB __Копировать
     Public Shared Function CreateWithJob As IProcessManager
C++ __Копировать
     public:
    static IProcessManager^ CreateWithJob()
F# __Копировать
     static member CreateWithJob : unit -> IProcessManager 
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
