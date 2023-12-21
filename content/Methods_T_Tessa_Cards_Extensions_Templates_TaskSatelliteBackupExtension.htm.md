# TaskSatelliteBackupExtension - методы
##  __Методы
[AddSatelliteToListAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension_AddSatelliteToListAsync.htm)|
Добавляет карточку-сателлит в список сателлитов, которые относятся к текущему
расширению и сохраняются в информации по основной карточке mainCard.Info. Если
список отсутствовал, то он должен быть создан в этом методе.  
(Унаследован от
[MultitypeSatelliteBackupExtension](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[MultitypeSatelliteBackupExtension](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension.htm))  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
[ClearSatelliteListAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension_ClearSatelliteListAsync.htm)|
Удаляет все карточки-сателлиты в списке сателлитов, которые относятся к
текущему расширению и сохраняются в информации по основной карточке
mainCard.Info.  
(Унаследован от
[MultitypeSatelliteBackupExtension](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension.htm))  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsMainCardTypeAsync](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension_IsMainCardTypeAsync.htm)|
Возвращает признак того, что заданный тип является типом основной карточки, к
которой относится карточка-сателлит.  
(Унаследован от
[MultitypeSatelliteBackupExtension](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetSatelliteIDListAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteBackupExtension_TryGetSatelliteIDListAsync.htm)|
Возвращает список идентификаторов карточек-сателлитов обрабатываемого типа,
которые относятся к текущему расширению, где список получен из базы данных,
или null, если карточки не найдены (аналогично пустому списку).  
[TryGetSatelliteInfoListAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteBackupExtension_TryGetSatelliteInfoListAsync.htm)|
Возвращает список данных о карточек-сателлитах обрабатываемого типа, которые
относятся к текущему расширению, где список получен из базы данных, или null,
если карточки не найдены (аналогично пустому списку).  
(Переопределяет
[MultitypeSatelliteBackupExtension.TryGetSatelliteInfoListAsync(IDbScope,
Guid,
CancellationToken)](M_Tessa_Cards_Extensions_Templates_MultitypeSatelliteBackupExtension_TryGetSatelliteInfoListAsync.htm))  
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
[TaskSatelliteBackupExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteBackupExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
