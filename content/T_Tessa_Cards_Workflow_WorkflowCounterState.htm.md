# WorkflowCounterState - перечисление
Состояние счётчика после его декремента.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum WorkflowCounterState
VB __Копировать
     Public Enumeration WorkflowCounterState
C++ __Копировать
     public enum class WorkflowCounterState
F# __Копировать
     type WorkflowCounterState
##  __Члены
NotFound| 0|  Счётчик отсутствует в списке.  
---|---|---  
InProgress| 1|  Счётчик присуствует в списке, значение больше нуля.  
Finished| 2|  Счётчик присутствовал в списке, дошёл до нуля (или меньше нуля)
и был удалён.  
## __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
