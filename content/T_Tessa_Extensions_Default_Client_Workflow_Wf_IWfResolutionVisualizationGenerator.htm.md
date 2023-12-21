# IWfResolutionVisualizationGenerator - интерфейс
Объект, создающий узлы визуализации резолюций по истории заданий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWfResolutionVisualizationGenerator
VB __Копировать
     Public Interface IWfResolutionVisualizationGenerator
C++ __Копировать
     public interface class IWfResolutionVisualizationGenerator
F# __Копировать
     type IWfResolutionVisualizationGenerator = interface end
##  __Методы
[GenerateAsync](M_Tessa_Extensions_Default_Client_Workflow_Wf_IWfResolutionVisualizationGenerator_GenerateAsync.htm)|
Создаёт узел со стрелкой от родительского узла по записи в истории заданий
резолюций. Возвращает созданный узел для этой записи или null, если узел не
был создан. Возвращённый узел не добавляется в макет визуализации.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)
