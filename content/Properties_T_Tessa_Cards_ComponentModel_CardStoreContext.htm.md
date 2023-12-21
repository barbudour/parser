# CardStoreContext - свойства
##  __Свойства
[AffectModified](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectModified.htm)|
Признак того, что изменения влияют на изменение информации по тому, когда
произошло изменение карточки и какой пользователь его выполнил. Это поле
эффективно только в случае, если значение свойства
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm)
равно false.  
---|---  
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm)|
Признак того, что изменения влияют на проверку и инкремент версии карточки.
При инкременте версии также изменяется информация по тому, когда произошло
изменение карточки и какой пользователь его выполнил. Этот флаг менее
приоритетный, чем
[DoesNotAffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_DoesNotAffectVersion.htm).  
[BuilderFactory](P_Tessa_Cards_ComponentModel_CardStoreContext_BuilderFactory.htm)|
Объект, помогающий создавать SQL-команды для сохранению карточки.  
[CancellationToken](P_Tessa_Cards_ComponentModel_CardStoreContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[CardID](P_Tessa_Cards_ComponentModel_CardStoreContext_CardID.htm)|
Идентификатор сохраняемой карточки.  
[CardMetadata](P_Tessa_Cards_ComponentModel_CardStoreContext_CardMetadata.htm)|
Метаинформация по типу сохраняемой карточки.  
[CardTypeCaption](P_Tessa_Cards_ComponentModel_CardStoreContext_CardTypeCaption.htm)|
Отображаемое имя типа сохраняемой карточки.  
[CardTypeID](P_Tessa_Cards_ComponentModel_CardStoreContext_CardTypeID.htm)|
Идентификатор типа сохраняемой карточки.  
[DoesNotAffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_DoesNotAffectVersion.htm)|
Признак того, что изменение карточки не приведёт к проверке и к увеличению
номера версии, даже если присутствуют изменяемые значения в основной карточке
или её файлах. При первом сохранении карточки версия всё равно увеличивается
до 1. Этот флаг более приоритетный, чем
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm).  
[ExcludedQueryCount](P_Tessa_Cards_ComponentModel_CardStoreContext_ExcludedQueryCount.htm)|
Количество запросов, выполненных через
[Executor](P_Tessa_Cards_ComponentModel_CardStoreContext_Executor.htm),
которые не учитываются в стандартном API при определении того, следует ли
выполнять проверку и инкремент версии карточки.  
[Executor](P_Tessa_Cards_ComponentModel_CardStoreContext_Executor.htm)|
Объект, выполняющий SQL-команды по сохранению карточки.  
[Files](P_Tessa_Cards_ComponentModel_CardStoreContext_Files.htm)|  Файлы
сохраняемой карточки.  
[ForceTransaction](P_Tessa_Cards_ComponentModel_CardStoreContext_ForceTransaction.htm)|
Признак того, что будет открыта транзакция независимо от наличия изменений в
карточке.  
[GeneralMetadata](P_Tessa_Cards_ComponentModel_CardStoreContext_GeneralMetadata.htm)|
Общая метаинформация по типам карточек.  
[HasUserInfo](P_Tessa_Cards_ComponentModel_CardStoreContext_HasUserInfo.htm)|
Признак того, что в контексте присутствует действительная информация об имени
и идентификаторе пользователя, выполняющего сохранение карточки. При
отсутствии карточки сохранение должно выполняться от имени пользователя
System.  
[RepairSections](P_Tessa_Cards_ComponentModel_CardStoreContext_RepairSections.htm)|
Флаг указывает на то, что нужно починить (добавить) строковые секции карточки
в случае, если они отсутствуют в БД.  
[Sections](P_Tessa_Cards_ComponentModel_CardStoreContext_Sections.htm)|
Секции сохраняемой карточки.  
[Session](P_Tessa_Cards_ComponentModel_CardStoreContext_Session.htm)|  Сессия
текущего пользователя.  
[StoreDateTime](P_Tessa_Cards_ComponentModel_CardStoreContext_StoreDateTime.htm)|
Время сохранения карточки в формате UTC.  
[StoreMethod](P_Tessa_Cards_ComponentModel_CardStoreContext_StoreMethod.htm)|
Специализация для способа сохранения карточки.  
[StoreMode](P_Tessa_Cards_ComponentModel_CardStoreContext_StoreMode.htm)|
Способ сохранения карточки.  
[TaskHistory](P_Tessa_Cards_ComponentModel_CardStoreContext_TaskHistory.htm)|
История заданий сохраняемой карточки  
[TaskHistoryGroups](P_Tessa_Cards_ComponentModel_CardStoreContext_TaskHistoryGroups.htm)|
Группы истории заданий сохраняемой карточки  
[TaskRowIDListToMakeInProgress](P_Tessa_Cards_ComponentModel_CardStoreContext_TaskRowIDListToMakeInProgress.htm)|
Список идентификаторов заданий, которые берутся в работу в процессе
сохранения. Для каждого такого задания выполняются дополнительные проверки
внутри блокировки на запись карточки.  
[Tasks](P_Tessa_Cards_ComponentModel_CardStoreContext_Tasks.htm)|  Задания
сохраняемой карточки.  
[UserID](P_Tessa_Cards_ComponentModel_CardStoreContext_UserID.htm)|
Идентификатор пользователя, выполняющего сохранение карточки.  
[UserName](P_Tessa_Cards_ComponentModel_CardStoreContext_UserName.htm)|  Имя
пользователя, выполняющего сохранение карточки.  
[ValidationResult](P_Tessa_Cards_ComponentModel_CardStoreContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации.  
## __См. также
#### Ссылки
[CardStoreContext - ](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
