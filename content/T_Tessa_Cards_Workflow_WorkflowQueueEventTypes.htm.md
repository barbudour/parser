# WorkflowQueueEventTypes - класс
Стандартные типы событий по обработке сигнала в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WorkflowQueueEventTypes
VB __Копировать
     Public NotInheritable Class WorkflowQueueEventTypes
C++ __Копировать
     public ref class WorkflowQueueEventTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WorkflowQueueEventTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowQueueEventTypes
##  __Методы
[IsKnown](M_Tessa_Cards_Workflow_WorkflowQueueEventTypes_IsKnown.htm)|
Возвращает признак того, что тип события является известным для стандартного
API.  
---|---  
## __Поля
[AfterPlatform](F_Tessa_Cards_Workflow_WorkflowQueueEventTypes_AfterPlatform.htm)|
Действие выполняется после обработки стандартных событий (завершение задания,
старт подпроцесса и др.). Это событие по умолчанию.  
---|---  
[All](F_Tessa_Cards_Workflow_WorkflowQueueEventTypes_All.htm)|  Список всех
типов событий, которые являются частью стандартного API.  
[BeforePlatform](F_Tessa_Cards_Workflow_WorkflowQueueEventTypes_BeforePlatform.htm)|
Действие выполняется перед обработкой стандартных событий (завершение задания,
старт подпроцесса и др.).  
## __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
