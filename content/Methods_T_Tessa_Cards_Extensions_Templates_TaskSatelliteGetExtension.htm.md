# TaskSatelliteGetExtension - методы
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
(Переопределяет
[CardGetExtension.AfterRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
(Переопределяет
[CardGetExtension.BeforeRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardGetExtension_BeforeRequest.htm))  
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
[LoadExternalCardsWithFilesListAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_LoadExternalCardsWithFilesListAsync.htm)|
Возвращает идентификаторы карточек-сателлитов, которые содержат файлы и для
которых файлы требуется загрузить как виртуальные файлы для текущей карточки-
сателлита. Например, это идентификаторы сателлитов для заданий, которые
расположены выше по иерархии в истории заданий.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareRequestToLoadMainCardAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_PrepareRequestToLoadMainCardAsync.htm)|
Подготавливает запрос на загрузку основной карточки, данные которой
используются, а также информация по правам доступа к которой используются при
загрузке карточки-сателлита.  
[PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync.htm)|
Выполняет постобработку загруженной карточки-сателлита, а также возвращает
дополнительную информацию, такую как токен прав доступа, которая используется
в других методах этого класса, в т.ч. для загрузки основной карточки. Если
такой информации нет, то возвращает null.  
[PrepareSatelliteWithMainCardInfoAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_PrepareSatelliteWithMainCardInfoAsync.htm)|
Подготавливает данные карточки-сателлита по данным загруженной основной
карточки.  
[SetupSatelliteFileAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_SetupSatelliteFileAsync.htm)|
Устанавливает свойства загруженного файла в карточке-сателлите для учёта того,
что файл может принадлежать основной карточке.  
[SetupVirtualSatelliteAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_SetupVirtualSatelliteAsync.htm)|
В виртуальной карточке-сателлите устанавливает идентификаторы основной
карточки и задания, к которым относится сателлит.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetMainCardIDAndTaskRowIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_TryGetMainCardIDAndTaskRowIDAsync.htm)|
Возвращает идентификатор основной карточки и идентификатор задания по
идентификатору карточки-сателлита. Значение false возвращается в том случае,
если сателлит не существует.  
[TryGetMainCardIDByTaskRowIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_TryGetMainCardIDByTaskRowIDAsync.htm)|
Возвращает идентификатор основной карточки по идентификатору задания или null,
если карточка не найдена.  
[TryGetTaskSatelliteIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_TryGetTaskSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита по идентификатору задания на
основании данных в базе данных или null, если сателлит не существует.  
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
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
