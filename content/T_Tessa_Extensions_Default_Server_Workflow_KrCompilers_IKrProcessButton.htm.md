# IKrProcessButton - интерфейс
Описывает объект предоставляющий информацию о вторичном процессе работающем в
режиме "Кнопка".
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessButton : IKrSecondaryProcess, 
    	IExecutionSources, IVisibilitySources
VB __Копировать
     Public Interface IKrProcessButton
    	Inherits IKrSecondaryProcess, IExecutionSources, IVisibilitySources
C++ __Копировать
     public interface class IKrProcessButton : IKrSecondaryProcess, 
    	IExecutionSources, IVisibilitySources
F# __Копировать
     type IKrProcessButton = 
        interface
            interface IKrSecondaryProcess
            interface IExecutionSources
            interface IVisibilitySources
        end
Implements
    [IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm), [IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm), [IVisibilitySources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IVisibilitySources.htm)
##  __Свойства
[ActionGrouping](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_ActionGrouping.htm)|
Значение, показывающее, необходимо ли группировать тайл в группу "Действия".  
---|---  
[AskConfirmation](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_AskConfirmation.htm)|
Спрашивать подтверждение перед выполнением.  
[Async](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_Async.htm)|
Возвращает значение, показывающе, что процесс допускает асинхронное
выполнение.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[ButtonHotkey](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_ButtonHotkey.htm)|
Сочетание клавиш.  
[Caption](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_Caption.htm)|
Отображаемое название кнопки.  
[Conditions](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_Conditions.htm)|
Возвращает перечисление параметров условий.  
[ConfirmationMessage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_ConfirmationMessage.htm)|
Текст подтверждения перед выполнением.  
[ContextRolesIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_ContextRolesIDs.htm)|
Возвращает cписок контекстных ролей, проверяемых перед выполнением процесса.  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
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
[Icon](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_Icon.htm)|
Значок.  
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
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_Order.htm)|
Порядок кнопки.  
[RefreshAndNotify](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_RefreshAndNotify.htm)|
Значение, показывающее, необходимо ли проверить наличие новых заданий после
выполнения.  
[RunOnce](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess_RunOnce.htm)|
Возвращает значение, показывающее, что процесс может быть запущен только один
раз в пределах одной и той же области выполнения процесса
([KrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope.htm)).  
(Унаследован от
[IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm))  
[TileGroup](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_TileGroup.htm)|
Группа кнопки.  
[TileSize](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_TileSize.htm)|
Размер кнопки.  
[Tooltip](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrProcessButton_Tooltip.htm)|
Подсказка.  
[VisibilitySourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IVisibilitySources_VisibilitySourceCondition.htm)|
Возвращает C# код, определяющий видимость.  
(Унаследован от
[IVisibilitySources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IVisibilitySources.htm))  
[VisibilitySqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IVisibilitySources_VisibilitySqlCondition.htm)|
Возвращает текст SQL запроса с условием определяющим видимость.  
(Унаследован от
[IVisibilitySources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IVisibilitySources.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
