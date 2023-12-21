# WorkflowEngineProcessFlags - перечисление
Настройки обработки процесса в
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)
##  __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum WorkflowEngineProcessFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration WorkflowEngineProcessFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class WorkflowEngineProcessFlags
F# __Копировать
     [<FlagsAttribute>]
    type WorkflowEngineProcessFlags
##  __Члены
None| 0|  Флаги отсутствуют.  
---|---|---  
GenerateNextLinks| 1|  Флаг определяет, нужна ли генерация переходов на
следующий узел после обработки.  
LockProcess| 2|  Флаг определяет, нужна ли блокировка процесса при обработке.  
DefaultRuntime| 3|  Набор флагов для дефолтной обработки в рантайме.  
IsAsync| 4|  Флаг определяет, производится ли асинхронная обработка процесса.  
DefaultAsync| 5|  Набор флагов для асинхронной обработки по умолчанию.  
IsDebug| 8|  Флаг определяет, производится ли обработка процесса в режиме
отладки.  
DefaultDebug| 11|  Набор флагов для отладочной обработки по умолчанию.  
StartNew| 16|  Флаг определяет, запускается ли новый процесс.  
SendToSubscribers| 32|  Флаг определяет, нужно ли отправлять сигнал на
подписчиков на сигнал  
NotInDb| 64|  Флаг определяет, что экземпляр процесса еще не сохранён в базе
данных.  
DefaultNew| 83|  Набор флагов для дефолтной обработки запуска нового процесса.  
SendToTaskSubscribers| 128|  Флаг определяет, нужно ли отправлять сигнал на
подписки по заданиям.  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
