# WorkflowHelper - класс
Предоставляет вспомогательные методы для работы с WorkflowEngine.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WorkflowHelper
VB __Копировать
     Public NotInheritable Class WorkflowHelper
C++ __Копировать
     public ref class WorkflowHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WorkflowHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowHelper
##  __Методы
[AppendApprovalInfoUserCompleteTask](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_AppendApprovalInfoUserCompleteTask.htm)|
Добавляет информацию о согласовавшем/не согласовавшем пользователе в строковую
секцию
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrApprovalCommonInfo_Name.htm).  
---|---  
[CombinePerformers](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_CombinePerformers.htm)|
Формирует единый список исполнителей, составленный из исполнителей указанных в
настройках действия и вычисляемых исполнителей.  
[CurrentPerformerIndexIncrement](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_CurrentPerformerIndexIncrement.htm)|
Увеличивает на указанное число порядковый номер текущего исполнителя.  
[GetCurrentPerformerIndex](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_GetCurrentPerformerIndex.htm)|
Возвращает порядковый номер текущего исполнителя из параметров действия.  
[GetKindAsync](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_GetKindAsync.htm)|
Возвращает информацию по указанному идентификатору вида задания.  
[GetProcessCycle](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_GetProcessCycle.htm)|
Возвращает номер текущего цикла процесса согласования.  
[GetValidatePerformerNotSpecifiedMessage](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_GetValidatePerformerNotSpecifiedMessage.htm)|
Формирует сообщение валидации о том, что нет ни одного исполнителя.  
[InializeActionCompletionOptions](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_InializeActionCompletionOptions.htm)|
Инициализирует указанный список строк, содержащий параметры обработки
вариантов завершения действий, заданными вариантами завершения.  
[InializeTaskCompletionOptionsAsync](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_InializeTaskCompletionOptionsAsync.htm)|
Инициализирует указанный список строк, содержащий параметры обработки
вариантов завершения заданий указанных типов.  
[IsWorkflowEngineTaskAsync](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_IsWorkflowEngineTaskAsync.htm)|
Возвращает значение, показывающее, что указанное задание task из карточки card
было отправлено из Workflow Engine.  
[ProcessCycleIncrement](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_ProcessCycleIncrement.htm)|
Увеличивает номер цикла процесса согласования, содержащийся в параметрах
процесса, на указанное значение.  
[SetCurrentPerformerIndex](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_SetCurrentPerformerIndex.htm)|
Устанавливает порядковый номер текущего исполнителя в параметрах действия.  
[SetProcessCycle](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_SetProcessCycle.htm)|
Устанавливает номер цикла процесса согласования в параметры процесса.  
[SetTaskKind](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_SetTaskKind.htm)|
Устанавливает вид задания.  
[TryGetPersonalRoleIDAsync](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper_TryGetPersonalRoleIDAsync.htm)|
Возвращает персональную роль (пользователя) для роли имеющую указанный
идентификатор.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
