# KrScopeContext - класс
Контекст Kr расширений на сохранение.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrScopeContext : IDisposable
VB __Копировать
     Public NotInheritable Class KrScopeContext
    	Implements IDisposable
C++ __Копировать
     public ref class KrScopeContext sealed : IDisposable
F# __Копировать
     [<SealedAttribute>]
    type KrScopeContext = 
        class
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrScopeContext
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Свойства
[Cards](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Cards.htm)|
Словарь карточек, расположенных в контексте. Доступ осуществляется по их
идентификатору.  
---|---  
[CardsWithTaskHistory](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_CardsWithTaskHistory.htm)|
Набор идентификаторов карточек, для которых была загружена история заданий.
Объекты карточек содержатся в
[Cards](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Cards.htm).  
[Current](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Current.htm)|
Текущий контекст KrScopeContext или значение null, если он недоступен.  
[ForceIncrementCardVersion](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_ForceIncrementCardVersion.htm)|
Набор идентификаторов карточек, для которых должен быть принудительно увеличен
номер версии при сохранении. Объекты карточек могут не содержатся в
[Cards](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Cards.htm).  
[HasCurrent](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_HasCurrent.htm)|
Признак того, что текущий код выполняется внутри операции с контекстом
KrScopeContext, а свойство
[Current](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Current.htm)
ссылается на действительный контекст.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Info.htm)|
Словарь с дополнительной информацией, сохранённой в контексте.  
[IsUsed](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_IsUsed.htm)|
Значение, показывающее, что текущий объект может быть доступен через свойство
[Current](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Current.htm)
в соответствующем потоке.  
[ProcessHolders](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_ProcessHolders.htm)|
Набор объектов
[ProcessHolder](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder.htm),
доступ к которым осуществляется по
[ProcessHolderID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder_ProcessHolderID.htm).  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации.  
## __Методы
[AddAsyncDisposableObject](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_AddAsyncDisposableObject.htm)|
Добавляет объект, для которого нужно вызвать метод
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) при выполнении метода
[InvalidateAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_InvalidateAsync.htm).  
---|---  
[AddCardFileContainer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_AddCardFileContainer.htm)|
Добавляет [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm) в
контекст.  
[AddDisposableObject](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_AddDisposableObject.htm)|
Добавляет объект, для которого нужно вызвать метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) при выполнении метода
[InvalidateAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_InvalidateAsync.htm).  
[AddSatellite](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_AddSatellite.htm)|
Добавляет карточку сателлита в контекст.  
[AddSecondaryKrSatellite](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_AddSecondaryKrSatellite.htm)|
Добавляет карточку сателлита вторичного процесса в контекст.  
[Create](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Create.htm)|
Создаёт область видимости для значения в текущем потоке.  
[Dispose](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Dispose.htm)|
Уведомляет о том, что объект больше не доступен по свойству
[Current](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_Current.htm).  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_InvalidateAsync.htm)|
Выполняет действия по освобождению ресурсов, занимаемых этим объектом.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetCardFileContainer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_TryGetCardFileContainer.htm)|
Возвращает [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm),
содержащийся в контексте.  
[TryGetSatellite](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_TryGetSatellite.htm)|
Возвращает карточку сателлита, содержащуюся в контексте.  
[TryGetSecondaryKrSatellite](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeContext_TryGetSecondaryKrSatellite.htm)|
Возвращает карточку сателлита вторичного процесса, содержащуюся в контексте.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope.htm)
