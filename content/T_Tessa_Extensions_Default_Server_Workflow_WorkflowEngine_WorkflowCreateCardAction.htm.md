# WorkflowCreateCardAction - класс
Класс для действия Создать карточку
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class WorkflowCreateCardAction : WorkflowActionBase
VB __Копировать
     Public Class WorkflowCreateCardAction
    	Inherits WorkflowActionBase
C++ __Копировать
     public ref class WorkflowCreateCardAction : public WorkflowActionBase
F# __Копировать
     type WorkflowCreateCardAction = 
        class
            inherit WorkflowActionBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm) __ WorkflowCreateCardAction
##  __Конструкторы
[WorkflowCreateCardAction](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowCreateCardAction__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowCreateCardAction  
---|---  
##  __Свойства
[Descriptor](P_Tessa_Workflow_Actions_WorkflowActionBase_Descriptor.htm)|
Дескриптор действия. По умолчанию используется дескриптор, переданный в
конструкторе действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
---|---  
[ID](P_Tessa_Workflow_Actions_WorkflowActionBase_ID.htm)|  ID типа карточки,
он же ID в реестре
[IWorkflowActionRegistry](T_Tessa_Workflow_Actions_IWorkflowActionRegistry.htm).  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[IsStandAlone](P_Tessa_Workflow_Actions_WorkflowActionBase_IsStandAlone.htm)|
Флаг, обозначающий, что данное действие может быть только единственным
действием в узле.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
##  __Методы
[CheckActive](M_Tessa_Workflow_Actions_WorkflowActionBase_CheckActive.htm)|
Метод для проверки факта, что действие активно и должно сохранить свое
состояние вместе с состояним своего узла.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
---|---  
[Compile](M_Tessa_Workflow_Actions_WorkflowActionBase_Compile.htm)|  Метод для
компиляции данного действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowCreateCardAction_ExecuteAsync.htm)|  
(Переопределяет [WorkflowActionBase.ExecuteAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled)](M_Tessa_Workflow_Actions_WorkflowActionBase_ExecuteAsync.htm))  
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
[PrepareForExecute](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowCreateCardAction_PrepareForExecute.htm)|  
(Переопределяет
[WorkflowActionBase.PrepareForExecute(WorkflowActionStateStorage,
IWorkflowEngineContext)](M_Tessa_Workflow_Actions_WorkflowActionBase_PrepareForExecute.htm))  
[PrepareForSaveTemplate](M_Tessa_Workflow_Actions_WorkflowActionBase_PrepareForSaveTemplate.htm)|
Метод подготовки действия для сохранения.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[ProcessAsync](M_Tessa_Workflow_Actions_WorkflowActionBase_ProcessAsync.htm)|
Метод, вызываемый при запуске действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate](M_Tessa_Workflow_Actions_WorkflowActionBase_Validate.htm)|  Метод
валидации действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
##  __Поля
[MainSection](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowCreateCardAction_MainSection.htm)|  
---|---  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)
