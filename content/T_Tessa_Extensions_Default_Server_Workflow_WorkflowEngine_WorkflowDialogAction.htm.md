# WorkflowDialogAction - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowDialogAction : WorkflowDialogAction
VB __Копировать
     Public NotInheritable Class WorkflowDialogAction
    	Inherits WorkflowDialogAction
C++ __Копировать
     public ref class WorkflowDialogAction sealed : public WorkflowDialogAction
F# __Копировать
     [<SealedAttribute>]
    type WorkflowDialogAction = 
        class
            inherit WorkflowDialogAction
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm) __[WorkflowDialogAction](T_Tessa_Workflow_Actions_WorkflowDialogAction.htm) __ WorkflowDialogAction
##  __Конструкторы
[WorkflowDialogAction](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowDialogAction__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowDialogAction  
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
[CheckActive](M_Tessa_Workflow_Actions_WorkflowDialogAction_CheckActive.htm)|
Метод для проверки факта, что действие активно и должно сохранить свое
состояние вместе с состояним своего узла.  
(Унаследован от
[WorkflowDialogAction](T_Tessa_Workflow_Actions_WorkflowDialogAction.htm))  
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
[ExecuteAsync](M_Tessa_Workflow_Actions_WorkflowDialogAction_ExecuteAsync.htm)|  
(Унаследован от
[WorkflowDialogAction](T_Tessa_Workflow_Actions_WorkflowDialogAction.htm))  
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
[PrepareForExecute](M_Tessa_Workflow_Actions_WorkflowDialogAction_PrepareForExecute.htm)|  
(Унаследован от
[WorkflowDialogAction](T_Tessa_Workflow_Actions_WorkflowDialogAction.htm))  
[PrepareForSaveTemplate](M_Tessa_Workflow_Actions_WorkflowActionBase_PrepareForSaveTemplate.htm)|
Метод подготовки действия для сохранения.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[ProcessAsync](M_Tessa_Workflow_Actions_WorkflowActionBase_ProcessAsync.htm)|
Метод, вызываемый при запуске действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[StoreDialogWithoutTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowDialogAction_StoreDialogWithoutTaskAsync.htm)|  
(Переопределяет
[WorkflowDialogAction.StoreDialogWithoutTaskAsync(IWorkflowEngineContext,
Dictionary<String,
Object>)](M_Tessa_Workflow_Actions_WorkflowDialogAction_StoreDialogWithoutTaskAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate](M_Tessa_Workflow_Actions_WorkflowActionBase_Validate.htm)|  Метод
валидации действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)
