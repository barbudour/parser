# IWfResolutionVisualizationContext - интерфейс
Контекст расширений на посещение записей в истории резолюций для визуализации
посредством
[IWfResolutionVisualizationGenerator](T_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationGenerator.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWfResolutionVisualizationContext : IExtensionContext
VB __Копировать
     Public Interface IWfResolutionVisualizationContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IWfResolutionVisualizationContext : IExtensionContext
F# __Копировать
     type IWfResolutionVisualizationContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[Card](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_Card.htm)|
Карточка, обход резолюций которой выполняется.  
[HistoryItem](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_HistoryItem.htm)|
Посещаемая запись в истории заданий.  
[Info](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_Info.htm)|
Дополнительная информация, которая может пригодиться между посещениями узлов.  
[Node](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_Node.htm)|
Узел, соответствующий текущей резолюции, или null, если узел для текущей
резолюции ещё не был создан. При установке узла в методе расширений
[OnNodeGenerating(IWfResolutionVisualizationContext)](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnNodeGenerating.htm)
генерация узла стандартными средствами не будет выполнена. В методе расширений
[OnNodeGenerated(IWfResolutionVisualizationContext)](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnNodeGenerated.htm)
узел должен быть установлен как текущий сгенерированный узел.  
[NodeFactory](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_NodeFactory.htm)|
Фабрика узлов визуализатора.  
[NodeLayout](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_NodeLayout.htm)|
Макет визуализатора.  
[ParentAction](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_ParentAction.htm)|
Действие родительской резолюции по отношению к текущей, в результате которого
текущая резолюция была создана.  
[ParentNode](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_ParentNode.htm)|
Узел, соответствующий родительской резолюции, или null, если текущая резолюция
не имеет родительской.  
[RootHistoryItem](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_RootHistoryItem.htm)|
Корневая запись в истории заданий среди посещаемых резолюций. Не может быть
равна null.  
[RootTask](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_RootTask.htm)|
Корневое задание среди посещаемых резолюций или null, если для записи в
истории заданий отсутствует задание.  
[Task](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_Task.htm)|
Задание, которое соответствует записи
[HistoryItem](P_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext_HistoryItem.htm),
или null, если задание уже завершено или не было загружено. Даже если задание
указано, его секции могут быть не загружены.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)
