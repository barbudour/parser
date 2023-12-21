# CardValidationContext - свойства
##  __Свойства
[CancellationToken](P_Tessa_Cards_Validation_CardValidationContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardMetadata](P_Tessa_Cards_Validation_CardValidationContext_CardMetadata.htm)|
Метаинформация по типам карточек, используемая в процессе валидации.  
[ExternalContextInfo](P_Tessa_Cards_Validation_CardValidationContext_ExternalContextInfo.htm)|
Произвольно структурированная информация из внешнего контекста (например,
контекста сохранения карточки), которая может быть заполнена валидатором и
использована либо другими валидаторами, либо внешними расширениями. Когда
внешний контекст неизвестен, будет создан пустой объект, но при этом свойство
никогда не возвращает null.  
[ForceWarnings](P_Tessa_Cards_Validation_CardValidationContext_ForceWarnings.htm)|
Признак того, что валидаторы-предупреждения срабатывают даже в том случае,
если они не должны срабатывать, например, на клиенте. Это полезно, если
выполняется валидация на клиенте без валидации на сервере.  
[IsSealed](P_Tessa_Cards_Validation_CardValidationContext_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[Limitations](P_Tessa_Cards_Validation_CardValidationContext_Limitations.htm)|
Объект, ограничивающий доступность объектов для валидации.  
[MainCard](P_Tessa_Cards_Validation_CardValidationContext_MainCard.htm)|
Основная карточка, для которой выполняется валидация.  
[MainCardMetadataBinder](P_Tessa_Cards_Validation_CardValidationContext_MainCardMetadataBinder.htm)|
Объект, выполняющий действия с основной карточкой, для которой выполняется
валидация.  
[MainCardType](P_Tessa_Cards_Validation_CardValidationContext_MainCardType.htm)|
Тип основной карточки, для которой выполняется валидация.  
[Session](P_Tessa_Cards_Validation_CardValidationContext_Session.htm)| Сессия
пользователя, в процессе работы которого выполняется валидация.  
[StoreMode](P_Tessa_Cards_Validation_CardValidationContext_StoreMode.htm)|
Способ сохранения проверяемого объекта - карточки, файла или задания.  
[TaskCard](P_Tessa_Cards_Validation_CardValidationContext_TaskCard.htm)|
Карточка задания, валидация которой выполняется, или null, если задание
завершается без данных карточки или валидация задания не выполняется.  
[TaskCardMetadataBinder](P_Tessa_Cards_Validation_CardValidationContext_TaskCardMetadataBinder.htm)|
Объект, выполняющий действия с карточкой задания, для которой выполняется
валидация, или null, если задание завершается без данных карточки или
валидация задания не выполняется.  
[TaskCardType](P_Tessa_Cards_Validation_CardValidationContext_TaskCardType.htm)|
Тип карточки задания, для которой выполняется валидация, или null, если
валидация задания не выполняется.  
[ValidationMode](P_Tessa_Cards_Validation_CardValidationContext_ValidationMode.htm)|
Способ выполнения валидации.  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
