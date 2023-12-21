# IWorkflowEngineCompiled - интерфейс
Интерфейс для скомпилированного объекта в WorkflowEngine.
## __Definition
 **Пространство имён:**
[Tessa.Workflow.Compilation](N_Tessa_Workflow_Compilation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineCompiled
VB __Копировать
     Public Interface IWorkflowEngineCompiled
C++ __Копировать
     public interface class IWorkflowEngineCompiled
F# __Копировать
     type IWorkflowEngineCompiled = interface end
##  __Методы
[Condition](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_Condition.htm)|
Скрипт условия.  
---|---  
[ExecuteActionAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_ExecuteActionAsync.htm)|
Запускает выполнение метода скомпилированного объекта с указанным именем и
параметрами.  
[ExecuteFuncAsync<T>](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_ExecuteFuncAsync__1.htm)|
Запускает выполнение метода скомпилированного объекта, возвращающего значение,
с указанным именем и параметрами.  
[InConditionAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_InConditionAsync.htm)|
Скрипт условия входа в узел.  
[OutConditionAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_OutConditionAsync.htm)|
Скрипт условия выхода из узла  
[PostScriptAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_PostScriptAsync.htm)|
Скрипт постобработки.  
[PreScriptAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_PreScriptAsync.htm)|
Скрипт предобработки.  
[SetContext](M_Tessa_Workflow_Compilation_IWorkflowEngineCompiled_SetContext.htm)|
Метод для установки текущего контекста.  
## __См. также
#### Ссылки
[Tessa.Workflow.Compilation - пространство
имён](N_Tessa_Workflow_Compilation.htm)
