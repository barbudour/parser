# InitializationExtensionHelper - класс
Вспомогательные поля и методы для выполнения инициализации приложения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Shared.Initialization](N_Tessa_Extensions_Platform_Shared_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class InitializationExtensionHelper
VB __Копировать
     Public NotInheritable Class InitializationExtensionHelper
C++ __Копировать
     public ref class InitializationExtensionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type InitializationExtensionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ InitializationExtensionHelper
##  __Методы
[ApplyWorkplacePolicyAsync(IList<IWorkplaceMetadata>,
IServerInitializationExtensionContext, IWorkplaceWalkerFactory,
WorkplaceMetadataSerializer,
CancellationToken)](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_ApplyWorkplacePolicyAsync.htm)|
Осуществляет фильтрацию рабочих мест в соответствии с политикой доступности.  
---|---  
[ApplyWorkplacePolicyAsync(IList<WorkplaceModel>,
IServerInitializationExtensionContext, IWorkplaceWalkerFactory,
IWorkplaceInterpreter, WorkplaceMetadataSerializer, IIndentationStrategy,
IConverter<IJsonWorkplaceMetadata, IWorkplaceMetadata>,
CancellationToken)](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_ApplyWorkplacePolicyAsync_1.htm)|
Осуществляет фильтрацию рабочих мест в соответствии с политикой доступности.  
[DeserializeSettingsToSectionsByTypeAsync(Guid, Dictionary<String, Object>,
Card, ICardMetadata, ICardRepairManager, Boolean, Boolean, Boolean,
CancellationToken)](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_DeserializeSettingsToSectionsByTypeAsync.htm)|
Десериализует настройки в секции карточки.  
[DeserializeSettingsToSectionsByTypeAsync(Guid, String, Card, ICardMetadata,
ICardRepairManager, Boolean, Boolean, Boolean, Boolean,
CancellationToken)](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_DeserializeSettingsToSectionsByTypeAsync_1.htm)|
Десериализует настройки в секции карточки.  
[DeserializeUserSettingsToSectionsAsync](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_DeserializeUserSettingsToSectionsAsync.htm)|
Десериализует настройки пользователя в секции карточки.  
[SerializeSettingsFromSectionsByTypeAsync](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_SerializeSettingsFromSectionsByTypeAsync.htm)|
Сериализует настройки указанного типа из карточки.  
[SerializeUserSettingsFromSectionsAsync](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_SerializeUserSettingsFromSectionsAsync.htm)|
Сериализует настройки пользователя из карточки сотрудника.  
[TryDeserializeUserSettings](M_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_TryDeserializeUserSettings.htm)|
Производит десериализацию настроек в формате JSON в объект с данными.
Возвращает null, если не удалось десериализовать настройки.  
## __Поля
[CardsKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_CardsKey.htm)|
Ключ метаинформации по типам карточек.  
---|---  
[ExistentSingletonsKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_ExistentSingletonsKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по существующим в
БД карточкам-синглтонам.  
[ExtensionsKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_ExtensionsKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по загруженным на
сервере сборкам с расширениями.  
[FileTemplatesKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_FileTemplatesKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по доступным
шаблонам файлов.  
[ForumsKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_ForumsKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по форумам и
обсуждениям.  
[LicenseKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_LicenseKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по лицензии.  
[LocalizationKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_LocalizationKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по строками
локализации.  
[PersonalRoleLanguageCaptionField](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_PersonalRoleLanguageCaptionField.htm)|
Поле в секции карточки-сателлита персональной роли, содержащее отображаемое
название языка.  
[PersonalRoleLanguageCodeField](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_PersonalRoleLanguageCodeField.htm)|
Поле в секции карточки-сателлита персональной роли, содержащее код языка.  
[PersonalRoleLanguageIDField](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_PersonalRoleLanguageIDField.htm)|
Поле в секции карточки-сателлита персональной роли, содержащее идентификатор
языка.  
[PersonalRoleNotificationSettingsField](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_PersonalRoleNotificationSettingsField.htm)|
Поле в секции карточки-сателлита персональной роли, содержащее настройки по
уведомлениям NotificationSettings.  
[PersonalRoleSettingsField](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_PersonalRoleSettingsField.htm)|
Поле в секции карточки-сателлита персональной роли, содержащее
пользовательские настройки Settings.  
[PersonalRoleVirtualSection](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_PersonalRoleVirtualSection.htm)|
Имя виртуальной секции в карточке персональной роли, которая используется для
хранения языка локализации и некоторых других настроек.  
[SearchQueriesKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_SearchQueriesKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по поисковым
запросам.  
[SingletonsKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_SingletonsKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по карточкам-
синглтонам.  
[ViewsKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_ViewsKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по
представлениям.  
[WebAppVersionKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_WebAppVersionKey.htm)|
Ключ, по которому в ответе на запрос по инициализации web-клиента
[WebClient](F_Tessa_Platform_Runtime_ApplicationIdentifiers_WebClient.htm) в
Response.Info передаётся строка с актуальной версией web-приложения для
текущего пользователя. Если версия, установленная у пользователя, отличается,
то пользователю будет предложено скачать обновление.  
[WorkplacesKey](F_Tessa_Extensions_Platform_Shared_Initialization_InitializationExtensionHelper_WorkplacesKey.htm)|
Поле в ответе на запрос response.Info, содержащее информацию по рабочим
местам.  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Shared.Initialization - пространство
имён](N_Tessa_Extensions_Platform_Shared_Initialization.htm)
