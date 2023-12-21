# CardTypeMetadataExtension - класс
Базовый класс для расширений на метаинформацию, который содержит
вспомогательные свойства и методы для получения метаинформации по типам
карточек. В классе-наследнике рекомендуется использовать оба конструктора для
разных регистраций: на клиенте (для предпросмотра карточек) и на сервере. Если
такие средства не требуются и вы хотите полностью управлять конструкторами
расширения, то используйте базовый класс
[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardTypeMetadataExtension : CardMetadataExtension
VB __Копировать
     Public MustInherit Class CardTypeMetadataExtension
    	Inherits CardMetadataExtension
C++ __Копировать
     public ref class CardTypeMetadataExtension abstract : public CardMetadataExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardTypeMetadataExtension = 
        class
            inherit CardMetadataExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm) __ CardTypeMetadataExtension
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrSecondaryProcessMetadataExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSecondaryProcessMetadataExtension.htm)
[Tessa.Extensions.Default.Shared.Settings.InjectForumCardMetadataExtension](T_Tessa_Extensions_Default_Shared_Settings_InjectForumCardMetadataExtension.htm)
[Tessa.Extensions.Default.Shared.Settings.PartnersCardMetadataExtension](T_Tessa_Extensions_Default_Shared_Settings_PartnersCardMetadataExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions.KrPermissionsExtensionMetadataExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsExtensionMetadataExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrCardMetadataExtensionBase](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf.WfCardMetadataExtension](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfCardMetadataExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine.KrUpdateDialogTypeMetadataExtension](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_KrUpdateDialogTypeMetadataExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.ConditionTypesMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_ConditionTypesMetadataExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.PersonalizationUserSettingsMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_PersonalizationUserSettingsMetadataExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.UserNotificationSettingsMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_UserNotificationSettingsMetadataExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.UserSettingsMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_UserSettingsMetadataExtension.htm)
[Tessa.Extensions.Platform.Shared.Roles.RoleTypesMetadataExtension](T_Tessa_Extensions_Platform_Shared_Roles_RoleTypesMetadataExtension.htm)
Подробнее __Less __
##  __Конструкторы
[CardTypeMetadataExtension()](M_Tessa_Cards_Extensions_CardTypeMetadataExtension__ctor.htm)|
Создаёт экземпляр класса на сервере с параметрами по умолчанию.  
---|---  
[CardTypeMetadataExtension(ICardMetadata)](M_Tessa_Cards_Extensions_CardTypeMetadataExtension__ctor_1.htm)|
Создаёт экземпляр класса на клиенте с указанием его зависимостей.  
## __Свойства
[ClientCardMetadata](P_Tessa_Cards_Extensions_CardTypeMetadataExtension_ClientCardMetadata.htm)|
Серверная метаинформация по всем типам карточек, доступная на клиенте, или
null, если выполняется построение метаинформации на сервере.  
---|---  
[ClientMode](P_Tessa_Cards_Extensions_CardTypeMetadataExtension_ClientMode.htm)|
Признак того, что расширение выполняется на клиенте. Обычно это происходит при
предпросмотре типа карточки с расширениями.  
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
[GetCardTypesOnServerAsync](M_Tessa_Cards_Extensions_CardTypeMetadataExtension_GetCardTypesOnServerAsync.htm)|
Возвращает список всех типов карточек, доступных на сервере в настоящий
момент. При вызове на сервере получает информацию из контекста context, а при
вызове на клиенте - из серверной метаинформации
[ClientCardMetadata](P_Tessa_Cards_Extensions_CardTypeMetadataExtension_ClientCardMetadata.htm).  
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
[ModifyMetadata](M_Tessa_Cards_Extensions_CardMetadataExtension_ModifyMetadata.htm)|
Изменяет метаинформацию по типам карточек после её построения.  
(Унаследован от
[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm))  
[ModifyTypes](M_Tessa_Cards_Extensions_CardMetadataExtension_ModifyTypes.htm)|
Изменяет типы карточек, по которым затем будет строиться метаинформация.  
(Унаследован от
[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetCardTypeAsync](M_Tessa_Cards_Extensions_CardTypeMetadataExtension_TryGetCardTypeAsync.htm)|
Возвращает метаинформацию по заданному типу карточки или null, если тип
карточки не найден.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
