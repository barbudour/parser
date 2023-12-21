# KrCreateBasedOnHelper - поля
##  __Поля
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
[KrCreateBasedOnHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
