# IKrAction - интерфейс
Описывает объект предоставляющий информацию о вторичном процессе работающем в
режиме "Действие".
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrAction : IKrSecondaryProcess, 
    	IExecutionSources
VB __Копировать
     Public Interface IKrAction
    	Inherits IKrSecondaryProcess, IExecutionSources
C++ __Копировать
     public interface class IKrAction : IKrSecondaryProcess, 
    	IExecutionSources
F# __Копировать
     type IKrAction = 
        interface
            interface IKrSecondaryProcess
            interface IExecutionSources
        end
Implements
    [IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm), [IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm)
##  __Свойства
[Async](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_Async.htm)|
Возвращает значение, показывающе, что процесс допускает асинхронное
выполнение.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
---|---  
[ContextRolesIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_ContextRolesIDs.htm)|
Возвращает cписок контекстных ролей, проверяемых перед выполнением процесса.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[EventType](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrAction_EventType.htm)|
Возвращает тип события, по которому запускается действие. Может иметь значение
по умолчанию для типа.  
[ExecutionAccessDeniedMessage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_ExecutionAccessDeniedMessage.htm)|
Возвращает сообщение о недоступности процесса для выполнения.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[ExecutionSourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources_ExecutionSourceCondition.htm)|
Возвращает C# код, определяющий доступность выполнения.  
(Унаследован от
[IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm))  
[ExecutionSqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources_ExecutionSqlCondition.htm)|
Возвращает текст SQL запроса с условием пределяющий доступность выполнения.  
(Унаследован от
[IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm))  
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_ID.htm)|
Возвращает идентификатор вторичного процесса.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[IsGlobal](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_IsGlobal.htm)|
Возвращает значение, показывающее, что процесс является глобальным.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_Name.htm)|
Возвращает название вторичного процесса.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[RunOnce](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_RunOnce.htm)|
Возвращает значение, показывающее, что процесс может быть запущен только один
раз в пределах одной и той же области выполнения процесса
([KrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope.htm)).  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
