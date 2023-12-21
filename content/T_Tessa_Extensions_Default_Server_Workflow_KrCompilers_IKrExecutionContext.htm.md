# IKrExecutionContext - интерфейс
Контекст
[IKrExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrExecutionContext : IExtensionContext
VB __Копировать
     Public Interface IKrExecutionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrExecutionContext : IExtensionContext
F# __Копировать
     type IKrExecutionContext = 
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
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_CardContext.htm)|
Контекст расширения карточки, содержащейся в контексте выполнения.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_CardID.htm)|
Идентификатор текущей карточки или null, если она не задана.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_CardType.htm)|
Тип текущей карточки или null, если он не задан.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_DocTypeID.htm)|
Идентификатор типа документа текущей карточки или null, если тип или карточка
не заданы.  
[ExecutionUnitIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_ExecutionUnitIDs.htm)|
Список идентификаторов единиц выполнения, которые необходимо выполнить, или
null, если выполняются все единицы выполнения.  
[GroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_GroupID.htm)|
Идентификатор группы единиц выполнения
[ExecutionUnitIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_ExecutionUnitIDs.htm).  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_KrComponents.htm)|
Включённые компоненты типового решения для текущей карточки или null, если
карточка не задана.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_SecondaryProcess.htm)|
Информация о вторичном процессе, для которого выполняется пересчёт или null,
если выполняется пересчёт для основного процесса.  
[TypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_TypeID.htm)|
Идентификатор типа карточки или документа.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_ValidationResult.htm)|  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_WorkflowProcess.htm)|  
## __Методы
[Copy(ISet<Guid>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_Copy.htm)|
Создаёт новый контекст выполнения на основе существующего с учётом новых
единиц выполнения.  
---|---  
[Copy(Nullable<Guid>,
ISet<Guid>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_Copy_1.htm)|
Создаёт новый контекст выполнения на основе существующего с учетом новых
единиц выполнения и идентификатора группы.  
[GetCompilationResultAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_GetCompilationResultAsync.htm)|
Возвращает результат компиляции
[IKrCompilationResult](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationResult.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
