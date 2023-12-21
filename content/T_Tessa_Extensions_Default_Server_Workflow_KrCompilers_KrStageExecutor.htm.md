# KrStageExecutor - класс
Объект, выполняющий построение маршрута по шаблонам этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrStageExecutor : KrExecutorBase
VB __Копировать
     Public NotInheritable Class KrStageExecutor
    	Inherits KrExecutorBase
C++ __Копировать
     public ref class KrStageExecutor sealed : public KrExecutorBase
F# __Копировать
     [<SealedAttribute>]
    type KrStageExecutor = 
        class
            inherit KrExecutorBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm) __ KrStageExecutor
##  __Заметки
Единицами выполнения являются шаблоны этапов.
##  __Конструкторы
[KrStageExecutor](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageExecutor__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
## __Свойства
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_CardCache.htm)|  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
---|---  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_DbScope.htm)|  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
[KrSqlExecutor](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_KrSqlExecutor.htm)|  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
[KrStageSerializer](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_KrStageSerializer.htm)|  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
[KrTypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_KrTypesCache.htm)|  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[ExecuteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrStageExecutor_ExecuteAsync.htm)|
Выполняет построение маршрута для объектов, указанных в контексте.  
(Переопределяет
[KrExecutorBase.ExecuteAsync(IKrExecutionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_ExecuteAsync.htm))  
[ExecuteSQLConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_ExecuteSQLConditionAsync.htm)|
Выполняет SQL-условие времени построения маршрута для единицы выполнения.  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
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
[RunConditionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_RunConditionsAsync.htm)|
Выполняет условия времени построения маршрута для единицы выполнения.  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
[RunForAllAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase_RunForAllAsync.htm)|
Выполняет заданное действие для всех единиц выполнения.  
(Унаследован от
[KrExecutorBase](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutorBase.htm))  
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
