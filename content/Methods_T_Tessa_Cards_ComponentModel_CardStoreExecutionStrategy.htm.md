# CardStoreExecutionStrategy - методы
##  __Методы
[CheckSectionsOnInsertAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_CheckSectionsOnInsertAsync.htm)|
Проверяет наличие в карточке всех строковых секций из типа карточки при её
создании. В случае отсутствия некоторых секций метод возвращает false и
добавляет сообщение в результат валидации.  
---|---  
[DeleteTaskHistoryAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_DeleteTaskHistoryAsync.htm)|
Удаляет запись в истории заданий TaskHistory с заданным идентификатором.  
[DeleteTaskHistoryGroupAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_DeleteTaskHistoryGroupAsync.htm)|
Удаляет запись о группе в истории заданий TaskHistoryGroups с заданным
идентификатором.  
[DeleteTaskRolesAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_DeleteTaskRolesAsync.htm)|
Удаляет роли заданий с заданными идентификаторами.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSectionRowRemoverAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_GetSectionRowRemoverAsync.htm)|
Возвращает объект, выполняющий удаление строк из заданной коллекционной или
древовидной секции.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InsertInstanceAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_InsertInstanceAsync.htm)|
Вставляет запись в таблицу экземпляров карточек Instances. В момент создания
открывается блокировка на запись, которая должна быть закрыта по завершению.  
[InsertTaskHistoryAsync(CardStoreContext,
CardTask)](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_InsertTaskHistoryAsync.htm)|
Вставляет запись о завершённом задании в таблицу с историей заданий
TaskHistory.  
[InsertTaskHistoryAsync(IQueryExecutor, IQueryBuilderFactory, Guid,
CardTaskHistoryItem,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_InsertTaskHistoryAsync_1.htm)|
Вставляет запись о завершённом задании в таблицу с историей заданий
TaskHistory. Метод рекомендуется использовать для восстановления записи из
истории заданий после удаления карточки.  
[InsertTaskHistoryGroupAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_InsertTaskHistoryGroupAsync.htm)|
Вставляет запись о завершённом задании в таблицу с группами истории заданий
TaskHistoryGroups.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StoreFileAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_StoreFileAsync.htm)|
Выполняет сохранение файла.  
[StoreSectionsAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_StoreSectionsAsync.htm)|
Выполняет сохранение секций карточки.  
[StoreTaskAsync](M_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy_StoreTaskAsync.htm)|
Выполняет сохранение задания. Возвращает список идентификаторов ролей заданий,
которые необходимо удалить, или null, если список пуст.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[CardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
