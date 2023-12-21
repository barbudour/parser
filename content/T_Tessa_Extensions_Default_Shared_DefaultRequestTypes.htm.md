# DefaultRequestTypes - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class DefaultRequestTypes
VB __Копировать
     Public NotInheritable Class DefaultRequestTypes
C++ __Копировать
     public ref class DefaultRequestTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type DefaultRequestTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultRequestTypes
##  __Поля
[Acquaintance](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_Acquaintance.htm)|
Отправка информации для массового ознакомления  
---|---  
[CAdESSignature](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_CAdESSignature.htm)|
Расширение цифровой подписи  
[GetDefaultAcquaintanceRoles](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_GetDefaultAcquaintanceRoles.htm)|
Запрос пользователей для заполнения списка информируемых  
[GetDocTypeInfo](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_GetDocTypeInfo.htm)|
Получение информации по типу карточки и типу документа (если карточка имеет
тип документа) по заданному идентификатору карточки.  
[GetFake1C](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_GetFake1C.htm)|
Тестовый пример на получение данных от некоторого внешнего сервиса 1С.  
[GetResolutionVisualizationData](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_GetResolutionVisualizationData.htm)|
Запрос на загрузку информации для визуализации резолюций.  
[GetUnavailableTypes](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_GetUnavailableTypes.htm)|
Получение списка недоступных для текущего пользователя типов карточек и
документов, определённых в типовом решении.  
[KrGetDocTypes](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_KrGetDocTypes.htm)|
Получение списка доступных типов документов, определённых в типовом решении.  
[MoveFiles](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_MoveFiles.htm)|
Запрос на перенос контента файла на заданный источник
[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm). Рекомендуется
вызывать запрос методом [MoveFilesToAsync(CardFileSourceType, ICardRepository,
Guid, Nullable<Guid>,
CancellationToken)](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_MoveFilesToAsync.htm).
В запросе должен быть указан идентификатор карточки
[CardID](P_Tessa_Cards_CardRequest_CardID.htm) и источник
[SetSourceID(CardRequest,
CardFileSourceType)](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_SetSourceID.htm).
Если также указан идентификатор файла
[FileID](P_Tessa_Cards_CardRequest_FileID.htm), то переносятся только все
версии заданного файла, иначе - все версии всех файлов карточки.  
[TestData](F_Tessa_Extensions_Default_Shared_DefaultRequestTypes_TestData.htm)|
Создание тестовых данных из карточки настроек типового решения.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
