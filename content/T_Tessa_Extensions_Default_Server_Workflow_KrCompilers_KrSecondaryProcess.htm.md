# KrSecondaryProcess - класс
Базовый абстрактный класс, предоставляющий основную информацию о вторичном
процессе.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrSecondaryProcess : IKrSecondaryProcess, 
    	IExecutionSources
VB __Копировать
     Public MustInherit Class KrSecondaryProcess
    	Implements IKrSecondaryProcess, IExecutionSources
C++ __Копировать
     public ref class KrSecondaryProcess abstract : IKrSecondaryProcess, 
    	IExecutionSources
F# __Копировать
     [<AbstractClassAttribute>]
    type KrSecondaryProcess = 
        class
            interface IKrSecondaryProcess
            interface IExecutionSources
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrSecondaryProcess
Derived
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.KrAction](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrAction.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.KrProcessButton](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrProcessButton.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.KrPureProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrPureProcess.htm)
Implements
    [IExecutionSources](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IExecutionSources.htm), [IKrSecondaryProcess](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrSecondaryProcess.htm)
##  __Конструкторы
[KrSecondaryProcess](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess__ctor.htm)|
Инициализирует новый экземпляр класса KrSecondaryProcess.  
---|---  
## __Свойства
[Async](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_Async.htm)|
Возвращает значение, показывающе, что процесс допускает асинхронное
выполнение.  
---|---  
[ContextRolesIDs](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ContextRolesIDs.htm)|
Возвращает cписок контекстных ролей, проверяемых перед выполнением процесса.  
[ExecutionAccessDeniedMessage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ExecutionAccessDeniedMessage.htm)|
Возвращает сообщение о недоступности процесса для выполнения.  
[ExecutionSourceCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ExecutionSourceCondition.htm)|
Возвращает C# код, определяющий доступность выполнения.  
[ExecutionSqlCondition](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ExecutionSqlCondition.htm)|
Возвращает текст SQL запроса с условием пределяющий доступность выполнения.  
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_ID.htm)|
Возвращает идентификатор вторичного процесса.  
[IsGlobal](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_IsGlobal.htm)|
Возвращает значение, показывающее, что процесс является глобальным.  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_Name.htm)|
Возвращает название вторичного процесса.  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
[RunOnce](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrSecondaryProcess_RunOnce.htm)|
Возвращает значение, показывающее, что процесс может быть запущен только один
раз в пределах одной и той же области выполнения процесса
([KrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope.htm)).  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
