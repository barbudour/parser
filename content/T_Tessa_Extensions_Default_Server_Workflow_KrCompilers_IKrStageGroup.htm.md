# IKrStageGroup - интерфейс
Объект, предоставляющий информацию о группе этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrStageGroup : IRuntimeSources, 
    	IDesignTimeSources
VB __Копировать
     Public Interface IKrStageGroup
    	Inherits IRuntimeSources, IDesignTimeSources
C++ __Копировать
     public interface class IKrStageGroup : IRuntimeSources, 
    	IDesignTimeSources
F# __Копировать
     type IKrStageGroup = 
        interface
            interface IRuntimeSources
            interface IDesignTimeSources
        end
Implements
    [IDesignTimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IDesignTimeSources.htm), [IRuntimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources.htm)
##  __Свойства
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageGroup_ID.htm)|
Идентификатор группы этапов.  
---|---  
[IsGroupReadonly](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageGroup_IsGroupReadonly.htm)|
Значение, показывающее, являются ли все этапы нередактируемыми.  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageGroup_Name.htm)|
Название группы этапов.  
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageGroup_Order.htm)|
Порядок группы этапов.  
[RuntimeSourceAfter](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources_RuntimeSourceAfter.htm)|
C# код сценария постобработки времени выполнения.  
(Унаследован от
[IRuntimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources.htm))  
[RuntimeSourceBefore](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources_RuntimeSourceBefore.htm)|
C# код сценария инициализации времени выполнения.  
(Унаследован от
[IRuntimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources.htm))  
[RuntimeSourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources_RuntimeSourceCondition.htm)|
C# код условия времени выполнения.  
(Унаследован от
[IRuntimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources.htm))  
[RuntimeSqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources_RuntimeSqlCondition.htm)|
Текст SQL запроса условия времени выполнения.  
(Унаследован от
[IRuntimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources.htm))  
[SecondaryProcessID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrStageGroup_SecondaryProcessID.htm)|
Идентификатор вторичного процесса, к которому привязана группа этапов.  
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
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
