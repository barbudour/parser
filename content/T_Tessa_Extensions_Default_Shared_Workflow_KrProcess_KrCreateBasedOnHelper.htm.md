# KrCreateBasedOnHelper - класс
Константы и вспомогательные методы для создания карточек на основании других
карточек.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrCreateBasedOnHelper
VB __Копировать
     Public NotInheritable Class KrCreateBasedOnHelper
C++ __Копировать
     public ref class KrCreateBasedOnHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrCreateBasedOnHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrCreateBasedOnHelper
##  __Методы
[InitializeRequestInfo(Dictionary<String, Object>, Card,
Boolean)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_InitializeRequestInfo_1.htm)|
Инициализирует информацию по запросу на создание карточки
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info на основании заданной
карточки baseCard.  
---|---  
[InitializeRequestInfo(Dictionary<String, Object>, Guid, Boolean,
KrToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_InitializeRequestInfo.htm)|
Инициализирует информацию по запросу на создание карточки
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info на основании заданной
карточки с идентификатором baseCardID.  
[TryGetDocDescription](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_TryGetDocDescription.htm)|
Возвращает поле DocDescription для описания ссылки на документ, которая обычно
возвращается типовым представлением RefDocumentsLookup, или null, если в
заданной карточке отсутствуют соответствующие секции.  
## __Поля
[CardIDKey](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_CardIDKey.htm)|
Ключ, по которому в [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info
содержится идентификатор карточки, для которой выполняется создание на
основании вместо обычного создания. Если не указан этот ключ и
[CardKey](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_CardKey.htm),
то не выполняется создание на основании.  
---|---  
[CardInfoKey](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_CardInfoKey.htm)|
Ключ, по которому в расширениях на создание карточки в context.Info доступен
объект базовой карточки. В такой карточке загружено всё, кроме истории заданий
и указаний по просрочке загруженных заданий по бизнес-календарю.  
[CardKey](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_CardKey.htm)|
Ключ, по которому в [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info
содержится объект загруженной карточки [Card](T_Tessa_Cards_Card.htm), для
которой выполняется создание на основании вместо обычного создания. Если не
указан этот ключ и
[CardIDKey](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_CardIDKey.htm),
то не выполняется создание на основании.  
[CopyFilesKey](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_CopyFilesKey.htm)|
Ключ, по которому в [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info
содержится признак того, что в создаваемой карточке должны быть скопированы
файлы из базовой карточки.  
[TokenKey](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_TokenKey.htm)|
Ключ, по которому в [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info
доступен токен безопасности
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
для карточки, на основании которой создаётся другая карточка, или null, если
токен отсутствует и права на чтение будут вычислены в процессе создания.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
