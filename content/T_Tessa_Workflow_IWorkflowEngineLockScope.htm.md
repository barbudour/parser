# IWorkflowEngineLockScope - интерфейс
Объект, отвечающий за блокировку экземпляра процесса.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineLockScope
VB __Копировать
     Public Interface IWorkflowEngineLockScope
C++ __Копировать
     public interface class IWorkflowEngineLockScope
F# __Копировать
     type IWorkflowEngineLockScope = interface end
##  __Методы
[CheckLockAsync](M_Tessa_Workflow_IWorkflowEngineLockScope_CheckLockAsync.htm)|
Проверяет наличие блокировки на экземпляре процесса и пишет ошибку в
validationResults, если процесс заблокирован в рамках другой транзакции.  
---|---  
[LockProcessAsync](M_Tessa_Workflow_IWorkflowEngineLockScope_LockProcessAsync.htm)|
Блокирует процесс на выполнение по его ID в рамках текущей транзакции, если он
еще не был заблокирован, и пишет ошибку в validationResults, если процесс
заблокирован в рамках другой транзакции.  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
