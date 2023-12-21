# KrWorkflowActionMethods.CreateTaskCompleteNotificationMethodTemplate - метод
Создаёт дескриптор метода изменения уведомления отправляющегося при завершении
задания с определённым вариантом завершения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static WorkflowActionMethodDescriptor CreateTaskCompleteNotificationMethodTemplate(
    	string[] storePath,
    	string[] listPath,
    	string[] errorDescriptionPath,
    	string[] methodDescriptionPath
    )
VB __Копировать
     Public Shared Function CreateTaskCompleteNotificationMethodTemplate ( 
    	storePath As String(),
    	listPath As String(),
    	errorDescriptionPath As String(),
    	methodDescriptionPath As String()
    ) As WorkflowActionMethodDescriptor
C++ __Копировать
     public:
    static WorkflowActionMethodDescriptor^ CreateTaskCompleteNotificationMethodTemplate(
    	array<String^>^ storePath, 
    	array<String^>^ listPath, 
    	array<String^>^ errorDescriptionPath, 
    	array<String^>^ methodDescriptionPath
    )
F# __Копировать
     static member CreateTaskCompleteNotificationMethodTemplate : 
            storePath : string[] * 
            listPath : string[] * 
            errorDescriptionPath : string[] * 
            methodDescriptionPath : string[] -> WorkflowActionMethodDescriptor 
#### Параметры
storePath [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Путь к месту в параметрах действия, где хранится текст скрипта. Для методов формируемых автоматически по строке - данное поле определяет путь к месту не в параметрах действия, а в строке.
listPath [String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Путь к месту в параметрах действия, где хранится таблица со скриптами. Путь к скрипту внутри строки определяется по storePath.
errorDescriptionPath
[String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Путь в строке к месту, где хранится строка используемая при формировании описания места возникновения ошибки при компиляции скрипта. Путь к строке определяется по listPath.
methodDescriptionPath
[String](https://learn.microsoft.com/dotnet/api/system.string)[]
    Путь в строке к месту, где хранится строка используемая при формировании описания метода. Путь к строке определяется по listPath.
#### Возвращаемое значение
[WorkflowActionMethodDescriptor](T_Tessa_Workflow_Actions_Descriptors_WorkflowActionMethodDescriptor.htm)  
Дескриптор метода действия.
##  __См. также
#### Ссылки
[KrWorkflowActionMethods -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrWorkflowActionMethods.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
