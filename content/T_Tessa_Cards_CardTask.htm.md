# CardTask - класс
Общая информация о задании, которое выдано на карточку.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardTask : CardInfoStorageObject
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardTask
    	Inherits CardInfoStorageObject
C++ __Копировать
    [SerializableAttribute]
    public ref class CardTask sealed : public CardInfoStorageObject
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardTask = 
        class
            inherit CardInfoStorageObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm) __[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm) __[CardStorageObject](T_Tessa_Cards_CardStorageObject.htm) __[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm) __ CardTask
##  __Конструкторы
[CardTask()](M_Tessa_Cards_CardTask__ctor.htm)|  Создаёт экземпляр класса и
пустое хранилище Dictionary<string, object>, декоратором для которого является
создаваемый объект.  
---|---  
[CardTask(Dictionary<String, Object>)](M_Tessa_Cards_CardTask__ctor_1.htm)|
Создаёт экземпляр класса с указанием хранилища, декоратором для которого
является создаваемый объект.  
[CardTask(IStorageObjectProvider)](M_Tessa_Cards_CardTask__ctor_2.htm)|
Создаёт экземпляр класса с указанием объекта, предоставляющего доступ к
хранилищу, декоратором для которого является создаваемый объект.  
## __Свойства
[Action](P_Tessa_Cards_CardTask_Action.htm)|  Действие, выполняемое для
задания. По умолчанию имеет значение Create.  
---|---  
[AuthorID](P_Tessa_Cards_CardTask_AuthorID.htm)|  Идентификатор автора задания
или null, если задание не было создано и в качестве автора используется
текущий пользователь.  
[AuthorName](P_Tessa_Cards_CardTask_AuthorName.htm)|  Имя автора задания или
null, если задание не было создано и в качестве автора используется текущий
пользователь или если имя автора будет определено автоматически при
сохранении. Автоматическое определение возможно, если значение этого свойства
равно null. Внимание! Должность автора
[AuthorPosition](P_Tessa_Cards_CardTask_AuthorPosition.htm) автоматически
заполняется только в том случае, если имя указано как null.  
[AuthorPosition](P_Tessa_Cards_CardTask_AuthorPosition.htm)|  Должность автора
задания или null, если задание не было создано и в качестве автора
используется текущий пользователь или если должность автора будет определена
автоматически при сохранении. Автоматическое определение возможно, если
значение свойства [AuthorName](P_Tessa_Cards_CardTask_AuthorName.htm) равно
null.  
[CanPostpone](P_Tessa_Cards_CardTask_CanPostpone.htm)|  Получает или задаёт
признак того, что задание может быть отложено. Этот флаг не влияет на
сохранение задания.  
[CanPostponeEffective](P_Tessa_Cards_CardTask_CanPostponeEffective.htm)|
Возможность откладывания задания
[CanPostpone](P_Tessa_Cards_CardTask_CanPostpone.htm), полученная с учётом
признака
[CanPostponeExplicit](P_Tessa_Cards_CardTask_CanPostponeExplicit.htm).  
[CanPostponeExplicit](P_Tessa_Cards_CardTask_CanPostponeExplicit.htm)|
Признак того, что для задания требуется принудительно установить возможность
откладывания [CanPostpone](P_Tessa_Cards_CardTask_CanPostpone.htm).  
[Card](P_Tessa_Cards_CardTask_Card.htm)|  Карточка задания.  
[Digest](P_Tessa_Cards_CardTask_Digest.htm)|  Digest задания, или null, если
задание ещё не создано или Digest задания не указан. Digest содержит
произвольный текст, описывающий задание и выводимый пользователям. Значение
нельзя изменить после того, как задание было создано.  
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Flags](P_Tessa_Cards_CardTask_Flags.htm)|  Флаги задания.  
[GroupRowID](P_Tessa_Cards_CardTask_GroupRowID.htm)|  Идентификатор группы
истории заданий.  
[HistoryItemParentRowID](P_Tessa_Cards_CardTask_HistoryItemParentRowID.htm)|
Ссылка на родительскую запись в истории заданий, которая учитывается только
при автоматическом создании записи в истории заданий в процессе сохранения
карточки. При создании и загрузке карточки поле не заполняется и равно null.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[InProgress](P_Tessa_Cards_CardTask_InProgress.htm)|  Дата взятия задания в
работу или null, если задание ещё не было взято в работу.  
[IsAuthor](P_Tessa_Cards_CardTask_IsAuthor.htm)|  Пользователь видит задание
как автор. Он входит в персональную роль автора задания как пользователь или
заместитель.  
[IsAuthorDeputy](P_Tessa_Cards_CardTask_IsAuthorDeputy.htm)|  Пользователь
видит задание как автор, т.к. является заместителем. Он входит в персональную
роль автора задания как пользователь или заместитель.  
[IsHidden](P_Tessa_Cards_CardTask_IsHidden.htm)|  Признак того, что задание не
следует показывать в UI несмотря на то, что оно присутствует в карточке.  
[IsHiddenFromAuthor](P_Tessa_Cards_CardTask_IsHiddenFromAuthor.htm)|  Получает
или задаёт признак того, что задание помечено как скрытое от автора. Этот флаг
влияет на сохранение задания.  
[IsLocked](P_Tessa_Cards_CardTask_IsLocked.htm)|  Задание не содержит
загруженных данных и доступно только для просмотра общей информации.  
[IsLockedEffective](P_Tessa_Cards_CardTask_IsLockedEffective.htm)|  Режим
просмотра [IsLocked](P_Tessa_Cards_CardTask_IsLocked.htm), полученный с учётом
признака [IsLockedExplicit](P_Tessa_Cards_CardTask_IsLockedExplicit.htm).  
[IsLockedExplicit](P_Tessa_Cards_CardTask_IsLockedExplicit.htm)|  Признак
того, что для задания требуется принудительно установить режим просмотра
[IsLocked](P_Tessa_Cards_CardTask_IsLocked.htm).  
[IsPerformer](P_Tessa_Cards_CardTask_IsPerformer.htm)|  Пользователь видит
задание как исполнитель. Либо он входит в роль, на которую назначено задание,
как пользователь или заместитель; либо он взял задание в работу, даже если уже
не входит в роль; либо он является заместителем пользователя, взявшего задание
в работу, в роли, на которую назначено задание.  
[IsPerformerDeputy](P_Tessa_Cards_CardTask_IsPerformerDeputy.htm)|
Пользователь видит задание как исполнитель, т.к. является заместителем. Либо
он входит в роль, на которую назначено задание, как заместитель; либо он
является заместителем пользователя, взявшего задание в работу, в роли, на
которую назначено задание.  
[IsPostponed](P_Tessa_Cards_CardTask_IsPostponed.htm)|  Задание отложено. Флаг
устанавливается при загрузке и не влияет на сохранение.  
[IsSystem](P_Tessa_Cards_CardTask_IsSystem.htm)|  Пользователь видит задание
как системный пользователь с особыми привилегиями.  
[OptionID](P_Tessa_Cards_CardTask_OptionID.htm)|  Идентификатор варианта
завершения задания, или null, если для задания ещё не был определён вариант
завершения.  
[OriginalRoleID](P_Tessa_Cards_CardTask_OriginalRoleID.htm)|  Идентификатор
текущей роли [RoleID](P_Tessa_Cards_CardTask_RoleID.htm), если роль изменяется
с флагом [UpdateRole](T_Tessa_Cards_CardTaskFlags.htm), или null, если роль не
изменяется или если значение ещё не заполнено платформой. Это свойство
используется платформой, не рекомендуется устанавливать его значение вручную.  
[OriginalRoleTypeID](P_Tessa_Cards_CardTask_OriginalRoleTypeID.htm)|
Идентификатор типа текущей роли
[RoleTypeID](P_Tessa_Cards_CardTask_RoleTypeID.htm), если роль изменяется с
флагом [UpdateRole](T_Tessa_Cards_CardTaskFlags.htm), или null, если роль не
изменяется или если значение ещё не заполнено платформой. Это свойство
используется платформой, не рекомендуется устанавливать его значение вручную.  
[ParentRowID](P_Tessa_Cards_CardTask_ParentRowID.htm)|  Ссылка на родительское
задание.  
[Planned](P_Tessa_Cards_CardTask_Planned.htm)|  Дата запланированного
завершения задания или null, если задание ещё не было создано.  
[PlannedQuants](P_Tessa_Cards_CardTask_PlannedQuants.htm)|  Количество квантов
календаря от времени на момент загрузки задания до времени его
запланированного завершения [Planned](P_Tessa_Cards_CardTask_Planned.htm) или
null, если задание ещё не было создано. Если возвращаемое количество квантов
отрицательное, то задание просрочено.  
[PlannedType](P_Tessa_Cards_CardTask_PlannedType.htm)|  Тип запаланированного
времени. В зависимости от указанного - трактует
[Planned](P_Tessa_Cards_CardTask_Planned.htm), как время исполнителя или
автора.  
[PostponeComment](P_Tessa_Cards_CardTask_PostponeComment.htm)|  Комментарий по
откладыванию задания или null, если задание не было отложено или пользователь
не задал комментария. Поле устанавливается пользователем при откладывании
задания.  
[Postponed](P_Tessa_Cards_CardTask_Postponed.htm)|  Дата и время, когда было
отложено задание, или null, если задание не было отложено. Поле
устанавливается системой при откладывании задания.  
[PostponedTo](P_Tessa_Cards_CardTask_PostponedTo.htm)|  Дата и время, до
которого было отложено задание, или null, если задание не было отложено. Поле
устанавливается пользователем при откладывании задания.  
[ProcessID](P_Tessa_Cards_CardTask_ProcessID.htm)|  Идентификатор бизнес-
процесса, к которому относится запись в истории заданий, которая будет
добавлена для задания, или null, если запись не относится к бизнес-процессу.
Свойство следует устанавливать перед изменением или завершением задания, для
которого будет добавлена запись в истории. Свойство не изменяется при
изменении записи в истории. По умолчанию значение равно null.  
[ProcessKind](P_Tessa_Cards_CardTask_ProcessKind.htm)|  Тип бизнес-процесса, к
которому относится запись в истории заданий, которая будет добавлена для
задания, или null, если запись не относится к бизнес-процессу или не содержит
информации по его типу. Свойство следует устанавливать перед изменением или
завершением задания, для которого будет добавлена запись в истории. Свойство
не изменяется при изменении записи в истории. По умолчанию значение равно
null.  
[ProcessName](P_Tessa_Cards_CardTask_ProcessName.htm)|  Отображаемое имя
бизнес-процесса, к которому относится запись в истории заданий, которая будет
добавлена для задания, или null, если запись не относится к бизнес-процессу.
Свойство следует устанавливать перед изменением или завершением задания, для
которого будет добавлена запись в истории. Свойство не изменяется при
изменении записи в истории. По умолчанию значение равно null.  
[Result](P_Tessa_Cards_CardTask_Result.htm)|  Результат завершения задания,
или null, если либо задание не завершается, либо результат устанавливается
серверными расширениями или не устанавливается вообще. Результат может быть
установлен не только при завершении задания, но и при создании записи в
истории заданий посредством указания флага
[CreateHistoryItem](T_Tessa_Cards_CardTaskFlags.htm).  
[RoleID](P_Tessa_Cards_CardTask_RoleID.htm)|  Идентификатор роли, на которую
назначено задание.  
[RoleName](P_Tessa_Cards_CardTask_RoleName.htm)|  Имя роли, на которую
назначено задание, или null, если задание ещё не было создано.  
[RoleTypeID](P_Tessa_Cards_CardTask_RoleTypeID.htm)|  Идентификатор типа
карточки для роли, на которую назначено задание, или Empty, если задание ещё
не было создано.  
[RowID](P_Tessa_Cards_CardTask_RowID.htm)|  Идентификатор задания.  
[SectionRows](P_Tessa_Cards_CardTask_SectionRows.htm)|  Пустые строки
коллекционных и древовидных секций, доступные по имени секции. Могут
использоваться для редактирования карточки задания.  
[Settings](P_Tessa_Cards_CardTask_Settings.htm)|  Настройки задания,
сериализуемые в JSON.  
[State](P_Tessa_Cards_CardTask_State.htm)|  Состояние строки с заданием.  
[StoredState](P_Tessa_Cards_CardTask_StoredState.htm)|  Начальное состояние
задания при загрузке или Created, если задание создаётся в первый раз.  
[TimeZoneID](P_Tessa_Cards_CardTask_TimeZoneID.htm)|  Идентификатор временной
зоны задания.  
[TimeZoneUtcOffsetMinutes](P_Tessa_Cards_CardTask_TimeZoneUtcOffsetMinutes.htm)|
Смещение временной зоны задания.  
[TypeCaption](P_Tessa_Cards_CardTask_TypeCaption.htm)|  Отображаемое имя типа
задания.  
[TypeID](P_Tessa_Cards_CardTask_TypeID.htm)|  Идентификатор типа задания.  
[TypeName](P_Tessa_Cards_CardTask_TypeName.htm)|  Имя типа задания.  
[UserID](P_Tessa_Cards_CardTask_UserID.htm)|  Идентификатор пользователя,
который взял задание в работу, или null, если задание ещё не было взято в
работу.  
[UserName](P_Tessa_Cards_CardTask_UserName.htm)|  Имя пользователя, который
взял задание в работу, или null, если задание ещё не было взято в работу.  
## __Методы
[Clean](M_Tessa_Cards_CardTask_Clean.htm)| Выполняет очистку хранилища от
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
[ClearPendingChangesAndCard](M_Tessa_Cards_CardTask_ClearPendingChangesAndCard.htm)|
Очищает все флаги [Flags](P_Tessa_Cards_CardTask_Flags.htm), влияющие на смену
состояния, а также все сохраняемые данные в карточке
[Card](P_Tessa_Cards_CardTask_Card.htm).  
[ContainsKey](M_Tessa_Platform_Storage_StorageObject_ContainsKey.htm)|
Возвращает признак того, что элемент с заданным ключом содержится в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[EnsureCacheResolved](M_Tessa_Cards_CardTask_EnsureCacheResolved.htm)|
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
[HasChanges](M_Tessa_Cards_CardTask_HasChanges.htm)|  Возвращает признак того,
что карточка задания содержит изменённые значения.  
[HasPendingStateChanges](M_Tessa_Cards_CardTask_HasPendingStateChanges.htm)|
Возвращает признак того, что во флагах
[Flags](P_Tessa_Cards_CardTask_Flags.htm) установлены флаги, влияющие на смену
состояния на изменённое.  
[Init](M_Tessa_Platform_Storage_StorageObject_Init.htm)|  Инициализирует
значение объекта с заданным ключом, если он отсутствовал в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[InitNotNull](M_Tessa_Platform_Storage_StorageObject_InitNotNull.htm)|
Инициализирует значение объекта с заданным ключом, если он отсутствовал в
хранилище или был равен null, посредством фабрики объектов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[IsEmpty](M_Tessa_Cards_CardTask_IsEmpty.htm)|  Возвращает признак того, что
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
[RemoveChanges](M_Tessa_Cards_CardTask_RemoveChanges.htm)|  Выполняет удаление
информации по состояниям, из которой можно было бы определить, что задание
изменено. Возвращает признак того, что при этом были внесены изменения.  
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
[RepairStorageAsync](M_Tessa_Cards_CardTask_RepairStorageAsync.htm)|
Исправляет хранилище объекта, типы в котором установлены некорректно, после
десериализации из JSON. Возвращает признак того, что при исправлении в объекте
были изменения.  
[Set<T>](M_Tessa_Platform_Storage_StorageObject_Set__1.htm)|  Устанавливает
значение в хранилище по заданному ключу. При этом не изменяется внутренний кэш
декораторов, поэтому метод следует использовать только для примитивных типов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetCard](M_Tessa_Cards_CardTask_SetCard.htm)|  Связывает данные текущего
объекта с заданной карточкой задания. При это устанавливаются свойства
[RowID](P_Tessa_Cards_CardTask_RowID.htm),
[TypeID](P_Tessa_Cards_CardTask_TypeID.htm),
[TypeName](P_Tessa_Cards_CardTask_TypeName.htm),
[TypeCaption](P_Tessa_Cards_CardTask_TypeCaption.htm) и
[Card](P_Tessa_Cards_CardTask_Card.htm).  
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
[TryGetCard](M_Tessa_Cards_CardTask_TryGetCard.htm)|  Возвращает карточку
задания или null, если карточка ещё не была задана.  
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
[TryGetOrCreateCardForStore](M_Tessa_Cards_CardTask_TryGetOrCreateCardForStore.htm)|
Возвращает карточку для сохранения задания или null, если карточка ещё не была
задана. В отличие от метода
[TryGetCard()](M_Tessa_Cards_CardTask_TryGetCard.htm), этот метод может
создать копию основной карточки и удалить из неё все поля, кроме изменяемых,
если выполняется завершение задания без удаления, т.е. свойство
[State](P_Tessa_Cards_CardTask_State.htm) равно
[Modified](T_Tessa_Cards_CardRowState.htm), а свойство
[Action](P_Tessa_Cards_CardTask_Action.htm) равно
[Complete](T_Tessa_Cards_CardTaskAction.htm).  
[TryGetSectionRows](M_Tessa_Cards_CardTask_TryGetSectionRows.htm)|  Возвращает
пустые строки для коллекционных и древовидных секций, доступные по имени
секции, или null, если строки ещё не были заданы.  
[TryGetString](M_Tessa_Platform_Storage_StorageObject_TryGetString.htm)|
Возвращает строковое представление для значения объекта из хранилища по
заданному ключу или null, если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[UpdateState](M_Tessa_Cards_CardTask_UpdateState.htm)|  Обновляет состояние
задания [State](P_Tessa_Cards_CardTask_State.htm) и действие с заданием
[Action](P_Tessa_Cards_CardTask_Action.htm) в зависимости от наличия изменений
во флагах или в данных карточки задания.  
[Validate()](M_Tessa_Platform_Validation_ValidationStorageObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationStorageObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ValidateInternal](M_Tessa_Cards_CardTask_ValidateInternal.htm)| Выполняет
валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardInfoStorageObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardInfoStorageObject_ValidateInternal.htm))  
##  __События
[StateChanged](E_Tessa_Cards_CardTask_StateChanged.htm)|  Событие, возникающее
при изменении состояния задания [State](P_Tessa_Cards_CardTask_State.htm).  
---|---  
## __Поля
[ActionKey](F_Tessa_Cards_CardTask_ActionKey.htm)|  
---|---  
[AuthorIDKey](F_Tessa_Cards_CardTask_AuthorIDKey.htm)|  
[AuthorNameKey](F_Tessa_Cards_CardTask_AuthorNameKey.htm)|  
[AuthorPositionKey](F_Tessa_Cards_CardTask_AuthorPositionKey.htm)|  
[CardKey](F_Tessa_Cards_CardTask_CardKey.htm)|  
[DigestKey](F_Tessa_Cards_CardTask_DigestKey.htm)|  
[GroupRowIDKey](F_Tessa_Cards_CardTask_GroupRowIDKey.htm)|  
[HistoryItemParentRowIDKey](F_Tessa_Cards_CardTask_HistoryItemParentRowIDKey.htm)|  
[InProgressKey](F_Tessa_Cards_CardTask_InProgressKey.htm)|  
[OptionIDKey](F_Tessa_Cards_CardTask_OptionIDKey.htm)|  
[ParentRowIDKey](F_Tessa_Cards_CardTask_ParentRowIDKey.htm)|  
[PlannedKey](F_Tessa_Cards_CardTask_PlannedKey.htm)|  
[PlannedQuantsKey](F_Tessa_Cards_CardTask_PlannedQuantsKey.htm)|  
[PlannedTypeKey](F_Tessa_Cards_CardTask_PlannedTypeKey.htm)|  
[PostponeCommentKey](F_Tessa_Cards_CardTask_PostponeCommentKey.htm)|  
[PostponedKey](F_Tessa_Cards_CardTask_PostponedKey.htm)|  
[PostponedToKey](F_Tessa_Cards_CardTask_PostponedToKey.htm)|  
[ProcessIDKey](F_Tessa_Cards_CardTask_ProcessIDKey.htm)|  
[ProcessKindKey](F_Tessa_Cards_CardTask_ProcessKindKey.htm)|  
[ProcessNameKey](F_Tessa_Cards_CardTask_ProcessNameKey.htm)|  
[ResultKey](F_Tessa_Cards_CardTask_ResultKey.htm)|  
[RoleIDKey](F_Tessa_Cards_CardTask_RoleIDKey.htm)|  
[RoleNameKey](F_Tessa_Cards_CardTask_RoleNameKey.htm)|  
[RoleTypeIDKey](F_Tessa_Cards_CardTask_RoleTypeIDKey.htm)|  
[RowIDKey](F_Tessa_Cards_CardTask_RowIDKey.htm)|  
[SectionRowsKey](F_Tessa_Cards_CardTask_SectionRowsKey.htm)|  
[SettingsKey](F_Tessa_Cards_CardTask_SettingsKey.htm)|  
[SystemFlagsKey](F_Tessa_Cards_CardTask_SystemFlagsKey.htm)|  
[SystemStateKey](F_Tessa_Cards_CardTask_SystemStateKey.htm)|  
[SystemStoredStateKey](F_Tessa_Cards_CardTask_SystemStoredStateKey.htm)|  
[TimeZoneIDKey](F_Tessa_Cards_CardTask_TimeZoneIDKey.htm)|  
[TimeZoneUtcOffsetMinutesKey](F_Tessa_Cards_CardTask_TimeZoneUtcOffsetMinutesKey.htm)|  
[TypeCaptionKey](F_Tessa_Cards_CardTask_TypeCaptionKey.htm)|  
[TypeIDKey](F_Tessa_Cards_CardTask_TypeIDKey.htm)|  
[TypeNameKey](F_Tessa_Cards_CardTask_TypeNameKey.htm)|  
[UserIDKey](F_Tessa_Cards_CardTask_UserIDKey.htm)|  
[UserNameKey](F_Tessa_Cards_CardTask_UserNameKey.htm)|  
## __Методы расширения
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
[SetBackground](M_Tessa_Cards_CardRequestExtensions_SetBackground.htm)|
Устанавливает цвет фона для задания.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
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
[SetTitle](M_Tessa_Cards_CardRequestExtensions_SetTitle.htm)|  Устанавливает
заголовок задания, который выводится вместо типа задания.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetBackground](M_Tessa_Cards_CardRequestExtensions_TryGetBackground.htm)|
Возвращает цвет фона для задания или null, если цвет фона не установлен.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
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
[TryGetTitle](M_Tessa_Cards_CardRequestExtensions_TryGetTitle.htm)|
Возвращает заголовок задания, который выводится вместо типа задания, или null,
если заголовок не задан и выводится тип задания.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
