# IKrSecondaryProcess - интерфейс
Объект, предоставляющий информацию о вторичном процессе.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrSecondaryProcess : IExecutionSources
VB __Копировать
     Public Interface IKrSecondaryProcess
    	Inherits IExecutionSources
C++ __Копировать
     public interface class IKrSecondaryProcess : IExecutionSources
F# __Копировать
     type IKrSecondaryProcess = 
        interface
            interface IExecutionSources
        end
Implements
    [IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm)
##  __Свойства
[Async](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_Async.htm)|
Возвращает значение, показывающе, что процесс допускает асинхронное
выполнение.  
---|---  
[ContextRolesIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_ContextRolesIDs.htm)|
Возвращает cписок контекстных ролей, проверяемых перед выполнением процесса.  
[ExecutionAccessDeniedMessage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_ExecutionAccessDeniedMessage.htm)|
Возвращает сообщение о недоступности процесса для выполнения.  
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
[IsGlobal](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_IsGlobal.htm)|
Возвращает значение, показывающее, что процесс является глобальным.  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_Name.htm)|
Возвращает название вторичного процесса.  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
[RunOnce](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_RunOnce.htm)|
Возвращает значение, показывающее, что процесс может быть запущен только один
раз в пределах одной и той же области выполнения процесса
([KrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope.htm)).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
