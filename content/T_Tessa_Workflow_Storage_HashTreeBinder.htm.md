# HashTreeBinder - класс
Объект, осуществляющий связь значений хеша с значениями в секциях карточки с
учетом возможности привязки данных к хешам родительского узла и процесса.
Также осуществляет обновление имен полей, имеющих ссылки на переходы процесса.
## __Definition
 **Пространство имён:** [Tessa.Workflow.Storage](N_Tessa_Workflow_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class HashTreeBinder : IWorkflowHashBinder
VB __Копировать
     Public NotInheritable Class HashTreeBinder
    	Implements IWorkflowHashBinder
C++ __Копировать
     public ref class HashTreeBinder sealed : IWorkflowHashBinder
F# __Копировать
     [<SealedAttribute>]
    type HashTreeBinder = 
        class
            interface IWorkflowHashBinder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ HashTreeBinder
Implements
    [IWorkflowHashBinder](T_Tessa_Workflow_IWorkflowHashBinder.htm)
##  __Конструкторы
[HashTreeBinder](M_Tessa_Workflow_Storage_HashTreeBinder__ctor.htm)|
Инициализирует новый экземпляр класса HashTreeBinder  
---|---  
##  __Методы
[AddLinkBinding(WorkflowStorageBase,
String[])](M_Tessa_Workflow_Storage_HashTreeBinder_AddLinkBinding.htm)|
Создаёт новую привязку для связи.  
---|---  
[AddLinkBinding(WorkflowStorageBase, String[],
String[])](M_Tessa_Workflow_Storage_HashTreeBinder_AddLinkBinding_1.htm)|
Создаёт новую привязку для связи.  
[AttachAction](M_Tessa_Workflow_Storage_HashTreeBinder_AttachAction.htm)|
Создаёт привязку для указанного действия.  
[AttachNode](M_Tessa_Workflow_Storage_HashTreeBinder_AttachNode.htm)|  Создаёт
привязку для указанного узла.  
[AttachProcess](M_Tessa_Workflow_Storage_HashTreeBinder_AttachProcess.htm)|
Создаёт привязку для указанного процесса.  
[CreateFieldBindingAsync](M_Tessa_Workflow_Storage_HashTreeBinder_CreateFieldBindingAsync.htm)|
Создаёт привязку поля строковой секции к хешу.  
[CreateRowFieldBindingAsync](M_Tessa_Workflow_Storage_HashTreeBinder_CreateRowFieldBindingAsync.htm)|
Создаёт привязку поля строки коллекционной или древовидной секции к хешу.  
[CreateTableBindingAsync](M_Tessa_Workflow_Storage_HashTreeBinder_CreateTableBindingAsync.htm)|
Создаёт привязку табличной секции к хешу.  
[DetachActionAsync](M_Tessa_Workflow_Storage_HashTreeBinder_DetachActionAsync.htm)|
Удаляет привязку для указанного действия.  
[DetachNodeAsync](M_Tessa_Workflow_Storage_HashTreeBinder_DetachNodeAsync.htm)|
Удаляет привязку для указанного узла.  
[DetachProcessAsync](M_Tessa_Workflow_Storage_HashTreeBinder_DetachProcessAsync.htm)|
Удаляет привязку для указанного процесса.  
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
[GetFieldError(CardSection,
String[])](M_Tessa_Workflow_Storage_HashTreeBinder_GetFieldError.htm)|  
[GetFieldError(CardSection, CardRow,
String[])](M_Tessa_Workflow_Storage_HashTreeBinder_GetFieldError_1.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSectionError](M_Tessa_Workflow_Storage_HashTreeBinder_GetSectionError.htm)|  
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
[MoveLinkBindings](M_Tessa_Workflow_Storage_HashTreeBinder_MoveLinkBindings.htm)|  
[RemoveRowBinding(WorkflowStorageBase, WorkflowStorageBase,
WorkflowStorageBase, String,
Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_RemoveRowBinding.htm)|  
[RemoveRowBinding(WorkflowStorageBase, WorkflowStorageBase,
WorkflowStorageBase, ParamSourceType, String[],
Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_RemoveRowBinding_1.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateBinded(WorkflowStorageBase, String[], Object,
Object)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateBinded_1.htm)|  
[UpdateBinded(WorkflowStorageBase, String[], Int32, String[], Object,
Object)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateBinded.htm)|  
[UpdateBinded(WorkflowStorageBase, WorkflowStorageBase, WorkflowStorageBase,
String, Object,
Object)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateBinded_2.htm)|  
[UpdateBinded(WorkflowStorageBase, WorkflowStorageBase, WorkflowStorageBase,
ParamSourceType, Object, Object,
String[])](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateBinded_3.htm)|  
[UpdateBinded(WorkflowStorageBase, WorkflowStorageBase, WorkflowStorageBase,
ParamSourceType, String[], Int32, String[], Object,
Object)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateBinded_4.htm)|  
[UpdateInserted(WorkflowStorageBase, String[],
Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateInserted.htm)|  
[UpdateInserted(WorkflowStorageBase, WorkflowStorageBase, WorkflowStorageBase,
String, Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateInserted_1.htm)|  
[UpdateInserted(WorkflowStorageBase, WorkflowStorageBase, WorkflowStorageBase,
ParamSourceType, String[],
Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateInserted_2.htm)|  
[UpdateRemoved(WorkflowStorageBase, String[],
Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateRemoved.htm)|  
[UpdateRemoved(WorkflowStorageBase, WorkflowStorageBase, WorkflowStorageBase,
String, Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateRemoved_1.htm)|  
[UpdateRemoved(WorkflowStorageBase, WorkflowStorageBase, WorkflowStorageBase,
ParamSourceType, String[],
Int32)](M_Tessa_Workflow_Storage_HashTreeBinder_UpdateRemoved_2.htm)|  
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
[Tessa.Workflow.Storage - пространство имён](N_Tessa_Workflow_Storage.htm)
