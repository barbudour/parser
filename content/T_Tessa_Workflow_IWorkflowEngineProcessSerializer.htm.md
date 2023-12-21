# IWorkflowEngineProcessSerializer - интерфейс
Объект для сериализации и десериализации карточек процесса Workflow Engine
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineProcessSerializer
VB __Копировать
     Public Interface IWorkflowEngineProcessSerializer
C++ __Копировать
     public interface class IWorkflowEngineProcessSerializer
F# __Копировать
     type IWorkflowEngineProcessSerializer = interface end
##  __Методы
[Deserialize](M_Tessa_Workflow_IWorkflowEngineProcessSerializer_Deserialize.htm)|
Метод для десериализации карточки процесса, которая была сериализована через
метод
[Serialize(Card)](M_Tessa_Workflow_IWorkflowEngineProcessSerializer_Serialize.htm)  
---|---  
[Serialize](M_Tessa_Workflow_IWorkflowEngineProcessSerializer_Serialize.htm)|
Метод для сериализации карточки процесса в бинарый вид с подписью данных.  
## __Методы расширения
[SerializeTo](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SerializeTo.htm)|
Метод для сериализации карточки процесса напрямую в Info по ключу
[WorkflowEngineProcessSerializedKey](F_Tessa_Workflow_Helpful_WorkflowEngineExtensions_WorkflowEngineProcessSerializedKey.htm)  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
---|---  
[TryDeserializeFrom](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_TryDeserializeFrom.htm)|
Метод для десирализации карточки процесса напрямую из Info по ключу
[WorkflowEngineProcessSerializedKey](F_Tessa_Workflow_Helpful_WorkflowEngineExtensions_WorkflowEngineProcessSerializedKey.htm)  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
