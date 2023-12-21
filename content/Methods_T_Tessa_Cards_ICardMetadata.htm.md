# ICardMetadata - методы
##  __Методы
[GetCardTypesAsync](M_Tessa_Cards_ICardMetadata_GetCardTypesAsync.htm)|
Возвращает список типов карточек карточек.  
---|---  
[GetDamagedCardTypeIDListAsync](M_Tessa_Cards_ICardMetadata_GetDamagedCardTypeIDListAsync.htm)|
Возвращает список идентификаторов повреждённых типов карточек. Собственно типы
карточек можно получить посредством сервиса типов карточек.  
[GetEnumerationsAsync](M_Tessa_Cards_ICardMetadata_GetEnumerationsAsync.htm)|
Возвращает список перечислений.  
[GetGlobalReferencesAsync](M_Tessa_Cards_ICardMetadata_GetGlobalReferencesAsync.htm)|
Возвращает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl]), совместно использующиеся в типах карточек.  
[GetMetadataForTypeAsync](M_Tessa_Cards_ICardMetadata_GetMetadataForTypeAsync.htm)|
Возвращает выборку из метаинформации, которая относится только к заданному
типу карточек. В возвращённую выборку не передаются перечисления.  
[GetSectionsAsync](M_Tessa_Cards_ICardMetadata_GetSectionsAsync.htm)|
Возвращает метаинформацию по секциям карточек.  
[GetValidationResultAsync](M_Tessa_Cards_ICardMetadata_GetValidationResultAsync.htm)|
Возвращает результат валидации при построении метаинформации.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SetCardTypesAsync](M_Tessa_Cards_ICardMetadata_SetCardTypesAsync.htm)|
Устанавливает список типов карточек.  
[SetDamagedCardTypeIDListAsync](M_Tessa_Cards_ICardMetadata_SetDamagedCardTypeIDListAsync.htm)|
Устанавливает список идентификаторов повреждённых типов карточек. Собственно
типы карточек можно получить посредством сервиса типов карточек.  
[SetEnumerationsAsync](M_Tessa_Cards_ICardMetadata_SetEnumerationsAsync.htm)|
Устанавливает список перечислений.  
[SetGlobalReferencesAsync](M_Tessa_Cards_ICardMetadata_SetGlobalReferencesAsync.htm)|
Устанавливает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl], [CardTypeValidator], [CardTypeExtension]), совместно
использующиеся в типах карточек.  
[SetSectionsAsync](M_Tessa_Cards_ICardMetadata_SetSectionsAsync.htm)|
Метаинформация по секциям карточек.  
[SetValidationResultAsync](M_Tessa_Cards_ICardMetadata_SetValidationResultAsync.htm)|
Устанавливает результат валидации при построении метаинформации.  
##  __Методы расширения
[GetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
---|---  
[GetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
##  __См. также
#### Ссылки
[ICardMetadata - ](T_Tessa_Cards_ICardMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
