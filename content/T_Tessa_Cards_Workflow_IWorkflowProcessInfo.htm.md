# IWorkflowProcessInfo - интерфейс
Информация по подпроцессу.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowProcessInfo
VB __Копировать
     Public Interface IWorkflowProcessInfo
C++ __Копировать
     public interface class IWorkflowProcessInfo
F# __Копировать
     type IWorkflowProcessInfo = interface end
##  __Свойства
[PendingProcessParametersUpdate](P_Tessa_Cards_Workflow_IWorkflowProcessInfo_PendingProcessParametersUpdate.htm)|
Признак того, что информация по подпроцессу была изменена, и требуется её
обновление. Обновление будет выполнено автоматически старте подпроцесса, при
завершении задания или при возвращении задания на роль.  
---|---  
[ProcessID](P_Tessa_Cards_Workflow_IWorkflowProcessInfo_ProcessID.htm)|
Идентификатор экземпляра подпроцесса.  
[ProcessParameters](P_Tessa_Cards_Workflow_IWorkflowProcessInfo_ProcessParameters.htm)|
Сериализуемые параметры подпроцесса.  
[ProcessTypeName](P_Tessa_Cards_Workflow_IWorkflowProcessInfo_ProcessTypeName.htm)|
Имя типа подпроцесса, по которому можно определить выполняемые для подпроцесса
действия.  
##  __Методы расширения
[ToTaskInfo](M_Tessa_Cards_Workflow_WorkflowExtensions_ToTaskInfo.htm)|
Преобразует заданный объект IWorkflowProcessInfo с информацией по подпроцессу
к объекту типа
[IWorkflowTaskInfo](T_Tessa_Cards_Workflow_IWorkflowTaskInfo.htm) с
информацией по заданию. При невозможности преобразовать тип будет выдано
исключение
[InvalidCastException](https://learn.microsoft.com/dotnet/api/system.invalidcastexception).
Значение null возвращается только в том случае, если объект processInfo равен
null.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
