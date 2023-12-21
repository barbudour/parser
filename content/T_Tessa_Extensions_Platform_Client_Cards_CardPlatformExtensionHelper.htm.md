# CardPlatformExtensionHelper - класс
Вспомогательный класс для платформенных расширений карточек.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardPlatformExtensionHelper
VB __Копировать
     Public NotInheritable Class CardPlatformExtensionHelper
C++ __Копировать
     public ref class CardPlatformExtensionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardPlatformExtensionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardPlatformExtensionHelper
##  __Методы
[SetDigestFromNewTemplatedCard](M_Tessa_Extensions_Platform_Client_Cards_CardPlatformExtensionHelper_SetDigestFromNewTemplatedCard.htm)|
Устанавливает Digest для ещё не сохранённой карточки шаблона, для которой
файлы загружаются через
[ExternalSource](P_Tessa_Cards_CardFile_ExternalSource.htm).  
---|---  
[SetDigestInContextAsync](M_Tessa_Extensions_Platform_Client_Cards_CardPlatformExtensionHelper_SetDigestInContextAsync.htm)|
Устанавливает Digest для запроса к сервису карточек из текущего контекста
[Current](P_Tessa_UI_UIContext_Current.htm) и возвращает признак того, что
Digest был установлен (хотя бы равным null).  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
