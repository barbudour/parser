# StageTypeDescriptor.Create - метод
Создать новый дескриптор.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static StageTypeDescriptor Create(
    	Action<StageTypeDescriptorBuilder> action
    )
VB __Копировать
     Public Shared Function Create ( 
    	action As Action(Of StageTypeDescriptorBuilder)
    ) As StageTypeDescriptor
C++ __Копировать
     public:
    static StageTypeDescriptor^ Create(
    	Action<StageTypeDescriptorBuilder^>^ action
    )
F# __Копировать
     static member Create : 
            action : Action<StageTypeDescriptorBuilder> -> StageTypeDescriptor 
#### Параметры
action
[Action](https://learn.microsoft.com/dotnet/api/system.action-1)<[StageTypeDescriptorBuilder](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptorBuilder.htm)>
    Метод, модифицирующий новый дескриптор.
#### Возвращаемое значение
[StageTypeDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor.htm)  
Новый дескриптор.
##  __См. также
#### Ссылки
[StageTypeDescriptor -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
