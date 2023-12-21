# Card - методы
##  __Методы
[Clean](M_Tessa_Cards_Card_Clean.htm)| Выполняет очистку хранилища от
избыточных данных.  
(Переопределяет
[CardInfoStorageObject.Clean()](M_Tessa_Cards_CardInfoStorageObject_Clean.htm))  
---|---  
[CleanCollectionAndSetNullIfEmpty](M_Tessa_Platform_Storage_StorageObject_CleanCollectionAndSetNullIfEmpty.htm)|
Очищает коллекцию, найденную по ключу key, после чего устанавливает null на
место коллекции, если она стала пустой.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ClearCache](M_Tessa_Platform_Storage_StorageObject_ClearCache.htm)|  Очищает
внутренний кэш декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Clone](M_Tessa_Cards_Card_Clone.htm)|  Выполняет глубокое клонирование
хранилища объекта и возвращает созданный строго типизированный декоратор для
хранилища.  
[ContainsKey](M_Tessa_Platform_Storage_StorageObject_ContainsKey.htm)|
Возвращает признак того, что элемент с заданным ключом содержится в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ConvertToInserted](M_Tessa_Cards_Card_ConvertToInserted.htm)|  Изменяет
карточку таким образом, что все её строки, файлы и задания считаются
добавленными, т.е. имеют состояние [Inserted](T_Tessa_Cards_CardRowState.htm)
или [Inserted](T_Tessa_Cards_CardFileState.htm), а также для карточки указан
[StoreMode](P_Tessa_Cards_Card_StoreMode.htm) как
[Insert](T_Tessa_Cards_CardStoreMode.htm). Возвращает признак того, что в
карточке были сделаны изменения.  
[EnsureCacheResolved](M_Tessa_Cards_Card_EnsureCacheResolved.htm)|
Инициализирует объект-обёртку для всех значений, в т.ч. для вложенных
объектов. Рекомендуется выполнять при создании заполненного объекта перед
асинхронным обращением к его вложенным объектам.  
(Переопределяет
[CardInfoStorageObject.EnsureCacheResolved()](M_Tessa_Cards_CardInfoStorageObject_EnsureCacheResolved.htm))  
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
[FromPlainJsonWithRepairAsync](M_Tessa_Cards_Card_FromPlainJsonWithRepairAsync.htm)|
Устанавливает содержимое карточки в соответствии с данными, десериализованными
из текстового JSON. Типы произвольных данных
[Info](P_Tessa_Platform_Storage_InfoStorageObject_Info.htm) для карточки,
файлов и заданий могут быть искажены, т.к. информация об их структуре
неизвестна объекту. В JSON все типы данных десериализуются как
[String](https://learn.microsoft.com/dotnet/api/system.string),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Int64](https://learn.microsoft.com/dotnet/api/system.int64) и
[Double](https://learn.microsoft.com/dotnet/api/system.double). Возвращает
текущую карточку для цепочки вызовов. Рассмотрите использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе
[FromTypedJson(String)](M_Tessa_Cards_Card_FromTypedJson.htm).  
[FromTypedJson](M_Tessa_Cards_Card_FromTypedJson.htm)|  Устанавливает
содержимое карточки в соответствии с данными, десериализованными из текстового
JSON с сохранением типов. Используйте метод
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением типов. Для десериализации других объектов, у
которых нет метода FromTypedJson (например, request/response), используйте
метод
[DeserializeFromTypedJson(String)](M_Tessa_Platform_Storage_StorageHelper_DeserializeFromTypedJson.htm),
записав полученную структуру в объект obj.SetStorage(storage).  
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
[HasChanges](M_Tessa_Cards_Card_HasChanges.htm)|  Возвращает признак того, что
хотя бы одна секция карточки или одна из вложенных карточек файлов или заданий
содержит изменения.  
[Init](M_Tessa_Platform_Storage_StorageObject_Init.htm)|  Инициализирует
значение объекта с заданным ключом, если он отсутствовал в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[InitNotNull](M_Tessa_Platform_Storage_StorageObject_InitNotNull.htm)|
Инициализирует значение объекта с заданным ключом, если он отсутствовал в
хранилище или был равен null, посредством фабрики объектов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[IsEmpty](M_Tessa_Cards_Card_IsEmpty.htm)|  Возвращает признак того, что
объект не содержит значимых данных для метода очистки
[Tessa.Platform.Storage.IStorageCleanable.Clean].  
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
[RemoveAllButChanged](M_Tessa_Cards_Card_RemoveAllButChanged.htm)|  Удаляет
информацию о всех полях или строках всех секций карточки, которые не были
изменены посредством
[IStorageObjectStateProvider](T_Tessa_Platform_Storage_IStorageObjectStateProvider.htm).  
[RemoveChanges](M_Tessa_Cards_Card_RemoveChanges.htm)|  Выполняет удаление
информации по состояниям, из которой можно было бы определить, что карточка
изменена. Возвращает признак того, что при этом были внесены изменения.  
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
[RepairStorageAsync](M_Tessa_Cards_Card_RepairStorageAsync.htm)|  Исправляет
хранилище объекта, типы в котором установлены некорректно, после
десериализации из JSON. Возвращает признак того, что при исправлении в объекте
были изменения.  
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
[TryGetFiles](M_Tessa_Cards_Card_TryGetFiles.htm)|  Возвращает список
прикреплённых к карточке файлов или null, если список ещё не был задан.  
[TryGetInfo](M_Tessa_Cards_CardInfoStorageObject_TryGetInfo.htm)|  Возвращает
дополнительную пользовательскую информацию по текущему объекту или null, если
информация ещё не была задана.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[TryGetList<T>](M_Tessa_Platform_Storage_StorageObject_TryGetList__1.htm)|
Возвращает строго типизированное значение объекта List<object> из хранилища по
заданному ключу или default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetPermissions](M_Tessa_Cards_Card_TryGetPermissions.htm)|  Возвращает
права доступа на карточку и её секции или null, если права ещё не были заданы.  
[TryGetSections](M_Tessa_Cards_Card_TryGetSections.htm)|  Возвращает данные
карточки, включающие содержимое всех строк и полей, или null, если данные ещё
не были заданы.  
[TryGetString](M_Tessa_Platform_Storage_StorageObject_TryGetString.htm)|
Возвращает строковое представление для значения объекта из хранилища по
заданному ключу или null, если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetTaskHistory](M_Tessa_Cards_Card_TryGetTaskHistory.htm)|  Возвращает
список с информацией по завершённым заданиям, которые были выданы на карточку,
или null, если список ещё не был задан.  
[TryGetTaskHistoryGroups](M_Tessa_Cards_Card_TryGetTaskHistoryGroups.htm)|
Возвращает список с информацией по группам заданий, которые были выданы на
карточку, или null, если список ещё не был задан.  
[TryGetTasks](M_Tessa_Cards_Card_TryGetTasks.htm)|  Возвращает список заданий,
которые были выданы на карточку и ещё не были завершены, или null, если список
ещё не был задан.  
[TryGetTopics](M_Tessa_Cards_Card_TryGetTopics.htm)|  Возвращает список
моделей с информацией по сообщениям в обсуждениях или null, если информация
ещё не была задана.  
[UpdateStates](M_Tessa_Cards_Card_UpdateStates.htm)|  Обновляет состояние всех
файлов и заданий в зависимости от наличия изменений в данных соответствующих
карточек.  
[Validate()](M_Tessa_Platform_Validation_ValidationStorageObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationStorageObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ValidateInternal](M_Tessa_Cards_Card_ValidateInternal.htm)| Выполняет
валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardInfoStorageObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardInfoStorageObject_ValidateInternal.htm))  
##  __Методы расширения
[AddKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AddKrProcessClientCommands.htm)|
Добавляет в указанное хранилище список клиентских команд.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
---|---  
[AddToHistory](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerExtensions_AddToHistory.htm)|
Добавить в историю процесса запись.  
(Определяется
[HandlerExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerExtensions.htm))  
[AreButtonsIgnored](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AreButtonsIgnored.htm)|
Получает из заданного хранилища значение флага показывающего, что при загрузке
карточки не надо добавлять в ответ информацию по тайлам вторичных процессов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[ClearOriginalVersion](M_Tessa_Cards_CardRequestExtensions_ClearOriginalVersion.htm)|
Удаляет информацию об оригинальной версии карточки.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
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
[GetActiveTasksSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetActiveTasksSection.htm)|
Возвращает секцию карточки содержащую активные задания.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetApprovalInfoSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetApprovalInfoSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по процессу.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
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
[GetKrApprovalHistorySection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrApprovalHistorySection.htm)|
Возвращает секцию карточки содержащую сопоставление истории заданий с историей
согласования (с учетом циклов согласования).  
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
[GetKrStageTemplateSection](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions_GetKrStageTemplateSection.htm)|  
(Определяется
[KrCompilersExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions.htm))  
[GetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberQueue.htm)|
Возвращает очередь действий с номерами, отложенных для выполнения на сервере
для текущей карточки. Если очередь отсутствует, то создаётся и возвращается
пустая очередь для этой карточки.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[GetPerformersSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetPerformersSection.htm)|
Возвращает секцию карточки содержащей исполнителей этапов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcChanges.htm)|
Возвращает информацию о различиях в маршруте до и после пересчёта.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetRecalcFlag](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcFlag_1.htm)|
Возвращает значение, показывающее, должен ли быть выполнен пересчёт маршрута
или нет.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStagePositions.htm)|
Возвращает информацию о позиции этапов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetStagesSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStagesSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по этапам процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetStartingSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStartingSecondaryProcess.htm)|
Возвращает из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetVisibleTiles](M_Tessa_Cards_CardRequestExtensions_GetVisibleTiles.htm)|
Возвращает массив, содержащий список всех видимых плиток. Массив всегда не
равен null. Данные видимости обычно устанавливаются при создании или загрузке
карточки, в т.ч. на сервере.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[GetWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_GetWorkflowQueue.htm)|
Возвращает очередь действий с Workflow, отложенных для выполнения на сервере
для текущей карточки. Если очередь отсутствует, то создаётся и возвращается
пустая очередь для этой карточки.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[HasHiddenStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasHiddenStages.htm)|
Возвращает значение, показывающее, что в информации о позиции этапов
содержится информация о скрытых этапах.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[HasNumberQueueToProcess](M_Tessa_Cards_Numbers_NumberExtensions_HasNumberQueueToProcess.htm)|
Возвращает признак того, что в карточке присутствует непустая очередь для
обработки.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[HasSkipStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasSkipStages.htm)|
Возвращает значение, показывающее, наличие скрытых пропущенных этапов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[HasStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasStagePositions.htm)|
Возвращает значение, показывающее, что в
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
содержится информация о позиции этапов.  
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
[IsMainProcessStarted](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_IsMainProcessStarted.htm)|
Возвращает значение, показывающее, что указанный сателлит содержит информацию
по основному процессу
[KrProcessName](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrProcessName.htm).  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[IsPartiallyLoaded](M_Tessa_Cards_CardRequestExtensions_IsPartiallyLoaded.htm)|
Возвращает признак того, что карточка может быть загружена частично (например,
без расширений), поэтому не все её поля могут быть корректно заполнены.
Актуально, например, для карточки, загруженной в контексте для действий с
номерами.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[RemoveLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveLocalTiles.htm)|
Удаляет из заданного хранилища информацию по локальным тайлам маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_RemoveNumberQueue.htm)|
Удаляет очередь действий с номерами для текущей карточки. Возвращает признак
того, что такая очередь присутствовала в карточке перед удалением.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[RemoveSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveSecondaryProcess.htm)|
Удаляет из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса добавленную
[SetStartingSecondaryProcess(CardInfoStorageObject,
StartingSecondaryProcessInfo)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveStagePositions.htm)|
Удаляет из
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
информацию о позиции этапов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_RemoveWorkflowQueue.htm)|
Удаляет очередь действий с Workflow для текущей карточки. Возвращает признак
того, что такая очередь присутствовала в карточке перед удалением.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[ResetAllTilesVisibility](M_Tessa_Cards_CardRequestExtensions_ResetAllTilesVisibility.htm)|
Удаляет всю информацию по видимости плиток. Плитки, которые используют
информацию по видимости, будут считать себя скрытыми. Возвращает признак того,
что информация присутствовала перед удалением.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
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
[SetNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_SetNumberQueue.htm)|
Устанавливает очередь действий с номерами для текущей карточки.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetOriginalVersion](M_Tessa_Cards_CardRequestExtensions_SetOriginalVersion.htm)|
Устанавливает оригинальную версию карточки, которая была очищена при экспорте.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetPartiallyLoaded](M_Tessa_Cards_CardRequestExtensions_SetPartiallyLoaded.htm)|
Устанавливает признак того, что карточка может быть загружена частично
(например, без расширений), поэтому не все её поля могут быть корректно
заполнены. Актуально, например, для карточки, загруженной в контексте для
действий с номерами.  
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
[SetStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStagePositions.htm)|
Задаёт в
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
информацию о позиции этапов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStagePositions_1.htm)|
Задаёт в
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
информацию о позиции этапов.  
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
[SetTemplateCreatedFromCard](M_Tessa_Cards_CardRequestExtensions_SetTemplateCreatedFromCard.htm)|
Устанавливает признак того, что карточка шаблона создаётся из другой карточки,
а не в результате создания по шаблону из экспортированной карточки шаблона.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetTemplateWasRepaired](M_Tessa_Cards_CardRequestExtensions_SetTemplateWasRepaired.htm)|
Устанавливает признак того, что карточка шаблона была исправлена после
изменения схемы данных.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetTileIsVisible](M_Tessa_Cards_CardRequestExtensions_SetTileIsVisible.htm)|
Устанавливает признак того, должна ли плитка быть видимой. Рекомендуется
вызывать метод при создании или загрузке карточки, в т.ч. на сервере.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_SetWorkflowQueue.htm)|
Устанавливает очередь действий с Workflow для текущей карточки.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[TileIsVisible](M_Tessa_Cards_CardRequestExtensions_TileIsVisible.htm)|
Возвращает признак того, что плитка с заданным именем должна быть видимой.
Данные видимости обычно устанавливаются при создании или загрузке карточки, в
т.ч. на сервере.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetActiveTasksSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetActiveTasksSection.htm)|
Возвращает секцию карточки содержащую активные задания.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetDigest](M_Tessa_Cards_CardRequestExtensions_TryGetDigest.htm)|
Возвращает Digest для сохранения в историю действий с карточкой или null, если
Digest не был установлен.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetKrApprovalCommonInfoSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrApprovalCommonInfoSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по процессу.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetKrApprovalHistorySection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrApprovalHistorySection.htm)|
Возвращает секцию карточки содержащую сопоставление истории заданий с историей
согласования (с учетом циклов согласования).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
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
[TryGetKrStageCommonMethodsSection](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions_TryGetKrStageCommonMethodsSection.htm)|  
(Определяется
[KrCompilersExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions.htm))  
[TryGetKrStageTemplatesSection](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions_TryGetKrStageTemplatesSection.htm)|  
(Определяется
[KrCompilersExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions.htm))  
[TryGetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_TryGetNumberQueue.htm)|
Возвращает очередь действий с номерами, отложенных для выполнения на сервере
для текущей карточки, или null, если для текущей карточки очередь ещё не была
создана.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[TryGetOriginalVersion](M_Tessa_Cards_CardRequestExtensions_TryGetOriginalVersion.htm)|
Возвращает оригинальную версию карточки, которая была очищена при экспорте.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetPerformersSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetPerformersSection.htm)|
Возвращает секцию карточки содержащей исполнителей этапов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetPluginType](M_Tessa_Cards_CardRequestExtensions_TryGetPluginType.htm)|
Возвращает тип плагина, установленный при выполнении запроса к карточке из
плагина Chronos, или null, если запрос выполнен не из плагина или из
неизвестного плагина.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStagePositions.htm)|
Возвращает информацию о позиции этапов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetStagesSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStagesSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по этапам процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetStartingKrProcessParameters](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStartingKrProcessParameters_1.htm)|
Возвращает параметры запускаемого процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetTemplateCreatedFromCard](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateCreatedFromCard.htm)|
Возвращает признак того, что карточка шаблона создаётся из другой карточки, а
не в результате создания по шаблону из экспортированной карточки шаблона.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetTemplateWasRepaired](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateWasRepaired.htm)|
Возвращает признак того, что структура карточки шаблона была исправлена после
изменения схемы данных.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetWorkflowQueue.htm)|
Возвращает очередь действий с Workflow, отложенных для выполнения на сервере
для текущей карточки, или null, если для текущей карточки очередь ещё не была
создана.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
##  __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
