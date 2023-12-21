# KrScopeLevel - класс
Объект, предоставляющий методы для управления текущим контекстом
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrScopeLevel
VB __Копировать
     Public NotInheritable Class KrScopeLevel
C++ __Копировать
     public ref class KrScopeLevel sealed
F# __Копировать
     [<SealedAttribute>]
    type KrScopeLevel = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrScopeLevel
##  __Заметки
После завершения работы с объектом, для выполнения задач связанных с
освобождением ресурсов, вызовите метод
[ExitAsync(IValidationResultBuilder)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel_ExitAsync.htm).
##  __Конструкторы
[KrScopeLevel](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel__ctor.htm)|
Инициализирует новый экземпляр класса KrScopeLevel  
---|---  
##  __Свойства
[CardTransactionStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel_CardTransactionStrategy.htm)|  
---|---  
[Exited](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel_Exited.htm)|
Значение, показывающее, что для этого объекта были выполнены действия по
освобождению ресурсов.  
[LevelID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel_LevelID.htm)|
Идентификатор объекта.  
[WithReaderLocks](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel_WithReaderLocks.htm)|
При загрузке объекта карточки (для инкремента версии, если карточка не
загружена ранее) использовать блокировку на чтение.  
## __Методы
[ApplyChangesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel_ApplyChangesAsync.htm)|
Обрабатывает изменения в карточках управляемых
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExitAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScopeLevel_ExitAsync.htm)|
Выполняет задачи, связанные с высвобождением ресурсов этого объекта.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope.htm)
