# WorkflowTaskInfo - класс
Информация по заданию, которая содержится в списке активных заданий.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class WorkflowTaskInfo : IWorkflowTaskInfo, 
    	IWorkflowProcessInfo
VB __Копировать
     Public Class WorkflowTaskInfo
    	Implements IWorkflowTaskInfo, IWorkflowProcessInfo
C++ __Копировать
     public ref class WorkflowTaskInfo : IWorkflowTaskInfo, 
    	IWorkflowProcessInfo
F# __Копировать
     type WorkflowTaskInfo = 
        class
            interface IWorkflowTaskInfo
            interface IWorkflowProcessInfo
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowTaskInfo
Implements
    [IWorkflowProcessInfo](T_Tessa_Cards_Workflow_IWorkflowProcessInfo.htm), [IWorkflowTaskInfo](T_Tessa_Cards_Workflow_IWorkflowTaskInfo.htm)
##  __Заметки
Классы-наследники могут добавлять строготипизированные свойства.
## __Конструкторы
[WorkflowTaskInfo(CardTask, IWorkflowProcessInfo, Dictionary<String,
Object>)](M_Tessa_Cards_Workflow_WorkflowTaskInfo__ctor.htm)|  Создаёт
информацию по новому заданию с указанием его свойств.  
---|---  
[WorkflowTaskInfo(CardTask, IWorkflowProcessInfo,
ISerializableObject)](M_Tessa_Cards_Workflow_WorkflowTaskInfo__ctor_1.htm)|
Создаёт информацию по заданию с указанием его свойств.  
## __Свойства
[PendingProcessParametersUpdate](P_Tessa_Cards_Workflow_WorkflowTaskInfo_PendingProcessParametersUpdate.htm)|
Признак того, что информация по подпроцессу была изменена, и требуется её
обновление. Обновление будет выполнено автоматически старте подпроцесса, при
завершении задания или при возвращении задания на роль.  
---|---  
[ProcessID](P_Tessa_Cards_Workflow_WorkflowTaskInfo_ProcessID.htm)|
Идентификатор экземпляра подпроцесса.  
[ProcessParameters](P_Tessa_Cards_Workflow_WorkflowTaskInfo_ProcessParameters.htm)|
Сериализуемые параметры подпроцесса.  
[ProcessTypeName](P_Tessa_Cards_Workflow_WorkflowTaskInfo_ProcessTypeName.htm)|
Имя типа подпроцесса, по которому можно определить выполняемые для подпроцесса
действия.  
[Task](P_Tessa_Cards_Workflow_WorkflowTaskInfo_Task.htm)| Задание в карточке.  
[TaskParameters](P_Tessa_Cards_Workflow_WorkflowTaskInfo_TaskParameters.htm)|
Сериализуемые параметры задания.  
##  __Методы
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
[ToTaskInfo](M_Tessa_Cards_Workflow_WorkflowExtensions_ToTaskInfo.htm)|
Преобразует заданный объект
[IWorkflowProcessInfo](T_Tessa_Cards_Workflow_IWorkflowProcessInfo.htm) с
информацией по подпроцессу к объекту типа
[IWorkflowTaskInfo](T_Tessa_Cards_Workflow_IWorkflowTaskInfo.htm) с
информацией по заданию. При невозможности преобразовать тип будет выдано
исключение
[InvalidCastException](https://learn.microsoft.com/dotnet/api/system.invalidcastexception).
Значение null возвращается только в том случае, если объект processInfo равен
null.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
