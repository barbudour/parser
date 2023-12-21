# WorkflowEngineProcessRequest - класс
Запрос на обработку процесса WorkflowEngine.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowEngineProcessRequest : StorageSerializable, 
    	IWorkflowEngineProcessRequest
VB __Копировать
     Public NotInheritable Class WorkflowEngineProcessRequest
    	Inherits StorageSerializable
    	Implements IWorkflowEngineProcessRequest
C++ __Копировать
     public ref class WorkflowEngineProcessRequest sealed : public StorageSerializable, 
    	IWorkflowEngineProcessRequest
F# __Копировать
     [<SealedAttribute>]
    type WorkflowEngineProcessRequest = 
        class
            inherit StorageSerializable
            interface IWorkflowEngineProcessRequest
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ WorkflowEngineProcessRequest
Implements
    [IWorkflowEngineProcessRequest](T_Tessa_Workflow_IWorkflowEngineProcessRequest.htm)
##  __Конструкторы
[WorkflowEngineProcessRequest](M_Tessa_Workflow_WorkflowEngineProcessRequest__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineProcessRequest  
---|---  
##  __Свойства
[CardID](P_Tessa_Workflow_WorkflowEngineProcessRequest_CardID.htm)|
Идентификатор карточки, для которой отправляется процесс, или null, если
карточка определяется по экземпляру процесса или процесс глобальный.  
---|---  
[EngineContext](P_Tessa_Workflow_WorkflowEngineProcessRequest_EngineContext.htm)|
Контекст обработки процесса.  
[NodeIDs](P_Tessa_Workflow_WorkflowEngineProcessRequest_NodeIDs.htm)|  Список
идентификаторов узлов, на которые производится отправка сигнала.  
[NodeInstanceIDs](P_Tessa_Workflow_WorkflowEngineProcessRequest_NodeInstanceIDs.htm)|
Список идентификаторов экземпляров узлов, на которые производится отправка
сигнала.  
[ProcessDigest](P_Tessa_Workflow_WorkflowEngineProcessRequest_ProcessDigest.htm)|
Наименование процесса или экземпляра процесса, отображаемое в асинхронной
операции, или null, если имя определяется автоматически.  
[ProcessFlag](P_Tessa_Workflow_WorkflowEngineProcessRequest_ProcessFlag.htm)|
Флаг для обработки процесса.  
[ProcessInstance](P_Tessa_Workflow_WorkflowEngineProcessRequest_ProcessInstance.htm)|
Экземпляр процесса.  
[ProcessInstanceID](P_Tessa_Workflow_WorkflowEngineProcessRequest_ProcessInstanceID.htm)|
Идентификатор экземпляра процесса.  
[ProcessTemplateID](P_Tessa_Workflow_WorkflowEngineProcessRequest_ProcessTemplateID.htm)|
Идентификатор шаблона процесса. Необходим при создании нового процесса, если
не задан
[ProcessTemplateVersionID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessTemplateVersionID.htm)  
[ProcessTemplateVersionID](P_Tessa_Workflow_WorkflowEngineProcessRequest_ProcessTemplateVersionID.htm)|
Идентификатор версии шаблона процесса. Необходим при создании нового процесса,
если не задан
[ProcessTemplateID](P_Tessa_Workflow_IWorkflowEngineProcessRequest_ProcessTemplateID.htm)  
[Signal](P_Tessa_Workflow_WorkflowEngineProcessRequest_Signal.htm)|
Отправляемый сигнал.  
[SignalProcessingMode](P_Tessa_Workflow_WorkflowEngineProcessRequest_SignalProcessingMode.htm)|
Флаг определяет метод обработки сигнала.  
[StoreCard](P_Tessa_Workflow_WorkflowEngineProcessRequest_StoreCard.htm)|
Сохраняемая карточка, в рамках которой запускается обработка процесса.  
[WorkflowCard](P_Tessa_Workflow_WorkflowEngineProcessRequest_WorkflowCard.htm)|
Карточка процесса, которая содержит в себе всю информацию о дереве процесса.  
## __Методы
[Deserialize](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
---|---  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Workflow_WorkflowEngineProcessRequest_DeserializeCore.htm)|  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Serialize](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Workflow_WorkflowEngineProcessRequest_SerializeCore.htm)|  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
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
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
