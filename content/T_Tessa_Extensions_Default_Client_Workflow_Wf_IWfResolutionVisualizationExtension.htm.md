# IWfResolutionVisualizationExtension - интерфейс
Расширение на визуализацию дерева резолюций.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWfResolutionVisualizationExtension : IExtension
VB __Копировать
     Public Interface IWfResolutionVisualizationExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IWfResolutionVisualizationExtension : IExtension
F# __Копировать
     type IWfResolutionVisualizationExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[OnNodeGenerated](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnNodeGenerated.htm)|
Метод, выполняемый после завершения генерации объекта узла, соответствующего
одной из резолюций.  
---|---  
[OnNodeGenerating](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnNodeGenerating.htm)|
Метод, выполняемый перед началом генерации объекта узла, соответствующего
одной из резолюций.  
[OnVisualizationCompleted](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnVisualizationCompleted.htm)|
Метод, выполняемый после завершения визуализации, но перед отображением.  
[OnVisualizationStarted](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationExtension_OnVisualizationStarted.htm)|
Метод, выполняемый перед началом визуализации.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)
