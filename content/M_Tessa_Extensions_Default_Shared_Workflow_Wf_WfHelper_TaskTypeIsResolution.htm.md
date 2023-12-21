# WfHelper.TaskTypeIsResolution - метод
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TaskTypeIsResolution(
    	Guid taskTypeID
    )
VB __Копировать
     Public Shared Function TaskTypeIsResolution ( 
    	taskTypeID As Guid
    ) As Boolean
C++ __Копировать
     public:
    static bool TaskTypeIsResolution(
    	Guid taskTypeID
    )
F# __Копировать
     static member TaskTypeIsResolution : 
            taskTypeID : Guid -> bool 
#### Параметры
taskTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа задания.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если тип задания с заданным идентификатором является одним из типов
заданий резолюции; false в противном случае.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
