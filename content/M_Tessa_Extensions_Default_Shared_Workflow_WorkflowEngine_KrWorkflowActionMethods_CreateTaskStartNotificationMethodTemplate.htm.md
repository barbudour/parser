# KrWorkflowActionMethods.CreateTaskStartNotificationMethodTemplate - метод
Создаёт дескриптор метода изменения уведомления отправляющегося при
отправлении задания.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static WorkflowActionMethodDescriptor CreateTaskStartNotificationMethodTemplate(
    	string[] storePath,
    	string methodName = "NotificationScript"
    )
VB __Копировать
     Public Shared Function CreateTaskStartNotificationMethodTemplate ( 
    	storePath As String(),
    	Optional methodName As String = "NotificationScript"
    ) As WorkflowActionMethodDescriptor
C++ __Копировать
     public:
    static WorkflowActionMethodDescriptor^ CreateTaskStartNotificationMethodTemplate(
    	array<String^>^ storePath, 
    	String^ methodName = L"NotificationScript"
    )
F# __Копировать
     static member CreateTaskStartNotificationMethodTemplate : 
            storePath : string[] * 
            ?methodName : string 
    (* Defaults:
            let _methodName = defaultArg methodName "NotificationScript"
    *)
    -> WorkflowActionMethodDescriptor 
#### Параметры
storePath [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Путь к месту в параметрах действия, где хранится текст скрипта. Для методов формируемых автоматически по строке - данное поле определяет путь к месту не в параметрах действия, а в строке.
methodName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя метода. Значение по умолчанию: NotificationScript.
#### Возвращаемое значение
[WorkflowActionMethodDescriptor](T_Tessa_Workflow_Actions_Descriptors_WorkflowActionMethodDescriptor.htm)  
Дескриптор метода действия.
##  __См. также
#### Ссылки
[KrWorkflowActionMethods -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
