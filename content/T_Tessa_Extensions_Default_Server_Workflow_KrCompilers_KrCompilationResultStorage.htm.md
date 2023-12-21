# KrCompilationResultStorage - класс
Объект, предоставляющий доступ к результатам компиляции подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrCompilationResultStorage : IKrCompilationResultStorage
VB __Копировать
     Public NotInheritable Class KrCompilationResultStorage
    	Implements IKrCompilationResultStorage
C++ __Копировать
     public ref class KrCompilationResultStorage sealed : IKrCompilationResultStorage
F# __Копировать
     [<SealedAttribute>]
    type KrCompilationResultStorage = 
        class
            interface IKrCompilationResultStorage
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrCompilationResultStorage
Implements
    [IKrCompilationResultStorage](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrCompilationResultStorage.htm)
##  __Конструкторы
[KrCompilationResultStorage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationResultStorage__ctor.htm)|
Инициализирует новый экземпляр класса KrCompilationResultStorage  
---|---  
##  __Методы
[DeleteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationResultStorage_DeleteAsync.htm)|
Удаляет информацию о компиляции сценариев карточки с указанным
идентификатором.  
---|---  
[DeleteCompilationResultAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationResultStorage_DeleteCompilationResultAsync.htm)|
Удаляет информацию о сборке и результатах валидации для карточки с указанным
идентификатором.  
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
[GetCompilationOutputAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationResultStorage_GetCompilationOutputAsync.htm)|
Возвращает информацию по компиляции для карточки с указанным идентификатором.  
[GetCompilationResultAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationResultStorage_GetCompilationResultAsync.htm)|
Возвращает результаты компиляции сценариев карточки с указанным
идентификатором.  
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
[UpsertAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilationResultStorage_UpsertAsync.htm)|
Сохраняет результаты компиляции сценариев карточки с указанным
идентификатором.  
## __Методы расширения
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
