# CardFileRequestBase - методы
##  __Методы
[Clean](M_Tessa_Cards_CardFileRequestBase_Clean.htm)| Выполняет очистку
хранилища от избыточных данных.  
(Переопределяет
[CardRequestBase.Clean()](M_Tessa_Cards_CardRequestBase_Clean.htm))  
---|---  
[CleanCollectionAndSetNullIfEmpty](M_Tessa_Platform_Storage_StorageObject_CleanCollectionAndSetNullIfEmpty.htm)|
Очищает коллекцию, найденную по ключу key, после чего устанавливает null на
место коллекции, если она стала пустой.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ClearCache](M_Tessa_Platform_Storage_StorageObject_ClearCache.htm)|  Очищает
внутренний кэш декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ContainsKey](M_Tessa_Platform_Storage_StorageObject_ContainsKey.htm)|
Возвращает признак того, что элемент с заданным ключом содержится в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[EnsureCacheResolved](M_Tessa_Cards_CardInfoStorageObject_EnsureCacheResolved.htm)|
Инициализирует объект-обёртку для всех значений, в т.ч. для вложенных
объектов. Рекомендуется выполнять при создании заполненного объекта перед
асинхронным обращением к его вложенным объектам.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
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
[FromJsonCore](M_Tessa_Platform_Storage_StorageObject_FromJsonCore.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON. Возвращает текущий объект для цепочки вызовов. Рассмотрите
использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе FromTypedJson.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[FromTypedJsonCore](M_Tessa_Platform_Storage_StorageObject_FromTypedJsonCore.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON с сохранением типов. Используйте метод
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением типов. Для десериализации других объектов, у
которых нет метода FromTypedJson (например, request/response), используйте
метод
[DeserializeFromTypedJson(String)](M_Tessa_Platform_Storage_StorageHelper_DeserializeFromTypedJson.htm),
записав полученную структуру в объект obj.SetStorage(storage).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Get<T>(String)](M_Tessa_Platform_Storage_StorageObject_Get__1.htm)|
Возвращает строго типизированное значение объекта из хранилища по заданному
ключу.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Get<T>(String,
Func<Object>)](M_Tessa_Platform_Storage_StorageObject_Get__1_1.htm)|
Возвращает строго типизированное значение объекта из хранилища по заданнному
ключу с указанием фабрики defaultValueFunc, создающей значение по умолчанию и
добавляющей его в хранилище, если оно было равно null.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetDictionary<T>](M_Tessa_Platform_Storage_StorageObject_GetDictionary__1.htm)|
Возвращает декоратор для коллекции пар ключ / значение, полученный из
хранилища по заданному ключу или созданный посредством заданной фабрики
defaultDictionaryFunc, и добавленный в хранилище, если он там отсутствует.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetList<T>](M_Tessa_Platform_Storage_StorageObject_GetList__1.htm)|
Возвращает декоратор для коллекции объектов, полученный из хранилища по
заданному ключу или созданный посредством заданной фабрики defaultListFunc, и
добавленный в хранилище, если он там отсутствует.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetObjectData](M_Tessa_Platform_Storage_StorageObject_GetObjectData.htm)|
Записывает сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetStorage](M_Tessa_Platform_Storage_StorageObject_GetStorage.htm)|
Возвращает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Init](M_Tessa_Platform_Storage_StorageObject_Init.htm)|  Инициализирует
значение объекта с заданным ключом, если он отсутствовал в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[InitNotNull](M_Tessa_Platform_Storage_StorageObject_InitNotNull.htm)|
Инициализирует значение объекта с заданным ключом, если он отсутствовал в
хранилище или был равен null, посредством фабрики объектов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[IsValid](M_Tessa_Platform_Validation_ValidationStorageObject_IsValid.htm)|
Выполняет проверку объекта на валидность и возвращает признак того, что объект
является валидным.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ObjectCanExistInStorageByKey<T>](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectCanExistInStorageByKey__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, может
содержаться в хранилище и в таком случае должно проходить проверку на
валидность посредством функции valueIsValid, причём значение для проверки
доступно из хранилища по ключу key.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectCanExistInStorageByValue<T>](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectCanExistInStorageByValue__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, может
содержаться в хранилище и в таком случае должно проходить проверку на
валидность посредством функции valueIsValid, причём значение для проверки
определяется по функции, передаваемой первым параметром метода Validate.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectExistsInStorageByKey(String)](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectExistsInStorageByKey.htm)|
Возвращает признак того, что значение, доступное по ключу key, содержится в
хранилище.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectExistsInStorageByKey<T>(String, Func<T,
Boolean>)](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectExistsInStorageByKey__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, содержится в
хранилище и проходит проверку на валидность посредством функции valueIsValid,
причём значение для проверки доступно из хранилища по ключу key.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectExistsInStorageByValue<T>](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectExistsInStorageByValue__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, содержится в
хранилище и проходит проверку на валидность посредством функции valueIsValid,
причём значение для проверки определяется по функции, передаваемой первым
параметром метода Validate.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[Remove](M_Tessa_Platform_Storage_StorageObject_Remove.htm)|  Удаляет объект с
заданным ключом из хранилища.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[RemoveSystemInfo](M_Tessa_Cards_CardInfoStorageObject_RemoveSystemInfo.htm)|
Удаляет системную информацию, которая может располагаться в любом месте в
хранилище текущего объекта и может быть найдена по ключам с префиксом
[SystemKeyPrefix](F_Tessa_Cards_CardHelper_SystemKeyPrefix.htm).
Внимание! После выполнения метода из карточки исчезнут важные сведения, такие
как информация об изменённых полях или о состоянии строк коллекционных и
древовидных секций.
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[RemoveUserInfo](M_Tessa_Cards_CardInfoStorageObject_RemoveUserInfo.htm)|
Удаляет пользовательскую информацию, которая может располагаться в любом месте
в хранилище текущего объекта и может быть найдена по ключам с префиксом
[UserKeyPrefix](F_Tessa_Cards_CardHelper_UserKeyPrefix.htm).  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Set<T>](M_Tessa_Platform_Storage_StorageObject_Set__1.htm)|  Устанавливает
значение в хранилище по заданному ключу. При этом не изменяется внутренний кэш
декораторов, поэтому метод следует использовать только для примитивных типов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetNull](M_Tessa_Platform_Storage_StorageObject_SetNull.htm)|  Устанавливает
значение null для элемента по заданному ключу и удаляет предыдущий элемент из
внутреннего кэша декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetNullIfEmptyEnumerable](M_Tessa_Platform_Storage_StorageObject_SetNullIfEmptyEnumerable.htm)|
Устанавливает равным null элемент с ключом key, если он является пустым
перечислением
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorage(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageObject_SetStorage.htm)|
Устанавливает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект, посредством копирования значений из заданного
хранилища. Если текущий объект реализует
[IStorageNotificationReceiver](T_Tessa_Platform_Storage_IStorageNotificationReceiver.htm),
то для него вызывается метод
[NotifyStorageUpdated()](M_Tessa_Platform_Storage_IStorageNotificationReceiver_NotifyStorageUpdated.htm).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorage(IStorageObjectProvider)](M_Tessa_Platform_Storage_StorageObject_SetStorage_1.htm)|
Устанавливает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект, посредством копирования значений из хранилища
заданного объекта. Если текущий объект реализует
[IStorageNotificationReceiver](T_Tessa_Platform_Storage_IStorageNotificationReceiver.htm),
то для него вызывается метод
[NotifyStorageUpdated()](M_Tessa_Platform_Storage_IStorageNotificationReceiver_NotifyStorageUpdated.htm).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorageValue](M_Tessa_Platform_Storage_StorageObject_SetStorageValue.htm)|
Устанавливает значение объекта, реализующего
[IStorageProvider](T_Tessa_Platform_Storage_IStorageProvider.htm), в хранилище
по заданному ключу. При этом также изменяется внутренний кэш декораторов,
поэтому метод следует использовать для декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToDynamic](M_Tessa_Platform_Storage_StorageObject_ToDynamic.htm)|  Возвращает
объект, осуществляющий доступ к хранилищу, декоратором для которого является
текущий объект, через позднее связывание.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToJson](M_Tessa_Platform_Storage_StorageObject_ToJson.htm)|  Сериализует
объект в текстовый JSON. Рассмотрите использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе FromTypedJson.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToTypedJson](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)|
Сериализует объект в текстовый JSON с сохранением информации по типам для всех
подобъектов, в т.ч. для Info. Используйте метод FromTypedJson для
десериализации. Для сериализации других объектов, у которых нет метода
ToTypedJson (например, request/response), используйте метод
[!:StorageHelper.SerializeToTypedJson(Dictionary<string,object>,bool)],
передав в него структуру объекта obj.GetStorage().  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGet<T>](M_Tessa_Platform_Storage_StorageObject_TryGet__1.htm)|  Возвращает
строго типизированное значение объекта из хранилища по заданному ключу или
default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetDictionary<T>](M_Tessa_Platform_Storage_StorageObject_TryGetDictionary__1.htm)|
Возвращает строго типизированное значение объекта Dictionary<string, object>
из хранилища по заданному ключу или default(T), если объект по заданному ключу
не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetInfo](M_Tessa_Cards_CardInfoStorageObject_TryGetInfo.htm)|  Возвращает
дополнительную пользовательскую информацию по текущему объекту или null, если
информация ещё не была задана.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[TryGetList<T>](M_Tessa_Platform_Storage_StorageObject_TryGetList__1.htm)|
Возвращает строго типизированное значение объекта List<object> из хранилища по
заданному ключу или default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetString](M_Tessa_Platform_Storage_StorageObject_TryGetString.htm)|
Возвращает строковое представление для значения объекта из хранилища по
заданному ключу или null, если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Validate()](M_Tessa_Platform_Validation_ValidationStorageObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationStorageObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ValidateInternal](M_Tessa_Cards_CardFileRequestBase_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardInfoStorageObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardInfoStorageObject_ValidateInternal.htm))  
##  __Методы расширения
[AddKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AddKrProcessClientCommands.htm)|
Добавляет в указанное хранилище список клиентских команд.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
---|---  
[AreButtonsIgnored](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AreButtonsIgnored.htm)|
Получает из заданного хранилища значение флага показывающего, что при загрузке
карточки не надо добавлять в ответ информацию по тайлам вторичных процессов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[ConsiderHiddenStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_ConsiderHiddenStages.htm)|
Возвращает значение, показывающее, что в карточку должны быть загружены
скрытые этапы маршрута.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[ConsiderSkippedStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_ConsiderSkippedStages.htm)|
Возвращает значение из заданного хранилища, показывающее, требуется ли
отображать пропущенные этапы.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[DontHideStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_DontHideStages_1.htm)|
Добавляет в указанное хранилище значение, показывающее, необходимо ли
загружать в карточку скрытые этапы маршрута или нет.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetHasRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetHasRecalcChanges.htm)|
Возвращает значение, показывающее, что после пересчёта были изменения в
маршруте или нет. Информация добавляется только при выставленном флаге
[HasChangesToInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetIgnorePermissionsWarning](M_Tessa_Cards_CardRequestExtensions_GetIgnorePermissionsWarning.htm)|
Возвращает признак того, что при сохранении карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение. Если признак не был установлен, то возвращается false.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[GetInfoAboutChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetInfoAboutChanges_1.htm)|
Возвращает режим вывода информации об изменениях в маршруте после пересчёта
или значение по умолчанию для типа, если хранилище его не содержало.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessClientCommands_1.htm)|
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessInstance.htm)|
Возвращает информацию об экземпляре процесса из указанного хранилища.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessLaunchResult.htm)|
Возвращает объект содержащий результат запуска процесса или значение по
умолчанию для типа, если указанный объект его не содержит.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetNoLockingMainCard](M_Tessa_Cards_CardRequestExtensions_GetNoLockingMainCard.htm)|
Возвращает признак того, что не следует выполнять блокировку основной карточки
при создании или изменении сателлита.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[GetRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcChanges.htm)|
Возвращает информацию о различиях в маршруте до и после пересчёта.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetRecalcFlag](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcFlag_1.htm)|
Возвращает значение, показывающее, должен ли быть выполнен пересчёт маршрута
или нет.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetStartingSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStartingSecondaryProcess.htm)|
Возвращает из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[IgnoreButtons](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IgnoreButtons.htm)|
Устанавливает значение, показывающее, что при загрузке карточки не надо
добавлять в ответ информацию по тайлам вторичных процессов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[IgnoreKrSatellite](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IgnoreKrSatellite.htm)|
Устанавливает значение, показывающее, что при загрузке карточки не надо
загружать и обрабатывать информацию содержащуюся в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
карточки.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IsKrSatelliteIgnored](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IsKrSatelliteIgnored.htm)|
Возвращает значение, показывающее, что при загрузке карточки не надо загружать
и обрабатывать информацию содержащуюся в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
карточки.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveLocalTiles.htm)|
Удаляет из заданного хранилища информацию по локальным тайлам маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveSecondaryProcess.htm)|
Удаляет из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса добавленную
[SetStartingSecondaryProcess(CardInfoStorageObject,
StartingSecondaryProcessInfo)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetDigest](M_Tessa_Cards_CardRequestExtensions_SetDigest_1.htm)|
Устанавливает Digest для сохранения в историю действий с карточкой.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetForceTaskPanel](M_Tessa_Cards_CardRequestExtensions_SetForceTaskPanel.htm)|  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetHasRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetHasRecalcChanges.htm)|
Задаёт значение, показывающее, что после пересчёта были изменения в маршруте
или нет. Информация добавляется только при выставленном флаге
[HasChangesToInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetIgnorePermissionsWarning](M_Tessa_Cards_CardRequestExtensions_SetIgnorePermissionsWarning.htm)|
Устанавливает признак того, что при обработке карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetInfoAboutChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetInfoAboutChanges_1.htm)|
Устанавливает в хранилище информацию о режиме информирования об изменениях в
маршруте после пересчёта.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessInstance_1.htm)|
Сохраняет в указанном объекте информация об экземпляре процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessLaunchResult.htm)|
Сохраняет результаты запуска процесса в указанном хранилище.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetLocalTiles.htm)|
Сохраняет в указанном объекте коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetNoLockingMainCard](M_Tessa_Cards_CardRequestExtensions_SetNoLockingMainCard.htm)|
Устанавливает признак того, что не следует выполнять блокировку основной
карточки при создании или изменении сателлита.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetPluginType](M_Tessa_Cards_CardRequestExtensions_SetPluginType.htm)|
Устанавливает тип плагина при выполнении запроса к карточке из плагина
Chronos. Стандартные типы перечислены в
[CardPluginTypes](T_Tessa_Cards_CardPluginTypes.htm).  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcChanges.htm)|
Сохраняет в заданном хранилище информацию о различиях в маршруте до и после
пересчёта.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetRecalcFlag](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcFlag_1.htm)|
Задаёт значение, показывающее, что должен быть выполнен пересчёт маршрута.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetStartingKrProcessParameters](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingKrProcessParameters_1.htm)|
Устанавливает параметры запускаемого процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetStartingSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm)|
Устанавливает информацию о процессе, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetDigest](M_Tessa_Cards_CardRequestExtensions_TryGetDigest.htm)|
Возвращает Digest для сохранения в историю действий с карточкой или null, если
Digest не был установлен.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessClientCommands.htm)|
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessInstance.htm)|
Возвращает информацию об экземпляре процесса из указанного хранилища.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessLaunchResult.htm)|
Возвращает объект, содержащий результат запуска процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetPluginType](M_Tessa_Cards_CardRequestExtensions_TryGetPluginType.htm)|
Возвращает тип плагина, установленный при выполнении запроса к карточке из
плагина Chronos, или null, если запрос выполнен не из плагина или из
неизвестного плагина.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetStartingKrProcessParameters](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStartingKrProcessParameters_1.htm)|
Возвращает параметры запускаемого процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
##  __См. также
#### Ссылки
[CardFileRequestBase - ](T_Tessa_Cards_CardFileRequestBase.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
