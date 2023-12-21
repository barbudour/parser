# ProcessRefHelper - класс
Хэлперы для работы с объектами
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm).
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ProcessRefHelper
VB __Копировать
     Public NotInheritable Class ProcessRefHelper
C++ __Копировать
     public ref class ProcessRefHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ProcessRefHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ProcessRefHelper
##  __Методы
[CreateContainerElement](M_Chronos_Platform_ProcessRefHelper_CreateContainerElement.htm)|
Создаёт XML-элемент, описывающий указанное перечисление ссылок на процессы.  
---|---  
[GetCurrentProcessRef](M_Chronos_Platform_ProcessRefHelper_GetCurrentProcessRef.htm)|
Возвращает ссылку на текущий исполняемый процесс.  
[GetDeadProcessRefs](M_Chronos_Platform_ProcessRefHelper_GetDeadProcessRefs.htm)|
Возвращает список процессов, на которые есть ссылки, но которые уже были
завершены.  
[GetProcessRef](M_Chronos_Platform_ProcessRefHelper_GetProcessRef.htm)|
Возвращает ссылку на указанный процесс.  
[KillMany](M_Chronos_Platform_ProcessRefHelper_KillMany.htm)|  Принудительно
завершает все процессы, ссылки на которое приведены в указанном перечислении.  
[ParseProcessRefContainer](M_Chronos_Platform_ProcessRefHelper_ParseProcessRefContainer.htm)|
Возвращает список ссылок на процессы, полученный из указанного XML-элемента.  
## __Поля
[ContainerElementName](F_Chronos_Platform_ProcessRefHelper_ContainerElementName.htm)|
Имя корневого элемента, который записывается в XML-представление списка
объектов [ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm).  
---|---  
[ProcessRefElementName](F_Chronos_Platform_ProcessRefHelper_ProcessRefElementName.htm)|
Имя элемента, являющегося XML-представлением объекта
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm).  
[ProcessRefIdAttributeName](F_Chronos_Platform_ProcessRefHelper_ProcessRefIdAttributeName.htm)|
Атрибут, в котором хранится идентификатор процесса для объекта
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm).  
[ProcessRefNameAttributeName](F_Chronos_Platform_ProcessRefHelper_ProcessRefNameAttributeName.htm)|
Атрибут, в котором хранится имя процесса для объекта
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm).  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
