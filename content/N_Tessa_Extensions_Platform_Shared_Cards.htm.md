# Tessa.Extensions.Platform.Shared.Cards - пространство имён
Общие зависимости и константы платформы, связанные с платформенными
карточками.
##  __Классы
[BusinessProcessTemplateExtendedRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_BusinessProcessTemplateExtendedRepairExtension.htm)|
Обратная совместимость с версией системы, которая при экспорте карточки
записывала расширенный тип карточки.  
---|---  
[BusinessProcessTemplateRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_BusinessProcessTemplateRepairExtension.htm)|
Обратная совместимость с версией системы, которая при экспорте карточки
записывала BSON.  
[CardDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Cards_CardDigestRequestExtension.htm)|
Получаем Digest по строке формата
[DigestFormat](P_Tessa_Cards_CardType_DigestFormat.htm), если она задана и
Digest ещё не был вычислен другими расширениями.  
[ClientAndConsoleRegistrator](T_Tessa_Extensions_Platform_Shared_Cards_ClientAndConsoleRegistrator.htm)|  
[ClientMetadataRegistrator](T_Tessa_Extensions_Platform_Shared_Cards_ClientMetadataRegistrator.htm)|  
[ConditionTypesMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_ConditionTypesMetadataExtension.htm)|
Выполняет инициализацию метаданных для типов условий.  
[DecompressCardGetExtension](T_Tessa_Extensions_Platform_Shared_Cards_DecompressCardGetExtension.htm)|
Выполняет декомпрессию карточки после успешного запроса на её получение.  
[DecompressCardGetFileVersionsExtension](T_Tessa_Extensions_Platform_Shared_Cards_DecompressCardGetFileVersionsExtension.htm)|
Выполняет декомпрессию списка версий файлов после успешного запроса на её
получение.  
[ErrorRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_ErrorRepairExtension.htm)|
Расширение
[ErrorGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ErrorGetExtension.htm)
при экспорте заменит сериализованный в typed json запрос Request на её
структуру в JSON. Это расширение обратно сериализует запрос Request в typed
json.  
[ExtendTasksStoreExtension](T_Tessa_Extensions_Platform_Shared_Cards_ExtendTasksStoreExtension.htm)|
Выполняет расширения по завершению заданий.  
[FileExtensionHelper](T_Tessa_Extensions_Platform_Shared_Cards_FileExtensionHelper.htm)|  
[FileSignaturesMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_FileSignaturesMetadataExtension.htm)|
Добавляет секцию с подписями для всех типов файлов, у которых отсутствует флаг
[NoSigning](T_Tessa_Cards_CardTypeFlags.htm).  
[FileTemplateHelper](T_Tessa_Extensions_Platform_Shared_Cards_FileTemplateHelper.htm)|  
[InvalidateSingletonDeleteExtension](T_Tessa_Extensions_Platform_Shared_Cards_InvalidateSingletonDeleteExtension.htm)|
После успешного удаления синглтона кэш карточек сбрасывается для этого
синглтона.  
[InvalidateSingletonStoreExtension](T_Tessa_Extensions_Platform_Shared_Cards_InvalidateSingletonStoreExtension.htm)|
После успешного сохранения синглтона кэш карточек сбрасывается для этого
синглтона.  
[JsonRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_JsonRepairExtension.htm)|  
[NoServerInGetDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Cards_NoServerInGetDigestRequestExtension.htm)|
Запрещает обращение к серверу при запросе
[GetDigest](F_Tessa_Cards_CardRequestTypes_GetDigest.htm) на клиенте.  
[PersonalizationUserSettingsMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_PersonalizationUserSettingsMetadataExtension.htm)|
Расширение, добавляющее на вкладку "Персонализация" в карточку "Сотрудник" и в
диалог "Мои настройки"  
[RepairRegistrator](T_Tessa_Extensions_Platform_Shared_Cards_RepairRegistrator.htm)|  
[SingletonDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Cards_SingletonDigestRequestExtension.htm)|  
[TemplateRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_TemplateRepairExtension.htm)|
Обратная совместимость с версией системы, которая при экспорте карточки
записывала BSON.  
[UserNotificationSettingsMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_UserNotificationSettingsMetadataExtension.htm)|  
[UserSettingsMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_UserSettingsMetadataExtension.htm)|  
[ValidateCardStoreExtension](T_Tessa_Extensions_Platform_Shared_Cards_ValidateCardStoreExtension.htm)|  
## __Перечисления
[FileTemplateType](T_Tessa_Extensions_Platform_Shared_Cards_FileTemplateType.htm)|  
---|---
