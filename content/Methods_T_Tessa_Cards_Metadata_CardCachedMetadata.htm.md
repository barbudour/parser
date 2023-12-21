# CardCachedMetadata - методы
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetCachedMetadataAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetCachedMetadataAsync.htm)|
Возвращает исходный объект метаинформации, который кэшируется текущим
объектом.  
[GetCardTypesAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetCardTypesAsync.htm)|
Возвращает список типов карточек карточек.  
[GetDamagedCardTypeIDListAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetDamagedCardTypeIDListAsync.htm)|
Возвращает список идентификаторов повреждённых типов карточек. Собственно типы
карточек можно получить посредством сервиса типов карточек.  
[GetEnumerationsAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetEnumerationsAsync.htm)|
Возвращает список перечислений.  
[GetGlobalReferencesAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetGlobalReferencesAsync.htm)|
Возвращает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl]), совместно использующиеся в типах карточек.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMetadataForTypeAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetMetadataForTypeAsync.htm)|
Возвращает выборку из метаинформации, которая относится только к заданному
типу карточек. В возвращённую выборку не передаются перечисления.  
[GetSectionsAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetSectionsAsync.htm)|
Возвращает метаинформацию по секциям карточек.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValidationResultAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_GetValidationResultAsync.htm)|
Возвращает результат валидации при построении метаинформации.  
[InvalidateAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_InvalidateAsync.htm)|
Сбрасывает кэш метаинформации. При следующем обращении к содержимому
метаинформации будет выполнен запрос на получение её из сервиса типов
карточек.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Cards_Metadata_CardCachedMetadata_Seal.htm)| Защищает объект от
изменений.  
[SetAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_SetAsync.htm)|
Устанавливает заданную метаинформацию в кэше. При этом метаинформация
защищается от изменений, если кэш также защищён от изменений.  
[SetCardTypesAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_SetCardTypesAsync.htm)|
Устанавливает список типов карточек.  
[SetDamagedCardTypeIDListAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_SetDamagedCardTypeIDListAsync.htm)|
Устанавливает список идентификаторов повреждённых типов карточек. Собственно
типы карточек можно получить посредством сервиса типов карточек.  
[SetEnumerationsAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_SetEnumerationsAsync.htm)|
Устанавливает список перечислений.  
[SetGlobalReferencesAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_SetGlobalReferencesAsync.htm)|
Устанавливает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl], [CardTypeValidator], [CardTypeExtension]), совместно
использующиеся в типах карточек.  
[SetSectionsAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_SetSectionsAsync.htm)|
Метаинформация по секциям карточек.  
[SetValidationResultAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_SetValidationResultAsync.htm)|
Устанавливает результат валидации при построении метаинформации.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateAsync](M_Tessa_Cards_Metadata_CardCachedMetadata_UpdateAsync.htm)|
Обновляет кэш метаинформации из сервиса типов карточек. Если объект защищён от
изменений посредством метода [Tessa.Platform.ISealable.Seal] и имеет доступ к
объектам метаинформации, переданным через конструктор, то выполняется более
эффективный запрос к серверу для получения актуальной метаинформации.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
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
[TryGetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
