# IKrRuntimeStage - интерфейс
Объект, предоставляющий информацию об этапе.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrRuntimeStage : IRuntimeSources, 
    	IExtraSources
VB __Копировать
     Public Interface IKrRuntimeStage
    	Inherits IRuntimeSources, IExtraSources
C++ __Копировать
     public interface class IKrRuntimeStage : IRuntimeSources, 
    	IExtraSources
F# __Копировать
     type IKrRuntimeStage = 
        interface
            interface IRuntimeSources
            interface IExtraSources
        end
Implements
    [IRuntimeSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IRuntimeSources.htm), [IExtraSources](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_IExtraSources.htm)
##  __Свойства
[CanBeSkipped](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_CanBeSkipped.htm)|
Возвращает значение признака, показывающего, разрешено ли пропускать этап.  
---|---  
[ExtraSources](P_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_IExtraSources_ExtraSources.htm)|
Возвращает список дополнительных методов.  
(Унаследован от
[IExtraSources](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_IExtraSources.htm))  
[GroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_GroupID.htm)|
Идентификатор группы, в которой находится шаблон, в котором находится этап.  
[GroupName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_GroupName.htm)|
Имя группы этапов, в которой находится шаблон, в котором находится этап.  
[GroupOrder](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_GroupOrder.htm)|
Порядок группы, в которой находится шаблон, в котором находится этап.  
[Hidden](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_Hidden.htm)|
Этап является скрытым.  
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_Order.htm)|
Порядок этапа в шаблоне.  
[Planned](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_Planned.htm)|
Дата выполнения.  
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
[Skip](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_Skip.htm)|
Флаг пропуска этапа.  
[SqlRoles](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_SqlRoles.htm)|
Запрос для вычисления SQL исполнителей.  
[StageID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_StageID.htm)|
Идентификатор этапа.  
[StageName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_StageName.htm)|
Название этапа.  
[StageTypeCaption](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_StageTypeCaption.htm)|
Отображаемое название типа этапа.  
[StageTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_StageTypeID.htm)|
Идентификатор типа этапа.  
[TemplateID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_TemplateID.htm)|
Идентификатор шаблона этапов.  
[TemplateName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_TemplateName.htm)|
Название шаблона этапов.  
[TimeLimit](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_TimeLimit.htm)|
Срок выполнения (рабочие дни).  
## __Методы
[GetSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrRuntimeStage_GetSettingsAsync.htm)|
Возвращает параметры этапа.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
