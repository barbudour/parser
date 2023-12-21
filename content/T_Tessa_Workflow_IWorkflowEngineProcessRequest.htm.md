# IWorkflowEngineProcessRequest - интерфейс
Запрос на обработку процесса WorkflowEngine.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineProcessRequest
VB __Копировать
     Public Interface IWorkflowEngineProcessRequest
C++ __Копировать
     public interface class IWorkflowEngineProcessRequest
F# __Копировать
     type IWorkflowEngineProcessRequest = interface end
##  __Свойства
[CardID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_CardID.htm)|
Идентификатор карточки, для которой отправляется процесс, или null, если
карточка определяется по экземпляру процесса или процесс глобальный.  
---|---  
[EngineContext](P_Tessa_Workflow_IWorkflowEngineProcessRequest_EngineContext.htm)|
Контекст обработки процесса.  
[NodeIDs](P_Tessa_Workflow_IWorkflowEngineProcessRequest_NodeIDs.htm)|  Список
идентификаторов узлов, на которые производится отправка сигнала.  
[NodeInstanceIDs](P_Tessa_Workflow_IWorkflowEngineProcessRequest_NodeInstanceIDs.htm)|
Список идентификаторов экземпляров узлов, на которые производится отправка
сигнала.  
[ProcessDigest](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessDigest.htm)|
Наименование процесса или экземпляра процесса, отображаемое в асинхронной
операции, или null, если имя определяется автоматически.  
[ProcessFlag](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessFlag.htm)|
Флаг для обработки процесса.  
[ProcessInstance](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessInstance.htm)|
Экземпляр процесса.  
[ProcessInstanceID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessInstanceID.htm)|
Идентификатор экземпляра процесса.  
[ProcessTemplateID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessTemplateID.htm)|
Идентификатор шаблона процесса. Необходим при создании нового процесса, если
не задан
[ProcessTemplateVersionID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessTemplateVersionID.htm)  
[ProcessTemplateVersionID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessTemplateVersionID.htm)|
Идентификатор версии шаблона процесса. Необходим при создании нового процесса,
если не задан
[ProcessTemplateID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessTemplateID.htm)  
[Signal](P_Tessa_Workflow_IWorkflowEngineProcessRequest_Signal.htm)|
Отправляемый сигнал.  
[SignalProcessingMode](P_Tessa_Workflow_IWorkflowEngineProcessRequest_SignalProcessingMode.htm)|
Флаг определяет метод обработки сигнала.  
[StoreCard](P_Tessa_Workflow_IWorkflowEngineProcessRequest_StoreCard.htm)|
Сохраняемая карточка, в рамках которой запускается обработка процесса.  
[WorkflowCard](P_Tessa_Workflow_IWorkflowEngineProcessRequest_WorkflowCard.htm)|
Карточка процесса, которая содержит в себе всю информацию о дереве процесса.  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
