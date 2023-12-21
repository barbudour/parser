# IWorkflowEngineCompilationCache - интерфейс
Кеш результатов компиляции в WorkflowEngine
## __Definition
 **Пространство имён:**
[Tessa.Workflow.Compilation](N_Tessa_Workflow_Compilation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineCompilationCache
VB __Копировать
     Public Interface IWorkflowEngineCompilationCache
C++ __Копировать
     public interface class IWorkflowEngineCompilationCache
F# __Копировать
     type IWorkflowEngineCompilationCache = interface end
##  __Методы
[GetAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache_GetAsync.htm)|
Получение значения из кэша по ID версии шаблона процесса  
---|---  
[GetTilesAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache_GetTilesAsync.htm)|
Получение значения из кэша по ID карточки шаблона процесса  
[InvalidateAllAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache_InvalidateAllAsync.htm)|
Метод для сброса кеша всех процессов  
[InvalidateAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache_InvalidateAsync.htm)|
Сброс кэша по ID версии шаблона процесса. В случае ошибки при инвалидации
файла со сборкой, возвращает
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
[InvalidateCardAsync](M_Tessa_Workflow_Compilation_IWorkflowEngineCompilationCache_InvalidateCardAsync.htm)|
Сброс кэша по ID карточки процесса. В случае ошибки при инвалидации файла со
сборкой, возвращает
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
## __См. также
#### Ссылки
[Tessa.Workflow.Compilation - пространство
имён](N_Tessa_Workflow_Compilation.htm)
