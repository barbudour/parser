# IKrStageTemplate - интерфейс
Объект, предоставляющий информацию об шаблоне этапов, необходимую для его
компиляции и выполнения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrStageTemplate : IDesignTimeSources
VB __Копировать
     Public Interface IKrStageTemplate
    	Inherits IDesignTimeSources
C++ __Копировать
     public interface class IKrStageTemplate : IDesignTimeSources
F# __Копировать
     type IKrStageTemplate = 
        interface
            interface IDesignTimeSources
        end
Implements
    [IDesignTimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources.htm)
##  __Свойства
[CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_CanChangeOrder.htm)|
Возвращает значение, показывающее, можно ли перемещать этапы.  
---|---  
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_ID.htm)|
Возвращает идентификатор шаблона этапов.  
[IsStagesReadonly](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_IsStagesReadonly.htm)|
Возвращает значение, показывающее, являются ли этапы нередактируемыми.  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_Name.htm)|
Возвращает название шаблона этапов.  
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_Order.htm)|
Возвращает порядок шаблона.  
[Position](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_Position.htm)|
Возвращает положение относительно этапов, добавленных вручную.  
[SourceAfter](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources_SourceAfter.htm)|
C# код сценария постобработки времени построения.  
(Унаследован от
[IDesignTimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources.htm))  
[SourceBefore](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources_SourceBefore.htm)|
C# код сценария инициализации времени построения.  
(Унаследован от
[IDesignTimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources.htm))  
[SourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources_SourceCondition.htm)|
C# код условия времени построения.  
(Унаследован от
[IDesignTimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources.htm))  
[SqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources_SqlCondition.htm)|
Текст SQL запроса условия времени построения.  
(Унаследован от
[IDesignTimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources.htm))  
[StageGroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_StageGroupID.htm)|
Возвращает идентификатор группы этапов, к которой относится шаблон.  
[StageGroupName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageTemplate_StageGroupName.htm)|
Возвращает название группы этапов, к которой относится шаблон.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
