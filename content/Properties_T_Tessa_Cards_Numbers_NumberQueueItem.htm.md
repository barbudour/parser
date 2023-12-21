# NumberQueueItem - свойства
##  __Свойства
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
---|---  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[EventType](P_Tessa_Cards_Numbers_NumberQueueItem_EventType.htm)|  Тип
события, происходящего с номером, в результате которого была добавлена запись
в очередь [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[Handled](P_Tessa_Cards_Numbers_NumberQueueItem_Handled.htm)|  Признак того,
что действие обработано. Обработанные действия не будут обработаны повторно и
могут быть удалены из очереди после завершения цепочки действий.  
[ID](P_Tessa_Cards_Numbers_NumberQueueItem_ID.htm)|  Идентификатор записи.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm)|  Номер, для
которого требуется выполнить действие в очереди. У номера должен быть заполнен
тип [Type](P_Tessa_Cards_Numbers_NumberStorageObject_Type.htm), но остальные
поля могут быть пустыми, если для выполнения действия
[QueueActionType](P_Tessa_Cards_Numbers_NumberQueueItem_QueueActionType.htm)
не требуется указать конкретный номер, а достаточно лишь общей информации.  
[QueueActionType](P_Tessa_Cards_Numbers_NumberQueueItem_QueueActionType.htm)|
Тип действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[QueueEventType](P_Tessa_Cards_Numbers_NumberQueueItem_QueueEventType.htm)|
Тип события по вызову действия с номером, в результате которого была добавлена
запись в очередь [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[QueuePredicateExpectedValue](P_Tessa_Cards_Numbers_NumberQueueItem_QueuePredicateExpectedValue.htm)|
Ожидаемое значение, которое возвращает предикат. Действие будет выполнено
только в том случае, если значение, возвращённое предикатом, и значение этого
свойства совпадут. По умолчанию значение равно true.  
[QueuePredicateType](P_Tessa_Cards_Numbers_NumberQueueItem_QueuePredicateType.htm)|
Тип предиката, определяющего необходимость вызова действия с номером. По
умолчанию указано значение
[Always](F_Tessa_Cards_Numbers_NumberQueuePredicateTypes_Always.htm).  
[SourceLocation](P_Tessa_Cards_Numbers_NumberQueueItem_SourceLocation.htm)|
Информация по местоположению номера в карточке, по которому номер следует
прочитать для выполнения действия. Если местоположение указано, то номер
[Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm) и тип номера
[SourceNumberType](P_Tessa_Cards_Numbers_NumberQueueItem_SourceNumberType.htm)
игнорируются.  
[SourceNumberType](P_Tessa_Cards_Numbers_NumberQueueItem_SourceNumberType.htm)|
Тип номера с дополнительной информацией, по которому номер следует прочитать
для выполнения действия, или null, если тип не указан и номер следует получить
из свойства [Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm). Если
тип номера указан, то номер
[Number](P_Tessa_Cards_Numbers_NumberQueueItem_Number.htm) игнорируется, но
при этом свойство
[SourceLocation](P_Tessa_Cards_Numbers_NumberQueueItem_SourceLocation.htm)
должно быть равно null.  
[TargetLocation](P_Tessa_Cards_Numbers_NumberQueueItem_TargetLocation.htm)|
Информация по местоположению номера в карточке, по которому номер следует
сохранить после выполнения действия.  
## __См. также
#### Ссылки
[NumberQueueItem - ](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
