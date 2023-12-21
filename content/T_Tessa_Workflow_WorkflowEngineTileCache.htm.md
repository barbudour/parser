# WorkflowEngineTileCache - класс
Объект для получения и кеширования информации о тайлах бизнес-процессов.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowEngineTileCache : IWorkflowEngineTileCache, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class WorkflowEngineTileCache
    	Implements IWorkflowEngineTileCache, IDisposable
C++ __Копировать
     public ref class WorkflowEngineTileCache sealed : IWorkflowEngineTileCache, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type WorkflowEngineTileCache = 
        class
            interface IWorkflowEngineTileCache
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineTileCache
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IWorkflowEngineTileCache](T_Tessa_Workflow_IWorkflowEngineTileCache.htm)
##  __Конструкторы
[WorkflowEngineTileCache](M_Tessa_Workflow_WorkflowEngineTileCache__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineTileCache  
---|---  
##  __Методы
[Dispose](M_Tessa_Workflow_WorkflowEngineTileCache_Dispose.htm)| Performs
application-defined tasks associated with freeing, releasing, or resetting
unmanaged resources.  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetTilesAsync](M_Tessa_Workflow_WorkflowEngineTileCache_GetTilesAsync.htm)|
Метод для получения информации о тайлах шаблонов бизнес-процессов из кеша.
Производит расчёт кеша, если он ещё не был произведен.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync](M_Tessa_Workflow_WorkflowEngineTileCache_InvalidateAsync.htm)|
Метод для сброса данных из кеша.  
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
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
