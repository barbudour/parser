# IWorkflowBindingExecutor - интерфейс
Описание объекта, который занимается получением и установкой значений по
привязке.
## __Definition
 **Пространство имён:**
[Tessa.Workflow.Bindings](N_Tessa_Workflow_Bindings.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowBindingExecutor
VB __Копировать
     Public Interface IWorkflowBindingExecutor
C++ __Копировать
     public interface class IWorkflowBindingExecutor
F# __Копировать
     type IWorkflowBindingExecutor = interface end
##  __Методы
[Get<T>](M_Tessa_Workflow_Bindings_IWorkflowBindingExecutor_Get__1.htm)|
Возвращает значение по привязке из параметров процесса, узла или действия.  
---|---  
[GetAsync<T>](M_Tessa_Workflow_Bindings_IWorkflowBindingExecutor_GetAsync__1.htm)|
Возвращает значение по привязке из контекста обработки процесса.  
[Set<T>(IWorkflowEngineContext, String,
T)](M_Tessa_Workflow_Bindings_IWorkflowBindingExecutor_Set__1_1.htm)|
Устанавливает значение по привязке по контексту обработки процесса.  
[Set<T>(Dictionary<String, Object>, Dictionary<String, Object>,
Dictionary<String, Object>, String,
T)](M_Tessa_Workflow_Bindings_IWorkflowBindingExecutor_Set__1.htm)|
Устанавливает значения по привязке по контексту обработки процесса.  
## __См. также
#### Ссылки
[Tessa.Workflow.Bindings - пространство имён](N_Tessa_Workflow_Bindings.htm)
