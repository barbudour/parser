# WfResolutionVisualizationContext - класс
Контекст расширений на посещение записей в истории резолюций для визуализации
посредством
[IWfResolutionVisualizationGenerator](T_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationGenerator.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WfResolutionVisualizationContext : IWfResolutionVisualizationContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class WfResolutionVisualizationContext
    	Implements IWfResolutionVisualizationContext, IExtensionContext
C++ __Копировать
     public ref class WfResolutionVisualizationContext sealed : IWfResolutionVisualizationContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type WfResolutionVisualizationContext = 
        class
            interface IWfResolutionVisualizationContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WfResolutionVisualizationContext
Implements
    [IWfResolutionVisualizationContext](T_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[WfResolutionVisualizationContext](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_CancellationToken.htm)|  
---|---  
[Card](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_Card.htm)|
Карточка, обход резолюций которой выполняется.  
[HistoryItem](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_HistoryItem.htm)|
Посещаемая запись в истории заданий.  
[Info](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_Info.htm)|
Дополнительная информация, которая может пригодиться между посещениями узлов.  
[Node](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_Node.htm)|
Узел, соответствующий текущей резолюции, или null, если узел для текущей
резолюции ещё не был создан. При установке узла в методе расширений
[OnNodeGenerating(IWfResolutionVisualizationContext)](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnNodeGenerating.htm)
генерация узла стандартными средствами не будет выполнена. В методе расширений
[OnNodeGenerated(IWfResolutionVisualizationContext)](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnNodeGenerated.htm)
узел должен быть установлен как текущий сгенерированный узел.  
[NodeFactory](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_NodeFactory.htm)|
Фабрика узлов визуализатора.  
[NodeLayout](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_NodeLayout.htm)|
Макет визуализатора.  
[ParentAction](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_ParentAction.htm)|
Действие родительской резолюции по отношению к текущей, в результате которого
текущая резолюция была создана.  
[ParentNode](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_ParentNode.htm)|
Узел, соответствующий родительской резолюции, или null, если текущая резолюция
не имеет родительской.  
[RootHistoryItem](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_RootHistoryItem.htm)|
Корневая запись в истории заданий среди посещаемых резолюций. Не может быть
равна null.  
[RootTask](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_RootTask.htm)|
Корневое задание среди посещаемых резолюций или null, если для записи в
истории заданий отсутствует задание.  
[Task](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_Task.htm)|
Задание, которое соответствует записи
[HistoryItem](P_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationContext_HistoryItem.htm),
или null, если задание уже завершено или не было загружено.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)
