# WorkflowEngineProcessSerializer - класс
Объект для сериализации и десериализации карточек процесса Workflow Engine
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowEngineProcessSerializer : IWorkflowEngineProcessSerializer
VB __Копировать
     Public NotInheritable Class WorkflowEngineProcessSerializer
    	Implements IWorkflowEngineProcessSerializer
C++ __Копировать
     public ref class WorkflowEngineProcessSerializer sealed : IWorkflowEngineProcessSerializer
F# __Копировать
     [<SealedAttribute>]
    type WorkflowEngineProcessSerializer = 
        class
            interface IWorkflowEngineProcessSerializer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineProcessSerializer
Implements
    [IWorkflowEngineProcessSerializer](T_Tessa_Workflow_IWorkflowEngineProcessSerializer.htm)
##  __Конструкторы
[WorkflowEngineProcessSerializer](M_Tessa_Workflow_WorkflowEngineProcessSerializer__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineProcessSerializer  
---|---  
##  __Методы
[Deserialize](M_Tessa_Workflow_WorkflowEngineProcessSerializer_Deserialize.htm)|
Метод для десериализации карточки процесса, которая была сериализована через
метод
[Serialize(Card)](M_Tessa_Workflow_IWorkflowEngineProcessSerializer_Serialize.htm)  
---|---  
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
[Serialize](M_Tessa_Workflow_WorkflowEngineProcessSerializer_Serialize.htm)|
Метод для сериализации карточки процесса в бинарый вид с подписью данных.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CardDataKey](F_Tessa_Workflow_WorkflowEngineProcessSerializer_CardDataKey.htm)|  
---|---  
[SignDataKey](F_Tessa_Workflow_WorkflowEngineProcessSerializer_SignDataKey.htm)|  
## __Методы расширения
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
[SerializeTo](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SerializeTo.htm)|
Метод для сериализации карточки процесса напрямую в Info по ключу
[WorkflowEngineProcessSerializedKey](F_Tessa_Workflow_Helpful_WorkflowEngineExtensions_WorkflowEngineProcessSerializedKey.htm)  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[TryDeserializeFrom](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_TryDeserializeFrom.htm)|
Метод для десирализации карточки процесса напрямую из Info по ключу
[WorkflowEngineProcessSerializedKey](F_Tessa_Workflow_Helpful_WorkflowEngineExtensions_WorkflowEngineProcessSerializedKey.htm)  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
