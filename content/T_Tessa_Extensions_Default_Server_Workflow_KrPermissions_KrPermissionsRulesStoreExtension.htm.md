# KrPermissionsRulesStoreExtension - класс
При сохранении карточки "Правила доступа" прописывает флаг IsContext для всех
ролей, а также выполняет изменение строковых полей для представления во
вложенном сохранении.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrPermissionsRulesStoreExtension : CardStoreExtension
VB __Копировать
     Public NotInheritable Class KrPermissionsRulesStoreExtension
    	Inherits CardStoreExtension
C++ __Копировать
     public ref class KrPermissionsRulesStoreExtension sealed : public CardStoreExtension
F# __Копировать
     [<SealedAttribute>]
    type KrPermissionsRulesStoreExtension = 
        class
            inherit CardStoreExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm) __ KrPermissionsRulesStoreExtension
##  __Конструкторы
[KrPermissionsRulesStoreExtension](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRulesStoreExtension__ctor.htm)|
Инициализирует новый экземпляр класса KrPermissionsRulesStoreExtension  
---|---  
##  __Методы
[AfterBeginTransaction](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRulesStoreExtension_AfterBeginTransaction.htm)|  
(Переопределяет
[CardStoreExtension.AfterBeginTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[AfterRequestFinally](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRulesStoreExtension_AfterRequestFinally.htm)|  
(Переопределяет
[CardStoreExtension.AfterRequestFinally(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequestFinally.htm))  
[BeforeCommitTransaction](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRulesStoreExtension_BeforeCommitTransaction.htm)|  
(Переопределяет
[CardStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeCommitTransaction.htm))  
[BeforeRequest](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRulesStoreExtension_BeforeRequest.htm)|  
(Переопределяет
[CardStoreExtension.BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeRequest.htm))  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetIsContextForAllRoles](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRulesStoreExtension_SetIsContextForAllRoles.htm)|
Устанавливает признак контекстные ли роли на секцию из списка с определенным
названием  
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
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
