# CardMetadataExtensionContext - свойства
##  __Свойства
[CancellationToken](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardMetadata](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_CardMetadata.htm)|
Построенная метаинформация по типам карточек, которую расширение может
изменять, или null, если расширение вызвано на этапе, на котором
метаинформация ещё не построена.  
[CardTypes](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_CardTypes.htm)|
Типы карточек, используемые для построения метаинформации.  
[DelayedSchemeCheckCardTypeIDSet](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_DelayedSchemeCheckCardTypeIDSet.htm)|
Идентификаторы типов карточек, проверка схемы для которых выполняется после
выполнения всех расширений на метаинформацию.
Рекомендуется добавить идентификатор типа карточки в методе расширения
[ModifyTypes(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyTypes.htm),
чтобы позже в методе расширения
[ModifyMetadata(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyMetadata.htm)
добавить секции и колонки, отсутствующие в схеме данных.
Если по завершении этого метода в типе карточки cardType.SchemeItems
присутствуют ссылки на секции или колонки, отсутствующие в секциях
cardMetadata.GetSectionsAsync(), то тип считается повреждённым, и добавляется
такое же сообщение об ошибке, как если бы проверка типа не была отложена.  
[EnableTracing](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
[GlobalReferences](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_GlobalReferences.htm)|
Словарь, содержащий глобальные объекты
([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm),
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm),
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm),
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm),
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)), совместно
использующиеся в типах карточек.  
[Info](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_Info.htm)|
Информация, используемая для передачи между расширениями в цепочке.  
[SchemeService](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_SchemeService.htm)|
Объект, обеспечивающий доступ к схеме данных.  
[ValidationResult](P_Tessa_Cards_Extensions_CardMetadataExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
## __См. также
#### Ссылки
[CardMetadataExtensionContext -
](T_Tessa_Cards_Extensions_CardMetadataExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
