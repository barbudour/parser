# IKrSqlExecutorContext - интерфейс
Контекст
[IKrSqlExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SqlProcessing](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrSqlExecutorContext : IExtensionContext
VB __Копировать
     Public Interface IKrSqlExecutorContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrSqlExecutorContext : IExtensionContext
F# __Копировать
     type IKrSqlExecutorContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_CardID.htm)|
Идентификатор карточки.  
[CardTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_CardTypeID.htm)|
Идентификатор типа карточки.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_DocTypeID.htm)|
Идентификатор типа документа.  
[GetErrorTextFunc](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_GetErrorTextFunc.htm)|
Функция, формирующая сообщение об ошибке.  
[GroupName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_GroupName.htm)|
Название группы этапов.  
[Query](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_Query.htm)|
Выполняемый запрос.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_SecondaryProcess.htm)|
Текущий вторичный процесс кнопки.  
[StageGroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_StageGroupID.htm)|
Идентификатор группы этапов.  
[StageName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_StageName.htm)|
Название этапа.  
[StageRowID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_StageRowID.htm)|
Идентификатор строки этапа.  
[StageTemplateID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_StageTemplateID.htm)|
Идентификатор шаблона этапов.  
[StageTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_StageTypeID.htm)|
Идентификатор типа этапа.  
[State](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_State.htm)|
Состояние карточки.  
[TemplateName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_TemplateName.htm)|
Название шаблона этапов.  
[TypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_TypeID.htm)|
Эффективный идентификатор типа. Если тип использует типы документов, то это
тип документа. Иначе это тип карточки.  
[UserID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_UserID.htm)|
Идентификатор пользователя  
[UserName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_UserName.htm)|
Имя пользователя.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext_ValidationResult.htm)|  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SqlProcessing -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing.htm)
