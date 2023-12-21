# Tessa.Workflow.Actions - пространство имён
Обработка действий для конструктора бизнес-процессов.
##  __Классы
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm)|
Базовый класс всех обработчиков действий.  
---|---  
[WorkflowActionRegistry](T_Tessa_Workflow_Actions_WorkflowActionRegistry.htm)|
Потокобезопасный реестр типов действий
[IWorkflowAction](T_Tessa_Workflow_Actions_IWorkflowAction.htm).  
[WorkflowActionTypes](T_Tessa_Workflow_Actions_WorkflowActionTypes.htm)|
Вспомогательный класс со всеми типами карточек, использующимеся в
WorkflowEngine по умолчанию, а также именами полей и секций действий  
[WorkflowAddFileFromTemplateAction](T_Tessa_Workflow_Actions_WorkflowAddFileFromTemplateAction.htm)|
Класс для действия Добавить файл по шаблону  
[WorkflowAndAction](T_Tessa_Workflow_Actions_WorkflowAndAction.htm)|  Класс
для действия условия "И"  
[WorkflowCommandAction](T_Tessa_Workflow_Actions_WorkflowCommandAction.htm)|
Класс для действия Команда  
[WorkflowConditionAction](T_Tessa_Workflow_Actions_WorkflowConditionAction.htm)|
Класс для действия условия  
[WorkflowDialogAction](T_Tessa_Workflow_Actions_WorkflowDialogAction.htm)|  
[WorkflowDialogContext](T_Tessa_Workflow_Actions_WorkflowDialogContext.htm)|
Контекст скриптов обработки диалогов в Workflow Engine.  
[WorkflowEmailAction](T_Tessa_Workflow_Actions_WorkflowEmailAction.htm)|
Класс для действия отправки уведомления  
[WorkflowEndProcessAction](T_Tessa_Workflow_Actions_WorkflowEndProcessAction.htm)|
Класс для действия завершения процесса  
[WorkflowHistoryManagementAction](T_Tessa_Workflow_Actions_WorkflowHistoryManagementAction.htm)|
Класс для действия управления историей  
[WorkflowNotificationInfoBase](T_Tessa_Workflow_Actions_WorkflowNotificationInfoBase.htm)|
Предоставляет основную информацию по уведомлению.  
[WorkflowScriptAction](T_Tessa_Workflow_Actions_WorkflowScriptAction.htm)|
Класс для действия Сценарий  
[WorkflowSendSignalAction](T_Tessa_Workflow_Actions_WorkflowSendSignalAction.htm)|
Класс для действия Отправить сигнал  
[WorkflowStartProcessAction](T_Tessa_Workflow_Actions_WorkflowStartProcessAction.htm)|
Класс для действия запуска процесса.  
[WorkflowSubprocessAction](T_Tessa_Workflow_Actions_WorkflowSubprocessAction.htm)|
Класс для действия подпроцесса  
[WorkflowSubprocessControlAction](T_Tessa_Workflow_Actions_WorkflowSubprocessControlAction.htm)|
Класс для действия управление подпроцессом  
[WorkflowTaskAction](T_Tessa_Workflow_Actions_WorkflowTaskAction.htm)|  Класс
для действия задания.  
[WorkflowTaskActionBase](T_Tessa_Workflow_Actions_WorkflowTaskActionBase.htm)|
Базовый класс для обработчиков действий, отправляющих задания.  
[WorkflowTaskControlAction](T_Tessa_Workflow_Actions_WorkflowTaskControlAction.htm)|
Класс для действия управление заданием  
[WorkflowTaskControlAction.TaskControlTypes](T_Tessa_Workflow_Actions_WorkflowTaskControlAction_TaskControlTypes.htm)|  
[WorkflowTaskGroupAction](T_Tessa_Workflow_Actions_WorkflowTaskGroupAction.htm)|
Класс для действия задания.  
[WorkflowTaskGroupControlAction](T_Tessa_Workflow_Actions_WorkflowTaskGroupControlAction.htm)|
Класс для действия управление группой заданий  
[WorkflowTaskNotificationInfo](T_Tessa_Workflow_Actions_WorkflowTaskNotificationInfo.htm)|
Предоставляет информацию о уведомлении получаемую из строки содержащей
параметры обработки варианта завершения.  
[WorkflowTaskNotificationInfoBase](T_Tessa_Workflow_Actions_WorkflowTaskNotificationInfoBase.htm)|
Предоставляет информацию о уведомлении по заданию.  
[WorkflowTimerAction](T_Tessa_Workflow_Actions_WorkflowTimerAction.htm)|
Класс для действия Таймер  
[WorkflowTimerControlAction](T_Tessa_Workflow_Actions_WorkflowTimerControlAction.htm)|
Класс для действия управление таймером  
## __Интерфейсы
[IWorkflowAction](T_Tessa_Workflow_Actions_IWorkflowAction.htm)|  Обработчик
действий. При разработке новых действий следует наследоваться от класса
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm).  
---|---  
[IWorkflowActionRegistry](T_Tessa_Workflow_Actions_IWorkflowActionRegistry.htm)|
Описывает реестр типов действий
[IWorkflowAction](T_Tessa_Workflow_Actions_IWorkflowAction.htm)
