# NestedStagesCleaner - класс
Предоставляет методы для удаления вложенных этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NestedStagesCleaner
VB __Копировать
     Public NotInheritable Class NestedStagesCleaner
C++ __Копировать
     public ref class NestedStagesCleaner abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NestedStagesCleaner = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NestedStagesCleaner
##  __Методы
[ClearAll](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_NestedStagesCleaner_ClearAll.htm)|
Изменяет состояние у всех строк секции, содержащей созданные по шаблону и
имеющие к нему привязку этапы в указанной карточке, на
[Deleted](T_Tessa_Cards_CardRowState.htm).  
---|---  
[ClearGroup](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_NestedStagesCleaner_ClearGroup.htm)|
Изменяет состояние у всех строк, в том числе дочерних (определяется по полю
[ParentStageRowID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_ParentStageRowID.htm)),
секции, содержащей этапы в указанной карточке, на
[Deleted](T_Tessa_Cards_CardRowState.htm) удовлетворяющих условию: этап
принадлежит к группе из stageGroupIDs и вложенному процессу с идентификатором
nestedProcessID.  
[ClearStage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_NestedStagesCleaner_ClearStage.htm)|
Изменяет состояние у строки, и её дочерних строках, имеющей заданный
идентификатор содержащей информацию о этапе маршрута, на
[Deleted](T_Tessa_Cards_CardRowState.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
