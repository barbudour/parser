# WindowsProcessManagerFactory - класс
Вспомогательные методы для создания объектов
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WindowsProcessManagerFactory
VB __Копировать
     Public NotInheritable Class WindowsProcessManagerFactory
C++ __Копировать
     public ref class WindowsProcessManagerFactory abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WindowsProcessManagerFactory = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WindowsProcessManagerFactory
##  __Методы
[CreateWithJob()](M_Chronos_Platform_Processes_WindowsProcessManagerFactory_CreateWithJob.htm)|
Создаёт объект
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm),
использующий WinAPI Job для контроля за временем жизни дочерних процессов.  
---|---  
[CreateWithJob(ProcessJob)](M_Chronos_Platform_Processes_WindowsProcessManagerFactory_CreateWithJob_1.htm)|
Создаёт объект
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm),
использующий указанный WinAPI Job для контроля за временем жизни дочерних
процессов.  
## __См. также
#### Ссылки
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
