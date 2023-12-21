# KrScopeMainCardAccessStrategy - класс
Представляет стратегию доступа к карточке. Является обёрткой над
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrScopeMainCardAccessStrategy : IMainCardAccessStrategy, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class KrScopeMainCardAccessStrategy
    	Implements IMainCardAccessStrategy, IAsyncDisposable
C++ __Копировать
     public ref class KrScopeMainCardAccessStrategy sealed : IMainCardAccessStrategy, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type KrScopeMainCardAccessStrategy = 
        class
            interface IMainCardAccessStrategy
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrScopeMainCardAccessStrategy
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IMainCardAccessStrategy](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IMainCardAccessStrategy.htm)
##  __Конструкторы
[KrScopeMainCardAccessStrategy](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy__ctor.htm)|
Инициализирует новый экземпляр класса KrScopeMainCardAccessStrategy.  
---|---  
## __Свойства
[WasFileContainerUsed](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy_WasFileContainerUsed.htm)|
Возвращает признак использования файлового контейнера.  
---|---  
[WasUsed](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy_WasUsed.htm)|
Признак того, что стратегия использовалась, т.е. вызывались методы доступа к
карточке.  
## __Методы
[DisposeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy_DisposeAsync.htm)|  
---|---  
[EnsureTaskHistoryLoadedAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy_EnsureTaskHistoryLoadedAsync.htm)|
Загрузка (при необходимости) истории заданий в карточку в соответствии с
правилами стратегии.  
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
[GetCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy_GetCardAsync.htm)|
Получение объекта карточки в соответствии с правилами стратегии.  
[GetFileContainerAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy_GetFileContainerAsync.htm)|
Возвращает файловый контейнер карточки полученный в соответствии с правилами
стратегии.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
