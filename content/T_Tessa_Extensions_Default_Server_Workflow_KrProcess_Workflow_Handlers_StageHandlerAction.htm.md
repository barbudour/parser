# StageHandlerAction - перечисление
Варианты взаимодействия StageRunner c этапом после выполнения его обработчика.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum StageHandlerAction
VB __Копировать
     Public Enumeration StageHandlerAction
C++ __Копировать
     public enum class StageHandlerAction
F# __Копировать
     type StageHandlerAction
##  __Члены
None| 0|  Обработчик не обработал событие этапа.  
---|---|---  
InProgress| 1|  Этап активен.  
Complete| 2|  Этап завершен.  
Skip| 3|  Этап пропущен.  
Transition| 4|  Переход к другому этапу в пределах группы.  
GroupTransition| 5|  Переход в начало другой группы.  
NextGroupTransition| 6|  Переход на следующую группу с учетом пересчета набора
групп.  
PreviousGroupTransition| 7|  Переход на предыдущую группу с учетом пересчета
набора групп.  
CurrentGroupTransition| 8|  Переход на текущую группу.  
SkipProcess| 9|  Пропуск всего процесса.  
CancelProcess| 10|  Отмена всего процесса.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
