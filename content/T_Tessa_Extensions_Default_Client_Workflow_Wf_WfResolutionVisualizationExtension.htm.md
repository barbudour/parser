# WfResolutionVisualizationExtension - класс
Базовый класс расширения на визуализацию дерева резолюций.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WfResolutionVisualizationExtension : IWfResolutionVisualizationExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class WfResolutionVisualizationExtension
    	Implements IWfResolutionVisualizationExtension, IExtension
C++ __Копировать
     public ref class WfResolutionVisualizationExtension abstract : IWfResolutionVisualizationExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type WfResolutionVisualizationExtension = 
        class
            interface IWfResolutionVisualizationExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WfResolutionVisualizationExtension
Implements
    [IWfResolutionVisualizationExtension](T_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[WfResolutionVisualizationExtension](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationExtension__ctor.htm)|
Инициализирует новый экземпляр класса WfResolutionVisualizationExtension  
---|---  
##  __Методы
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
[OnNodeGenerated](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationExtension_OnNodeGenerated.htm)|
Метод, выполняемый после завершения генерации объекта узла, соответствующего
одной из резолюций.  
[OnNodeGenerating](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationExtension_OnNodeGenerating.htm)|
Метод, выполняемый перед началом генерации объекта узла, соответствующего
одной из резолюций.  
[OnVisualizationCompleted](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationExtension_OnVisualizationCompleted.htm)|
Метод, выполняемый после завершения визуализации, но перед отображением.  
[OnVisualizationStarted](M_Tessa_Extensions_Default_Client_Workflow_Wf_WfResolutionVisualizationExtension_OnVisualizationStarted.htm)|
Метод, выполняемый перед началом визуализации.  
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
