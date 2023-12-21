# WfHelper.TaskTypeIsResolutionWithoutControl - метод
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции, который не требует контроля исполнения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TaskTypeIsResolutionWithoutControl(
    	Guid taskTypeID
    )
VB __Копировать
     Public Shared Function TaskTypeIsResolutionWithoutControl ( 
    	taskTypeID As Guid
    ) As Boolean
C++ __Копировать
     public:
    static bool TaskTypeIsResolutionWithoutControl(
    	Guid taskTypeID
    )
F# __Копировать
     static member TaskTypeIsResolutionWithoutControl : 
            taskTypeID : Guid -> bool 
#### Параметры
taskTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа задания.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если тип задания с заданным идентификатором является одним из типов
заданий резолюции, который не требует контроля исполнения; false в противном
случае.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
