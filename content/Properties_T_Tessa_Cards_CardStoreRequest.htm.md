# CardStoreRequest - свойства
##  __Свойства
[AffectVersion](P_Tessa_Cards_CardStoreRequest_AffectVersion.htm)|  Признак
того, что изменение карточки будет принудительно выполняться с проверкой её
версии и приведёт к увеличению номера версии, даже если отсутствуют изменяемые
значения в основной карточке или её файлах. Изменение заданий не приводит к
проверке и увеличению версии, только если этот флаг установлен в false. Этот
флаг менее приоритетный, чем
[DoesNotAffectVersion](P_Tessa_Cards_CardStoreRequest_DoesNotAffectVersion.htm).  
---|---  
[Card](P_Tessa_Cards_CardStoreRequest_Card.htm)|  Карточка.  
[DoesNotAffectVersion](P_Tessa_Cards_CardStoreRequest_DoesNotAffectVersion.htm)|
Признак того, что изменение карточки не приведёт к проверке версии и к
увеличению номера версии, даже если присутствуют изменяемые значения в
основной карточке или её файлах. При первом сохранении карточки версия всё
равно увеличивается до 1. Этот флаг более приоритетный, чем
[AffectVersion](P_Tessa_Cards_CardStoreRequest_AffectVersion.htm).  
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[FileMapping](P_Tessa_Cards_CardStoreRequest_FileMapping.htm)|  Маппинг для
контента сохраняемых файлов. Значение актуально задавать при сохранении
карточки с контентом файлов, которые являются виртуальными, т.е. принадлежат
другой карточке.  
[ForceReleaseLock](P_Tessa_Cards_CardStoreRequest_ForceReleaseLock.htm)|
Признак того, что для карточки будет принудительно закрыта блокировка на
запись даже в том случае, если она не должна быть закрыта. Этот флаг имеет
смысл только в том случае, когда
[Method](P_Tessa_Cards_CardStoreRequest_Method.htm) равен
[Restore](T_Tessa_Cards_CardStoreMethod.htm). Актуально, например, при
восстановлении карточки-сателлита.  
[ForceTransaction](P_Tessa_Cards_CardStoreRequest_ForceTransaction.htm)|
Признак того, что для карточки будет принудительно открыта транзакция даже в
том случае, если изменения карточки отсутствуют. Это позволит гарантировать,
что расширения внутри транзакции будут выполнены. При отсутствии других
изменений в карточке транзакция будет открыта без блокировки.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Method](P_Tessa_Cards_CardStoreRequest_Method.htm)|  Способ сохранения
карточки.  
[ServiceType](P_Tessa_Cards_CardStoreRequest_ServiceType.htm)|  Тип сервиса,
от которого был получен текущий объект запроса. Позволяет определить
надёжность данных в запросе. При сериализации значение не передаётся с клиента
на сервер. Это свойство используется платформой, не рекомендуется
устанавливать его значение вручную.  
## __См. также
#### Ссылки
[CardStoreRequest - ](T_Tessa_Cards_CardStoreRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
