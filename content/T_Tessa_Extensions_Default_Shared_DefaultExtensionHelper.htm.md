# DefaultExtensionHelper - класс
Общие вспомогательные методы для расширений типового решения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared](N_Tessa_Extensions_Default_Shared.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class DefaultExtensionHelper
VB __Копировать
     Public NotInheritable Class DefaultExtensionHelper
C++ __Копировать
     public ref class DefaultExtensionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type DefaultExtensionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultExtensionHelper
##  __Методы
[GetDocTypeInfoAsync](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_GetDocTypeInfoAsync.htm)|
Возвращает информацию по типу карточки и типу документа (если он присутствует)
для карточки с заданными идентификатором. Возвращает результат выполнения
запроса. Поскольку запрос расширяемый, то даже при успешном запросе (т.е. при
отсутствии расширений) возвращаемые out-параметры могут быть равны null.
Возвращает cardTypeID \- идентификатор типа карточки, полученный по
идентификатору карточки cardID, или null, если карточка с таким
идентификатором не существует
Возвращает docTypeID \- идентификатор типа документа, полученный по
идентификатору карточки cardID, или null, если либо карточка с таким
идентификатором не существует, либо тип карточки не добавлен в типовое
решение, либо тип карточки не поддерживает типы документов.
Возвращает docTypeTitle \- отображаемое название типа документа, полученное по
идентификатору карточки cardID, или null, если либо карточка с таким
идентификатором не существует, либо тип карточки не добавлен в типовое
решение, либо тип карточки не поддерживает типы документов  
---|---  
[GetKrDocStateCardID](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_GetKrDocStateCardID.htm)|
Возвращает уникальный идентификатор виртуальной карточки состояния документа.  
[MoveFilesToAsync](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_MoveFilesToAsync.htm)|
Переносит все файлы или заданный файл fileID для карточки cardID на
местоположение контента файлов sourceType. Перенос файла включает перенос всех
его версий. Если версия уже располагалась в заданном местоположении, то
действий не производится. Метод корректно выполняется только в том случае,
если пользователь является администратором. Возвращает результат выполнения
метода, в котором, как правило, содержатся ошибки в случае неудачного
выполнения. Возвращаемый объект никогда не равен null.  
[SetSourceID](M_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_SetSourceID.htm)|
Устанавливает местоположение контента файлов в запросе request.  
## __Поля
[CardTypeIDResponseKey](F_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_CardTypeIDResponseKey.htm)|  
---|---  
[DocTypeIDResponseKey](F_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_DocTypeIDResponseKey.htm)|  
[DocTypeTitleResponseKey](F_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_DocTypeTitleResponseKey.htm)|  
[SourceIDKey](F_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_SourceIDKey.htm)|
Константа для установки местоположения контента файлов в запросах
[CardRequest](T_Tessa_Cards_CardRequest.htm).  
[StateIDKey](F_Tessa_Extensions_Default_Shared_DefaultExtensionHelper_StateIDKey.htm)|
Ключ, по которому в Info карточки или запроса передаётся идентификатор
состояния для виртуальной карточки состояния документа.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared - пространство
имён](N_Tessa_Extensions_Default_Shared.htm)
