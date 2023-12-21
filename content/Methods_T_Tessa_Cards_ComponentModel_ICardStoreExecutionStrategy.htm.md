# ICardStoreExecutionStrategy - методы
##  __Методы
[CheckSectionsOnInsertAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_CheckSectionsOnInsertAsync.htm)|
Проверяет наличие в карточке всех строковых секций из типа карточки при её
создании. В случае отсутствия некоторых секций метод возвращает false и
добавляет сообщение в результат валидации.  
---|---  
[DeleteTaskHistoryAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_DeleteTaskHistoryAsync.htm)|
Удаляет запись в истории заданий TaskHistory с заданным идентификатором.  
[DeleteTaskHistoryGroupAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_DeleteTaskHistoryGroupAsync.htm)|
Удаляет запись о группе в истории заданий TaskHistoryGroups с заданным
идентификатором.  
[DeleteTaskRolesAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_DeleteTaskRolesAsync.htm)|
Удаляет роли заданий с заданными идентификаторами.  
[GetSectionRowRemoverAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_GetSectionRowRemoverAsync.htm)|
Возвращает объект, выполняющий удаление строк из заданной коллекционной или
древовидной секции.  
[InsertInstanceAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_InsertInstanceAsync.htm)|
Вставляет запись в таблицу экземпляров карточек Instances. В момент создания
открывается блокировка на запись, которая должна быть закрыта по завершению.  
[InsertTaskHistoryAsync(CardStoreContext,
CardTask)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_InsertTaskHistoryAsync.htm)|
Вставляет запись о завершённом задании в таблицу с историей заданий
TaskHistory.  
[InsertTaskHistoryAsync(IQueryExecutor, IQueryBuilderFactory, Guid,
CardTaskHistoryItem,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_InsertTaskHistoryAsync_1.htm)|
Вставляет запись о завершённом задании в таблицу с историей заданий
TaskHistory. Метод рекомендуется использовать для восстановления записи из
истории заданий после удаления карточки.  
[InsertTaskHistoryGroupAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_InsertTaskHistoryGroupAsync.htm)|
Вставляет запись о завершённом задании в таблицу с группами истории заданий
TaskHistoryGroups.  
[StoreFileAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_StoreFileAsync.htm)|
Выполняет сохранение файла.  
[StoreSectionsAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_StoreSectionsAsync.htm)|
Выполняет сохранение секций карточки.  
[StoreTaskAsync](M_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy_StoreTaskAsync.htm)|
Выполняет сохранение задания. Возвращает список идентификаторов ролей заданий,
которые необходимо удалить, или null, если список пуст.  
## __См. также
#### Ссылки
[ICardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
