# KrExecutorBase - класс
Базовая абстрактная реализация
[IKrExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrExecutorBase : IKrExecutor
VB __Копировать
     Public MustInherit Class KrExecutorBase
    	Implements IKrExecutor
C++ __Копировать
     public ref class KrExecutorBase abstract : IKrExecutor
F# __Копировать
     [<AbstractClassAttribute>]
    type KrExecutorBase = 
        class
            interface IKrExecutor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrExecutorBase
Derived
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.KrGroupExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrGroupExecutor.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.KrStageExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageExecutor.htm)
Implements
    [IKrExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutor.htm)
##  __Конструкторы
[KrExecutorBase](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
## __Свойства
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_CardCache.htm)|  
---|---  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_DbScope.htm)|  
[KrSqlExecutor](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_KrSqlExecutor.htm)|  
[KrStageSerializer](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_KrStageSerializer.htm)|  
[KrTypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_KrTypesCache.htm)|  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExecuteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_ExecuteAsync.htm)|
Выполняет построение маршрута для объектов, указанных в контексте.  
[ExecuteScriptConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_ExecuteScriptConditionAsync.htm)|
Выполняет C#-условие времени построения маршрута для единицы выполнения.  
[ExecuteSQLConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_ExecuteSQLConditionAsync.htm)|
Выполняет SQL-условие времени построения маршрута для единицы выполнения.  
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
[RunAfterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_RunAfterAsync.htm)|
Выполняет сценарий постобработки для единицы выполнения.  
[RunBeforeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_RunBeforeAsync.htm)|
Выполняет сценарий инициализации для единицы выполнения.  
[RunConditionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_RunConditionsAsync.htm)|
Выполняет условия времени построения маршрута для единицы выполнения.  
[RunForAllAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_RunForAllAsync.htm)|
Выполняет заданное действие для всех единиц выполнения.  
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
