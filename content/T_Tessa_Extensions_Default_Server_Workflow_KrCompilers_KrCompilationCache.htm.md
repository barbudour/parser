# KrCompilationCache - класс
Кэш с результатами компиляции объектов подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrCompilationCache : IKrCompilationCache, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class KrCompilationCache
    	Implements IKrCompilationCache, IDisposable
C++ __Копировать
     public ref class KrCompilationCache sealed : IKrCompilationCache, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type KrCompilationCache = 
        class
            interface IKrCompilationCache
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrCompilationCache
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IKrCompilationCache](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationCache.htm)
##  __Конструкторы
[KrCompilationCache](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationCache__ctor.htm)|
Инициализирует новый экземпляр класса KrCompilationCache.  
---|---  
## __Методы
[BuildAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationCache_BuildAsync.htm)|
Выполняет сборку, если в кэше нет сборки или сборка invalidate. Если в кэше
есть актуальная сборка, возвращается null.  
---|---  
[Dispose](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationCache_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
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
[GetAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationCache_GetAsync.htm)|
Возвращает значения из кэша.  
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
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationCache_InvalidateAsync.htm)|
Сбрасывает значения кэша.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RebuildAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationCache_RebuildAsync.htm)|
Явно сбрасывает кэш сборки и выполняет пересборку. Кэш KrStageTenolateCache не
сбрасывается.  
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
