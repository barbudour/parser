# CardExtensionHelper - методы
##  __Методы
[FixUniqueIdentifiersAsync](M_Tessa_Cards_Extensions_CardExtensionHelper_FixUniqueIdentifiersAsync.htm)|
Исправляет список уникальных ссылок, задаваемых идентификаторами любого типа в
полях из списка identifierFieldNames в списке полей rows. Под уникальностью
ссылки подразумевается, что в одну и ту же карточку не может быть добавлено
более одной ссылки с одним и тем же идентификатором. Возвращает признак того,
что была найдена хотя бы одна строка-дубликат. Если задано removeDuplicates
как false, то дубликаты не удаляются.  
---|---  
[FixUniqueIdentifiersOnClientAsync](M_Tessa_Cards_Extensions_CardExtensionHelper_FixUniqueIdentifiersOnClientAsync.htm)|
Исправляет список уникальных ссылок, задаваемых идентификаторами любого типа в
полях identifierFieldName в коллекционной секции с именем sectionName. Под
уникальностью ссылки подразумевается, что в одну и ту же карточку не может
быть добавлено более одной ссылки с одним и тем же идентификатором. Метод
следует вызывать в расширении на сохранение карточки, файла или задания,
передаваемого в поле card.  
[FixUniqueIdentifiersOnClientStoreBeforeRequestAsync](M_Tessa_Cards_Extensions_CardExtensionHelper_FixUniqueIdentifiersOnClientStoreBeforeRequestAsync.htm)|
Исправляет список уникальных ссылок, задаваемых идентификаторами любого типа в
полях identifierFieldName в коллекционной секции с именем sectionName. Под
уникальностью ссылки подразумевается, что в одну и ту же карточку не может
быть добавлено более одной ссылки с одним и тем же идентификатором. Метод
следует вызывать в расширении на сохранение карточки в методе
[BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeRequest.htm)
на клиенте.  
[FixUniqueIdentifiersOnClientStoreTaskBeforeRequestAsync](M_Tessa_Cards_Extensions_CardExtensionHelper_FixUniqueIdentifiersOnClientStoreTaskBeforeRequestAsync.htm)|
Исправляет список уникальных ссылок, задаваемых идентификаторами любого типа в
полях identifierFieldName в коллекционной секции с именем sectionName. Под
уникальностью ссылки подразумевается, что в одну и ту же карточку не может
быть добавлено более одной ссылки с одним и тем же идентификатором. Метод
следует вызывать в расширении на сохранение задания в методе
[StoreTaskBeforeRequest(ICardStoreTaskExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreTaskExtension_StoreTaskBeforeRequest.htm)
на клиенте.  
## __См. также
#### Ссылки
[CardExtensionHelper - ](T_Tessa_Cards_Extensions_CardExtensionHelper.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
