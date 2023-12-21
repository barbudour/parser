# MultitypeSatelliteDeleteExtension - методы
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Переопределяет
[CardDeleteExtension.AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterBeginTransaction.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_AfterRequest.htm)|
Действие, выполняемое после удаления карточки как при успешном, так и при
неудачном результате.  
(Переопределяет
[CardDeleteExtension.AfterRequest(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterRequest.htm))  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardDeleteExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после удаления карточки
как при успешном, так и при неудачном результате. Необработанные исключения не
прерывают выполнение цепочки расширений.  
(Унаследован от
[CardDeleteExtension](T_Tessa_Cards_Extensions_CardDeleteExtension.htm))  
[BeforeCommitTransaction](M_Tessa_Cards_Extensions_CardDeleteExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
(Унаследован от
[CardDeleteExtension](T_Tessa_Cards_Extensions_CardDeleteExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_BeforeRequest.htm)|
Действие, выполняемое перед удалением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы удаление карточки стандартными
средствами не выполнялось.  
(Переопределяет
[CardDeleteExtension.BeforeRequest(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_CardDeleteExtension_BeforeRequest.htm))  
[CreateSatelliteInfoAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_CreateSatelliteInfoAsync.htm)|
Создаёт информацию по карточке-сателлиту, которая относится к текущему
расширению.  
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
[GetAdditionalInfoForDeletionAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_GetAdditionalInfoForDeletionAsync.htm)|
Возвращает дополнительную информацию для использования в запросах на удаление
карточек-сателлитов в методе PrepareSatelliteDeleteRequest. Например, это
токен прав доступа. Метод может вернуть null, если такая информация
отсутствует.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsMainCardTypeAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_IsMainCardTypeAsync.htm)|
Возвращает признак того, что заданный тип является типом основной карточки, к
которой относится карточка-сателлит.  
[IsSatelliteCardTypeAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_IsSatelliteCardTypeAsync.htm)|
Возвращает признак того, что заданный тип является типом карточки-сателлита.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareSatelliteDeleteRequestAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_PrepareSatelliteDeleteRequestAsync.htm)|
Подготавливает запрос на удаление карточки-сателлита, которое выполняется
одновременно с удалением основной карточки.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetSatelliteCardListAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_TryGetSatelliteCardListAsync.htm)|
Возвращает список с карточками-сателлитами, которые относятся к текущему
расширению, где список получен по данным основной карточки mainCard.Info, или
null, если список не был установлен.  
[TryGetSatelliteInfoListAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension_TryGetSatelliteInfoListAsync.htm)|
Возвращает список объектов с информацией по файлам всех карточек-сателлитов по
идентификатору основной карточки или null, если карточки-сателлиты не найдены
(аналогично пустому списку).  
## __Методы расширения
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
[MultitypeSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
