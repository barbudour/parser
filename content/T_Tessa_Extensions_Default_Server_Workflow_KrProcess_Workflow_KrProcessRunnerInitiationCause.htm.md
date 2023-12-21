# KrProcessRunnerInitiationCause - перечисление
Перечисление причин запуска процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum KrProcessRunnerInitiationCause
VB __Копировать
     Public Enumeration KrProcessRunnerInitiationCause
C++ __Копировать
     public enum class KrProcessRunnerInitiationCause
F# __Копировать
     type KrProcessRunnerInitiationCause
##  __Члены
StartProcess| 0|  Запуск процесса.  
---|---|---  
CompleteTask| 1|  Завершение задания.  
ReinstateTask| 2|  Возврат задания на роль после взятия в работу.  
Signal| 3|  Обработка поступившего в процесс сигнала.  
InMemoryLaunching| 4|  Выполнение процесса в памяти.  
Resurrection| 5|  Возобновление сериализованного процесса.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
