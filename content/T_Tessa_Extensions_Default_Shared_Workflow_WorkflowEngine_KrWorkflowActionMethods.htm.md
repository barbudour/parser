# KrWorkflowActionMethods - класс
Описания методов действий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrWorkflowActionMethods
VB __Копировать
     Public NotInheritable Class KrWorkflowActionMethods
C++ __Копировать
     public ref class KrWorkflowActionMethods abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrWorkflowActionMethods = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrWorkflowActionMethods
##  __Методы
[CreateActionCompleteNotificationMethodTemplate](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateActionCompleteNotificationMethodTemplate.htm)|
Создаёт дескриптор метода изменения уведомления отправляющегося при завершении
задания с определённым вариантом завершения.  
---|---  
[CreateActionOptionMethodTemplate](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateActionOptionMethodTemplate.htm)|
Создаёт дескриптор метода выполняющегося при завершении действия с
определённым вариантом завершения.  
[CreateCompletionTaskNotificationMethodTemplate](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateCompletionTaskNotificationMethodTemplate.htm)|
Создаёт дескриптор метода изменения уведомления отправляющегося при завершении
задания.  
[CreateTaskCompleteNotificationMethodTemplate](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateTaskCompleteNotificationMethodTemplate.htm)|
Создаёт дескриптор метода изменения уведомления отправляющегося при завершении
задания с определённым вариантом завершения.  
[CreateTaskInitMethodTemplate](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateTaskInitMethodTemplate.htm)|
Создаёт дескриптор метода инициализации задания.  
[CreateTaskOptionMethodTemplate](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateTaskOptionMethodTemplate.htm)|
Создаёт дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения.  
[CreateTaskStartNotificationMethodTemplate](M_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateTaskStartNotificationMethodTemplate.htm)|
Создаёт дескриптор метода изменения уведомления отправляющегося при
отправлении задания.  
## __Поля
[ActionCompleteParams](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_ActionCompleteParams.htm)|  
---|---  
[AdditionalApprovalTaskInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_AdditionalApprovalTaskInitMethod.htm)|
Дескриптор метода инициализации задания дополнительного согласования
[KrAdditionalApprovalTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrAdditionalApprovalTypeID.htm).  
[AdditionalApprovalTaskStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_AdditionalApprovalTaskStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания дополнительного согласования
[KrAdditionalApprovalTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrAdditionalApprovalTypeID.htm).  
[CreateCardInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_CreateCardInitMethod.htm)|
Дескриптор метода инициализации карточки в действии создания карточки.  
[EditInterjectTaskInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_EditInterjectTaskInitMethod.htm)|
Дескриптор метода инициализации задания доработки автором
[KrEditInterjectTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrEditInterjectTypeID.htm).  
[EditInterjectTaskStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_EditInterjectTaskStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания доработки автором
[KrEditInterjectTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrEditInterjectTypeID.htm).  
[KrAmendingCompleteNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrAmendingCompleteNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при завершении задания
с определённым вариантом завершения в действии
[KrAmendingDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrAmendingDescriptor.htm).  
[KrAmendingInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrAmendingInitMethod.htm)|
Дескриптор метода инициализации задания в действии
[KrAmendingDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrAmendingDescriptor.htm).  
[KrAmendingOptionMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrAmendingOptionMethod.htm)|
Дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения в действии
[KrAmendingDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrAmendingDescriptor.htm).  
[KrAmendingStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrAmendingStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания в действии
[KrAmendingDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrAmendingDescriptor.htm).  
[KrApprovalActionOptionActionMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrApprovalActionOptionActionMethod.htm)|
Дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения в действии
[KrApprovalDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrApprovalDescriptor.htm).  
[KrApprovalCompleteActionNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrApprovalCompleteActionNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при завершении
действия с определённым вариантом завершения в действии
[KrApprovalDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrApprovalDescriptor.htm).  
[KrApprovalCompleteNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrApprovalCompleteNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при завершении задания
с определённым вариантом завершения в действии
[KrApprovalDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrApprovalDescriptor.htm).  
[KrApprovalInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrApprovalInitMethod.htm)|
Дескриптор метода инициализации задания в действии
[KrApprovalDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrApprovalDescriptor.htm).  
[KrApprovalOptionMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrApprovalOptionMethod.htm)|
Дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения в действии
[KrApprovalDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrApprovalDescriptor.htm).  
[KrApprovalStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrApprovalStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания в действии
[KrApprovalDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrApprovalDescriptor.htm).  
[KrSigningActionOptionActionMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrSigningActionOptionActionMethod.htm)|
Дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения в действии
[KrSigningDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrSigningDescriptor.htm).  
[KrSigningCompleteActionNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrSigningCompleteActionNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при завершении
действия с определённым вариантом завершения в действии
[KrSigningDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrSigningDescriptor.htm).  
[KrSigningCompleteNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrSigningCompleteNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при завершении задания
с определённым вариантом завершения в действии
[KrSigningDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrSigningDescriptor.htm).  
[KrSigningInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrSigningInitMethod.htm)|
Дескриптор метода инициализации задания в действии
[KrSigningDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrSigningDescriptor.htm).  
[KrSigningOptionMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrSigningOptionMethod.htm)|
Дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения в действии
[KrSigningDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrSigningDescriptor.htm).  
[KrSigningStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrSigningStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания в действии
[KrSigningDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrSigningDescriptor.htm).  
[KrTaskRegistrationTaskCompleteNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrTaskRegistrationTaskCompleteNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при завершении задания
с определённым вариантом завершения в действии
[KrTaskRegistrationDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrTaskRegistrationDescriptor.htm).  
[KrTaskRegistrationTaskInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrTaskRegistrationTaskInitMethod.htm)|
Дескриптор метода инициализации задания в действии
[KrTaskRegistrationDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrTaskRegistrationDescriptor.htm).  
[KrTaskRegistrationTaskOptionMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrTaskRegistrationTaskOptionMethod.htm)|
Дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения в действии
[KrTaskRegistrationDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrTaskRegistrationDescriptor.htm).  
[KrTaskRegistrationTaskStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrTaskRegistrationTaskStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания в действии
[KrTaskRegistrationDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrTaskRegistrationDescriptor.htm).  
[KrUniversalTaskCompleteNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrUniversalTaskCompleteNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при завершении задания
с определённым вариантом завершения в действии
[KrUniversalTaskDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrUniversalTaskDescriptor.htm).  
[KrUniversalTaskInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrUniversalTaskInitMethod.htm)|
Дескриптор метода инициализации задания в действии
[KrUniversalTaskDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrUniversalTaskDescriptor.htm).  
[KrUniversalTaskOptionMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrUniversalTaskOptionMethod.htm)|
Дескриптор метода выполняющегося при завершении задания с определённым
вариантом завершения в действии
[KrUniversalTaskDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrUniversalTaskDescriptor.htm).  
[KrUniversalTaskStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_KrUniversalTaskStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания в действии
[KrUniversalTaskDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrDescriptors_KrUniversalTaskDescriptor.htm).  
[RequestCommentTaskInitMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_RequestCommentTaskInitMethod.htm)|
Дескриптор метода инициализации задания запроса комментария
[KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm).  
[RequestCommentTaskStartNotificationMethod](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_RequestCommentTaskStartNotificationMethod.htm)|
Дескриптор метода изменения уведомления отправляющегося при отправлении
задания запроса комментария
[KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm).  
[TaskCompleteBaseParams](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods_TaskCompleteBaseParams.htm)|  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
