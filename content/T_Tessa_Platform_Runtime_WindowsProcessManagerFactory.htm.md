# WindowsProcessManagerFactory - класс
Вспомогательные методы для создания объектов
[IProcessManager](T_Tessa_Platform_Runtime_IProcessManager.htm) с
использованием WinAPI. Используйте методы этого класса только на ОС Windows.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
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
[CreateWithJob()](M_Tessa_Platform_Runtime_WindowsProcessManagerFactory_CreateWithJob.htm)|
Создаёт объект
[IProcessManager](T_Tessa_Platform_Runtime_IProcessManager.htm), использующий
WinAPI Job для контроля за временем жизни дочерних процессов.  
---|---  
[CreateWithJob(ProcessJob)](M_Tessa_Platform_Runtime_WindowsProcessManagerFactory_CreateWithJob_1.htm)|
Создаёт объект
[IProcessManager](T_Tessa_Platform_Runtime_IProcessManager.htm), использующий
указанный WinAPI Job для контроля за временем жизни дочерних процессов.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
