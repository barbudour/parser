# CardRepository - методы
##  __Методы
[DeleteAsync](M_Tessa_Cards_CardRepository_DeleteAsync.htm)|  Удаляет карточку
со всеми файлами и заданиями по информации, переданной в запросе. Для
успешного удаления карточки необходимо предварительно удалить все карточки,
которые на неё ссылаются.  
---|---  
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
[GetAsync](M_Tessa_Cards_CardRepository_GetAsync.htm)| Возвращает данные
карточки по заданному запросу.  
[GetFileVersionsAsync](M_Tessa_Cards_CardRepository_GetFileVersionsAsync.htm)|
Возвращает информацию о версиях файла по заданному запросу.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NewAsync](M_Tessa_Cards_CardRepository_NewAsync.htm)| Возвращает заполненную
структуру карточки по заданному запросу. Физически карточка не создаётся.  
[RequestAsync](M_Tessa_Cards_CardRepository_RequestAsync.htm)| Выполняет
универсальный запрос к сервису карточек.  
[StoreAsync](M_Tessa_Cards_CardRepository_StoreAsync.htm)| Сохраняет карточку,
переданную в запросе.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[ApplyUserSettingsToRolesAsync](M_Tessa_Cards_CardExtensions_ApplyUserSettingsToRolesAsync.htm)|
Асинхронно выполняет копирование настроек одного сотрудника на заданный список
ролей (без учёта заместителей). Запрос доступен только для администраторов.
Возвращает сообщения валидации, в т.ч. возникшие ошибки. Возвращаемое значение
не равно null.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[ChangePasswordForCurrentUserAsync](M_Tessa_Cards_CardExtensions_ChangePasswordForCurrentUserAsync.htm)|
Асинхронно изменяет пароль для текущего сотрудника, если у него тип входа
"Пользователь Tessa". Возвращает сообщения валидации, в т.ч. возникшие ошибки.
Возвращаемое значение не равно null.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[ForumAddTopicPermissionRequestAsync](M_Tessa_Forums_ForumPermissionsRequestExtensions_ForumAddTopicPermissionRequestAsync.htm)|  
(Определяется
[ForumPermissionsRequestExtensions](T_Tessa_Forums_ForumPermissionsRequestExtensions.htm))  
[ForumMessagesPermissionRequestAsync](M_Tessa_Forums_ForumPermissionsRequestExtensions_ForumMessagesPermissionRequestAsync.htm)|  
(Определяется
[ForumPermissionsRequestExtensions](T_Tessa_Forums_ForumPermissionsRequestExtensions.htm))  
[ForumPermissionsRequestAsync<TRequest,
TResponse>](M_Tessa_Forums_ForumRequestExtensions_ForumPermissionsRequestAsync__2.htm)|  
(Определяется
[ForumRequestExtensions](T_Tessa_Forums_ForumRequestExtensions.htm))  
[ForumRequestAsync<TRequest,
TResponse>](M_Tessa_Forums_ForumRequestExtensions_ForumRequestAsync__2.htm)|  
(Определяется
[ForumRequestExtensions](T_Tessa_Forums_ForumRequestExtensions.htm))  
[ForumRequestWithoutResponseAsync<TRequest>](M_Tessa_Forums_ForumRequestExtensions_ForumRequestWithoutResponseAsync__1.htm)|  
(Определяется
[ForumRequestExtensions](T_Tessa_Forums_ForumRequestExtensions.htm))  
[ForumSuperModeratorPermissionRequestAsync](M_Tessa_Forums_ForumPermissionsRequestExtensions_ForumSuperModeratorPermissionRequestAsync.htm)|  
(Определяется
[ForumPermissionsRequestExtensions](T_Tessa_Forums_ForumPermissionsRequestExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetDigestAsync](M_Tessa_Cards_CardExtensions_GetDigestAsync.htm)|  Асинхронно
возвращает Digest для заданной карточки, полученный выполнением запроса
[GetDigest](F_Tessa_Cards_CardRequestTypes_GetDigest.htm), или null, если
Digest неизвестен или не требуется.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[GetFileSourceAsync](M_Tessa_Cards_CardExtensions_GetFileSourceAsync_1.htm)|
Асинхронно возвращает местоположение контента файла для заданного файла file
указанной карточки card. Местоположение определяется выполнением запроса
[GetFileSource](F_Tessa_Cards_CardRequestTypes_GetFileSource.htm). Метод
возвращает null, если определить местоположение не удалось, обычно в этом
случае будет использоваться местоположение по умолчанию.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[GetTypeIDAsync](M_Tessa_Cards_CardExtensions_GetTypeIDAsync.htm)|  Асинхронно
возвращает результат выполнения запроса
[GetTypeIDList](F_Tessa_Cards_CardRequestTypes_GetTypeIDList.htm) на получение
идентификатора типа карточки по заданному идентификатору карточки. Значение
null возвращается в случае, если идентификатор типа не был определён.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[GetTypeIDListAsync](M_Tessa_Cards_CardExtensions_GetTypeIDListAsync.htm)|
Асинхронно возвращает результат выполнения запроса
[GetTypeIDList](F_Tessa_Cards_CardRequestTypes_GetTypeIDList.htm) на получение
идентификаторов типов карточек по заданным идентификаторам карточек. Элементы
результирующего массива со значениями null возвращаются в случае, если
идентификатор типа не был определён.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[InvalidateCacheAsync](M_Tessa_Cards_CardRequestExtensions_InvalidateCacheAsync.htm)|
Выполняет запрос по сбросу кэшей на сервере. Может быть вызван с сервера или
клиента для сессии пользователя с правами администратора. Если в качестве
списка имён cacheNames указывается null, то выполняется сброс всех кэшей; если
указан пустой массив, то сброс не будет выполнен, однако, запрос будет запущен
(т.е. расширения могут определить список кэшей для сброса сами). Возвращает
результат выполнения операции, который не равен null.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ResolveUserPermissionsAsync](M_Tessa_Forums_ForumPermissionsRequestExtensions_ResolveUserPermissionsAsync.htm)|  
(Определяется
[ForumPermissionsRequestExtensions](T_Tessa_Forums_ForumPermissionsRequestExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[TryAddTaskAsync](M_Tessa_Cards_CardExtensions_TryAddTaskAsync.htm)|  Создаёт
и добавляет возвращаемое задание с заданными параметрами. После создания может
потребоваться заполнить секции задания и другие параметры
[CardTask](T_Tessa_Cards_CardTask.htm). Возвращённый объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
ошибки и сообщения, возникшие при создании задания, он всегда не равен null.
Возвращённый объект [CardTask](T_Tessa_Cards_CardTask.htm) может быть равен
null, если при создании были ошибки. В этом случае возвращённый объект
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) содержит
эти ошибки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
##  __См. также
#### Ссылки
[CardRepository - ](T_Tessa_Cards_CardRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
