# KrExecutionContext - класс
Контекст
[IKrExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrExecutionContext : IKrExecutionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class KrExecutionContext
    	Implements IKrExecutionContext, IExtensionContext
C++ __Копировать
     public ref class KrExecutionContext sealed : IKrExecutionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type KrExecutionContext = 
        class
            interface IKrExecutionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrExecutionContext
Implements
    [IKrExecutionContext](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrExecutionContext](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext__ctor.htm)|
Инициализирует новый экземпляр класса KrExecutionContext.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_CardContext.htm)|
Контекст расширения карточки, содержащейся в контексте выполнения.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_CardID.htm)|
Идентификатор текущей карточки или null, если она не задана.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_CardType.htm)|
Тип текущей карточки или null, если он не задан.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_DocTypeID.htm)|
Идентификатор типа документа текущей карточки или null, если тип или карточка
не заданы.  
[ExecutionUnitIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_ExecutionUnitIDs.htm)|
Список идентификаторов единиц выполнения, которые необходимо выполнить, или
null, если выполняются все единицы выполнения.  
[GroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_GroupID.htm)|
Идентификатор группы единиц выполнения
[ExecutionUnitIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionContext_ExecutionUnitIDs.htm).  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_KrComponents.htm)|
Включённые компоненты типового решения для текущей карточки или null, если
карточка не задана.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_SecondaryProcess.htm)|
Информация о вторичном процессе, для которого выполняется пересчёт или null,
если выполняется пересчёт для основного процесса.  
[TypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_TypeID.htm)|
Идентификатор типа карточки или документа.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_ValidationResult.htm)|  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_WorkflowProcess.htm)|  
## __Методы
[Copy(ISet<Guid>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_Copy.htm)|
Создаёт новый контекст выполнения на основе существующего с учётом новых
единиц выполнения.  
---|---  
[Copy(Nullable<Guid>,
ISet<Guid>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_Copy_1.htm)|
Создаёт новый контекст выполнения на основе существующего с учетом новых
единиц выполнения и идентификатора группы.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetCompilationResultAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionContext_GetCompilationResultAsync.htm)|
Возвращает результат компиляции
[IKrCompilationResult](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationResult.htm).  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
