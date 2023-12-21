# WorkflowEngineProcessResult - класс
Результат обработки сигнала в
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)
##  __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowEngineProcessResult : IWorkflowEngineProcessResult
VB __Копировать
     Public NotInheritable Class WorkflowEngineProcessResult
    	Implements IWorkflowEngineProcessResult
C++ __Копировать
     public ref class WorkflowEngineProcessResult sealed : IWorkflowEngineProcessResult
F# __Копировать
     [<SealedAttribute>]
    type WorkflowEngineProcessResult = 
        class
            interface IWorkflowEngineProcessResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineProcessResult
Implements
    [IWorkflowEngineProcessResult](T_Tessa_Workflow_IWorkflowEngineProcessResult.htm)
##  __Конструкторы
[WorkflowEngineProcessResult(IWorkflowEngineContext)](M_Tessa_Workflow_WorkflowEngineProcessResult__ctor_2.htm)|
Инициализирует новый экземпляр класса WorkflowEngineProcessResult  
---|---  
[WorkflowEngineProcessResult(IValidationResultBuilder, Dictionary<String,
Object>)](M_Tessa_Workflow_WorkflowEngineProcessResult__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineProcessResult  
[WorkflowEngineProcessResult(ValidationResult, Dictionary<String,
Object>)](M_Tessa_Workflow_WorkflowEngineProcessResult__ctor_1.htm)|
Инициализирует новый экземпляр класса WorkflowEngineProcessResult  
##  __Свойства
[Empty](P_Tessa_Workflow_WorkflowEngineProcessResult_Empty.htm)|  Пустой
результат обработки процесса.  
---|---  
[EndSignals](P_Tessa_Workflow_WorkflowEngineProcessResult_EndSignals.htm)|
Сигналы, отправляемые на подписчиков при завершении процесса.  
[ResponseInfo](P_Tessa_Workflow_WorkflowEngineProcessResult_ResponseInfo.htm)|
Инфо, отправляемое в ответе на клиент.  
[StopPending](P_Tessa_Workflow_WorkflowEngineProcessResult_StopPending.htm)|
Определяет, осуществляется ли остановка процесса.  
[ValidationResult](P_Tessa_Workflow_WorkflowEngineProcessResult_ValidationResult.htm)|
Результат валидации выполнения обработки процесса.  
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
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
