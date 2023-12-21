# KrTileHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Tiles](N_Tessa_Extensions_Default_Client_Tiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrTileHelper
VB __Копировать
     Public NotInheritable Class KrTileHelper
C++ __Копировать
     public ref class KrTileHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrTileHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrTileHelper
##  __Методы
[GetUnavailableTypesAsync](M_Tessa_Extensions_Default_Client_Tiles_KrTileHelper_GetUnavailableTypesAsync.htm)|
Возвращает список недоступных идентификаторов для создания эффективных (типы
карточек, не использующие типы документов и типы документов) типов.  
---|---  
[OpenMarkedCardAsync](M_Tessa_Extensions_Default_Client_Tiles_KrTileHelper_OpenMarkedCardAsync.htm)|
Ставит в Info карточки отметку, по которой сработает соответствующее
расширение, и открывает карточку. Перед вызовом открытия карточки можно
использовать диалог для подтверждения/отмены действия и опционального вызова
предварительного сохранения карточки.  
[SetUnavailableTypes](M_Tessa_Extensions_Default_Client_Tiles_KrTileHelper_SetUnavailableTypes.htm)|
Устанавливает кэш недоступных идентификаторов, который может быть получен
вызовом [GetUnavailableTypesAsync(ICardRepository, IKrTypesCache,
CancellationToken)](M_Tessa_Extensions_Default_Client_Tiles_KrTileHelper_GetUnavailableTypesAsync.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Tiles - пространство
имён](N_Tessa_Extensions_Default_Client_Tiles.htm)
